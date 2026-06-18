# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSupabaseProjectRequest(DaraModel):
    def __init__(
        self,
        account_password: str = None,
        auto_scale: bool = None,
        client_token: str = None,
        disk_performance_level: str = None,
        engine_version: str = None,
        pay_type: str = None,
        period: str = None,
        project_name: str = None,
        project_spec: str = None,
        region_id: str = None,
        security_iplist: str = None,
        storage_size: int = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The password of the initial account.
        # 
        # Password rules:
        # 
        # - The password must be 8 to 32 characters in length.
        # - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - Supported special characters include !@#$%^&*()_+-=.
        # 
        # This parameter is required.
        self.account_password = account_password
        # Specifies whether to enable auto start/stop. If this parameter is not specified, the default value is false.
        self.auto_scale = auto_scale
        # The idempotency token. This token ensures that duplicate requests do not trigger the same operation more than once.
        self.client_token = client_token
        # The performance level (PL) of the cloud disk. If this parameter is not specified, the default value PL0 is used.
        # 
        # Valid values:
        # 
        # - PL0
        # - PL1
        # - PL2
        # - PL3.
        self.disk_performance_level = disk_performance_level
        # The DPI engine version. If this parameter is not specified, the default value PG15 is used.
        # 
        # Valid values:
        # 
        # - PG15: PostgreSQL 15.
        # - PG17: PostgreSQL 17.
        self.engine_version = engine_version
        # The billing method. If this parameter is not specified, the default value Free is used.
        # 
        # Valid values:
        # 
        # - Free: free tier.
        # - Postpaid: pay-as-you-go.
        # - Prepaid: subscription.
        self.pay_type = pay_type
        # The unit of the subscription duration. This parameter takes effect only when PayType is set to PrePay. If this parameter is not specified, the default value Month is used.
        # 
        # Valid values:
        # 
        # - Month: month.
        # - Year: year.
        self.period = period
        # The name of the Supabase project.
        # 
        # Naming rules:
        # 
        # - The name must be 1 to 128 characters in length.
        # - The name can contain letters, digits, hyphens (-), and underscores (_).
        # - The name must start with a letter or an underscore (_).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The specifications of the Supabase project. The Free billing type uses free-tier specifications. For paid billing types, the specifications must match those available on the console.
        # 
        # This parameter is required.
        self.project_spec = project_spec
        # The region ID. Specifies the region in which to create the project.
        self.region_id = region_id
        # The IP address whitelist. Separate multiple IP addresses or CIDR blocks with commas (,). If this parameter is not specified, the default value 0.0.0.0/0 is used.
        # 
        # This parameter is required.
        self.security_iplist = security_iplist
        # The storage size. Unit: GB. If this parameter is not specified for non-Free billing types, the default value is 1 GB.
        self.storage_size = storage_size
        # The subscription duration of the resource. This parameter takes effect only when PayType is set to PrePay. If this parameter is not specified, the default value is 1.
        self.used_time = used_time
        # The vSwitch ID. This parameter is required. The zone of the vSwitch must be the same as the value of ZoneId.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC). This parameter is required.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The zone ID. The zone of the vSwitch specified by VSwitchId must be the same as the value of this parameter.
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
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.auto_scale is not None:
            result['AutoScale'] = self.auto_scale

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.project_spec is not None:
            result['ProjectSpec'] = self.project_spec

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

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
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('AutoScale') is not None:
            self.auto_scale = m.get('AutoScale')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProjectSpec') is not None:
            self.project_spec = m.get('ProjectSpec')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

