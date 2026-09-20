# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeIpWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        groups: main_models.DescribeIpWhitelistResponseBodyGroups = None,
        request_id: str = None,
    ):
        self.groups = groups
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = main_models.DescribeIpWhitelistResponseBodyGroups()
            self.groups = temp_model.from_map(m.get('Groups'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeIpWhitelistResponseBodyGroups(DaraModel):
    def __init__(
        self,
        group: List[main_models.DescribeIpWhitelistResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for v1 in self.group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Group'] = []
        if self.group is not None:
            for k1 in self.group:
                result['Group'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k1 in m.get('Group'):
                temp_model = main_models.DescribeIpWhitelistResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k1))

        return self

class DescribeIpWhitelistResponseBodyGroupsGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ip_list: main_models.DescribeIpWhitelistResponseBodyGroupsGroupIpList = None,
        ip_version: int = None,
    ):
        self.group_name = group_name
        self.ip_list = ip_list
        self.ip_version = ip_version

    def validate(self):
        if self.ip_list:
            self.ip_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ip_list is not None:
            result['IpList'] = self.ip_list.to_map()

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IpList') is not None:
            temp_model = main_models.DescribeIpWhitelistResponseBodyGroupsGroupIpList()
            self.ip_list = temp_model.from_map(m.get('IpList'))

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        return self

class DescribeIpWhitelistResponseBodyGroupsGroupIpList(DaraModel):
    def __init__(
        self,
        ip: List[str] = None,
    ):
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

