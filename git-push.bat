@echo off
cd  /d D:/Projects/Error-Collection-Notes/Math-Exercises
git add .
git commit -m "自动同步： %date % %time%"
git push ssh://ztx@192.168.0.102:20032/home/ztx/git-repos/math-notes.git main
echo “自动推送完成”
pause