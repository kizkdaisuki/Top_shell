#! /bin/bash

function func_init() {
  top_name=$1
  top_cmd=$2
  todo_time=$3
  todo_importance=$4
  todo_another=$5
}

func_init $1 $2 $3 $4 $5
python3 /Users/mac/kizk/project/PY/Top_shell/main.py ${top_name} ${top_cmd} ${todo_time} ${todo_importance} ${todo_another}
echo 'hello'
