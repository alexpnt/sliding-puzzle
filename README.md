Sliding-puzzle
==============

Turn any image into a sliding puzzle 

#### Features: ####
* Control of granularity
* Puzzle/Unpuzzle an image


####Requirements:####
* python 2.x
* PIL (Python Imaging Library)

####Usage:####

    Sliding Puzzle
    
    optional arguments:
      -h, --help            show this help message and exit
      -f FILENAME, --filename FILENAME
                            input filename
      -p PASSWORD, --password PASSWORD
                            key for the random generator
      -n NSHUFFLE, --nshuffle NSHUFFLE
                            number of times to shuffle the blocks (>0)
      -g GRANULARITY, --granularity GRANULARITY
                            granularity to be used (>0): a bigger value means
                            bigger blocks, default=1
      -u, --unpuzzle        unpuzzle the image
      -s, --save            save the output image

     
####Examples:####
**Original**

![eg](https://raw.githubusercontent.com/AlexPnt/sliding-puzzle/master/img/sea.png)

**granularity 20**

![eg](https://raw.githubusercontent.com/AlexPnt/sliding-puzzle/master/img/sea_puzzled_20.png)

**granularity 14**

![eg](https://raw.githubusercontent.com/AlexPnt/sliding-puzzle/master/img/sea_puzzled_14.png)

**granularity 5**

![eg](https://raw.githubusercontent.com/AlexPnt/sliding-puzzle/master/img/sea_puzzled_5.png)

**granularity 1**

![eg](https://raw.githubusercontent.com/AlexPnt/sliding-puzzle/master/img/sea_puzzled_1.png)
