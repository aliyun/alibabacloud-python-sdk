# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateTrafficControlTaskCodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        pre_need_config: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.pre_need_config = pre_need_config
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.pre_need_config is not None:
            result['PreNeedConfig'] = self.pre_need_config

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('PreNeedConfig') is not None:
            self.pre_need_config = m.get('PreNeedConfig')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

