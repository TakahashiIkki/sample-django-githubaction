from django.test import TestCase


class BlogTestCase(TestCase):

    def test_post(self):
        response = self.client.post(
            '/api/blog',
            {
                "data": {
                    "type": "blog",
                    "attributes": {
                        "title": "sample",
                        "text": "aaaaaaaaaa",
                    }
                }
            },
            content_type='application/vnd.api+json')

        self.assertEqual(response.status_code, 201)
