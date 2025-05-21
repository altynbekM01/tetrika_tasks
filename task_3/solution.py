tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

def appearance(intervals: dict[str, list[int]]) -> int:
    def to_pairs(lst):
        return [(lst[i], lst[i + 1]) for i in range(0, len(lst), 2)]

    def clip_to_lesson(pairs, lesson_start, lesson_end):
        return [
            (max(start, lesson_start), min(end, lesson_end))
            for start, end in pairs
            if end > lesson_start and start < lesson_end
        ]

    def merge_periods(periods):
        if not periods:
            return []
        periods.sort()
        merged = [periods[0]]
        for current in periods[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
        return merged

    def intersect(pupil_periods, tutor_periods):
        result = 0
        i, j = 0, 0
        while i < len(pupil_periods) and j < len(tutor_periods):
            p_start, p_end = pupil_periods[i]
            t_start, t_end = tutor_periods[j]

            start = max(p_start, t_start)
            end = min(p_end, t_end)
            if start < end:
                result += end - start

            if p_end < t_end:
                i += 1
            else:
                j += 1
        return result

    lesson_start, lesson_end = intervals['lesson']
    pupil_periods = merge_periods(clip_to_lesson(to_pairs(intervals['pupil']), lesson_start, lesson_end))
    tutor_periods = merge_periods(clip_to_lesson(to_pairs(intervals['tutor']), lesson_start, lesson_end))

    return intersect(pupil_periods, tutor_periods)


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

