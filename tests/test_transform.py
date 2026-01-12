from src.pipeline.transform import transform_data


def test_transform_filters_underage():
    input_data = [
        {"id": 1, "name": "A", "age": 10},
        {"id": 2, "name": "B", "age": 18},
        {"id": 3, "name": "C", "age": 30},
    ]

    result = transform_data(input_data)

    assert len(result) == 2
    assert all(row["age"] >= 18 for row in result)
