# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceIpWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        db_ip_white_list_groups: List[main_models.DescribeInstanceIpWhitelistResponseBodyDbIpWhiteListGroups] = None,
        instance_name: str = None,
        ip_white_list_groups: List[main_models.DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups] = None,
        request_id: str = None,
    ):
        self.branch_name = branch_name
        self.db_ip_white_list_groups = db_ip_white_list_groups
        # The instance ID of the AI application.
        self.instance_name = instance_name
        # The IP whitelist groups.
        self.ip_white_list_groups = ip_white_list_groups
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.db_ip_white_list_groups:
            for v1 in self.db_ip_white_list_groups:
                 if v1:
                    v1.validate()
        if self.ip_white_list_groups:
            for v1 in self.ip_white_list_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        result['DbIpWhiteListGroups'] = []
        if self.db_ip_white_list_groups is not None:
            for k1 in self.db_ip_white_list_groups:
                result['DbIpWhiteListGroups'].append(k1.to_map() if k1 else None)

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        result['IpWhiteListGroups'] = []
        if self.ip_white_list_groups is not None:
            for k1 in self.ip_white_list_groups:
                result['IpWhiteListGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        self.db_ip_white_list_groups = []
        if m.get('DbIpWhiteListGroups') is not None:
            for k1 in m.get('DbIpWhiteListGroups'):
                temp_model = main_models.DescribeInstanceIpWhitelistResponseBodyDbIpWhiteListGroups()
                self.db_ip_white_list_groups.append(temp_model.from_map(k1))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.ip_white_list_groups = []
        if m.get('IpWhiteListGroups') is not None:
            for k1 in m.get('IpWhiteListGroups'):
                temp_model = main_models.DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups()
                self.ip_white_list_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ip_whitelist: str = None,
    ):
        # The group name.
        self.group_name = group_name
        # The list of IP addresses.
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        return self

class DescribeInstanceIpWhitelistResponseBodyDbIpWhiteListGroups(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ip_whitelist: str = None,
    ):
        self.group_name = group_name
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        return self

