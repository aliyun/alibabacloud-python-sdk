# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        plan_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The instance ID of the specified simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the plan to which you want to upgrade. You can call [ListPlans](https://help.aliyun.com/document_detail/189314.html) to query plan information.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The region ID of the specified simple application server.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

