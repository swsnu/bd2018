"""
Example command for running this script:
python run_parallax.py --max_steps=10

Example command for examining the checkpoint file:
python <PARALLAX_HOME>/tensorflow/tensorflow/python/tools/inspect_checkpoint.py --file_name=parallax_ckpt/model.ckpt-0 --tensor_name=conv1/kernel
"""


import os
import time
import tensorflow as tf
import parallax

from model import lenet
from tensorflow.examples.tutorials.mnist import input_data

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('resource_info_file',
                           os.path.abspath(os.path.join(
                               os.path.dirname(__file__),
                               '.',
                               'resource_info')),
                           'Filename containing cluster information')
tf.app.flags.DEFINE_integer('max_steps', 1000000,
                            """Number of iterations to run for each workers.""")
tf.app.flags.DEFINE_integer('log_frequency', 50,
                            """How many steps between two runop logs.""")
tf.app.flags.DEFINE_integer('batch_size', 32,
                            """Batch size""")
tf.app.flags.DEFINE_boolean('sync', True, '')

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# Build single-GPU lenet model
single_gpu_graph = tf.Graph()
with single_gpu_graph.as_default():
  ops = lenet()
  train_op = ops['train_op']
  loss = ops['loss']
  acc = ops['acc']
  x = ops['images']
  y = ops['labels']
  is_training = ops['is_training']

parallax_config = parallax.Config()
ckpt_config = parallax.CheckPointConfig(ckpt_dir='parallax_ckpt',
                                        save_ckpt_steps=1)
parallax_config.ckpt_config = ckpt_config

sess, num_workers, worker_id, num_replicas_per_worker = parallax.parallel_run(
    single_gpu_graph,
    FLAGS.resource_info_file,
    sync=FLAGS.sync,
    parallax_config=parallax_config)

start = time.time()
for i in range(FLAGS.max_steps):
  batch = mnist.train.next_batch(FLAGS.batch_size, shuffle=False)
  _, loss_ = sess.run([train_op, loss], feed_dict={x: [batch[0]],
                                                   y: [batch[1]],
                                                   is_training: [True]})
  if i % FLAGS.log_frequency == 0:
    end = time.time()
    throughput = float(FLAGS.log_frequency) / float(end - start)
    acc_ = sess.run(acc, feed_dict={x: [mnist.test.images],
                                    y: [mnist.test.labels],
                                    is_training: [False]})[0]
    parallax.log.info("step: %d, test accuracy: %lf, throughput: %f steps/sec"
                      % (i, acc_, throughput))
    start = time.time()
