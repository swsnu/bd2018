import tensorflow as tf
import time

from tensorflow.examples.tutorials.mnist import input_data
from model import lenet

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_integer('max_steps', 1000000,
                            """Number of iterations to run for each workers.""")
tf.app.flags.DEFINE_integer('log_frequency', 50,
                            """How many steps between two runop logs.""")
tf.app.flags.DEFINE_integer('batch_size', 32,
                            """Batch size""")

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

ops = lenet()
train_op = ops['train_op']
loss = ops['loss']
acc = ops['acc']
x = ops['images']
y = ops['labels']
is_training = ops['is_training']


with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
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
      print("step %d, test accuracy %lf, throughput: %f steps/sec" % (i, acc_, throughput))
      start = time.time()
