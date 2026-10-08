# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListEcsNotInClusterResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        ecs_entity_list: main_models.ListEcsNotInClusterResponseBodyEcsEntityList = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        self.ecs_entity_list = ecs_entity_list
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ecs_entity_list:
            self.ecs_entity_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.ecs_entity_list is not None:
            result['EcsEntityList'] = self.ecs_entity_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EcsEntityList') is not None:
            temp_model = main_models.ListEcsNotInClusterResponseBodyEcsEntityList()
            self.ecs_entity_list = temp_model.from_map(m.get('EcsEntityList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEcsNotInClusterResponseBodyEcsEntityList(DaraModel):
    def __init__(
        self,
        ecs_entity: List[main_models.ListEcsNotInClusterResponseBodyEcsEntityListEcsEntity] = None,
    ):
        self.ecs_entity = ecs_entity

    def validate(self):
        if self.ecs_entity:
            for v1 in self.ecs_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EcsEntity'] = []
        if self.ecs_entity is not None:
            for k1 in self.ecs_entity:
                result['EcsEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_entity = []
        if m.get('EcsEntity') is not None:
            for k1 in m.get('EcsEntity'):
                temp_model = main_models.ListEcsNotInClusterResponseBodyEcsEntityListEcsEntity()
                self.ecs_entity.append(temp_model.from_map(k1))

        return self

class ListEcsNotInClusterResponseBodyEcsEntityListEcsEntity(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        eip: str = None,
        expired: bool = None,
        inner_ip: str = None,
        instance_id: str = None,
        instance_name: str = None,
        mem: int = None,
        private_ip: str = None,
        public_ip: str = None,
        region_id: str = None,
        status: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cpu = cpu
        self.eip = eip
        self.expired = expired
        self.inner_ip = inner_ip
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.mem = mem
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.region_id = region_id
        self.status = status
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.eip is not None:
            result['Eip'] = self.eip

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

