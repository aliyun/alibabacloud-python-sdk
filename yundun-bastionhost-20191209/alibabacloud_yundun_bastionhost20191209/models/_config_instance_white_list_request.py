# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ConfigInstanceWhiteListRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        white_list: List[str] = None,
        white_list_policies: List[main_models.ConfigInstanceWhiteListRequestWhiteListPolicies] = None,
    ):
        # The ID of the bastion host for which you want to configure a whitelist of public IP addresses.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        self.region_id = region_id
        # The IP address whitelist that you want to configure.
        self.white_list = white_list
        self.white_list_policies = white_list_policies

    def validate(self):
        if self.white_list_policies:
            for v1 in self.white_list_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        result['WhiteListPolicies'] = []
        if self.white_list_policies is not None:
            for k1 in self.white_list_policies:
                result['WhiteListPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        self.white_list_policies = []
        if m.get('WhiteListPolicies') is not None:
            for k1 in m.get('WhiteListPolicies'):
                temp_model = main_models.ConfigInstanceWhiteListRequestWhiteListPolicies()
                self.white_list_policies.append(temp_model.from_map(k1))

        return self

class ConfigInstanceWhiteListRequestWhiteListPolicies(DaraModel):
    def __init__(
        self,
        description: str = None,
        entry: str = None,
    ):
        self.description = description
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.entry is not None:
            result['Entry'] = self.entry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        return self

