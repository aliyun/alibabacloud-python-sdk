# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTranscodeTaskStatusRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        push_domain: str = None,
        security_token: str = None,
        stream_name: str = None,
        transcoding_template: str = None,
    ):
        self.app = app
        self.push_domain = push_domain
        self.security_token = security_token
        self.stream_name = stream_name
        self.transcoding_template = transcoding_template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.transcoding_template is not None:
            result['TranscodingTemplate'] = self.transcoding_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TranscodingTemplate') is not None:
            self.transcoding_template = m.get('TranscodingTemplate')

        return self

