# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMem0SecurityIpsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_name: str = None,
        modify_mode: str = None,
        region_id: str = None,
        security_iplist: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The name of the whitelist group of the instance.
        self.group_name = group_name
        # The modification mode of the whitelist. Valid values:
        # 
        # - 0: overwrites the whitelist group.
        # - 1: adds a whitelist group.
        # - 2: deletes a whitelist group.
        self.modify_mode = modify_mode
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IP addresses in the whitelist group. Separate multiple IP addresses with commas (,).
        # 
        # This parameter is required.
        self.security_iplist = security_iplist

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

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

