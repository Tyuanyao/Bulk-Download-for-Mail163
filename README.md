# Bulk-Download-for-Mail163 (批量下载163邮箱附件)

## English Destription
This repository include  the code for Bulk Download in 163 mailbox, it has two step:
* Automatically log in 163 mail box
* and download the mail attachments in bulk for a time range

I write this code for the convience of quickly receiving the students' homework from 163 mail box since I start to be a TA at the university last year 2018.

### what is the convience?
By running this code, you can download the mail attachements in bulk by setting the time period you want, i.e. change the value of variable **upper** and **lower** in the code, and you are no longer need to open every mail to download the mail attachment one by one, which is really exhuasted if you have over 100 students in the class like me.

If your university have the system to receive homeworks from every student online, I admire you.

### Preparation
1. Make sure you have installed the [chromedriver](http://chromedriver.chromium.org/).
2. This code require Python package [Selenium](https://pypi.org/project/selenium/).

### How to use it
1. Change the  chromedriver path :
>  chromedriver = "C:/Users/***/AppData/Local/Google/Chrome/Application/chromedriver.exe"
2. Set your time range by changing the two variable:
> lower = 20190628      #from
  upper = int(time.strftime("%Y%m%d", time.localtime()))  #to

3.  Set your own mail account and password:
> inputText.send_keys("youracountname")
> password.send_keys("yourpassword")
4. Run it

## 中文说明
这个项目包含批量下载163邮箱附件的代码，代码的操作分为两步：
* 自动模拟登陆163邮箱
* 批量下载指定时间范围内的邮件附件。

自我去年2018年开始当助教之后，就编写了这份代码方便我收作业。

### 有什么方便？
通过修改程序里的两个变量值**upper** 和 **lower**，指定时间范围，就可以下载在这个范围内所有邮件的附件，再也不需要一封封邮件打开下载附件，如果你需要连续收100多份作业，一封封邮件打开会非常心酸。

如果你们大学有那种线上收作业的系统，我羡慕你。

### 准备
1. 确保安装了 [chromedriver](http://chromedriver.chromium.org/).
2. 这份程序需要Python包 [Selenium](https://pypi.org/project/selenium/).

### 如何使用
1. 修改chromedriver路径:
>  chromedriver = "C:/Users/***/AppData/Local/Google/Chrome/Application/chromedriver.exe"
2. 通过修改两个变量值设置你需要的时间范围:
> lower = 20190628      #from
  upper = int(time.strftime("%Y%m%d", time.localtime()))  #to

3. 设置你自己的邮箱用户名和密码:
> inputText.send_keys("youracountname")
> password.send_keys("yourpassword")
4. 运行
