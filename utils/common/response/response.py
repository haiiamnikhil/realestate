from django.urls import reverse


class ResponseGenerator:

    def render_response_json(self, success: bool = True,
                             message: str = '', error: str = None, redirect_url: str = None, data: dict = None, template_render: str = None, **kwargs):
        """
        redirect_url : Should be the name of view from urls.py
        """
        params = {}
        params['success'] = success
        params['message'] = message
        params['error'] = error
        params['data'] = data
        params['template_render'] = template_render
        
        if redirect_url is not None:
            params['redirect_url'] = reverse(redirect_url)
        
        if kwargs:
            for key, value in kwargs.items():
                params[key] = value
                
        return params
