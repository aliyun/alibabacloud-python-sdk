# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        renew_period: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the instance
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_id = owner_id
        # The code of the service to which the instance belongs.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The duration of the subscription renewal. Unit: months. Valid values:
        # 
        # *   1 to 9
        # *   12
        # *   24
        # *   36
        # 
        # This parameter is required.
        self.renew_period = renew_period

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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.renew_period is not None:
            result['RenewPeriod'] = self.renew_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RenewPeriod') is not None:
            self.renew_period = m.get('RenewPeriod')

        return self

