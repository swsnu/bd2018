#install and run
mvn compile exec:java -Dexec.mainClass=edu.snu.bd.examples.Homework \
    -Dexec.args="--runner=SparkRunner --inputFile=input.txt --output=`pwd`/spark_output/output" \
    -Pspark-runner
