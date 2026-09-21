# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityIPGroupRequest(DaraModel):
    def __init__(
        self,
        gip_list: str = None,
        global_ig_name: str = None,
        global_security_group_id: str = None,
        region_name: str = None,
    ):
        # The IP addresses in the whitelist template.
        # 
        # > Separate multiple IP addresses with commas (,). A maximum of 1,000 IP addresses or CIDR blocks can be added to all IP address whitelists.
        # 
        # This parameter is required.
        self.gip_list = gip_list
        # The name of the IP address whitelist template. The name must meet the following requirements:
        # 
        # - It can contain lowercase letters, digits, and underscores (_).
        # 
        # - It must start with a letter and end with a letter or a digit.
        # 
        # - It must be 2 to 120 characters in length.
        # 
        # > This parameter overwrites the initial value.
        # 
        # This parameter is required.
        self.global_ig_name = global_ig_name
        # The ID of the IP address whitelist template.
        # 
        # This parameter is required.
        self.global_security_group_id = global_security_group_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gip_list is not None:
            result['GIpList'] = self.gip_list

        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name

        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')

        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')

        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        return self

