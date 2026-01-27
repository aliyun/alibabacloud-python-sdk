# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IdpFeishuSubConfig(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        corp_id: str = None,
        event_aes_key: str = None,
        event_label: str = None,
        event_verify_token: str = None,
        redirect_uri: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.corp_id = corp_id
        self.event_aes_key = event_aes_key
        self.event_label = event_label
        self.event_verify_token = event_verify_token
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

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

        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

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

        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')

        return self

