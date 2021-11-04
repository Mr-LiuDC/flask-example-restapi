# flask-example-restapi

## 环境准备

创建虚拟环境

```bash
# python3.5以上版本
python -m venv /path/to/venv
# 或者用 virtualenv
virtualenv --no-site-packages venv

# 激活虚拟环境
./path/to/venv/Scripts/activate
```

安装所需依赖

```bash
pip install -r requirements.txt
# 或者指定加速源
pip install -r requirements.txt -i https://pypi.douban.com/simple/
```

导出所有依赖

```bash
pip freeze
# 或者输出到文件
pip freeze > requirements.txt
```

## 数据准备

初始化数据库

```bash
flask db init
flask db migrate
# 或者添加备注信息
flask db migrate -m "Initial migration"
flask db upgrade
flask db history
flask db downgrade 版本号
```
