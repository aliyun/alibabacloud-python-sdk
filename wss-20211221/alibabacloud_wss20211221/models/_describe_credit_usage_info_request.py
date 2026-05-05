# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCreditUsageInfoRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        instance_ids: List[str] = None,
        usage_type: str = None,
    ):
        self.biz_type = biz_type
        self.instance_ids = instance_ids
        self.usage_type = usage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        return self

