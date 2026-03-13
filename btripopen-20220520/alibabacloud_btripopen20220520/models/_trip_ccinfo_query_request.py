# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TripCCInfoQueryRequest(DaraModel):
    def __init__(
        self,
        business_instance_id: str = None,
        node_id: str = None,
        third_business_id: str = None,
    ):
        self.business_instance_id = business_instance_id
        self.node_id = node_id
        self.third_business_id = third_business_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_instance_id is not None:
            result['business_instance_id'] = self.business_instance_id

        if self.node_id is not None:
            result['node_id'] = self.node_id

        if self.third_business_id is not None:
            result['third_business_id'] = self.third_business_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('business_instance_id') is not None:
            self.business_instance_id = m.get('business_instance_id')

        if m.get('node_id') is not None:
            self.node_id = m.get('node_id')

        if m.get('third_business_id') is not None:
            self.third_business_id = m.get('third_business_id')

        return self

