# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityIpsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_groups: main_models.DescribeSecurityIpsResponseBodySecurityIpGroups = None,
        security_ips: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the information of IP whitelists.
        self.security_ip_groups = security_ip_groups
        # The IP addresses in the default whitelist.
        self.security_ips = security_ips

    def validate(self):
        if self.security_ip_groups:
            self.security_ip_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_ip_groups is not None:
            result['SecurityIpGroups'] = self.security_ip_groups.to_map()

        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityIpGroups') is not None:
            temp_model = main_models.DescribeSecurityIpsResponseBodySecurityIpGroups()
            self.security_ip_groups = temp_model.from_map(m.get('SecurityIpGroups'))

        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')

        return self

class DescribeSecurityIpsResponseBodySecurityIpGroups(DaraModel):
    def __init__(
        self,
        security_ip_group: List[main_models.DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup] = None,
    ):
        self.security_ip_group = security_ip_group

    def validate(self):
        if self.security_ip_group:
            for v1 in self.security_ip_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecurityIpGroup'] = []
        if self.security_ip_group is not None:
            for k1 in self.security_ip_group:
                result['SecurityIpGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_ip_group = []
        if m.get('SecurityIpGroup') is not None:
            for k1 in m.get('SecurityIpGroup'):
                temp_model = main_models.DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup()
                self.security_ip_group.append(temp_model.from_map(k1))

        return self

class DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup(DaraModel):
    def __init__(
        self,
        security_ip_group_attribute: str = None,
        security_ip_group_name: str = None,
        security_ip_list: str = None,
    ):
        # The attribute of the IP address whitelist.
        self.security_ip_group_attribute = security_ip_group_attribute
        # The name of the IP whitelist.
        self.security_ip_group_name = security_ip_group_name
        # The name of the IP whitelist.
        self.security_ip_list = security_ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_ip_group_attribute is not None:
            result['SecurityIpGroupAttribute'] = self.security_ip_group_attribute

        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name

        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIpGroupAttribute') is not None:
            self.security_ip_group_attribute = m.get('SecurityIpGroupAttribute')

        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')

        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')

        return self

