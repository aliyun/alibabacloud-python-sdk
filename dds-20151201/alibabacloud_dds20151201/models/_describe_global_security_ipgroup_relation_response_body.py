# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalSecurityIPGroupRelationResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        global_security_ipgroup_rel: List[main_models.DescribeGlobalSecurityIPGroupRelationResponseBodyGlobalSecurityIPGroupRel] = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbcluster_id = dbcluster_id
        # The global IP whitelist templates associated with the instance.
        self.global_security_ipgroup_rel = global_security_ipgroup_rel
        # The unique ID of the request. If the request fails, provide this ID for technical support to troubleshoot the failure.
        self.request_id = request_id

    def validate(self):
        if self.global_security_ipgroup_rel:
            for v1 in self.global_security_ipgroup_rel:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['GlobalSecurityIPGroupRel'] = []
        if self.global_security_ipgroup_rel is not None:
            for k1 in self.global_security_ipgroup_rel:
                result['GlobalSecurityIPGroupRel'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.global_security_ipgroup_rel = []
        if m.get('GlobalSecurityIPGroupRel') is not None:
            for k1 in m.get('GlobalSecurityIPGroupRel'):
                temp_model = main_models.DescribeGlobalSecurityIPGroupRelationResponseBodyGlobalSecurityIPGroupRel()
                self.global_security_ipgroup_rel.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGlobalSecurityIPGroupRelationResponseBodyGlobalSecurityIPGroupRel(DaraModel):
    def __init__(
        self,
        gip_list: str = None,
        global_ig_name: str = None,
        global_security_group_id: str = None,
        region_id: str = None,
    ):
        # The IP addresses in the whitelist template.
        # 
        # >  Separate multiple IP addresses with commas (,). You can create up to 1,000 IP addresses or CIDR blocks for all IP whitelists.
        self.gip_list = gip_list
        # The name of the IP whitelist template.
        self.global_ig_name = global_ig_name
        # The ID of the IP whitelist template.
        self.global_security_group_id = global_security_group_id
        # The region ID of the instance.
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

