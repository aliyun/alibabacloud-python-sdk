# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class ModifyGlobalSecurityIPGroupNameResponseBody(DaraModel):
    def __init__(
        self,
        global_security_ipgroup: List[main_models.ModifyGlobalSecurityIPGroupNameResponseBodyGlobalSecurityIPGroup] = None,
        request_id: str = None,
    ):
        # The global IP whitelist templates.
        self.global_security_ipgroup = global_security_ipgroup
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.global_security_ipgroup:
            for v1 in self.global_security_ipgroup:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GlobalSecurityIPGroup'] = []
        if self.global_security_ipgroup is not None:
            for k1 in self.global_security_ipgroup:
                result['GlobalSecurityIPGroup'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_security_ipgroup = []
        if m.get('GlobalSecurityIPGroup') is not None:
            for k1 in m.get('GlobalSecurityIPGroup'):
                temp_model = main_models.ModifyGlobalSecurityIPGroupNameResponseBodyGlobalSecurityIPGroup()
                self.global_security_ipgroup.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyGlobalSecurityIPGroupNameResponseBodyGlobalSecurityIPGroup(DaraModel):
    def __init__(
        self,
        gip_list: str = None,
        global_ig_name: str = None,
        global_security_group_id: str = None,
        region_id: str = None,
    ):
        # The IP addresses in the whitelist template.
        # 
        # > Separate multiple IP addresses with commas (,). You can create up to 1,000 IP addresses or CIDR blocks for all IP address whitelists.
        self.gip_list = gip_list
        # The name of the IP whitelist template.
        self.global_ig_name = global_ig_name
        # The ID of the IP whitelist template.
        self.global_security_group_id = global_security_group_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        self.region_id = region_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')

        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')

        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

