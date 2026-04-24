# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class UpdateApiKeyQuotaResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateApiKeyQuotaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.UpdateApiKeyQuotaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateApiKeyQuotaResponseBodyData(DaraModel):
    def __init__(
        self,
        custom_key_list: List[main_models.UpdateApiKeyQuotaResponseBodyDataCustomKeyList] = None,
    ):
        self.custom_key_list = custom_key_list

    def validate(self):
        if self.custom_key_list:
            for v1 in self.custom_key_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomKeyList'] = []
        if self.custom_key_list is not None:
            for k1 in self.custom_key_list:
                result['CustomKeyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_key_list = []
        if m.get('CustomKeyList') is not None:
            for k1 in m.get('CustomKeyList'):
                temp_model = main_models.UpdateApiKeyQuotaResponseBodyDataCustomKeyList()
                self.custom_key_list.append(temp_model.from_map(k1))

        return self

class UpdateApiKeyQuotaResponseBodyDataCustomKeyList(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        limit_rate: float = None,
        limit_type: str = None,
        token_quota: int = None,
    ):
        # Api Key
        self.api_key = api_key
        self.limit_rate = limit_rate
        self.limit_type = limit_type
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

        if m.get('LimitRate') is not None:
            self.limit_rate = m.get('LimitRate')

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        if m.get('TokenQuota') is not None:
            self.token_quota = m.get('TokenQuota')

        return self

