# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class Logstash(DaraModel):
    def __init__(
        self,
        config: Dict[str, str] = None,
        created_at: str = None,
        data_node: bool = None,
        description: str = None,
        end_time: int = None,
        endpoint_list: List[main_models.LogstashEndpointList] = None,
        instance_id: str = None,
        network_config: main_models.LogstashNetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.LogstashNodeSpec = None,
        payment_type: str = None,
        protocol: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.LogstashTags] = None,
        updated_at: str = None,
        version: str = None,
        zone_count: int = None,
        zone_infos: List[main_models.LogstashZoneInfos] = None,
    ):
        self.config = config
        self.created_at = created_at
        self.data_node = data_node
        self.description = description
        self.end_time = end_time
        self.endpoint_list = endpoint_list
        self.instance_id = instance_id
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.protocol = protocol
        self.resource_group_id = resource_group_id
        self.status = status
        self.tags = tags
        self.updated_at = updated_at
        self.version = version
        self.zone_count = zone_count
        self.zone_infos = zone_infos

    def validate(self):
        if self.endpoint_list:
            for v1 in self.endpoint_list:
                 if v1:
                    v1.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.zone_infos:
            for v1 in self.zone_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.data_node is not None:
            result['dataNode'] = self.data_node

        if self.description is not None:
            result['description'] = self.description

        if self.end_time is not None:
            result['endTime'] = self.end_time

        result['endpointList'] = []
        if self.endpoint_list is not None:
            for k1 in self.endpoint_list:
                result['endpointList'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount

        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.version is not None:
            result['version'] = self.version

        if self.zone_count is not None:
            result['zoneCount'] = self.zone_count

        result['zoneInfos'] = []
        if self.zone_infos is not None:
            for k1 in self.zone_infos:
                result['zoneInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('dataNode') is not None:
            self.data_node = m.get('dataNode')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        self.endpoint_list = []
        if m.get('endpointList') is not None:
            for k1 in m.get('endpointList'):
                temp_model = main_models.LogstashEndpointList()
                self.endpoint_list.append(temp_model.from_map(k1))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('networkConfig') is not None:
            temp_model = main_models.LogstashNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.LogstashNodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.LogstashTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('zoneCount') is not None:
            self.zone_count = m.get('zoneCount')

        self.zone_infos = []
        if m.get('zoneInfos') is not None:
            for k1 in m.get('zoneInfos'):
                temp_model = main_models.LogstashZoneInfos()
                self.zone_infos.append(temp_model.from_map(k1))

        return self

class LogstashZoneInfos(DaraModel):
    def __init__(
        self,
        status: str = None,
        zone_id: str = None,
    ):
        self.status = status
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class LogstashTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class LogstashNodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class LogstashNetworkConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vs_area is not None:
            result['vsArea'] = self.vs_area

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        return self

class LogstashEndpointList(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        self.host = host
        self.port = port
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['host'] = self.host

        if self.port is not None:
            result['port'] = self.port

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

