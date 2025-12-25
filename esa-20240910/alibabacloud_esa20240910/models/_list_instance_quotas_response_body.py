# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListInstanceQuotasResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        quotas: List[main_models.ListInstanceQuotasResponseBodyQuotas] = None,
        request_id: str = None,
        status: str = None,
    ):
        # The plan ID.
        self.instance_id = instance_id
        # The quotas in the plan.
        self.quotas = quotas
        # The request ID.
        self.request_id = request_id
        # The plan status. Valid values:
        # 
        # *   online: The plan is in service.
        # *   offline: The plan has expired within an allowable period. In this state, the plan is unavailable.
        # *   disable: The plan is released.
        self.status = status

    def validate(self):
        if self.quotas:
            for v1 in self.quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.ListInstanceQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstanceQuotasResponseBodyQuotas(DaraModel):
    def __init__(
        self,
        quota_name: str = None,
        quota_value: str = None,
        quota_value_type: str = None,
    ):
        # The quota name.
        self.quota_name = quota_name
        # The quota value.
        self.quota_value = quota_value
        # The threshold type of the quota. Valid values:
        # 
        # *   value: enumerates the values of the quota.
        # *   bool: specifies whether the quota is available.
        # *   num: the upper limit of the quota.
        # *   range: the value range for the quota.
        # *   custom: other types than the preceding four quota threshold types.
        self.quota_value_type = quota_value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value

        if self.quota_value_type is not None:
            result['QuotaValueType'] = self.quota_value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')

        if m.get('QuotaValueType') is not None:
            self.quota_value_type = m.get('QuotaValueType')

        return self

