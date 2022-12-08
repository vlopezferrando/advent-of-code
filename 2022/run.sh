for py in *.py; do
  echo -n "Problem ${py%.py}: "
  python3 $py && echo OK || echo Fail
done
