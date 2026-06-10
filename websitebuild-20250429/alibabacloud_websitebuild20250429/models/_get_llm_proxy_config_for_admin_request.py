# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLlmProxyConfigForAdminRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        capability: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Capability Type: llm, image, video
        self.capability = capability

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.capability is not None:
            result['Capability'] = self.capability

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Capability') is not None:
            self.capability = m.get('Capability')

        return self

