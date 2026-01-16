# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeLogstashResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeLogstashResponseBodyResult = None,
    ):
        # Detailed information about the instance.
        self.request_id = request_id
        # The configurations of the instance.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeLogstashResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeLogstashResponseBodyResult(DaraModel):
    def __init__(
        self,
        extend_configs: List[Dict[str, Any]] = None,
        resource_group_id: str = None,
        tags: List[main_models.DescribeLogstashResponseBodyResultTags] = None,
        zone_infos: List[main_models.DescribeLogstashResponseBodyResultZoneInfos] = None,
        config: Dict[str, Any] = None,
        created_at: str = None,
        description: str = None,
        endpoint_list: List[main_models.DescribeLogstashResponseBodyResultEndpointList] = None,
        instance_id: str = None,
        network_config: main_models.DescribeLogstashResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.DescribeLogstashResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        status: str = None,
        updated_at: str = None,
        version: str = None,
        vpc_instance_id: str = None,
    ):
        # The configuration information of the node.
        self.extend_configs = extend_configs
        # The number of data nodes.
        self.resource_group_id = resource_group_id
        # The key of the tag.
        self.tags = tags
        # The status of the zone. Valid values:
        # 
        # *   ISOLATION: offline
        # *   NORMAL
        self.zone_infos = zone_infos
        # The billing method of the instance. Valid values:
        # 
        # *   prepaid: subscription
        # *   postpaid: pay-as-you-go
        self.config = config
        # The state of the instance. Four states are supported:
        # 
        # *   Normal: active
        # *   Active: activating
        # *   Freeze: inactive
        # *   Invalid: invalid
        self.created_at = created_at
        # The time when the instance was created.
        self.description = description
        # The ID of the zone where the node resides.
        self.endpoint_list = endpoint_list
        # The access information of the node.
        self.instance_id = instance_id
        # The ID of the virtual private cloud (VPC).
        self.network_config = network_config
        # The name of the instance.
        self.node_amount = node_amount
        # The specifications of the node.
        self.node_spec = node_spec
        # The ID of the resource group to which the instance belongs.
        self.payment_type = payment_type
        # The ID of the virtual private cloud (VPC) to which the elastic container instances belong.
        self.status = status
        # The edition of the dedicated KMS instance.
        self.updated_at = updated_at
        # The ID of the instance.
        self.version = version
        # The time when the instance was last updated.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.zone_infos:
            for v1 in self.zone_infos:
                 if v1:
                    v1.validate()
        if self.endpoint_list:
            for v1 in self.endpoint_list:
                 if v1:
                    v1.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_configs is not None:
            result['ExtendConfigs'] = self.extend_configs

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['ZoneInfos'] = []
        if self.zone_infos is not None:
            for k1 in self.zone_infos:
                result['ZoneInfos'].append(k1.to_map() if k1 else None)

        if self.config is not None:
            result['config'] = self.config

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

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

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.version is not None:
            result['version'] = self.version

        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendConfigs') is not None:
            self.extend_configs = m.get('ExtendConfigs')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeLogstashResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k1))

        self.zone_infos = []
        if m.get('ZoneInfos') is not None:
            for k1 in m.get('ZoneInfos'):
                temp_model = main_models.DescribeLogstashResponseBodyResultZoneInfos()
                self.zone_infos.append(temp_model.from_map(k1))

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.endpoint_list = []
        if m.get('endpointList') is not None:
            for k1 in m.get('endpointList'):
                temp_model = main_models.DescribeLogstashResponseBodyResultEndpointList()
                self.endpoint_list.append(temp_model.from_map(k1))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('networkConfig') is not None:
            temp_model = main_models.DescribeLogstashResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.DescribeLogstashResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')

        return self

class DescribeLogstashResponseBodyResultNodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # Whether to use disk encryption:
        # 
        # *   true
        # *   false
        self.disk = disk
        # The disk type of the node.
        self.disk_encryption = disk_encryption
        # The network configurations.
        self.disk_type = disk_type
        # The disk size of the node.
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

        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class DescribeLogstashResponseBodyResultNetworkConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        # The ID of the vSwitch to which the instance is connected.
        self.type = type
        # The zone where the cluster resides.
        self.vpc_id = vpc_id
        # The network type of the instance. Valid values: Currently, only Virtual Private Cloud (VPC) are supported.
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

class DescribeLogstashResponseBodyResultEndpointList(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
        zone_id: str = None,
    ):
        # The tags added to the ALB instance.
        self.host = host
        # The IP address of the node.
        self.port = port
        # The port number.
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

class DescribeLogstashResponseBodyResultZoneInfos(DaraModel):
    def __init__(
        self,
        status: str = None,
        zone_id: str = None,
    ):
        # The zone ID of the new instance.
        self.status = status
        # The configuration of cluster extension parameters.
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

class DescribeLogstashResponseBodyResultTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The value of the tag.
        self.tag_key = tag_key
        # The information about the zones.
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

