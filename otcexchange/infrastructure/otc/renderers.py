from collections import OrderedDict

from rest_framework.renderers import JSONRenderer as BaseJSONRenderer
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


class JSONRenderer(BaseJSONRenderer):
    """
    Renderer which unifies responses for all kind of request no matter is 5XX or 2XX.
    e.g. {'body': ..., 'message': ..., 'status': ...}
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """ to wrap api response in a data ,message dict context """
        if data is None:
            return b''

        rendered_data = {}
        response = renderer_context['response']
        data_type = type(data)

        if 'pagination' in data:
            rendered_data['pagination'] = data.pop('pagination')
            data = data.pop('result')

        if data_type in [dict, OrderedDict, ReturnDict]:
            # separate message part of response from data part
            if not response.exception:
                # Only in this case, if data has message in its body, if it won't remove, response gonna has two message
                message = data.pop('message') if 'message' in data else ''
                body = data
                status = data.pop('json_status') if 'json_status' in data else 'SUCCESS'
            else:
                message = data.get('detail', data)
                body = {}
                status = 'FAIL'
        elif data_type == list or data_type == ReturnList:
            if not response.exception:
                message = ''
                body = data
                status = 'SUCCESS'
            else:
                message = data
                body = {}
                if len(data) == 1:
                    message = data[0]
                status = 'FAIL'
        else:
            # response is a solid string so it should be a message
            message = data
            body = {}
            status = 'SUCCESS'

        rendered_data.update({
            'status': status, 'message': message, 'body': body
        })

        return super().render(rendered_data, accepted_media_type, renderer_context)