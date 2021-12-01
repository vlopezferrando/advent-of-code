for py in *.py; do
  echo -n "Problem ${py%.py}: "
  python3 $py | paste -sd " " -
done
