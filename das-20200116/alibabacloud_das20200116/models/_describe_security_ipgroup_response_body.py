# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityIPGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSecurityIPGroupResponseBodyData = None,
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
            temp_model = main_models.DescribeSecurityIPGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSecurityIPGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        security_ip_groups: List[main_models.DescribeSecurityIPGroupResponseBodyDataSecurityIpGroups] = None,
    ):
        self.security_ip_groups = security_ip_groups

    def validate(self):
        if self.security_ip_groups:
            for v1 in self.security_ip_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecurityIpGroups'] = []
        if self.security_ip_groups is not None:
            for k1 in self.security_ip_groups:
                result['SecurityIpGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_ip_groups = []
        if m.get('SecurityIpGroups') is not None:
            for k1 in m.get('SecurityIpGroups'):
                temp_model = main_models.DescribeSecurityIPGroupResponseBodyDataSecurityIpGroups()
                self.security_ip_groups.append(temp_model.from_map(k1))

        return self

class DescribeSecurityIPGroupResponseBodyDataSecurityIpGroups(DaraModel):
    def __init__(
        self,
        db_instances: List[str] = None,
        engine_info_list: List[main_models.DescribeSecurityIPGroupResponseBodyDataSecurityIpGroupsEngineInfoList] = None,
        gecs_sg_id_list: str = None,
        gip_list: str = None,
        global_ig_name: str = None,
        global_security_group_id: str = None,
        region_id: str = None,
        security_ip_type: str = None,
        uid: str = None,
        user_id: str = None,
        whitelist_net_type: str = None,
    ):
        self.db_instances = db_instances
        self.engine_info_list = engine_info_list
        self.gecs_sg_id_list = gecs_sg_id_list
        self.gip_list = gip_list
        self.global_ig_name = global_ig_name
        self.global_security_group_id = global_security_group_id
        self.region_id = region_id
        self.security_ip_type = security_ip_type
        self.uid = uid
        self.user_id = user_id
        self.whitelist_net_type = whitelist_net_type

    def validate(self):
        if self.engine_info_list:
            for v1 in self.engine_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instances is not None:
            result['DbInstances'] = self.db_instances

        result['EngineInfoList'] = []
        if self.engine_info_list is not None:
            for k1 in self.engine_info_list:
                result['EngineInfoList'].append(k1.to_map() if k1 else None)

        if self.gecs_sg_id_list is not None:
            result['GEcsSgIdList'] = self.gecs_sg_id_list

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

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstances') is not None:
            self.db_instances = m.get('DbInstances')

        self.engine_info_list = []
        if m.get('EngineInfoList') is not None:
            for k1 in m.get('EngineInfoList'):
                temp_model = main_models.DescribeSecurityIPGroupResponseBodyDataSecurityIpGroupsEngineInfoList()
                self.engine_info_list.append(temp_model.from_map(k1))

        if m.get('GEcsSgIdList') is not None:
            self.gecs_sg_id_list = m.get('GEcsSgIdList')

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

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')

        return self

class DescribeSecurityIPGroupResponseBodyDataSecurityIpGroupsEngineInfoList(DaraModel):
    def __init__(
        self,
        engine_name: str = None,
        instance_ids: List[str] = None,
        instance_num: int = None,
    ):
        self.engine_name = engine_name
        self.instance_ids = instance_ids
        self.instance_num = instance_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')

        return self

