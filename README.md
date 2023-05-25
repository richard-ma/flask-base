# flask-base

## 简介

## 最小Flask APP
* 创建文件: `/app/__init__.py`
* 运行命令: `flask --app app:create_app run`

## 创建目录结构
* 创建目录: `/app/templates`
* 创建文件: `/app/templates/.placeholder`
* 创建目录: `/app/templates/static`
* 创建文件: `/app/templates/static/.placeholder`
* 创建目录: `/tests`
* 创建文件: `/tests/.placeholder`
* .gitignore: 添加`instance`目录

## 配置文件最佳实践
* 修改`app/__init__.py`，确认创建instance目录
* 添加`config_sample.py`文件作为配置样本
* 建立到`config_sample.py`的软连接`config.py`
* 修改`app/__init__.py`，读取`config.py`中的配置
* .gitignore: 添加`config.py`

## 安装
* 创建`instance`目录
* 将`config_sample.py`文件复制到根目录下，并更名为`config.py`，或建立软连接