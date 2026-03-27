# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppRecommendedCommoditiesRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        extend: str = None,
        resource_conditions: str = None,
        scene: str = None,
    ):
        self.biz_id = biz_id
        self.extend = extend
        self.resource_conditions = resource_conditions
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.resource_conditions is not None:
            result['ResourceConditions'] = self.resource_conditions

        if self.scene is not None:
            result['Scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('ResourceConditions') is not None:
            self.resource_conditions = m.get('ResourceConditions')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        return self

