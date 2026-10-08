# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListApplicationEcuResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        ecu_info_list: main_models.ListApplicationEcuResponseBodyEcuInfoList = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        self.ecu_info_list = ecu_info_list
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ecu_info_list:
            self.ecu_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.ecu_info_list is not None:
            result['EcuInfoList'] = self.ecu_info_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EcuInfoList') is not None:
            temp_model = main_models.ListApplicationEcuResponseBodyEcuInfoList()
            self.ecu_info_list = temp_model.from_map(m.get('EcuInfoList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListApplicationEcuResponseBodyEcuInfoList(DaraModel):
    def __init__(
        self,
        ecu_entity: List[main_models.ListApplicationEcuResponseBodyEcuInfoListEcuEntity] = None,
    ):
        self.ecu_entity = ecu_entity

    def validate(self):
        if self.ecu_entity:
            for v1 in self.ecu_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EcuEntity'] = []
        if self.ecu_entity is not None:
            for k1 in self.ecu_entity:
                result['EcuEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecu_entity = []
        if m.get('EcuEntity') is not None:
            for k1 in m.get('EcuEntity'):
                temp_model = main_models.ListApplicationEcuResponseBodyEcuInfoListEcuEntity()
                self.ecu_entity.append(temp_model.from_map(k1))

        return self

class ListApplicationEcuResponseBodyEcuInfoListEcuEntity(DaraModel):
    def __init__(
        self,
        app_id: str = None,
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
        self.app_id = app_id
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

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

