# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceIpWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        ip_white_list_groups: List[main_models.DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups] = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.ip_white_list_groups = ip_white_list_groups
        self.request_id = request_id

    def validate(self):
        if self.ip_white_list_groups:
            for v1 in self.ip_white_list_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

