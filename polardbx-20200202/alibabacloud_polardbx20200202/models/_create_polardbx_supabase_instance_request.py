# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolardbxSupabaseInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        client_token: str = None,
        dashboard_password: str = None,
        db_instance_description: str = None,
        db_password: str = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tenant_mode: bool = None,
        used_time: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # The idempotency token.
        self.client_token = client_token
        # The dashboard password.
        # 
        # This parameter is required.
        self.dashboard_password = dashboard_password
        # The instance description.
        self.db_instance_description = db_instance_description
        # The database password.
        # 
        # This parameter is required.
        self.db_password = db_password
        # The billing type. Valid values:
        # - PREPAY: subscription.
        # - POSTPAY: pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The billing cycle. Valid values:
        # - Year
        # - Month
        # - Hour
        self.period = period
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to enable multi-tenant mode.
        self.tenant_mode = tenant_mode
        # The subscription duration.
        self.used_time = used_time
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # VPC ID
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password

        if self.db_instance_description is not None:
            result['DbInstanceDescription'] = self.db_instance_description

        if self.db_password is not None:
            result['DbPassword'] = self.db_password

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')

        if m.get('DbInstanceDescription') is not None:
            self.db_instance_description = m.get('DbInstanceDescription')

        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

