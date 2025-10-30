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
        # This parameter is required.
        self.account_password = account_password
        self.client_token = client_token
        self.disk_performance_level = disk_performance_level
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.project_spec = project_spec
        self.region_id = region_id
        # This parameter is required.
        self.security_iplist = security_iplist
        self.storage_size = storage_size
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.vpc_id = vpc_id
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

