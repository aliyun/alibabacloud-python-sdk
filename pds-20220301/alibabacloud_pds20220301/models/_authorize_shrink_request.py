# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeShrinkRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        hide_consent: bool = None,
        login_type: str = None,
        redirect_uri: str = None,
        response_type: str = None,
        scope_shrink: str = None,
        state: str = None,
    ):
        # The application ID returned when the application was created.
        # 
        # This parameter is required.
        self.client_id = client_id
        # Specifies whether to hide the consent page.
        self.hide_consent = hide_consent
        # The authentication method. Valid values:
        # 
        # *   default: all logon methods that are integrated on the default logon page provided by Drive and Photo Service.
        # *   ding: logs on by scanning a DingTalk QR code.
        # *   ding_sns: logs on by entering a DingTalk account and its password.
        # *   ram: logs on as an Alibaba Cloud Resource Access Management (RAM) user.
        # *   wechat: logs on by scanning a WeCom QR code.
        # *   wechat_app: logs on without authentication in WeCom.
        # 
        # This parameter is required.
        self.login_type = login_type
        # The callback URL specified when the application was created.
        # 
        # This parameter is required.
        self.redirect_uri = redirect_uri
        # The format in which to return the response. Set the value to code.
        # 
        # This parameter is required.
        self.response_type = response_type
        # The requested permissions. By default, all permissions are requested.
        self.scope_shrink = scope_shrink
        # The user-defined parameter to return in the callback URL after the requested permissions are granted.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['client_id'] = self.client_id

        if self.hide_consent is not None:
            result['hide_consent'] = self.hide_consent

        if self.login_type is not None:
            result['login_type'] = self.login_type

        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri

        if self.response_type is not None:
            result['response_type'] = self.response_type

        if self.scope_shrink is not None:
            result['scope'] = self.scope_shrink

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')

        if m.get('hide_consent') is not None:
            self.hide_consent = m.get('hide_consent')

        if m.get('login_type') is not None:
            self.login_type = m.get('login_type')

        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')

        if m.get('response_type') is not None:
            self.response_type = m.get('response_type')

        if m.get('scope') is not None:
            self.scope_shrink = m.get('scope')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

