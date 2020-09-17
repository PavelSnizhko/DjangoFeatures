REVIEW_SCHEMA = {
    '$schema': 'https://json-schema.org/#schema',
    'type': 'object',
    'properties': {
        'django_project': {
            'type': 'string',
            'minLength': 10,
            'macLength': 33,
        },
        'grade': {
            'type': 'integer',
            'minimum': 1,
            'maximum': 100
        },
    },
    'required': ['django_project', 'grade']
}