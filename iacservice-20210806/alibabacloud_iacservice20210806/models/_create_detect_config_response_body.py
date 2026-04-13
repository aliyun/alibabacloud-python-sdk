# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDetectConfigResponseBody(DaraModel):
    def __init__(
        self,
        detect_config_id: str = None,
        request_id: str = None,
    ):
        self.detect_config_id = detect_config_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detect_config_id is not None:
            result['detectConfigId'] = self.detect_config_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detectConfigId') is not None:
            self.detect_config_id = m.get('detectConfigId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

