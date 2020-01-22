### 2020-1-11
1. 建立git仓库
2. 配置vscode环境

git remote add origin git@github.com:meowsir/Python.git  
git push -u origin master  

**Branch 'master' set up to track remote branch 'master' from 'origin'.**问题解决方案
1.添加到本地仓库 
git add . 
2.添加提交描述 
git commit -m '内容' 
3.提交前先从远程仓库主分支中拉取请求 
git pull origin master 
4.把本地仓库代码提交 
git push -u origin master 