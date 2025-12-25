# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDTCSecurityIpHostsForSQLServerResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        ip_host_pair_num: str = None,
        items: main_models.DescribeDTCSecurityIpHostsForSQLServerResponseBodyItems = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The number of distributed transaction whitelists.
        self.ip_host_pair_num = ip_host_pair_num
        # Details of distributed transaction whitelists.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.ip_host_pair_num is not None:
            result['IpHostPairNum'] = self.ip_host_pair_num

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IpHostPairNum') is not None:
            self.ip_host_pair_num = m.get('IpHostPairNum')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeDTCSecurityIpHostsForSQLServerResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDTCSecurityIpHostsForSQLServerResponseBodyItems(DaraModel):
    def __init__(
        self,
        white_list_groups: List[main_models.DescribeDTCSecurityIpHostsForSQLServerResponseBodyItemsWhiteListGroups] = None,
    ):
        self.white_list_groups = white_list_groups

    def validate(self):
        if self.white_list_groups:
            for v1 in self.white_list_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WhiteListGroups'] = []
        if self.white_list_groups is not None:
            for k1 in self.white_list_groups:
                result['WhiteListGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.white_list_groups = []
        if m.get('WhiteListGroups') is not None:
            for k1 in m.get('WhiteListGroups'):
                temp_model = main_models.DescribeDTCSecurityIpHostsForSQLServerResponseBodyItemsWhiteListGroups()
                self.white_list_groups.append(temp_model.from_map(k1))

        return self

class DescribeDTCSecurityIpHostsForSQLServerResponseBodyItemsWhiteListGroups(DaraModel):
    def __init__(
        self,
        security_ip_hosts: str = None,
        whitelist_group_name: str = None,
    ):
        # The IP address of the ECS instance and the hostname of the Windows computer. Format: `IP address,Hostname`. Multiple values are separated with semicolons (;).
        self.security_ip_hosts = security_ip_hosts
        # The name of the distributed transaction whitelist.
        self.whitelist_group_name = whitelist_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_ip_hosts is not None:
            result['SecurityIpHosts'] = self.security_ip_hosts

        if self.whitelist_group_name is not None:
            result['WhitelistGroupName'] = self.whitelist_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIpHosts') is not None:
            self.security_ip_hosts = m.get('SecurityIpHosts')

        if m.get('WhitelistGroupName') is not None:
            self.whitelist_group_name = m.get('WhitelistGroupName')

        return self

