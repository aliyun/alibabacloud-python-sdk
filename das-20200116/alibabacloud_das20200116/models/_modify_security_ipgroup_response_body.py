# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class ModifySecurityIPGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ModifySecurityIPGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        # ListResult<InstanceSSL>
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.ModifySecurityIPGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifySecurityIPGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        global_security_ipgroup: List[main_models.ModifySecurityIPGroupResponseBodyDataGlobalSecurityIPGroup] = None,
    ):
        self.global_security_ipgroup = global_security_ipgroup

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_security_ipgroup = []
        if m.get('GlobalSecurityIPGroup') is not None:
            for k1 in m.get('GlobalSecurityIPGroup'):
                temp_model = main_models.ModifySecurityIPGroupResponseBodyDataGlobalSecurityIPGroup()
                self.global_security_ipgroup.append(temp_model.from_map(k1))

        return self

class ModifySecurityIPGroupResponseBodyDataGlobalSecurityIPGroup(DaraModel):
    def __init__(
        self,
        gip_list: str = None,
        global_ig_name: str = None,
        global_security_group_id: str = None,
        region_id: str = None,
        security_ip_type: str = None,
        whitelist_net_type: str = None,
    ):
        self.gip_list = gip_list
        self.global_ig_name = global_ig_name
        self.global_security_group_id = global_security_group_id
        self.region_id = region_id
        self.security_ip_type = security_ip_type
        self.whitelist_net_type = whitelist_net_type

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

        if self.security_ip_type is not None:
            result['SecurityIpType'] = self.security_ip_type

        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type

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

        if m.get('SecurityIpType') is not None:
            self.security_ip_type = m.get('SecurityIpType')

        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')

        return self

