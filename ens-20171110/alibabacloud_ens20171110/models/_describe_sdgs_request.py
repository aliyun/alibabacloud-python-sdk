# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSDGsRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        sdgids: List[str] = None,
    ):
        # The list of AIC instance IDs to query.
        self.instance_ids = instance_ids
        # The list of SDG IDs to query.
        self.sdgids = sdgids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.sdgids is not None:
            result['SDGIds'] = self.sdgids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('SDGIds') is not None:
            self.sdgids = m.get('SDGIds')

        return self

