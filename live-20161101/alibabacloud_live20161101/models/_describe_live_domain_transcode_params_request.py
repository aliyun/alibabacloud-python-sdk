# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainTranscodeParamsRequest(DaraModel):
    def __init__(
        self,
        security_token: str = None,
        app: str = None,
        pushdomain: str = None,
        template_name: str = None,
    ):
        self.security_token = security_token
        # This parameter is required.
        self.app = app
        # This parameter is required.
        self.pushdomain = pushdomain
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.app is not None:
            result['app'] = self.app

        if self.pushdomain is not None:
            result['pushdomain'] = self.pushdomain

        if self.template_name is not None:
            result['template_name'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('app') is not None:
            self.app = m.get('app')

        if m.get('pushdomain') is not None:
            self.pushdomain = m.get('pushdomain')

        if m.get('template_name') is not None:
            self.template_name = m.get('template_name')

        return self

