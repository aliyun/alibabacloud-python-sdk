# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class GetAgentListResponseBody(DaraModel):
    def __init__(
        self,
        agent_list: List[main_models.GetAgentListResponseBodyAgentList] = None,
        request_id: str = None,
    ):
        self.agent_list = agent_list
        self.request_id = request_id

    def validate(self):
        if self.agent_list:
            for v1 in self.agent_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AgentList'] = []
        if self.agent_list is not None:
            for k1 in self.agent_list:
                result['AgentList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_list = []
        if m.get('AgentList') is not None:
            for k1 in m.get('AgentList'):
                temp_model = main_models.GetAgentListResponseBodyAgentList()
                self.agent_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAgentListResponseBodyAgentList(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_os: str = None,
        agent_port: str = None,
        agent_status: int = None,
        agent_version: str = None,
        ecs_id: str = None,
        first_login_time: str = None,
        last_active_time: str = None,
        os_cpu: int = None,
        os_mem: int = None,
        pkt_loss: int = None,
        private_ip: str = None,
        public_ip: str = None,
        rmagent_cpu: int = None,
        rmagent_mem: int = None,
        send_byte_count: int = None,
        send_bytes: int = None,
        send_packet_count: int = None,
        send_packets: int = None,
        sys_config: str = None,
        tags: List[main_models.GetAgentListResponseBodyAgentListTags] = None,
        vpc_id: str = None,
    ):
        self.agent_id = agent_id
        self.agent_os = agent_os
        self.agent_port = agent_port
        self.agent_status = agent_status
        self.agent_version = agent_version
        self.ecs_id = ecs_id
        self.first_login_time = first_login_time
        self.last_active_time = last_active_time
        self.os_cpu = os_cpu
        self.os_mem = os_mem
        self.pkt_loss = pkt_loss
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.rmagent_cpu = rmagent_cpu
        self.rmagent_mem = rmagent_mem
        self.send_byte_count = send_byte_count
        self.send_bytes = send_bytes
        self.send_packet_count = send_packet_count
        self.send_packets = send_packets
        self.sys_config = sys_config
        self.tags = tags
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_os is not None:
            result['AgentOs'] = self.agent_os

        if self.agent_port is not None:
            result['AgentPort'] = self.agent_port

        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id

        if self.first_login_time is not None:
            result['FirstLoginTime'] = self.first_login_time

        if self.last_active_time is not None:
            result['LastActiveTime'] = self.last_active_time

        if self.os_cpu is not None:
            result['OsCpu'] = self.os_cpu

        if self.os_mem is not None:
            result['OsMem'] = self.os_mem

        if self.pkt_loss is not None:
            result['PktLoss'] = self.pkt_loss

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.rmagent_cpu is not None:
            result['RmagentCpu'] = self.rmagent_cpu

        if self.rmagent_mem is not None:
            result['RmagentMem'] = self.rmagent_mem

        if self.send_byte_count is not None:
            result['SendByteCount'] = self.send_byte_count

        if self.send_bytes is not None:
            result['SendBytes'] = self.send_bytes

        if self.send_packet_count is not None:
            result['SendPacketCount'] = self.send_packet_count

        if self.send_packets is not None:
            result['SendPackets'] = self.send_packets

        if self.sys_config is not None:
            result['SysConfig'] = self.sys_config

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentOs') is not None:
            self.agent_os = m.get('AgentOs')

        if m.get('AgentPort') is not None:
            self.agent_port = m.get('AgentPort')

        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')

        if m.get('FirstLoginTime') is not None:
            self.first_login_time = m.get('FirstLoginTime')

        if m.get('LastActiveTime') is not None:
            self.last_active_time = m.get('LastActiveTime')

        if m.get('OsCpu') is not None:
            self.os_cpu = m.get('OsCpu')

        if m.get('OsMem') is not None:
            self.os_mem = m.get('OsMem')

        if m.get('PktLoss') is not None:
            self.pkt_loss = m.get('PktLoss')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('RmagentCpu') is not None:
            self.rmagent_cpu = m.get('RmagentCpu')

        if m.get('RmagentMem') is not None:
            self.rmagent_mem = m.get('RmagentMem')

        if m.get('SendByteCount') is not None:
            self.send_byte_count = m.get('SendByteCount')

        if m.get('SendBytes') is not None:
            self.send_bytes = m.get('SendBytes')

        if m.get('SendPacketCount') is not None:
            self.send_packet_count = m.get('SendPacketCount')

        if m.get('SendPackets') is not None:
            self.send_packets = m.get('SendPackets')

        if m.get('SysConfig') is not None:
            self.sys_config = m.get('SysConfig')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetAgentListResponseBodyAgentListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetAgentListResponseBodyAgentListTags(DaraModel):
    def __init__(
        self,
        tag_id: int = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_id = tag_id
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

