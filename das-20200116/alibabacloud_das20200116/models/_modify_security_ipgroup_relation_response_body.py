# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class ModifySecurityIPGroupRelationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ModifySecurityIPGroupRelationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code.
        self.code = code
        # ListResult<InstanceSSL>
        self.data = data
        # The returned message.
        # >If the request is successful, Successful is returned. If the request fails, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # * true: The request is successful.
        # * false: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ModifySecurityIPGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifySecurityIPGroupRelationResponseBodyData(DaraModel):
    def __init__(
        self,
        global_security_ipgroup_rel: List[main_models.ModifySecurityIPGroupRelationResponseBodyDataGlobalSecurityIPGroupRel] = None,
        instance_id: str = None,
    ):
        # The binding information of the cross-engine IP whitelist template.
        self.global_security_ipgroup_rel = global_security_ipgroup_rel
        # The instance ID.
        self.instance_id = instance_id

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
        result['GlobalSecurityIPGroupRel'] = []
        if self.global_security_ipgroup_rel is not None:
            for k1 in self.global_security_ipgroup_rel:
                result['GlobalSecurityIPGroupRel'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_security_ipgroup_rel = []
        if m.get('GlobalSecurityIPGroupRel') is not None:
            for k1 in m.get('GlobalSecurityIPGroupRel'):
                temp_model = main_models.ModifySecurityIPGroupRelationResponseBodyDataGlobalSecurityIPGroupRel()
                self.global_security_ipgroup_rel.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class ModifySecurityIPGroupRelationResponseBodyDataGlobalSecurityIPGroupRel(DaraModel):
    def __init__(
        self,
        gip_list: str = None,
        global_ig_name: str = None,
        global_security_group_id: str = None,
        region_id: str = None,
    ):
        # The IP addresses in the whitelist template.
        # 
        # > Separate multiple IP addresses with commas (,). You can add up to 1,000 IP addresses or CIDR blocks across all IP whitelists.
        self.gip_list = gip_list
        # The name of the IP whitelist template. The name must meet the following requirements:
        # 
        # - Contains only lowercase letters, digits, and underscores (_).
        # 
        # - Starts with a letter and ends with a letter or digit.
        # 
        # - Contains 2 to 120 characters in length.
        self.global_ig_name = global_ig_name
        # The ID of the IP whitelist template.
        self.global_security_group_id = global_security_group_id
        # The region ID.
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

