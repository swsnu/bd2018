# [HW2] Distributed DL training on Parallax

**Due Dec. 5 (Wed), 6pm**

**Questions about HW2: Please create new issues in https://github.com/swsnu/bd2018/issues**

# Total Credit: 10
* Find an open-sourced TensorFlow model to run (0.5 credits)
* Make the model run on a distributed environment using vanilla TensorFlow, Horovod, and Parallax (4.5 credits)
* Check correctness of your distributed programs by comparing the results (2.5 credits)
* Compare the performance of vanilla TensorFlow, Horovod, and Parallax (2.5 credits)
* Report

## Find an open-sourced TensorFlow model to run (0.5 credits)
* Find a public model on the internet that you want to run
  * e.g., https://github.com/tensorflow/models, https://github.com/tensorflow/tensor2tensor, ...
* The model should be based on a published paper - i.e., no toy model (arXiv paper is ok)
* **No image classification / object recognition / object detection models**

## Make the model run on a distributed environment using vanilla TensorFlow, Horovod, and Parallax (4.5 credits)
* Learn the TensorFlow / Horovod / Parallax programming model & APIs
  * TensorFlow: https://www.tensorflow.org
  * Distributed TensorFlow (PS architecture): https://www.tensorflow.org/deploy/distributed, https://github.com/tensorflow/benchmarks/tree/master/scripts/tf_cnn_benchmarks
  * Horovod (AllReduce architecture): https://github.com/uber/horovod/blob/master/examples/tensorflow_mnist.py
  * Parallax (Hybrid architecture): https://github.com/snuspl/parallax/blob/master/doc/quick_start.md
* Copying the model code from the Internet is fine
  * If you are copying the code, please leave a reference on the report
* Use at least two workers when running your scripts
* Provide scripts that run your model with three different distribution libraries above
  * e.g., run_tf.py, run_parallax.py, ...
  * Explain how to run the script (e.g., command line argument)
  * Using synthetic data is fine (e.g., feed random-generated NumPy array)
    * If you are going to use real dataset, provide an additional script for downloading the dataset
  * The script should be able to use multiple machines
    * If you do not have a distributed environment, launch multiple processes on a machine to mimic the execution behavior
  * The scripts should run on Ubuntu (which will be used by TAs for grading)
    * If you do not have a Ubuntu machine, please use Virtualbox/Docker to make sure your code runs correctly

## Check your distributed programs run correctly by comparing the results (2.5 credits)
* Compare results (produced model parameters) of three different distribution library
  * Remove any non-deterministic behaviors (i.e., random initialization, random data shuffling) to compare the results
  * Inspecting TensorFlow checkpoint: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/inspect_checkpoint.py
* If there are any differences, explain them in your report and discuss why they happen
* TAs will run your scripts to reproduce the results

## Compare the performance of vanilla TensorFlow, Horovod, and Parallax (2.5 credits)
* Compare performance (throughput) of three different distribution library
  * Performance of the first 50~100 iterations (may depend on your model) can be unstable, so just discard them
* If there are any differences, explain them in your report and discuss why they happen
* Please also specify your environment (i.e., # machines, CPU / GPU spec, ...)

**You don't have to fully train your model!**

# Submission guide

## Installation guide
* OpenMPI: https://www.open-mpi.org/faq/?category=building#easy-build
  * Prerequisites: `apt-get install autoconf automake libtool`
* NVIDIA driver: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-installation
  * You can install only the driver if you are going to use NVIDIA docker
* CUDA: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-installation
  * Or use NVIDIA docker: https://github.com/NVIDIA/nvidia-docker
* NCCL: https://docs.nvidia.com/deeplearning/sdk/nccl-install-guide/index.html#tar
  * Use OS agnostic version
* Parallax: https://github.com/snuspl/parallax/blob/master/doc/installation.md


## Skeleton code guide
* model.py: MNIST model
* run.py: run single-GPU training
* run_tf.py: run distributed training with vanilla TensorFlow
* run_horovod.py: run distributed training with Horovod
* run_parallax.py: run distributed training with Parallax
* You can find more examples in
  * https://github.com/snuspl/parallax/tree/master/parallax/parallax/examples
  * https://github.com/tensorflow/benchmarks/tree/master/scripts/tf_cnn_benchmarks


## HW upload guide
* Upload to your private Github repository
  * https://github.com/YOUR_GITHUB_ID/bd18f-YOUR_NAME (e.g., https://github.com/johnyangk/bd18f-YoungSeok)
  * The code
  * The report in PDF format

