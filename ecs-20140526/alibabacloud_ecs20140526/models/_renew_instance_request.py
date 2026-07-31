# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        expected_renew_day: int = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The day on which to renew the instance to a [unified expiration date](https://help.aliyun.com/document_detail/63396.html). Valid values: 1 to 28.
        # 
        # To use this parameter, you must first [set a unified expiration date for ECS instances](~~63396#694cb636c0rp6~~). The value of this parameter must match the unified expiration date that you have set. Otherwise, the call fails.
        # 
        # > You must specify either the renewal period parameters (Period and PeriodUnit) or the unified expiration date parameter (ExpectedRenewDay), but not both.
        self.expected_renew_day = expected_renew_day
        # The ID of the instance that you want to renew.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The renewal period for the subscription instance. If you specify DedicatedHostId, the value of Period cannot exceed the remaining subscription period of the dedicated host. Valid values:
        # 
        # <props="china">
        # - If you set PeriodUnit to Week, valid values of Period are 1, 2, 3, and 4.
        # - If you set PeriodUnit to Month, valid values of Period are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        # 
        # 
        # 
        # <props="intl">If you set PeriodUnit to Month, valid values of Period are 1, 2, 3, 4, 5, 6, 7, 8, 9, and 12.
        # 
        # > You must specify either the renewal period parameters (Period and PeriodUnit) or the unified expiration date parameter (ExpectedRenewDay), but not both.
        self.period = period
        # The unit of the renewal period. This parameter specifies the unit for the Period parameter. Valid values:
        # 
        # <props="china">
        # - Week.
        # - Month.
        # 
        # 
        # 
        # <props="intl">Month.
        # 
        # Default value: Month.
        self.period_unit = period_unit
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.expected_renew_day is not None:
            result['ExpectedRenewDay'] = self.expected_renew_day

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ExpectedRenewDay') is not None:
            self.expected_renew_day = m.get('ExpectedRenewDay')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

