# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOpenSearchWhitelistGroupRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_name: str = None,
        ips: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        # The name of the instance.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The name of the whitelist group.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The list of allowed source IP addresses.
        # 
        # This parameter is required.
        self.ips = ips
        # The ID of the region in which the instance resides. > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196841.html) operation to query the regions supported by PolarDB-X, including region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the group ID.
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

        if self.group_name is not None:
            result['GroupName'] = self.group_name

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

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IPs') is not None:
            self.ips = m.get('IPs')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

