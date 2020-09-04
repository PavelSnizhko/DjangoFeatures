REVIEW_SCHEMA = {
    '$schema': 'https://json-schema.org/#schema',
    'type': 'object',
    'properties': {
        'feedback': {
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
    'required': ['feedback', 'grade']
}