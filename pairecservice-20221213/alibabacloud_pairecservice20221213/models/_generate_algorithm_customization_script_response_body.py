# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateAlgorithmCustomizationScriptResponseBody(DaraModel):
    def __init__(
        self,
        log_id: str = None,
        oss_address: str = None,
        request_id: str = None,
    ):
        self.log_id = log_id
        self.oss_address = oss_address
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.oss_address is not None:
            result['OssAddress'] = self.oss_address

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('OssAddress') is not None:
            self.oss_address = m.get('OssAddress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

