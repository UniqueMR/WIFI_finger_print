wifi_orentation

# 室内指纹定位开发日志

## 环境配置

### 安装nginx

* 启动：start .\nginx.exe 
* 关闭：.\nginx.exe -s quit

### django

* 安装：pip install django

#### 创建项目

* django-admin startproject xxx

#### 创建应用

* django-admin startapp xxx

#### 迁移数据库

* python manage.py makemigrations 
* python manage.py migrate

#### 运行django

* python manage.py runserver

#### 项目settings.py设置

* ALLOWED_HOSTS = ['*']
* 挂载应用：将应用放入INSTALLED_APPS
* 在应用中创建templates文件夹，在'DIRS'中将templates配置为存储html的文件夹
* 设置STATIC路由'/static/'，MEDIA路由'/upload'，MEDIA目录'upload'；创建upload目录（和项目以及应用文件夹平级）

#### 项目路由urls.py设置

* from django.conf import settings
* from django.conf.urls.static import static
* 添加STATIC和MEDIA的路由
* 在应用目录中创建static目录，存储静态文件

#### 添加index路由

* 在urls.py文件中使用path的方式添加index路由，将路由指向 views.py中的函数views.index
* 在views.py中创建index函数，接收用户的request，呈现页面index.html

### 安装npm

### 安装vue/cli

### 安装mysql数据库

