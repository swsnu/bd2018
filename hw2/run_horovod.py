import os
import time
import tensorflow as tf
import horovod.tensorflow as hvd

import model
from model import lenet
from tensorflow.examples.tutorials.mnist import input_data

hvd.init()

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_integer('max_steps', 1000000,
                            """Number of iterations to run for each workers.""")
tf.app.flags.DEFINE_integer('log_frequency', 50,
                            """How many steps between two runop logs.""")
tf.app.flags.DEFINE_integer('batch_size', 32,
                            """Batch size""")

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

ops = lenet(only_logits=True)
logits = ops['logits']
x = ops['images']
y = ops['labels']
is_training = ops['is_training']
global_step = ops['global_step']

loss = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=logits))
loss += model.weight_decay * tf.losses.get_regularization_loss()
acc = tf.reduce_mean(tf.cast(
    tf.equal(tf.argmax(logits, axis=1), tf.argmax(y, axis=1)),
    tf.float32))

optimizer = tf.train.AdamOptimizer(learning_rate=model.learning_rate)
optimizer = hvd.DistributedOptimizer(optimizer)
train_op = optimizer.minimize(loss, global_step=global_step)

with tf.train.MonitoredTrainingSession() as sess:
  start = time.time()
  for i in range(FLAGS.max_steps):
    batch = mnist.train.next_batch(FLAGS.batch_size)
    _, loss_ = sess.run([train_op, loss], feed_dict={x: batch[0],
                                                     y: batch[1],
                                                     is_training: True})
    if i % FLAGS.log_frequency == 0:
      end = time.time()
      throughput = float(FLAGS.log_frequency) / float(end - start)
      acc_ = sess.run(acc, feed_dict={x: mnist.test.images,
                                      y: mnist.test.labels,
                                      is_training: False})
      print("step: %d, test accuracy: %lf, throughput: %f steps/sec"
            % (i, acc_, throughput))
      start = time.time()

