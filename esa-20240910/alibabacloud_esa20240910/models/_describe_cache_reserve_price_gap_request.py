# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCacheReservePriceGapRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        target_quota_gb: int = None,
    ):
        self.instance_id = instance_id
        self.target_quota_gb = target_quota_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.target_quota_gb is not None:
            result['TargetQuotaGb'] = self.target_quota_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TargetQuotaGb') is not None:
            self.target_quota_gb = m.get('TargetQuotaGb')

        return self

