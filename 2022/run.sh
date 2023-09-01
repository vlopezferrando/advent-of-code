for py in *.py; do
  echo -n "Problem ${py%.py}: "

  if [ "$py" = "16.py" ]; then
    g++ -o 16 -O3 16.cc
    python 16.py > 16.cc.in
    ./16 < 16.cc.in && echo OK || echo Fail
  else
    python3 $py && echo OK || echo Fail
  fi
done
