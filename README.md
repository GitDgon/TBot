Windows:  
`python3 -m venv myvenv`
`myvenv\Scripts\activate`

`status -v `
`git status --ignored`

Откатить до определенного commita на Githab
`git reset --hard <hash коммита: ea06...dd7v>`

Сохранение на GIT:
`git add .`
`git commit -m "Изменил модель bd svs_k"`
`git push origin master`

Сохранение библиотек:
`pip freeze > reqiurements.txt`
install requirements: 
`pip install -r requirements.txt`
