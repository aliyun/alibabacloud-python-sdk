# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        resource_group_list: main_models.ListResourceGroupResponseBodyResourceGroupList = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.resource_group_list = resource_group_list

    def validate(self):
        if self.resource_group_list:
            self.resource_group_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_list is not None:
            result['ResourceGroupList'] = self.resource_group_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupList') is not None:
            temp_model = main_models.ListResourceGroupResponseBodyResourceGroupList()
            self.resource_group_list = temp_model.from_map(m.get('ResourceGroupList'))

        return self

class ListResourceGroupResponseBodyResourceGroupList(DaraModel):
    def __init__(
        self,
        res_group_entity: List[main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntity] = None,
    ):
        self.res_group_entity = res_group_entity

    def validate(self):
        if self.res_group_entity:
            for v1 in self.res_group_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResGroupEntity'] = []
        if self.res_group_entity is not None:
            for k1 in self.res_group_entity:
                result['ResGroupEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.res_group_entity = []
        if m.get('ResGroupEntity') is not None:
            for k1 in m.get('ResGroupEntity'):
                temp_model = main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntity()
                self.res_group_entity.append(temp_model.from_map(k1))

        return self

class ListResourceGroupResponseBodyResourceGroupListResGroupEntity(DaraModel):
    def __init__(
        self,
        admin_user_id: str = None,
        create_time: int = None,
        description: str = None,
        id: int = None,
        name: str = None,
        region_id: str = None,
        slb_list: main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntitySlbList = None,
        update_time: int = None,
        ecs_list: main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsList = None,
    ):
        self.admin_user_id = admin_user_id
        self.create_time = create_time
        self.description = description
        self.id = id
        self.name = name
        self.region_id = region_id
        self.slb_list = slb_list
        self.update_time = update_time
        self.ecs_list = ecs_list

    def validate(self):
        if self.slb_list:
            self.slb_list.validate()
        if self.ecs_list:
            self.ecs_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_user_id is not None:
            result['AdminUserId'] = self.admin_user_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slb_list is not None:
            result['SlbList'] = self.slb_list.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.ecs_list is not None:
            result['ecsList'] = self.ecs_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUserId') is not None:
            self.admin_user_id = m.get('AdminUserId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlbList') is not None:
            temp_model = main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntitySlbList()
            self.slb_list = temp_model.from_map(m.get('SlbList'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('ecsList') is not None:
            temp_model = main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsList()
            self.ecs_list = temp_model.from_map(m.get('ecsList'))

        return self

class ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsList(DaraModel):
    def __init__(
        self,
        ecs_entity: List[main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntity] = None,
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
                temp_model = main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntity()
                self.ecs_entity.append(temp_model.from_map(k1))

        return self

class ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntity(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        description: str = None,
        ecu_entity: main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntityEcuEntity = None,
        eip: str = None,
        expired: bool = None,
        group_id: str = None,
        host_name: str = None,
        inner_ip: str = None,
        instance_id: str = None,
        instance_name: str = None,
        mem: int = None,
        private_ip: str = None,
        public_ip: str = None,
        region_id: str = None,
        serial_num: str = None,
        sg_id: str = None,
        status: str = None,
        user_id: str = None,
        vpc_entity: main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntityVpcEntity = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.cpu = cpu
        self.description = description
        self.ecu_entity = ecu_entity
        self.eip = eip
        self.expired = expired
        self.group_id = group_id
        self.host_name = host_name
        self.inner_ip = inner_ip
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.mem = mem
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.region_id = region_id
        self.serial_num = serial_num
        self.sg_id = sg_id
        self.status = status
        self.user_id = user_id
        self.vpc_entity = vpc_entity
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.ecu_entity:
            self.ecu_entity.validate()
        if self.vpc_entity:
            self.vpc_entity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.description is not None:
            result['Description'] = self.description

        if self.ecu_entity is not None:
            result['EcuEntity'] = self.ecu_entity.to_map()

        if self.eip is not None:
            result['Eip'] = self.eip

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

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

        if self.serial_num is not None:
            result['SerialNum'] = self.serial_num

        if self.sg_id is not None:
            result['SgId'] = self.sg_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vpc_entity is not None:
            result['VpcEntity'] = self.vpc_entity.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcuEntity') is not None:
            temp_model = main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntityEcuEntity()
            self.ecu_entity = temp_model.from_map(m.get('EcuEntity'))

        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

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

        if m.get('SerialNum') is not None:
            self.serial_num = m.get('SerialNum')

        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VpcEntity') is not None:
            temp_model = main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntityVpcEntity()
            self.vpc_entity = temp_model.from_map(m.get('VpcEntity'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntityVpcEntity(DaraModel):
    def __init__(
        self,
        cidrblock: str = None,
        description: str = None,
        ecs_num: int = None,
        expired: bool = None,
        region_id: str = None,
        status: str = None,
        user_id: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidrblock = cidrblock
        self.description = description
        self.ecs_num = ecs_num
        self.expired = expired
        self.region_id = region_id
        self.status = status
        self.user_id = user_id
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidrblock is not None:
            result['Cidrblock'] = self.cidrblock

        if self.description is not None:
            result['Description'] = self.description

        if self.ecs_num is not None:
            result['EcsNum'] = self.ecs_num

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrblock') is not None:
            self.cidrblock = m.get('Cidrblock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcsNum') is not None:
            self.ecs_num = m.get('EcsNum')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class ListResourceGroupResponseBodyResourceGroupListResGroupEntityEcsListEcsEntityEcuEntity(DaraModel):
    def __init__(
        self,
        available_cpu: int = None,
        available_mem: int = None,
        cpu: int = None,
        create_time: int = None,
        docker_env: bool = None,
        ecu_id: str = None,
        heartbeat_time: int = None,
        instance_id: str = None,
        ip_addr: str = None,
        mem: int = None,
        name: str = None,
        online: bool = None,
        region_id: str = None,
        update_time: int = None,
        user_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.available_cpu = available_cpu
        self.available_mem = available_mem
        self.cpu = cpu
        self.create_time = create_time
        self.docker_env = docker_env
        self.ecu_id = ecu_id
        self.heartbeat_time = heartbeat_time
        self.instance_id = instance_id
        self.ip_addr = ip_addr
        self.mem = mem
        self.name = name
        self.online = online
        self.region_id = region_id
        self.update_time = update_time
        self.user_id = user_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_cpu is not None:
            result['AvailableCpu'] = self.available_cpu

        if self.available_mem is not None:
            result['AvailableMem'] = self.available_mem

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.docker_env is not None:
            result['DockerEnv'] = self.docker_env

        if self.ecu_id is not None:
            result['EcuId'] = self.ecu_id

        if self.heartbeat_time is not None:
            result['HeartbeatTime'] = self.heartbeat_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_addr is not None:
            result['IpAddr'] = self.ip_addr

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.name is not None:
            result['Name'] = self.name

        if self.online is not None:
            result['Online'] = self.online

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableCpu') is not None:
            self.available_cpu = m.get('AvailableCpu')

        if m.get('AvailableMem') is not None:
            self.available_mem = m.get('AvailableMem')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DockerEnv') is not None:
            self.docker_env = m.get('DockerEnv')

        if m.get('EcuId') is not None:
            self.ecu_id = m.get('EcuId')

        if m.get('HeartbeatTime') is not None:
            self.heartbeat_time = m.get('HeartbeatTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpAddr') is not None:
            self.ip_addr = m.get('IpAddr')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListResourceGroupResponseBodyResourceGroupListResGroupEntitySlbList(DaraModel):
    def __init__(
        self,
        slb_entity: List[main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntitySlbListSlbEntity] = None,
    ):
        self.slb_entity = slb_entity

    def validate(self):
        if self.slb_entity:
            for v1 in self.slb_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlbEntity'] = []
        if self.slb_entity is not None:
            for k1 in self.slb_entity:
                result['SlbEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slb_entity = []
        if m.get('SlbEntity') is not None:
            for k1 in m.get('SlbEntity'):
                temp_model = main_models.ListResourceGroupResponseBodyResourceGroupListResGroupEntitySlbListSlbEntity()
                self.slb_entity.append(temp_model.from_map(k1))

        return self

class ListResourceGroupResponseBodyResourceGroupListResGroupEntitySlbListSlbEntity(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_type: str = None,
        expired: bool = None,
        group_id: int = None,
        network_type: str = None,
        region_id: str = None,
        slb_id: str = None,
        slb_name: str = None,
        slb_status: str = None,
        user_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.address = address
        self.address_type = address_type
        self.expired = expired
        self.group_id = group_id
        self.network_type = network_type
        self.region_id = region_id
        self.slb_id = slb_id
        self.slb_name = slb_name
        self.slb_status = slb_status
        self.user_id = user_id
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_name is not None:
            result['SlbName'] = self.slb_name

        if self.slb_status is not None:
            result['SlbStatus'] = self.slb_status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')

        if m.get('SlbStatus') is not None:
            self.slb_status = m.get('SlbStatus')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

