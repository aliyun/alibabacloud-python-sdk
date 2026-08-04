# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IdpDingtalkSubConfig(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        corp_id: str = None,
        event_aes_key: str = None,
        event_label: str = None,
        event_verify_token: str = None,
        exclusive: bool = None,
        oauth: bool = None,
        redirect_uri: str = None,
    ):
        # Your application\\"s unique identifier. You can get this identifier from the DingTalk Open Platform.
        self.app_key = app_key
        # Your application\\"s secret key. You can get this key from the DingTalk Open Platform.
        self.app_secret = app_secret
        # Your enterprise\\"s unique ID in DingTalk.
        self.corp_id = corp_id
        # The AES key used to decrypt the content of event callbacks. This ensures the confidentiality of the event data.
        self.event_aes_key = event_aes_key
        # A custom label for event subscriptions. This field is reserved for future use.
        self.event_label = event_label
        # The token used to verify the authenticity of event callback requests from DingTalk.
        self.event_verify_token = event_verify_token
        # Specifies whether this identity provider is the exclusive login method. If set to `true`, other login methods are disabled.
        self.exclusive = exclusive
        # Specifies whether to enable the OAuth authentication flow.
        self.oauth = oauth
        # The URL where the user is redirected after successful authorization. You must register this URL on the DingTalk Open Platform.
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.event_aes_key is not None:
            result['EventAesKey'] = self.event_aes_key

        if self.event_label is not None:
            result['EventLabel'] = self.event_label

        if self.event_verify_token is not None:
            result['EventVerifyToken'] = self.event_verify_token

        if self.exclusive is not None:
            result['Exclusive'] = self.exclusive

        if self.oauth is not None:
            result['Oauth'] = self.oauth

        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('EventAesKey') is not None:
            self.event_aes_key = m.get('EventAesKey')

        if m.get('EventLabel') is not None:
            self.event_label = m.get('EventLabel')

        if m.get('EventVerifyToken') is not None:
            self.event_verify_token = m.get('EventVerifyToken')

        if m.get('Exclusive') is not None:
            self.exclusive = m.get('Exclusive')

        if m.get('Oauth') is not None:
            self.oauth = m.get('Oauth')

        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')

        return self

