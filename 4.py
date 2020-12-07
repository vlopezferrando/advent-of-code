import re

# Read rows
rows = ['']
for line in open('input').read().splitlines():
    if line == '':
        rows.append('')
    else:
        rows[-1] += ' ' + line

# Part 1
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with_required_fields = []
for row in rows:
    fields = {
        field.split(':')[0]: field.split(':')[1]
        for field in row.split(' ')[1:]
    }
    if all(f in fields for f in required_fields):
        with_required_fields.append(fields)
print(len(with_required_fields))

# Part 2
valid = []
for d in with_required_fields:
    try:
        byr = int(d['byr'])
        assert(1920 <= byr and byr <= 2002)

        iyr = int(d['iyr'])
        assert(2010 <= iyr and iyr <= 2020)

        eyr = int(d['eyr'])
        assert(2020 <= eyr and eyr <= 2030)

        hgt, hgt_unit = int(d['hgt'][:-2]), d['hgt'][-2:]
        if hgt_unit == 'cm':
            assert(150 <= hgt and hgt <= 193)
        elif hgt_unit == 'in':
            assert(59 <= hgt and hgt <= 76)
        else:
            raise

        assert(re.fullmatch(r'#[0-9a-f]{6}', d['hcl']))

        assert(re.fullmatch(r'\d{9}', d['pid']))

        assert(d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

        valid.append(d)
    except:
        pass
print(len(valid))
