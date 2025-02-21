test = {
  'name': 'Recap Lists and Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d = {'dog': 'bone', 'cat': 'mouse', 'bird': 'work', 'cow': 'grass'}
          >>> 'mouse' in d
          4c6983d5f50ec727a8c698b81146ec40
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> points = {'Maria':[4, 2], 'Tom':[1, 4], 'John':[1, 2]}
          >>> total = []
          >>> for i in points:
          >>>   total.append(sum(points[i]))
          >>> total
          e9f62bd2194e2169ac2d4b6433f76bf8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = [3, 6, 8, 2]
          >>> b = ['a','A','er']
          >>> c = a[3::-2]+b[:-1]
          >>> c
          3762b10dc2b83d11e87af224cba99f1c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
