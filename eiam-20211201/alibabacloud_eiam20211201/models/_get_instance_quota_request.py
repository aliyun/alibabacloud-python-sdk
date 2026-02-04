# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceQuotaRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        quota_key: str = None,
    ):
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 配额类型，QuotaEnum
        # 
        # This parameter is required.
        self.quota_key = quota_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.quota_key is not None:
            result['QuotaKey'] = self.quota_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QuotaKey') is not None:
            self.quota_key = m.get('QuotaKey')

        return self

