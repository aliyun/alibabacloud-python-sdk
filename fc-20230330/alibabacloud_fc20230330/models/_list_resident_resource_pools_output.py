# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ListResidentResourcePoolsOutput(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        resident_resource_pools: List[main_models.ResidentResourcePool] = None,
    ):
        self.next_token = next_token
        self.resident_resource_pools = resident_resource_pools

    def validate(self):
        if self.resident_resource_pools:
            for v1 in self.resident_resource_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['residentResourcePools'] = []
        if self.resident_resource_pools is not None:
            for k1 in self.resident_resource_pools:
                result['residentResourcePools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.resident_resource_pools = []
        if m.get('residentResourcePools') is not None:
            for k1 in m.get('residentResourcePools'):
                temp_model = main_models.ResidentResourcePool()
                self.resident_resource_pools.append(temp_model.from_map(k1))

        return self

