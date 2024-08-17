from test_generator.priority import Priority
from test_generator.scenario import TestScenario
from test_generator.suite import Suite

SCENARIOS_STR = """## Описание

**Feature** - {feature}

**Story** - {story}

**API** - {api_method} {api_endpoint}

## Сценарии

### Позитивные
{positive_scenarios_str}

### Негативные
{negative_scenarios_str}"""

DEFAULT_SUITE = Suite(
    feature='UserFeature',
    story='UserStory',
    api_method='GET',
    api_endpoint='/path/to/endpoint',
    test_scenarios=[
        TestScenario(
            priority=Priority.P0.value,
            subject='YOUR SUBJECT',
            test_name='',
            description='YOUR DESCRIPTION',
            expected_result='YOUR EXPECTED RESULT',
            is_positive=True,
            params=[],
        ),
        TestScenario(
            priority=Priority.P2.value,
            subject='YOUR SUBJECT',
            test_name='',
            description='YOUR DESCRIPTION',
            expected_result='YOUR EXPECTED RESULT',
            is_positive=False,
            params=['param_1', 'param_2', 'param_3', 'param_4'],
        ),
    ]
)
