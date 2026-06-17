# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSaasServiceRequest(DaraModel):
    def __init__(
        self,
        cu: int = None,
        pay_type: str = None,
        period: str = None,
        plan: str = None,
        region_id: str = None,
        service_type: str = None,
        used_time: str = None,
        workspace_id: str = None,
    ):
        # The compute resources of the SaaS service.
        self.cu = cu
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        # 
        # > - If you leave this parameter empty, a Free service is created by default.
        # > - The subscription billing method offers discounts for purchases of one year or longer. Select a billing method as needed.
        self.pay_type = pay_type
        # The unit of the duration for which you want to purchase the resource. Valid values:
        # - **Month**: month.
        # - **Year**: year.
        # 
        # > This parameter is required when you create a subscription instance.
        self.period = period
        # Deprecated.
        self.plan = plan
        # The region ID of the instance.
        self.region_id = region_id
        # The service type. Valid values:
        # 
        # - **memroy**
        # - **drama**.
        # 
        # This parameter is required.
        self.service_type = service_type
        # The duration for which you want to purchase the resource. Valid values:
        # - If **Period** is set to **Month**, the valid values are 1 to 11.
        # - If **Period** is set to **Year**, the valid values are 1 to 3.
        # 
        # > This parameter is required when you create a subscription instance.
        self.used_time = used_time
        # The workspace of the SaaS service.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.plan is not None:
            result['Plan'] = self.plan

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Plan') is not None:
            self.plan = m.get('Plan')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

