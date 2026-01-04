# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        service_code: str = None,
    ):
        # The supported natural language. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US** (default): English
        # *   **ja**: Japanese
        self.accept_language = accept_language
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate this value. Ensure that the value is unique among all requests. Only ASCII characters are allowed.
        # 
        # >  If you do not specify this parameter, the value of **RequestId** is used.**** **RequestId** of each request is different.
        self.client_token = client_token
        # The service code. Set the value to **nlb**.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        return self

