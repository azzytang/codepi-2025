boulder_progress = iter([1])

if dialogue := next(boulder_progress, None):
    print(dialogue)
else:
    print('none')
