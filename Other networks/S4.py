# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:02:20 2018

@author: zhaoyuzhi
"""

import layer_definition as nl   #build a new layer and get ImageToMatrix function
import tensorflow as tf
import xlrd
import numpy as np
import pandas as pd

IMAGEURL = "C:\\Users\\zhaoyuzhi\\Desktop\\train"
IMAGESAVEURL_F1_lfw = "C:\\Users\\zhaoyuzhi\\Desktop\\train\\lfw_5590_F1"
IMAGESAVEURL_F1_net = "C:\\Users\\zhaoyuzhi\\Desktop\\train\\net_7876_F1"
IMAGESAVEURL_F1_lfw_test = "C:\\Users\\zhaoyuzhi\\Desktop\\train\\lfw_5590_F1_test"
IMAGESAVEURL_F1_net_test = "C:\\Users\\zhaoyuzhi\\Desktop\\train\\net_7876_F1_test"
train = xlrd.open_workbook('trainImageList.xlsx')
train_table = train.sheet_by_index(0)
test = xlrd.open_workbook('testImageList.xlsx')
test_table = test.sheet_by_index(0)
x_data = np.zeros([10000,39,39], dtype = np.float32)                #input imagematrix_data
y_data = np.ones([10000,10], dtype = np.float32)                    #correct output landmarks_data
x_test = np.zeros([3466,39,39], dtype = np.float32)
y_test = np.ones([3466,10], dtype = np.float32)

newlandmarks = np.zeros(10, dtype = np.float32)

## handle train data
for i in range(4151):                                               #train data part 1
    #get 39*39 numpy matrix of a single image
    imagename = train_table.cell(i+1,0).value
    true_imagename = imagename[9:]
    imagematrix = nl.ImageToMatrix(IMAGESAVEURL_F1_lfw + '\\' + true_imagename)
    #extract image size and rawlandmarks data for normalized newlandmarks
    width = train_table.cell(i+1,4).value - train_table.cell(i+1,3).value
    height = train_table.cell(i+1,2).value - train_table.cell(i+1,1).value
    rawlandmarks = train_table.row_slice(i+1, start_colx=5, end_colx=15)
    #get ten normalized newlandmarks(coordinates of LE,RE,N,LM,RM)
    for j in range(0,9,2):
        newlandmarks[j] = (rawlandmarks[j].value - train_table.cell(i+1,3).value + 0.05 * width) / (1.1 * width) * 39
    for k in range(1,10,2):
        newlandmarks[k] = (rawlandmarks[k].value - train_table.cell(i+1,1).value + 0.05 * height) / (1.1 * height) * 39
    #one dimension which represents one grey picture, set the first dimension as index
    x_data[i,:,:] = imagematrix
    y_data[i,:] = newlandmarks

for i in range(5849):                                               #train data part 2
    #get 39*39 numpy matrix of a single image
    imagename = train_table.cell(i+4152,0).value
    true_imagename = imagename[9:]
    imagematrix = nl.ImageToMatrix(IMAGESAVEURL_F1_net + '\\' + true_imagename)
    #extract image size and rawlandmarks data for normalized newlandmarks
    width = train_table.cell(i+4152,4).value - train_table.cell(i+4152,3).value
    height = train_table.cell(i+4152,2).value - train_table.cell(i+4152,1).value
    rawlandmarks = train_table.row_slice(i+4152, start_colx=5, end_colx=15)
    #get ten normalized newlandmarks(coordinates of LE,RE,N,LM,RM)
    for j in range(0,9,2):
        newlandmarks[j] = (rawlandmarks[j].value - train_table.cell(i+4152,3).value + 0.05 * width) / (1.1 * width) * 39
    for k in range(1,10,2):
        newlandmarks[k] = (rawlandmarks[k].value - train_table.cell(i+4152,1).value + 0.05 * height) / (1.1 * height) * 39
    #one dimension which represents one grey picture, set the first dimension as index
    x_data[i+4151,:,:] = imagematrix
    y_data[i+4151,:] = newlandmarks

## handle test data
for i in range(1439):                                               #test data part 1
    #get 39*39 numpy matrix of a single image
    imagename = test_table.cell(i+1,0).value
    true_imagename = imagename[9:]
    imagematrix = nl.ImageToMatrix(IMAGESAVEURL_F1_lfw_test + '\\' + true_imagename)
    #extract image size and rawlandmarks data for normalized newlandmarks
    width = test_table.cell(i+1,4).value - test_table.cell(i+1,3).value
    height = test_table.cell(i+1,2).value - test_table.cell(i+1,1).value
    rawlandmarks = test_table.row_slice(i+1, start_colx=5, end_colx=15)
    #get ten normalized newlandmarks(coordinates of LE,RE,N,LM,RM)
    for j in range(0,9,2):
        newlandmarks[j] = (rawlandmarks[j].value - test_table.cell(i+1,3).value + 0.05 * width) / (1.1 * width) * 39
    for k in range(1,10,2):
        newlandmarks[k] = (rawlandmarks[k].value - test_table.cell(i+1,1).value + 0.05 * height) / (1.1 * height) * 39
    #one dimension which represents one grey picture, set the first dimension as index
    x_test[i,:,:] = imagematrix
    y_test[i,:] = newlandmarks

for i in range(2027):                                               #test data part 2
    #get 39*39 numpy matrix of a single image
    imagename = test_table.cell(i+1440,0).value
    true_imagename = imagename[9:]
    imagematrix = nl.ImageToMatrix(IMAGESAVEURL_F1_net_test + '\\' + true_imagename)
    #extract image size and rawlandmarks data for normalized newlandmarks
    width = test_table.cell(i+1440,4).value - test_table.cell(i+1440,3).value
    height = test_table.cell(i+1440,2).value - test_table.cell(i+1440,1).value
    rawlandmarks = test_table.row_slice(i+1440, start_colx=5, end_colx=15)
    #get ten normalized newlandmarks(coordinates of LE,RE,N,LM,RM)
    for j in range(0,9,2):
        newlandmarks[j] = (rawlandmarks[j].value - test_table.cell(i+1440,3).value + 0.05 * width) / (1.1 * width) * 39
    for k in range(1,10,2):
        newlandmarks[k] = (rawlandmarks[k].value - test_table.cell(i+1440,1).value + 0.05 * height) / (1.1 * height) * 39
    #one dimension which represents one grey picture, set the first dimension as index
    x_test[i+1439,:,:] = imagematrix
    y_test[i+1439,:] = newlandmarks

## F1
x = tf.placeholder(tf.float32, shape=[None,39,39], name='x')        #input imagematrix_data to be fed
y = tf.placeholder(tf.float32, shape=[None,10], name='y')           #correct output to be fed
keep_prob = tf.placeholder(tf.float32, name='keep_prob')            #keep_prob parameter to be fed

x_image = tf.reshape(x, [-1,39,39,1])

## convolutional layer 1, kernel 4*4, insize 1, outsize 20
W_conv1 = tf.Variable(tf.truncated_normal(shape=[4,4,1,20], stddev=0.1), name = 'W_conv1')
b_conv1 = tf.Variable(tf.constant(0.1, shape=[20]), name = 'b_conv1')
h_conv1 = nl.conv_layer(x_image, W_conv1) + b_conv1                 #outsize = batch*36*36*20
a_conv1 = tf.nn.relu(h_conv1)                                       #outsize = batch*36*36*20

## max pooling layer 1
h_pool1 = nl.max_pool_22_layer(a_conv1)                             #outsize = batch*18*18*20
a_pool1 = tf.nn.relu(h_pool1)                                       #outsize = batch*18*18*20

## convolutional layer 2, kernel 3*3, insize 20, outsize 40
W_conv2 = tf.Variable(tf.truncated_normal(shape=[3,3,20,40], stddev=0.1), name = 'W_conv2')
b_conv2 = tf.Variable(tf.constant(0.1, shape=[40]), name = 'b_conv2')
h_conv2 = nl.conv_layer(a_pool1, W_conv2) + b_conv2                 #outsize = batch*16*16*40
a_conv2 = tf.nn.relu(h_conv2)                                       #outsize = batch*16*16*40

## max pooling layer 2
h_pool2 = nl.max_pool_22_layer(a_conv2)                             #outsize = batch*8*8*40
a_pool2 = tf.nn.relu(h_pool2)                                       #outsize = batch*8*8*40

## flatten layer
x_flat = tf.reshape(a_pool2, [-1,2560])                              #outsize = batch*2560

## fully connected layer 1
W_fc1 = tf.Variable(tf.truncated_normal(shape=[2560,120], stddev=0.1), name = 'W_fc1')
b_fc1 = tf.Variable(tf.constant(0.1, shape=[120]), name = 'b_fc1')
h_fc1 = tf.matmul(x_flat, W_fc1) + b_fc1                            #outsize = batch*120
a_fc1 = tf.nn.relu(h_fc1)                                           #outsize = batch*120
a_fc1_dropout = tf.nn.dropout(a_fc1, keep_prob)                     #dropout layer 1

## fully connected layer 2
W_fc2 = tf.Variable(tf.truncated_normal(shape=[120,10], stddev=0.1), name = 'W_fc2')
b_fc2 = tf.Variable(tf.constant(0.1, shape=[10]), name = 'b_fc2')
h_fc2 = tf.matmul(a_fc1_dropout, W_fc2) + b_fc2                     #outsize = batch*10
a_fc2 = tf.nn.relu(h_fc2, name = 'prediction')                      #outsize = batch*10

#regularization and loss function
original_cost = tf.reduce_mean(tf.pow(y - a_fc2, 2))
tv = tf.trainable_variables()   #L2 regularization
regularization_cost = 1 / 32 * tf.reduce_sum([ tf.nn.l2_loss(v) for v in tv ])   #1 / 32 is a hyper parameter
cost = original_cost + regularization_cost
Optimizer = tf.train.AdamOptimizer(0.0001).minimize(cost)
init = tf.global_variables_initializer()
#average accuracy every batch
accuracy = tf.reduce_mean((y - a_fc2), 0)                           #average accuracy every batch
testaccuracy = np.zeros([27,10], dtype = np.float32)
cache_F1 = np.zeros([3456,10], dtype = np.float32)
#save the model
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    for i in range(2000):                                           #number of iterations:5000*625=3125000, 50 millon images
        for m in range(625):                                        #training process using training data 10000 images
            train_xbatch = x_data[(m*16):(m*16+16),:,:]             #train 16 data every batch, not including m*16+16
            train_ybatch = y_data[(m*16):(m*16+16),:]               #train 16 data every batch, not including m*16+16
            sess.run(Optimizer, feed_dict = {x:train_xbatch, y:train_ybatch, keep_prob:0.5})
            if m % 125 == 0:
                iteration = i * 625 + m
                print('The iteration number is:',iteration)
                print('The loss is:',sess.run(original_cost, feed_dict = {x:train_xbatch, y:train_ybatch, keep_prob:1}))
        if (i+1) % 250 == 0:
            save_path = saver.save(sess, "F1_net/save_net.ckpt")    #save the model

    for k in range(27):
        test_xbatch = x_test[(k*128):(k*128+128),:,:]               #test 128 data every batch, not including k*128+128
        test_ybatch = y_test[(k*128):(k*128+128),:]		           #test 128 data every batch, not including k*128+128
        testaccuracy[k,:] = accuracy.eval(feed_dict = {x:test_xbatch, y:test_ybatch, keep_prob:1})
        cache_F1[(k*128):(k*128+128),:] = a_fc2.eval(feed_dict = {x:test_xbatch, keep_prob:1})

#print euclidean distance of the keypoints
printaccuracy = np.mean(testaccuracy, 0)
LE_accuracy = np.sqrt(np.square(printaccuracy[0])+np.square(printaccuracy[1])) / 39
RE_accuracy = np.sqrt(np.square(printaccuracy[2])+np.square(printaccuracy[3])) / 39
N_accuracy = np.sqrt(np.square(printaccuracy[4])+np.square(printaccuracy[5])) / 39
LM_accuracy = np.sqrt(np.square(printaccuracy[6])+np.square(printaccuracy[7])) / 39
RM_accuracy = np.sqrt(np.square(printaccuracy[8])+np.square(printaccuracy[9])) / 39
print('LE_error_rate is:',LE_accuracy)
print('RE_error_rate is:',RE_accuracy)
print('N_error_rate is:',N_accuracy)
print('LM_error_rate is:',LM_accuracy)
print('RM_error_rate is:',RM_accuracy)
print(cache_F1)

## save the predicted keypoints to excel
cache_F1_df = pd.DataFrame(cache_F1)
writer = pd.ExcelWriter('F1_test.xlsx')
cache_F1_df.to_excel(writer,'sheet1')
writer.save()
