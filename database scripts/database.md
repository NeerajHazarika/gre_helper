# TABLE: questions
```
questions (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    img_src TEXT,
    topic TEXT,
    type TEXT,
    passage_chart_img_src TEXT,
    correct_ans TEXT,
    section TEXT
)
```

# TABLE: tests
```
tests (
    test_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_set_list TEXT
)
```

# TABLE: attempt
```
attempts (
    attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    validity INTEGER,
    test_id INTEGER ALTERNATE KEY,
    submission TEXT,
    time_created TEXT,
    tips TEXT,
    recommended_test_id ALTERNATE KEY,
)
```
