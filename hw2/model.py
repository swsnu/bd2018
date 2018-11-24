from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

learning_rate = 1e-3
weight_decay = 1e-4
num_classes = 10
dropout_keep_prob = 0.5

def lenet(only_logits=False):
  np.random.seed(0)
  images_ph = tf.placeholder(tf.float32, shape=[None, 784])
  labels_ph = tf.placeholder(tf.int64, shape=[None, num_classes])
  is_training_ph = tf.placeholder(tf.bool, shape=())

  global_step = tf.train.get_or_create_global_step()

  images = tf.reshape(images_ph, [-1, 28, 28, 1])

  net = tf.layers.conv2d(images, 10, [5, 5],
                         activation=tf.nn.relu,
                         kernel_initializer=tf.constant_initializer(np.random.randn(5, 5, 1, 10) * 1e-2),
                         kernel_regularizer=tf.nn.l2_loss,
                         name='conv1')
  net = tf.layers.max_pooling2d(net, [2, 2], 2, name='pool1')
  net = tf.layers.conv2d(net, 20, [5, 5],
                         activation=tf.nn.relu,
                         kernel_initializer=tf.constant_initializer(np.random.randn(5, 5, 10, 20) * 1e-2),
                         kernel_regularizer=tf.nn.l2_loss,
                         name='conv2')
  net = tf.layers.max_pooling2d(net, [2, 2], 2, name='pool2')
  net = tf.layers.flatten(net)

  net = tf.layers.dense(net, 50,
                        activation=tf.nn.relu,
                        kernel_initializer=tf.constant_initializer(np.random.randn(320, 50) * 1e-2),
                        kernel_regularizer=tf.nn.l2_loss,
                        name='fc3')
  net = tf.layers.dropout(net, 1 - dropout_keep_prob, training=is_training_ph, name='dropout3')
  logits = tf.layers.dense(net, num_classes,
                           activation=None,
                           kernel_initializer=tf.constant_initializer(np.random.randn(50, 10) * 1e-2),
                           kernel_regularizer=tf.nn.l2_loss,
                           name='fc4')

  if only_logits:
    return {'logits': logits,
            'images': images_ph,
            'labels': labels_ph,
            'is_training': is_training_ph,
            'global_step': global_step}

  loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels_ph, logits=logits))
  loss += weight_decay * tf.losses.get_regularization_loss()
  acc = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(logits, axis=1), tf.argmax(labels_ph, axis=1)), tf.float32))

  optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
  train_op = optimizer.minimize(loss, global_step=global_step)

  return {'train_op': train_op,
          'logits': logits,
          'loss': loss,
          'acc': acc,
          'images': images_ph,
          'labels': labels_ph,
          'is_training': is_training_ph,
          'global_step': global_step}
