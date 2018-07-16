import json

from rest_framework.renderers import JSONRenderer
from aggregator.apps.aggregator.renderers import AggregatorJSONRenderer


class UserJSONRenderer(AggregatorJSONRenderer):
    charset = 'utf-8'
    object_label = 'user'

    def render(self, data, media_type=None, renderer_context=None):
        # If we receive a `token` key as part of the response, it will be a
        # byte object. Byte objects don't serialize well, so we need to
        # decode it before rendering the User object.
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            # Also as mentioned above, we will decode `token` if it is of type
            # bytes.
            data['token'] = token.decode('utf-8')

        # Finally, we can render our data under the "user" namespace.
        return json.dumps({
            'user': data
        })


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)
        token = data.get('token', None)

        if errors is not None:
            return super(UserJSONRenderer, self).render(data)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')
        return json.dumps({
            'user': data
        })

        return super (UserJSONRenderer, self).render (data)