# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateInnerIpWhitelistGroupRequest(DaraModel):
    def __init__(
        self,
        cidr_ip_list: List[str] = None,
        inner_ip_whitelist_group_id: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.cidr_ip_list = cidr_ip_list
        # This parameter is required.
        self.inner_ip_whitelist_group_id = inner_ip_whitelist_group_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_ip_list is not None:
            result['CidrIpList'] = self.cidr_ip_list

        if self.inner_ip_whitelist_group_id is not None:
            result['InnerIpWhitelistGroupId'] = self.inner_ip_whitelist_group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIpList') is not None:
            self.cidr_ip_list = m.get('CidrIpList')

        if m.get('InnerIpWhitelistGroupId') is not None:
            self.inner_ip_whitelist_group_id = m.get('InnerIpWhitelistGroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

