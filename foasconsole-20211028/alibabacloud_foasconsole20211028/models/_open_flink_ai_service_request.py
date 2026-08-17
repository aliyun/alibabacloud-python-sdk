# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenFlinkAiServiceRequest(DaraModel):
    def __init__(
        self,
        region: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

