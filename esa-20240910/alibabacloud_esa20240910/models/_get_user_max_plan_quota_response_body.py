# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserMaxPlanQuotaResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        plan_name: str = None,
        quota_value: str = None,
        request_id: str = None,
    ):
        # The plan instance ID. You can obtain this value by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.instance_id = instance_id
        # The plan name.
        # 
        # <props="china">
        # - Free Edition: entranceplan
        # - Basic: basic
        # - Standard: medium
        # - Premium Edition: high
        # 
        # 
        # <props="intl">
        # - Entrance: entranceplan_intl
        # - Pro: basicplan_intl
        # - Premium: vipplan_intl
        self.plan_name = plan_name
        # The quota value.
        self.quota_value = quota_value
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

