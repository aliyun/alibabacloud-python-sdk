# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterAccessWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_security_groups: main_models.DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroups = None,
        items: main_models.DescribeDBClusterAccessWhitelistResponseBodyItems = None,
        request_id: str = None,
    ):
        # The Elastic Compute Service (ECS) security groups that are associated with the cluster.
        self.dbcluster_security_groups = dbcluster_security_groups
        # The details about the cluster.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbcluster_security_groups:
            self.dbcluster_security_groups.validate()
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_security_groups is not None:
            result['DBClusterSecurityGroups'] = self.dbcluster_security_groups.to_map()

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterSecurityGroups') is not None:
            temp_model = main_models.DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroups()
            self.dbcluster_security_groups = temp_model.from_map(m.get('DBClusterSecurityGroups'))

        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBClusterAccessWhitelistResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterAccessWhitelistResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbcluster_iparray: List[main_models.DescribeDBClusterAccessWhitelistResponseBodyItemsDBClusterIPArray] = None,
    ):
        self.dbcluster_iparray = dbcluster_iparray

    def validate(self):
        if self.dbcluster_iparray:
            for v1 in self.dbcluster_iparray:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBClusterIPArray'] = []
        if self.dbcluster_iparray is not None:
            for k1 in self.dbcluster_iparray:
                result['DBClusterIPArray'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster_iparray = []
        if m.get('DBClusterIPArray') is not None:
            for k1 in m.get('DBClusterIPArray'):
                temp_model = main_models.DescribeDBClusterAccessWhitelistResponseBodyItemsDBClusterIPArray()
                self.dbcluster_iparray.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterAccessWhitelistResponseBodyItemsDBClusterIPArray(DaraModel):
    def __init__(
        self,
        dbcluster_iparray_attribute: str = None,
        dbcluster_iparray_name: str = None,
        security_ips: str = None,
    ):
        # The attributes of the IP whitelist group. Set this parameter to **hidden** to hide the IP whitelist group in the console.
        # 
        # > *   The IP whitelist group that has appeared in the console cannot be hidden.
        # > *   This parameter can be specified only when the **WhiteListType** parameter is set to **IP**.
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        # The name of the IP whitelist group. The group name must be 2 to 120 characters in length and consists of lowercase letters and digits. It must start with a letter, and end with a letter or a digit.
        # 
        # *   If the specified whitelist group name does not exist, the whitelist group is created.
        # *   If the specified whitelist group name exists, the whitelist group is modified.
        # *   If you do not specify this parameter, the default group is modified.
        # 
        # > *   You can create a maximum of 50 IP whitelist groups for a cluster.
        # >*   This parameter can be specified only when the **WhiteListType** parameter is set to **IP**.
        self.dbcluster_iparray_name = dbcluster_iparray_name
        # The IP addresses or Classless Inter-Domain Routing (CIDR) blocks in the IP whitelist group. You can add 1,000 IP addresses or CIDR blocks to all the IP whitelist groups. Separate multiple IP addresses with commas (,). The following two formats are supported:
        # 
        # *   IP addresses. Example: 10.23.12.24.
        # *   CIDR blocks. Example: 10.23.12.24/24. 24 indicates the length of the prefix of the CIDR block. The length is the range of 1 to 32.
        # 
        # >  This parameter can be specified only when the **WhiteListType** parameter is set to **IP**.
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute

        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name

        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')

        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')

        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')

        return self

class DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroups(DaraModel):
    def __init__(
        self,
        dbcluster_security_group: List[main_models.DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroupsDBClusterSecurityGroup] = None,
    ):
        self.dbcluster_security_group = dbcluster_security_group

    def validate(self):
        if self.dbcluster_security_group:
            for v1 in self.dbcluster_security_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBClusterSecurityGroup'] = []
        if self.dbcluster_security_group is not None:
            for k1 in self.dbcluster_security_group:
                result['DBClusterSecurityGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbcluster_security_group = []
        if m.get('DBClusterSecurityGroup') is not None:
            for k1 in m.get('DBClusterSecurityGroup'):
                temp_model = main_models.DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroupsDBClusterSecurityGroup()
                self.dbcluster_security_group.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterAccessWhitelistResponseBodyDBClusterSecurityGroupsDBClusterSecurityGroup(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        # The ID of the ECS security group.
        self.security_group_id = security_group_id
        # The name of the ECS security group.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

