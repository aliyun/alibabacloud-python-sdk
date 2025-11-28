# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSupabaseProjectRequest(DaraModel):
    def __init__(
        self,
        account_password: str = None,
        client_token: str = None,
        disk_performance_level: str = None,
        project_name: str = None,
        project_spec: str = None,
        region_id: str = None,
        security_iplist: str = None,
        storage_size: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The password of the initial account.
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # *   The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The client token that is used to ensure the idempotence of the request. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/327176.html).
        self.client_token = client_token
        # The performance level of Enterprise SSDs (ESSDs). Default value: PL0. Valid values:
        # 
        # *   PL0
        # *   PL1
        self.disk_performance_level = disk_performance_level
        # The name of the Supabase project. The name must meet the following requirements:
        # 
        # *   The name must be 1 to 128 characters in length.
        # *   The name can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The name must start with a letter or an underscore (_).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The specifications of the Supabase project. Default value: 1C1G.
        # 
        # This parameter is required.
        self.project_spec = project_spec
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        self.region_id = region_id
        # The IP address whitelist.
        # 
        # A value of 127.0.0.1 denies access from any external IP address. You can call the [ModifySecurityIps](https://help.aliyun.com/document_detail/86928.html) operation to modify the IP address whitelist after you create a project.
        # 
        # This parameter is required.
        self.security_iplist = security_iplist
        # The storage size. Unit: GB. Default value: 1.
        self.storage_size = storage_size
        # The vSwitch ID.
        # 
        # > 
        # 
        # *   **This parameter** must be specified.
        # 
        # *   The zone where the **vSwitch** resides must be the same as the zone that is specified by **ZoneId**.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        # 
        # > 
        # 
        # *   You can call the [DescribeRdsVpcs](https://help.aliyun.com/document_detail/208327.html) operation to query the available VPC IDs.
        # 
        # *   This parameter must be specified.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent zone list.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')

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

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

