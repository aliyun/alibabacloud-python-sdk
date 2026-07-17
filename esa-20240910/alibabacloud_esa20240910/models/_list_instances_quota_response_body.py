# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListInstancesQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota_name: str = None,
        quota_value_type: str = None,
        quota_values: List[main_models.ListInstancesQuotaResponseBodyQuotaValues] = None,
        request_id: str = None,
    ):
        # The quota name.
        self.quota_name = quota_name
        # The threshold type of the quota. Valid values:
        # 
        # - **value**: Enumeration type. The enumeration range of quota values.
        # - **bool**: Boolean type. Indicates whether the quota is available.
        # - **num**: Numeric type. The upper limit of the quota usage.
        # - **range**: Range type. The value range of the quota.
        # - **custom**: Custom type. Other types beyond the four threshold types above.
        self.quota_value_type = quota_value_type
        # The list of quota values.
        self.quota_values = quota_values
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.quota_values:
            for v1 in self.quota_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.quota_value_type is not None:
            result['QuotaValueType'] = self.quota_value_type

        result['QuotaValues'] = []
        if self.quota_values is not None:
            for k1 in self.quota_values:
                result['QuotaValues'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('QuotaValueType') is not None:
            self.quota_value_type = m.get('QuotaValueType')

        self.quota_values = []
        if m.get('QuotaValues') is not None:
            for k1 in m.get('QuotaValues'):
                temp_model = main_models.ListInstancesQuotaResponseBodyQuotaValues()
                self.quota_values.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancesQuotaResponseBodyQuotaValues(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        quota_value: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The quota value.
        self.quota_value = quota_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')

        return self

