# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class UpdateApiKeyQuotaRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        keys: List[main_models.UpdateApiKeyQuotaRequestKeys] = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # A list of API keys.
        self.keys = keys

    def validate(self):
        if self.keys:
            for v1 in self.keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Keys'] = []
        if self.keys is not None:
            for k1 in self.keys:
                result['Keys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.keys = []
        if m.get('Keys') is not None:
            for k1 in m.get('Keys'):
                temp_model = main_models.UpdateApiKeyQuotaRequestKeys()
                self.keys.append(temp_model.from_map(k1))

        return self

class UpdateApiKeyQuotaRequestKeys(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        daily_token_quota: int = None,
        limit_rate: float = None,
        limit_type: str = None,
        token_quota: int = None,
    ):
        # The API key.
        self.api_key = api_key
        self.daily_token_quota = daily_token_quota
        # The limit rate. This parameter is required when `LimitType` is set to `ratio`.
        self.limit_rate = limit_rate
        # The limit type. Valid values:
        # 
        # - `ratio`: Allocates the quota proportionally.
        # 
        # - `fixed`: Allocates a fixed quota.
        # 
        # - `auto`: Allocates the quota automatically.
        self.limit_type = limit_type
        # The token quota. This parameter is required when `LimitType` is set to `fixed`.
        self.token_quota = token_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.daily_token_quota is not None:
            result['DailyTokenQuota'] = self.daily_token_quota

        if self.limit_rate is not None:
            result['LimitRate'] = self.limit_rate

        if self.limit_type is not None:
            result['LimitType'] = self.limit_type

        if self.token_quota is not None:
            result['TokenQuota'] = self.token_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('DailyTokenQuota') is not None:
            self.daily_token_quota = m.get('DailyTokenQuota')

        if m.get('LimitRate') is not None:
            self.limit_rate = m.get('LimitRate')

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        if m.get('TokenQuota') is not None:
            self.token_quota = m.get('TokenQuota')

        return self

