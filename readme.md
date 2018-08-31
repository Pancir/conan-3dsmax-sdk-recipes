# Conan recipe for wrapping 3Ds Max's SDK
License [BSD (3-Clause)](http://opensource.org/licenses/BSD-3-Clause) read the [License](license.txt) file.  
We are not allowed to distribute 3Ds Max's SDK, so you have to get it yourself.
Usually 3Ds Max's SDK is located on installation disk.  
This is the set of python scripts for generating simple conan recipes
for placement 3Ds Max's SDKs into your own conan repository.  
Although the recipes don't constrain you to use any settings,
they can be used only for windows and for the x64 3Ds Max SDK.


## Dependencies
- [Cmake 3.7+](https://cmake.org)
- [Conan 1.6+](https://www.conan.io)
- [Python 2 or 3](https://www.python.org)


## Warning
The conan must be installed with `pip`, 
the pip is included in the python installation package, 
so if you have installed the python correctly, 
you don't need to install the pip separately.  
If the conan is not installed with the pip you'll get an error 
about `"from distutils.version import StrictVersion"`



## How to prepare and create packages
You have to prepare the file [deploy.py](deploy.py).  
Read the comments and write your own data there: 
* Specify your Visual Studio version.
* Specify 3 variables if you want to upload packages to your own conan remote.
* Specify the correct paths to 3Ds Max's SDK and 3Ds Max versions in the bottom of the file.

Then run:
```
python deploy.py
```
It will create packages for SDK and place them into you conan local cache
 so they will be available for using. It also will upload packages if it is enabled.


## Usage
In you conan file add following requirements:
```
3DsMaxSdk9/last@steptosky/stable
3DsMaxSdk2008/last@steptosky/stable
3DsMaxSdk2009/last@steptosky/stable
3DsMaxSdk2010/last@steptosky/stable
3DsMaxSdk2011/last@steptosky/stable
3DsMaxSdk2012/last@steptosky/stable
3DsMaxSdk2013/last@steptosky/stable
3DsMaxSdk2014/last@steptosky/stable
3DsMaxSdk2015/last@steptosky/stable
3DsMaxSdk2016/last@steptosky/stable
3DsMaxSdk2017/last@steptosky/stable
3DsMaxSdk2018/last@steptosky/stable
3DsMaxSdk2019/last@steptosky/stable
```

