for py in *.py; do
  echo "Problem ${py%.py}:"
  python $py
  echo
done
