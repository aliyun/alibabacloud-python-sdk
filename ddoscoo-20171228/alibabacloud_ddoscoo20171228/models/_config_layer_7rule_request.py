# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigLayer7RuleRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_ids: List[str] = None,
        proxy_type_list: str = None,
        proxy_types: List[str] = None,
        real_servers: List[str] = None,
        resource_group_id: str = None,
        rs_type: int = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.instance_ids = instance_ids
        self.proxy_type_list = proxy_type_list
        self.proxy_types = proxy_types
        # This parameter is required.
        self.real_servers = real_servers
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rs_type = rs_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.proxy_type_list is not None:
            result['ProxyTypeList'] = self.proxy_type_list

        if self.proxy_types is not None:
            result['ProxyTypes'] = self.proxy_types

        if self.real_servers is not None:
            result['RealServers'] = self.real_servers

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rs_type is not None:
            result['RsType'] = self.rs_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ProxyTypeList') is not None:
            self.proxy_type_list = m.get('ProxyTypeList')

        if m.get('ProxyTypes') is not None:
            self.proxy_types = m.get('ProxyTypes')

        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')

        return self

