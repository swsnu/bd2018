# [HW1] Beam on Spark/Nemo

**Due Oct. 31 (Wed), 6pm**

**Questions about HW1: Please create new issues in https://github.com/swsnu/bd2018/issues**

# Total Credit: 10
* Find at least 2 datasets to process (2 credits)
* Develop a batch BeamSQL application (6 credits)
* Provide scripts to run the application on Spark/Nemo, and write a report (2 credits)

## Find at least 2 datasets to process (2 credits)
* Find 2 public datasets on the internet that you want to process
  * e.g., https://github.com/caesar0301/awesome-public-datasets
* Each dataset must be larger than 1MB

## Develop a batch BeamSQL application (6 credits)
* Learn the Apache Beam programming model 
  * Beam: https://beam.apache.org/
  * BeamSQL: https://beam.apache.org/documentation/dsls/sql/overview/
* Develop a batch BeamSQL application that processes the 2 datasets
* The application must meet the following requirements
  * Read 2 datasets
  * Contain at least one SQL 'JOIN'
  * Contain at least one User Defined Function (UDF) embedded in the SQL query (https://beam.apache.org/documentation/dsls/sql/user-defined-functions/)
  * The UDF must call at least one external Java library (e.g., https://en.wikipedia.org/wiki/List_of_numerical_libraries#Java) - You need to include the library in the Maven pom.xml
  * Write the final results to a local file (https://beam.apache.org/documentation/programming-guide/#pipeline-io-writing-data)
* We will check if you’re copying existing Beam apps from the Internet

## Provide scripts to run the application on Spark/Nemo, and write a report (2 credits)
* TAs will run your scripts to reproduce the results
  * The scripts should run on either Mac or Ubuntu (which will be used by TAs for grading)
  * If you're not using those OSes, please use Virtualbox/Docker to make sure your code runs correctly
* Scripts
  * download_datasets.sh: Downloads the 2 datasets from the web
  * run_spark.sh, run_nemo.sh: You should be able to reuse the scripts provided in the skeleton code
* Report
  * Attach at least two screenshots of the Nemo IR
  * Screenshot of the Nemo IR visualizer using https://nemo.snuspl.snu.ac.kr:50443/nemo-dag/ (Can be found in the /REEF_LOCAL_RUNTIME/BD_HW_ONE-XXX/dag/ in your local directory after running the job)
  * Compare the different Nemo DAGs in the following aspects: DAG Topology, annotations on vertices and edges, etc

# Submission guide

## Skeleton code guide
* JAVA_HOME must be set on your computer
  * ref: https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04
* Homework.java: Study the code. This runs a WordCount pipeline, and then a BeamSQL query
* ./download_datasets.sh: Run this script to download a sample dataset ('input.txt' file)
* ./run_spark.sh: Run, and check /spark_output for the results
  * Ignore the error `java.lang.IllegalArgumentException: Directory /home/ubuntu/bd_hw/target/classes is not allowed for addJar`, and [WARNING]s such as `Couldn't destroy threadgroup org.codehaus.mojo.exec.ExecJavaMojo$IsolatedThreadGroup`. They are irrelevant to the correctness of the program.
  * If interested, read the Spark documentation https://spark.apache.org/
* ./run_nemo.sh: Run, and check /nemo_output for the results
  * Drag-and-drop different /REEF_LOCAL_RUNTIME/BD_HW_ONE-XXX/dag/PlanXX.json files into https://nemo.snuspl.snu.ac.kr:50443/nemo-dag/ to visualize Nemo DAGs (how they are optimized)
  * These are the optimization passes used in the DefaultPolicy https://github.com/apache/incubator-nemo/blob/master/compiler/optimizer/src/main/java/org/apache/nemo/compiler/optimizer/pass/compiletime/composite/DefaultCompositePass.java
  * If interested, read the Nemo documentation https://nemo.apache.org/

## HW upload guide
* Upload to your private Github repository
  * https://github.com/YOUR_GITHUB_ID/bd17f-YOUR_NAME (e.g., https://github.com/johnyangk/bd17f-YoungSeok)
  * The code
  * Report in PDF format
* Do not upload the datasets! (they may be big, so we'll instead use the scripts to download them)

