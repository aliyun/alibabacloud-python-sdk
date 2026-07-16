# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiKeyRequest(DaraModel):
    def __init__(
        self,
        daily_token_quota: int = None,
        instance_id: str = None,
        key_name: str = None,
        limit_rate: float = None,
        limit_type: str = None,
        quantity: int = None,
        token_quota: int = None,
    ):
        self.daily_token_quota = daily_token_quota
        # The instance ID.
        self.instance_id = instance_id
        # The API key name.
        self.key_name = key_name
        # The proportion of the total quota to allocate. This parameter applies only when `LimitType` is set to `ratio`.
        self.limit_rate = limit_rate
        # The limit type. Valid values:
        # 
        # - `ratio`: Sets the limit as a ratio of the total available quota.
        # 
        # - `fixed`: Sets the limit to a fixed number of tokens.
        # 
        # - `auto`: Automatically allocates the quota.
        self.limit_type = limit_type
        # The number of API keys to create. Default value: **1**.
        self.quantity = quantity
        # The fixed token quota for the API key. This parameter applies only when `LimitType` is set to `fixed`.
        self.token_quota = token_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.daily_token_quota is not None:
            result['DailyTokenQuota'] = self.daily_token_quota

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
        if m.get('DailyTokenQuota') is not None:
            self.daily_token_quota = m.get('DailyTokenQuota')

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

