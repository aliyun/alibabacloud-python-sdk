# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiKeyRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        key_name: str = None,
        limit_rate: float = None,
        limit_type: str = None,
        quantity: int = None,
        token_quota: int = None,
    ):
        self.instance_id = instance_id
        self.key_name = key_name
        self.limit_rate = limit_rate
        self.limit_type = limit_type
        self.quantity = quantity
        self.token_quota = token_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.limit_rate is not None:
            result['LimitRate'] = self.limit_rate

        if self.limit_type is not None:
            result['LimitType'] = self.limit_type

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.token_quota is not None:
            result['TokenQuota'] = self.token_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('LimitRate') is not None:
            self.limit_rate = m.get('LimitRate')

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('TokenQuota') is not None:
            self.token_quota = m.get('TokenQuota')

        return self

