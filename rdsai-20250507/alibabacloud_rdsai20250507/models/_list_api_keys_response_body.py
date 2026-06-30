# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListApiKeysResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListApiKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The unique request ID.
        self.request_id = request_id
        # Indicates if the request succeeded.
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
            temp_model = main_models.ListApiKeysResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListApiKeysResponseBodyData(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        custom_key_list: List[main_models.ListApiKeysResponseBodyDataCustomKeyList] = None,
        daily_token_quota: int = None,
        is_rate_limited: bool = None,
        page: int = None,
        page_size: int = None,
        system_api_key: str = None,
        threshold_percent: int = None,
        total: int = None,
    ):
        # The base URL for model calls.
        self.base_url = base_url
        # The custom API key list.
        self.custom_key_list = custom_key_list
        self.daily_token_quota = daily_token_quota
        # Specifies if the system-generated key is rate-limited.
        self.is_rate_limited = is_rate_limited
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The system-generated key.
        self.system_api_key = system_api_key
        # The alarm threshold percentage for the SystemApiKey. For example, a value of 80 indicates that an alarm is triggered when usage reaches 80% of the quota. The alarm clears when usage falls below this threshold.
        self.threshold_percent = threshold_percent
        # The total number of entries.
        self.total = total

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
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        result['CustomKeyList'] = []
        if self.custom_key_list is not None:
            for k1 in self.custom_key_list:
                result['CustomKeyList'].append(k1.to_map() if k1 else None)

        if self.daily_token_quota is not None:
            result['DailyTokenQuota'] = self.daily_token_quota

        if self.is_rate_limited is not None:
            result['IsRateLimited'] = self.is_rate_limited

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.system_api_key is not None:
            result['SystemApiKey'] = self.system_api_key

        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        self.custom_key_list = []
        if m.get('CustomKeyList') is not None:
            for k1 in m.get('CustomKeyList'):
                temp_model = main_models.ListApiKeysResponseBodyDataCustomKeyList()
                self.custom_key_list.append(temp_model.from_map(k1))

        if m.get('DailyTokenQuota') is not None:
            self.daily_token_quota = m.get('DailyTokenQuota')

        if m.get('IsRateLimited') is not None:
            self.is_rate_limited = m.get('IsRateLimited')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SystemApiKey') is not None:
            self.system_api_key = m.get('SystemApiKey')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListApiKeysResponseBodyDataCustomKeyList(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        daily_token_quota: int = None,
        is_rate_limited: bool = None,
        key_name: str = None,
        limit_rate: float = None,
        limit_type: str = None,
        threshold_percent: int = None,
        token_quota: int = None,
    ):
        # The API key.
        self.api_key = api_key
        self.daily_token_quota = daily_token_quota
        # Specifies if the API key is rate-limited.
        self.is_rate_limited = is_rate_limited
        # The key name.
        self.key_name = key_name
        # The limit, specified as a ratio in decimal format. This parameter is used when LimitType is ratio.
        self.limit_rate = limit_rate
        # The limit type. Valid values:
        # 
        # - **fixed**: A fixed value.
        # 
        # - **ratio**: A percentage of the total quota.
        # 
        # - **auto**: The quota is allocated automatically.
        self.limit_type = limit_type
        # The alarm threshold percentage. For example, a value of 80 indicates that an alarm is triggered when usage reaches 80% of the quota. The alarm clears when usage falls below this threshold.
        self.threshold_percent = threshold_percent
        # The token quota.
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

        if self.is_rate_limited is not None:
            result['IsRateLimited'] = self.is_rate_limited

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.limit_rate is not None:
            result['LimitRate'] = self.limit_rate

        if self.limit_type is not None:
            result['LimitType'] = self.limit_type

        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent

        if self.token_quota is not None:
            result['TokenQuota'] = self.token_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('DailyTokenQuota') is not None:
            self.daily_token_quota = m.get('DailyTokenQuota')

        if m.get('IsRateLimited') is not None:
            self.is_rate_limited = m.get('IsRateLimited')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('LimitRate') is not None:
            self.limit_rate = m.get('LimitRate')

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        if m.get('TokenQuota') is not None:
            self.token_quota = m.get('TokenQuota')

        return self

