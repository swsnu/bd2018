# Big Data and Deep Learning Systems
## Fall 2018

## Announcements

## Schedule (TBD)
| Week | Lecture | Homework/Project |
|------|---------|------------------|
| Week1 9.4/6 | Introduction. Resource Manager: YARN, Mesos, Borg | |
| Week2 9.11/13 | Meta-framework: REEF, Dataflow processing: MR, Dryad | |
| Week3 9.18/20 | Dataflow processing: Spark, Tez, Vortex, Naiad | Team formation & project proposal due, HW1 out |
| Week4 9.25(추석)/27 | Programming: Hive, DryadLINQ, Spark/Shark, Pig, FlumeJava, Beam |  |
| Week5 10.2/4 | Stream processing: SparkStreaming, Storm, Heron, Flink, MIST |  |
| Week6 10.9/11 | Stream processing: SparkStreaming, Storm, Heron, Flink, MIST | HW1 due, HW2 out |
| Week7 10.16/18 | ML/DL framework: Parameter server/Tensorflow |   |
| Week8 10.23/10.25 | DL framework - Tensorflow/Caffe2/Torch | Project progress presentation (11.1)|
| Week9 10.30/11.1 | DL framework - Tensorflow/Caffe2/Torch  | |
| Week10 11.6/8 | DL framework - Tensorflow/Caffe2/Torch | HW2 due |
| Week11 11.13/15 |  Graph processing - Pregel, GraphLab, X-Stream, Arabesque | |
| Week12 11.20/22 |  Graph processing - Pregel, GraphLab, X-Stream, Arabesque | Survey paper due (covering >= 5 papers) |
| Week13 11.27/29 | DS - GFS, Bigtable, Dynamo ||
| Week14 12.4/6 | Coordination - Chubby, Zookeeper ||
| Week15 12.11/13 | TBD, Project presentation ||
| Week16 12.18 | Project presentation | Project report due - 12.20  |


## Reading list

### Resource management
- [YARN](https://www.cse.ust.hk/~weiwa/teaching/Fall15-COMP6611B/reading_list/YARN.pdf). Apache Hadoop YARN: Yet Another Resource Negotiator. Vinod Kumar Vavilapalli, Arun C Murthy, Chris Douglas, Sharad Agarwal, Mahadev Konar, Robert Evans, Thomas Graves, Jason Lowe, Hitesh Shah, Siddharth Seth, Bikas Saha, Carlo Curino, Owen O’Malley, Sanjay Radia, Benjamin Reed, Eric Baldeschwieler. SOCC 2013.
- [Mesos](http://static.usenix.org/event/nsdi11/tech/full_papers/Hindman_new.pdf). Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center. Benjamin Hindman, Andy Konwinski, Matei Zaharia, Ali Ghodsi, Anthony D. Joseph, Randy Katz, Scott Shenker, Ion Stoica. NSDI 2011.
- [Borg](https://pdos.csail.mit.edu/6.824/papers/borg.pdf). Large-scale cluster management at Google with Borg. Abhishek Verma, Luis Pedrosa, Madhukar Korupolu, David Oppenheimer, Eric Tune, John Wilkes. EuroSys 2015.  

### Meta-framework
- [REEF](). Apache REEF: Retainable Evaluator Execution Framework. Byung-Gon Chun, Tyson Condie, Yingda Chen, Brian Cho, Andrew Chung, Carlo Curino, Chris Douglas, Matteo Interlandi, Beomyeol Jeon, Joo Seong Jeong, Gye-Won Lee, Yunseong Lee, Tony Majestro, Dahlia Malkhi, Sergiy Matusevych, Brandon Myers, Mariia Mykhailova, Shravan Narayanamurthy, Joseph Noor, Raghu Ramakrishnan, Sriram Rao, Russell Sears, Beysim Sezgin, Tae-Geon Um, Julia Wang, Markus Weimer, Markus Weimer, Youngseok Yang. ACM TOCS September 2017.

### Dataflow Processing Framework
- [MapReduce](https://www.usenix.org/legacy/event/osdi04/tech/full_papers/dean/dean.pdf). MapReduce: Simpliﬁed Data Processing on Large Clusters. Jeffrey Dean and Sanjay Ghemawat. OSDI 2004.
- [Dryad](https://birrell.org/andrew/papers/Dryad-Eurosys.pdf). Dryad: Distributed Data-Parallel Programs from Sequential Building Blocks. Michael Isard, Mihai Budiu, Yuan Yu, Andrew Birrell, Dennis Fetterly. Eurosys 2007.
- [Spark](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf). Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing. Matei Zaharia, Mosharaf Chowdhury, Tathagata Das, Ankur Dave, Justin Ma, Murphy McCauley, Michael J. Franklin, Scott Shenker, Ion Stoica. NSDI 2012.
- [CIEL](https://www.usenix.org/legacy/event/nsdi11/tech/full_papers/Murray.pdf). CIEL: a universal execution engine for distributed data-ﬂow computing. Derek G. Murray, Malte Schwarzkopf, Christopher Smowton, Steven Smith, Anil Madhavapeddy, Steven Hand. NSDI 2011.
- [Naiad](sigops.org/sosp/sosp13/papers/p439-murray.pdf). Naiad: A Timely Dataﬂow System. Derek G. Murray, Frank McSherry, Rebecca Isaacs, Michael Isard, Paul Barham, Martin Abadi. SOSP 2013.
- [Tez](https://www.cse.ust.hk/~weiwa/teaching/Fall16-COMP6611B/reading_list/Tez.pdf). Apache Tez: A Unifying Framework for Modeling and
Building Data Processing Applications. Bikas Saha, Hitesh Shah, Siddharth Seth, Gopal Vijayaraghavan, Arun Murthy, Carlo Curino. SIGMOD 2015.
- [Optimus](https://pdfs.semanticscholar.org/9ec7/8da630bed253d3ae41af753eb0013d4273be.pdf). Optimus: A Dynamic Rewriting Framework
for Data-Parallel Execution Plans. Qifa Ke, Michael Isard, Yuan Yu. EuroSys 2013.
- [Pado](http://dl.acm.org/citation.cfm?id=3064181&dl=ACM&coll=DL&CFID=977360376&CFTOKEN=40744495). Pado: A Data Processing Engine for Harnessing Transient Resources in Datacenters. Youngseok Yang, Geon-Woo Kim, Won Wook Song, Yunseong Lee, Andrew Chung, Zhengping Qian, Brian Cho, Byung-Gon Chun. EuroSys 2017.
- [PerfAnalysis](https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-ousterhout.pdf). Making Sense of Performance in
Data Analytics Frameworks. Kay Ousterhout, Ryan Rasti, Sylvia Ratnasamy, Scott Shenker, Byung-Gon Chun. NSDI 2015.

### High-level Data Processing Programming 
- [Hive](http://infolab.stanford.edu/~ragho/hive-icde2010.pdf). Hive – A Petabyte Scale Data Warehouse Using Hadoop. Ashish Thusoo, Joydeep Sen Sarma, Namit Jain, Zheng Shao, Prasad Chakka, Ning Zhang, Suresh Antony, Hao Liu and Raghotham Murthy. ICDE 2010.
- [Pig](http://infolab.stanford.edu/~olston/publications/sigmod08.pdf). Pig Latin: A Not-So-Foreign Language for Data Processing. Christopher Olston, Benjamin Reed, Utkarsh Srivastava, Ravi Kumar, Andrew Tomkins. SIGMOD 2008.
- [FlumeJava](http://pages.cs.wisc.edu/~akella/CS838/F12/838-CloudPapers/FlumeJava.pdf). FlumeJava: Easy, Efﬁcient Data-Parallel Pipelines. Craig Chambers, Ashish Raniwala, Frances Perry, Stephen Adams, Robert R. Henry, Robert Bradshaw, Nathan Weizenbaum. PLDI 2010.
- [DryadLINQ](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/yu_y/yu_y.pdf). DryadLINQ: A System for General-Purpose Distributed Data-Parallel Computing Using a High-Level Language. Yuan Yu, Michael Isard, Dennis Fetterly, Mihai Budiu, Úlfar Erlingsson, Pradeep Kumar Gunda, Jon Currey. OSDI 2008.
- [SCOPE](www.vldb.org/pvldb/1/1454166.pdf). SCOPE: Easy and Efficient Parallel Processing of Massive Data Sets. Ronnie Chaiken, Bob Jenkins, Per-Åke Larson, Bill Ramsey, Darren Shakib, Simon Weaver, Jingren Zhou. VLDB 2008. 
- [Beam](https://beam.apache.org/). Apache Beam.

### Stream Processing
- [Storm](http://db.cs.berkeley.edu/cs286/papers/storm-sigmod2014.pdf). Storm @ Twitter. Ankit Toshniwal, Siddarth Taneja, Amit Shukla, Karthik Ramasamy, Jignesh M. Patel, Sanjeev Kulkarni, Jason Jackson, Krishna Gade, Maosong Fu, Jake Donham, Nikunj Bhagat, Sailesh Mittal, Dmitriy Ryaboy. SIGMOD 2014.
- [Heron](https://pdfs.semanticscholar.org/e847/c3ec130da57328db79a7fea794b07dbccdd9.pdf). Twitter Heron: Stream Processing at Scale. Sanjeev Kulkarni, Nikunj Bhagat, Maosong Fu, Vikas Kedigehalli, Christopher Kellogg, Sailesh Mittal, Jignesh M. Patel, Karthik Ramasamy, Siddarth Taneja. SIGMOD 2015.
- [SparkStreaming](https://people.csail.mit.edu/matei/papers/2013/sosp_spark_streaming.pdf). Discretized Streams: Fault-Tolerant Streaming Computation at Scale. Matei Zaharia, Tathagata Das, Haoyuan Li, Timothy Hunter, Scott Shenker, Ion Stoica. SOSP 2013.
- [Flink](http://flink.apache.org/). Apache Flink.
- [StreamScope](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-lin-wei.pdf). StreamScope: Continuous Reliable Distributed Processing of Big Data Streams. Wei Lin, Haochuan Fan, Zhengping Qian, Junwei Xu, Sen Yang, Jingren Zhou, Lidong Zhou. NSDI 2016.
- [MillWheel](http://research.google.com/pubs/archive/41378.pdf). MillWheel: Fault-Tolerant Stream Processing at Internet Scale. Tyler Akidau, Alex Balikov, Kaya Bekiroglu, Slava Chernyak, Josh Haberman, Reuven Lax, Sam McVeety, Daniel Mills, Paul Nordstrom, Sam Whittle. VLDB 2013.
- [Dataflow](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43864.pdf). The Dataflow Model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing. Tyler Akidau, Robert Bradshaw, Craig Chambers, Slava Chernyak, Rafael J. Fernandez-Moctezuma, Reuven Lax, Sam McVeety, Daniel Mills, Frances Perry, Eric Schmidt, Sam Whittle. VLDB 2015.
- [Samza](http://www.vldb.org/pvldb/vol10/p1634-noghabi.pdf). Samza: Stateful Scalable Stream Processing at LinkedIn. Shadi A. Noghabi, Kartik Paramasivam,  Yi Pan, Navina Ramesh, Jon Bringhurst, Indranil Gupta,  Roy H. Campbell. VLDB 2017.
- [RealtimeFacebook](http://web.eecs.umich.edu/~mosharaf/Readings/Facebook-Streaming.pdf). Realtime Data Processing at Facebook. Guoqiang Jerry Chen, Janet L. Wiener, Shridhar Iyer, Anshul Jaiswal, Ran Lei, Nikhil Simha, Wei Wang, Kevin Wilfong, Tim Williamson, Serhat Yilmaz. SIGMOD 2016.
- [Trill](http://www.vldb.org/pvldb/vol8/p401-chandramouli.pdf). Trill: A High-Performance Incremental Query Processor for Diverse Analytics. Badrish Chandramouli, Jonathan Goldstein, Mike Barnett, Robert DeLine, Danyel Fisher, John C. Platt, James F. Terwilliger, John Wernsing. VLDB 2014.
- [SEEP](http://lsds.doc.ic.ac.uk/sites/default/files/sigmod13-seep.pdf). Integrating Scale Out and Fault Tolerance in Stream Processing using Operator State Management. Raul Castro Fernandez, Matteo Migliavacca, Evangelia Kalyvianaki, Peter Pietzuch. SIGMOD 2013.

### Machine Learning/Deep Learning
- [PS](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-li_mu.pdf). Scaling Distributed Machine Learning with the Parameter Server. Mu Li, David G. Andersen, Jun Woo Park, Alexander J. Smola, Amr Ahmed, Vanja Josifovski, James Long, Eugene J. Shekita, and Bor-Yiing Su. OSDI 2014.
- [Petuum](http://www.cs.cmu.edu/~seunghak/petuum_kdd15.pdf). Petuum: A New Platform for Distributed Machine Learning on Big Data. Eric P. Xing, Qirong Ho, Wei Dai, Jin Kyu Kim, Jinliang Wei, Seunghak Lee, Xun Zheng, Pengtao Xie, Abhimanu Kumar, and Yaoliang Yu. KDD 2015.
- [Adam](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-chilimbi.pdf). Project Adam: Building an Efficient and Scalable Deep Learning Training System. Trishul Chilimbi, Yutaka Suzue, Johnson Apacible, and Karthik Kalyanaraman. OSDI 2014.
- [TensorFlow](https://www.usenix.org/system/files/conference/osdi16/osdi16-abadi.pdf). TensorFlow: A System for Large-Scale
Machine Learning. Martín Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Geoffrey Irving, Michael Isard, Manjunath Kudlur, Josh Levenberg, Rajat Monga, Sherry Moore, Derek G. Murray, Benoit Steiner, Paul Tucker, Vijay Vasudevan, Pete Warden, Martin Wicke, Yuan Yu, Xiaoqiang Zheng. OSDI 2016.
- [TenorFlowDCF](https://arxiv.org/pdf/1805.01772.pdf). Dynamic Control Flow in Large-Scale Machine Learning. Yuan Yu, Martin Abadi, Paul Barham, Eugene Brevdo, Mike Burrows, Andy Davis, Jeff Dean, Sanjay Ghemawat, Tim Harley, Peter Hawkins, Michael Isard, Manjunath Kudlur, Rajat Monga, Derek Murray, Xiaoqiang Zheng. EuroSys 2018.
- [RDAG](http://spl.snu.ac.kr/wp-content/uploads/2018/04/eurosys18-rdag.pdf). Improving the Expressiveness of Deep Learning Frameworks with Recursion. Eunji Jeong*, Joo Seong Jeong*, Soojeong Kim, Gyeong-In Yu, Byung-Gon Chun. EuroSys 2018.
- [Parallax](https://arxiv.org/pdf/1808.02621.pdf). Parallax: Automatic Data-Parallel Training of Deep Neural Networks. Soojeong Kim, Gyeong-In Yu, Hojin Park, Sungwoo Cho, Eunji Jeong, Hyeonmin Ha, Sanha Lee, Joo Seong Jeong, Byung-Gon Chun. arXiv:1808.02621, August 2018.
- [Caffe2](https://caffe2.ai/). Caffe2: A New Lightweight, Modular, and Scalable Deep Learning Framework.
- [PyTorch](https://pytorch.org/). PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration.
- [Torch](http://torch.ch/). Torch: A Scientific Computing Framework for LuaJIT.
- [MXNet](https://arxiv.org/pdf/1512.01274.pdf) MXNet: A Flexible and Efficient Machine Learning Library for Heterogeneous Distributed Systems. Tianqi Chen, Mu Li, Yutian Li, Min Lin, Naiyan Wang, Minjie Wang, Tianjun Xiao,  Bing Xu, Chiyuan Zhang, Zheng Zhang. arXiv:1512.01274v1. Dec. 3, 2015. (Web site: http://mxnet.io)
- [Caffe](http://ucb-icsi-vision-group.github.io/caffe-paper/caffe.pdf). Caffe: Convolutional Architecture for Fast Feature Embedding. Yangqing Jia, Evan Shelhamer, Jeff Donahue, Sergey Karayev, Jonathan Long, Ross Girshick, Sergio Guadarrama, Trevor Darrell. ACM Multimedia 2014.
- [DistBelief](https://static.googleusercontent.com/media/research.google.com/en//archive/large_deep_networks_nips2012.pdf). Large Scale Distributed Deep Networks. Jeffrey Dean, Greg S. Corrado, Rajat Monga, Kai Chen, Matthieu Devin, Quoc V. Le, Mark Z. Mao, Marc’Aurelio Ranzato, Andrew Senior, Paul Tucker, Ke Yang, Andrew Y. Ng. NIPS 2012.
- [BaiduDL](https://cs.stanford.edu/~acoates/papers/CoatesHuvalWangWuNgCatanzaro_icml2013.pdf). Deep learning with COTS HPC systems. Adam Coates, Brody Huval, Tao Wang, David J. Wu, Andrew Y. Ng, Bryan Catanzaro. ICML 2013.
- [DyNet](https://arxiv.org/pdf/1701.03980.pdf). DyNet: The Dynamic Neural Network Toolkit. Graham Neubig, Chris Dyer, Yoav Goldberg, Austin Matthews, Waleed Ammar, Antonios Anastasopoulos, Miguel Ballesteros, David Chiang, Daniel Clothiaux, Trevor Cohn, Kevin Duh, Manaal Faruqui, Cynthia Gan, Dan Garrette, Yangfeng Ji, Lingpeng Kong, Adhiguna Kuncoro, Gaurav Kumar, Chaitanya Malaviya, Paul Michel, Yusuke Oda, Matthew Richardson, Naomi Saphra, Swabha Swayamdipta, Pengcheng Yin. 2017
- [PRETZEL] PRETZEL: Opening the Black Box of Machine Learning Prediction Serving Systems. Yunseong Lee, Alberto Scolari, Byung-Gon Chun, Marco Domenico Santambrogio, Markus Weimer, Matteo Interlandi. OSDI 2018.
- [TPU](https://arxiv.org/pdf/1704.04760.pdf). In-Datacenter Performance Analysis of a Tensor Processing Unit. Norman P. Jouppi, Cliff Young, Nishant Patil, David Patterson, Gaurav Agrawal, Raminder Bajwa, Sarah Bates,
Suresh Bhatia, Nan Boden, Al Borchers, Rick Boyle, Pierre-luc Cantin, Clifford Chao, Chris Clark, Jeremy Coriell,
Mike Daley, Matt Dau, Jeffrey Dean, Ben Gelb, Tara Vazir Ghaemmaghami, Rajendra Gottipati, William Gulland,
Robert Hagmann, C. Richard Ho, Doug Hogberg, John Hu, Robert Hundt, Dan Hurt, Julian Ibarz, Aaron Jaffey, Alek
Jaworski, Alexander Kaplan, Harshit Khaitan, Daniel Killebrew, Andy Koch, Naveen Kumar, Steve Lacy, James Laudon,
James Law, Diemthu Le, Chris Leary, Zhuyuan Liu, Kyle Lucke, Alan Lundin, Gordon MacKean, Adriana Maggiore,
Maire Mahony, Kieran Miller, Rahul Nagarajan, Ravi Narayanaswami, Ray Ni, Kathy Nix, Thomas Norrie, Mark Omernick,
Narayana Penukonda, Andy Phelps, Jonathan Ross, Matt Ross, Amir Salek, Emad Samadiani, Chris Severn, Gregory Sizikov,
Matthew Snelham, Jed Souter, Dan Steinberg, Andy Swing, Mercedes Tan, Gregory Thorson, Bo Tian, Horia Toma,
Erick Tuttle, Vijay Vasudevan, Richard Walter, Walter Wang, Eric Wilcox, and Doe Hyun Yoon. ISCA 2017.
- [Theano](https://arxiv.org/pdf/1605.02688.pdf). Theano: A Python framework for fast computation of mathematical expressions. Rami Al-Rfou, Guillaume Alain, Amjad Almahairi, Christof Angermueller, Dzmitry Bahdanau, Nicolas Ballas, Frédéric Bastien, Justin Bayer, Anatoly Belikov, Alexander Belopolsky, Yoshua Bengio, Arnaud Bergeron, James Bergstra, Valentin Bisson, Josh Bleecher Snyder, Nicolas Bouchard, Nicolas Boulanger-Lewandowski, Xavier Bouthillier, Alexandre de Brébisson, Olivier Breuleux, Pierre-Luc Carrier, Kyunghyun Cho, Jan Chorowski, Paul Christiano, Tim Cooijmans, Marc-Alexandre Côté, Myriam Côté, Aaron Courville, Yann N. Dauphin, Olivier Delalleau, Julien Demouth, Guillaume Desjardins, Sander Dieleman, Laurent Dinh, Mélanie Ducoffe, Vincent Dumoulin, Samira Ebrahimi Kahou, Dumitru Erhan, Ziye Fan, Orhan Firat, Mathieu Germain, Xavier Glorot, Ian Goodfellow, Matt Graham, Caglar Gulcehre, Philippe Hamel, Iban Harlouchet, Jean-Philippe Heng, Balázs Hidasi, Sina Honari, Arjun Jain, Sébastien Jean, Kai Jia, Mikhail Korobov, Vivek Kulkarni, Alex Lamb, Pascal Lamblin, Eric Larsen, César Laurent, Sean Lee, Simon Lefrancois, Simon Lemieux, Nicholas Léonard, Zhouhan Lin, Jesse A. Livezey, Cory Lorenz, Jeremiah Lowin, Qianli Ma, Pierre-Antoine Manzagol, Olivier Mastropietro, Robert T. McGibbon, Roland Memisevic, Bart van Merriënboer, Vincent Michalski, Mehdi Mirza, Alberto Orlandi, Christopher Pal, Razvan Pascanu, Mohammad Pezeshki, Colin Raffel, Daniel Renshaw, Matthew Rocklin, Adriana Romero, Markus Roth, Peter Sadowski, John Salvatier, François Savard, Jan Schlüter, John Schulman, Gabriel Schwartz, Iulian Vlad Serban, Dmitriy Serdyuk, Samira Shabanian, Étienne Simon, Sigurd Spieckermann, S. Ramana Subramanyam, Jakub Sygnowski, Jérémie Tanguay, Gijs van Tulder, Joseph Turian, Sebastian Urban, Pascal Vincent, Francesco Visin, Harm de Vries, David Warde-Farley, Dustin J. Webb, Matthew Willson, Kelvin Xu, Lijun Xue, Li Yao, Saizheng Zhang, Ying Zhang. arXiv:1605.02688. May 9, 2016.

### Graph Processing
- [Pregel](http://kowshik.github.io/JPregel/pregel_paper.pdf). Pregel: A System for Large-Scale Graph Processing. Grzegorz Malewicz, Matthew H. Austern, Aart J. C. Bik, James C. Dehnert, Ilan Horn, Naty Leiser, and Grzegorz Czajkowski. SIGMOD 2010. 
- [GraphLab](https://arxiv.org/pdf/1006.4990.pdf). GraphLab: A New Framework For Parallel Machine Learning. Yucheng Low, Joseph Gonzalez, Aapo Kyrola, Danny Bickson, Carlos Guestrin, Joseph M. Hellerstein. UAI 2010.
- [DistributedGraphLab](http://vldb.org/pvldb/vol5/p716_yuchenglow_vldb2012.pdf). Distributed GraphLab: A Framework for Machine Learning and Data Mining in the Cloud. Yucheng Low, Joseph Gonzalez, Aapo Kyrola, Danny Bickson, Carlos Guestrin, Joseph M. Hellerstein. VLDB 2012.
- [PowerGraph](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-167.pdf). PowerGraph: Distributed Graph-Parallel Computation on Natural Graphs. Joseph E. Gonzalez, Yucheng Low, Haijie Gu, Danny Bickson, Carlos Guestrin. OSDI 2012.
- [PowerLyra](https://pdfs.semanticscholar.org/b58c/cf23de1566df0fd10bfe24bd717ed47a2025.pdf). PowerLyra: Differentiated Graph Computation and Partitioning on Skewed Graphs. Rong Chen, Jiaxin Shi, Yanzhe Chen, Haibo Chen. EuroSys 2015.
- [Gemini](https://www.usenix.org/system/files/conference/osdi16/osdi16-zhu.pdf). Gemini: A Computation-Centric Distributed
Graph Processing System. Xiaowei Zhu, Wenguang Chen, Weimin Zheng, Xiaosong Ma. OSDI 2016.
- [GraphX](https://amplab.cs.berkeley.edu/wp-content/uploads/2014/09/graphx.pdf). GraphX: Graph Processing in a Distributed Dataflow Framework. Joseph E. Gonzalez, Reynold S. Xin, Ankur Dave, Daniel Crankshaw, Michael J. Franklin, Ion Stoica. OSDI 2014.
- [Arabesque](https://arxiv.org/pdf/1510.04233.pdf). Arabesque: A System for Distributed Graph Mining Extended version. Carlos H. C. Teixeira, Alexandre J. Fonseca, Marco Serafini, Georgos Siganos, Mohammed J. Zaki, Ashraf Aboulnaga. Shorter version appeared at SOSP 2015.
- [Giraph](https://research.fb.com/wp-content/uploads/2016/11/one-trillion-edges-graph-processing-at-facebook-scale.pdf?). One Trillion Edges: Graph Processing at Facebook-Scale. Avery Ching, Sergey Edunov, Maja Kabiljo, Dionysios Logothetis, Sambavi Muthukrishnan. VLDB 2015.

### Distributed Store
- [GFS](http://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf). The Google File System. Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung. SOSP 2003. 
- [Bigtable](http://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf). Bigtable: A Distributed Storage System for Structured Data. Fay Chang, Jeffrey Dean, Sanjay Ghemawat, Wilson C. Hsieh, Deborah A. Wallach, Mike Burrows, Tushar Chandra, Andrew Fikes, Robert E. Gruber. OSDI 2006.
- [Dynamo](http://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf). Dynamo: Amazon’s Highly Available Key-value Store. Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall and Werner Vogels. SOSP 2007.
- [Spanner](http://research.google.com/archive/spanner-osdi2012.pdf). Spanner: Google’s Globally-Distributed Database. James C. Corbett, Jeffrey Dean, Michael Epstein, Andrew Fikes, Christopher Frost, JJ Furman, Sanjay Ghemawat, Andrey Gubarev, Christopher Heiser, Peter Hochschild, Wilson Hsieh, Sebastian Kanthak, Eugene Kogan, Hongyi Li, Alexander Lloyd, Sergey Melnik, David Mwaura, David Nagle, Sean Quinlan, Rajesh Rao, Lindsay Rolig, Yasushi Saito, Michal Szymaniak, Christopher Taylor, Ruth Wang, Dale Woodford. OSDI 2012.
- [Memcache](https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf). Scaling Memcache at Facebook. Rajesh Nishtala, Hans Fugal, Steven Grimm, Marc Kwiatkowski, Herman Lee, Harry C. Li, Ryan McElroy, Mike Paleczny, Daniel Peek, Paul Saab, David Stafford, Tony Tung, Venkateshwaran Venkataramani. NSDI 2013. 
- [TAO](http://0b4af6cdc2f0c5998459-c0245c5c937c5dedcca3f1764ecc9b2f.r43.cf2.rackcdn.com/11730-atc13-bronson.pdf). TAO: Facebook’s Distributed Data Store for the Social Graph. Nathan Bronson, Zach Amsden, George Cabrera, Prasad Chakka, Peter Dimov, Hui Ding,Jack Ferris, Anthony Giardullo, Sachin Kulkarni, Harry Li, Mark Marchukov, Dmitri Petrov, Lovro Puzar, Yee Jiun Song, Venkat Venkataramani. USENIX ATC 2013.

### Coordination
- [Chubby](https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf). The Chubby lock service for loosely-coupled distributed systems. Mike Burrows. OSDI 2006.
- [Zookeeper](https://www.usenix.org/legacy/event/usenix10/tech/full_papers/Hunt.pdf). ZooKeeper: Wait-free coordination for Internet-scale systems. Patrick Hunt, Mahadev Konar, Flavio P. Junqueira, Benjamin Reed. ATC 2010. 
