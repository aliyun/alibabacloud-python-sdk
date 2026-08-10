# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLangfuseSecurityIPListRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        group_name: str = None,
        modify_mode: str = None,
        region_id: str = None,
        security_iplist: str = None,
    ):
        # The Langfuse instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the whitelist group.
        self.group_name = group_name
        # The modification mode. Valid values:
        # 
        # - 0: overwrite
        # - 1: increase
        # - 2: delete
        # 
        # > Specify 0 to use the overwrite mode.
        self.modify_mode = modify_mode
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IP addresses to add to the instance whitelist. Separate multiple IP addresses with commas (,). For example, 192.168.0.0/24 indicates that all IP addresses in the 192.168.0.XX range are allowed to access the instance.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

