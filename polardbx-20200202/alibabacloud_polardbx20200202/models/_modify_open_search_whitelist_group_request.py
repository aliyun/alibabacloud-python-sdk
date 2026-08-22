# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOpenSearchWhitelistGroupRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_id: str = None,
        ips: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The list of source IP address restrictions.
        # 
        # This parameter is required.
        self.ips = ips
        # The region in which the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The remarks.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.ips is not None:
            result['IPs'] = self.ips

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IPs') is not None:
            self.ips = m.get('IPs')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

