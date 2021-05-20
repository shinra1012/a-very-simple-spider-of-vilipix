It is **a very simple** spider case for vilipix (A mirror of pixiv), based on selenium.

At now , The only function of this program is to get all the images of daily rank. (Default : from 20201220 to 20210520 ,by set the check_point to default_check_point). But other functions can be created easily by lightly changing the code.

Chrome is necessary. I test it on Ubuntu. (Chrome Driver may be necessary if you are using Windows.)

The images will be saved to different dir , divided by the author of the image .Check the parser. (Default like ./output/1 ,./output/2 , ...)

When stopped, It will save the statement automatically. Feel free to stop it. Once saved, do not forget to change the check_point setting to your own.

As some authors' dir were deleted , the program would no longer save his ( or her) works. However you are supposed to do that when the program is stopped. As the check function only works when the program is starting. 

**The ownership of the images belongs to the author.**

