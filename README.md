## create-3d-graph-gif
Gets a three-dimensional dataframe and create a GIF of a three-dimensional graph base on the data.

## introduction
3D plots are a significant tool for performing data visualization. At the same time, the main problem with these plots, is that they are usually limited to a very specific angle, and present a three-dimensional reality in a two-dimensional format. Also, standard 3D display methods are usually more complex and sometimes even require complex software and additional installations for those viewing the information.

In order to overcome these gaps, the code here is designed to create GIFs from 3D data. The simple code allows you to enter a pandas dataframe object, and create a GIF output. The code allows the creation of a three-dimensional output that scans the data from any direction and creates for the viewer a feeling that it is indeed a three-dimensional display.

Also, since the output is based on a GIF file, it can be shared with people who do not have any sophisticated software. You can even transfer it via your mobile phone or share it on social networks. Example of one from the outputs:

![example](https://github.com/EtzionData/create-3d-graph-gif/blob/master/Picture/example.gif)

## libraries
The code uses the following libraries in Python:

**matplotlib**

**imageio**

**pandas**

## application
An application of the code is attached to this page under the name: 

**"implementation.py"** 
the examples outputs are also attached here.

## Using the code
To use this code, you just need to import it as follows:
``` sh
# import
from create_3d_gif import pd_to_gif
from pandas import read_csv

# define variables
data= read_csv(r'path\file.csv')
xyz = ["x","y","z"]
name= "my_gif" # you not need to add ".gif"
clrs= "colors"

# application
pd_to_gif(data ,xyz ,name ,clrs)
```

## variables

**data:** pandas dataframe object.

**xyz:** simple list that contain 3 strings. each one of them is column name inside **"data"** that you want to use it as one of your axis.

**name:** string which represents the filename of the GIF you want to save

**clrs:** optional. simple string of colors column in **"data"**. this allow to you created Colorful and varied outputs. If you do not enter this variable, all entities will be **blue** by default


