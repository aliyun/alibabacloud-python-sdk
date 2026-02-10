# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserVpcRequest(DaraModel):
    def __init__(
        self,
        k_8s_region_id: str = None,
    ):
        # Region.
        # 
        # This parameter is required.
        self.k_8s_region_id = k_8s_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.k_8s_region_id is not None:
            result['K8sRegionId'] = self.k_8s_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sRegionId') is not None:
            self.k_8s_region_id = m.get('K8sRegionId')

        return self

