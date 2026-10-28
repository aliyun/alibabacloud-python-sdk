# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaAlarmsRequest(DaraModel):
    def __init__(
        self,
        alarm_name: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: List[main_models.ListQuotaAlarmsRequestQuotaDimensions] = None,
    ):
        # The name of the quota usage alert.
        self.alarm_name = alarm_name
        # The maximum number of records to return.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that specifies the start point of the query.
        # 
        # > If you do not specify this parameter, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > To obtain the abbreviation of an Alibaba Cloud service name, see the `ProductCode` parameter in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        self.product_code = product_code
        # The quota ID.
        # 
        # > - To obtain the quota ID of an Alibaba Cloud service, see the `QuotaActionCode` parameter in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # >
        # > - If you specify this parameter, you must also specify `ProductCode`.
        self.quota_action_code = quota_action_code
        # The quota dimensions.
        self.quota_dimensions = quota_dimensions

    def validate(self):
        if self.quota_dimensions:
            for v1 in self.quota_dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k1 in self.quota_dimensions:
                result['QuotaDimensions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k1 in m.get('QuotaDimensions'):
                temp_model = main_models.ListQuotaAlarmsRequestQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k1))

        return self

class ListQuotaAlarmsRequestQuotaDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # > - The number of key-value pairs that you can specify for the quota dimensions varies based on the Alibaba Cloud service.
        # >
        # > - If you set `ProductCode` to `ecs`, `ecs-spec`, `actiontrail`, or `ess`, you must specify both the key and value for the quota dimension.
        self.key = key
        # The value of the quota dimension.
        # 
        # > - The number of key-value pairs that you can specify for the quota dimensions varies based on the Alibaba Cloud service.
        # >
        # > - If you set `ProductCode` to `ecs`, `ecs-spec`, `actiontrail`, or `ess`, you must specify both the key and value for the quota dimension.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

