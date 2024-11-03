<!--
 * @Author: gumpcpy gumpcpy@gmail.com
 * @Date: 2024-11-01 20:06:13
 * @LastEditors: gumpcpy gumpcpy@gmail.com
 * @LastEditTime: 2024-11-03 16:37:01
 * @Description: 
-->

## 安裝python環境 (mac)
### 1-安裝 miniconda

    https://docs.anaconda.com/miniconda/miniconda-install/

### 2-安裝python

    https://www.python.org/downloads/

    查看版本

    python -V

### 3-安裝vscode

    https://code.visualstudio.com/Download

### 4-安裝 homebrew

    https://brew.sh/

查看版本

    brew --version
### 5-安裝git

    brew install git

    git --version

    git config --global user.name "Your Name"
    git config --global user.email "your_email@example.com"

    git config --list


## 建立一個新的python專案

### 1-下載github PYTHON_STARTER

    https://github.com/gumpcpy/PY_LEARN

### 2-建立虛擬環境 

進入資料夾 
my_env改成我要的環境名稱 版本用你想要用的
    
    conda create -n my_env python=3.11

啟動環境

    conda activate my_env

安裝我需要的包 conda 先試試看 不行才用 pip
    
    conda install 我需要的包

進入 PRACTICE 建立 .py
