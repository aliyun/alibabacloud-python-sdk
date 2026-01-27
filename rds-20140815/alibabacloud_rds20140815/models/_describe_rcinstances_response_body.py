# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCInstancesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        rcinstances: List[main_models.DescribeRCInstancesResponseBodyRCInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The details of the instance.
        self.rcinstances = rcinstances
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.rcinstances:
            for v1 in self.rcinstances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['RCInstances'] = []
        if self.rcinstances is not None:
            for k1 in self.rcinstances:
                result['RCInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.rcinstances = []
        if m.get('RCInstances') is not None:
            for k1 in m.get('RCInstances'):
                temp_model = main_models.DescribeRCInstancesResponseBodyRCInstances()
                self.rcinstances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRCInstancesResponseBodyRCInstances(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        cpu: int = None,
        create_mode: str = None,
        db_type: str = None,
        deployment_set_id: str = None,
        description: str = None,
        expired_time: str = None,
        gmt_created: str = None,
        host_ip: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        memory: int = None,
        node_type: str = None,
        public_ip: str = None,
        region_id: str = None,
        security_group_id: str = None,
        spot_strategy: str = None,
        status: str = None,
        tag_resources: List[main_models.DescribeRCInstancesResponseBodyRCInstancesTagResources] = None,
        tags: List[main_models.DescribeRCInstancesResponseBodyRCInstancesTags] = None,
        vpc_attributes: main_models.DescribeRCInstancesResponseBodyRCInstancesVpcAttributes = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The cluster name.
        self.cluster_name = cluster_name
        self.cpu = cpu
        self.create_mode = create_mode
        # The database type.
        self.db_type = db_type
        self.deployment_set_id = deployment_set_id
        # The instance description.
        self.description = description
        self.expired_time = expired_time
        # The time when the task was created. The time is displayed in GMT.
        self.gmt_created = gmt_created
        # The host IP address.
        self.host_ip = host_ip
        # The host name.
        self.host_name = host_name
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        # The instance ID.
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.instance_type_family = instance_type_family
        self.memory = memory
        self.node_type = node_type
        self.public_ip = public_ip
        # The region ID.
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.spot_strategy = spot_strategy
        # The instance status. Valid values:
        # 
        # *   **Pending**
        # *   **Running**
        # *   **Starting**
        # *   **Stopping**
        # *   **Stopped**
        # 
        # >  If the value returned for the DescribeRCInstances operation is different from the value that is returned for the **DescribeRCInstanceAttribute** operation, the value returned for the **DescribeRCInstanceAttribute** operation shall prevail.
        self.status = status
        self.tag_resources = tag_resources
        self.tags = tags
        self.vpc_attributes = vpc_attributes
        # The VPC ID.
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.tag_resources:
            for v1 in self.tag_resources:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.vpc_attributes:
            self.vpc_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.host_ip is not None:
            result['HostIp'] = self.host_ip

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.status is not None:
            result['Status'] = self.status

        result['TagResources'] = []
        if self.tag_resources is not None:
            for k1 in self.tag_resources:
                result['TagResources'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_attributes is not None:
            result['VpcAttributes'] = self.vpc_attributes.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k1 in m.get('TagResources'):
                temp_model = main_models.DescribeRCInstancesResponseBodyRCInstancesTagResources()
                self.tag_resources.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeRCInstancesResponseBodyRCInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcAttributes') is not None:
            temp_model = main_models.DescribeRCInstancesResponseBodyRCInstancesVpcAttributes()
            self.vpc_attributes = temp_model.from_map(m.get('VpcAttributes'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeRCInstancesResponseBodyRCInstancesVpcAttributes(DaraModel):
    def __init__(
        self,
        nat_ip_address: str = None,
        private_ip_address: List[str] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.nat_ip_address = nat_ip_address
        self.private_ip_address = private_ip_address
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_ip_address is not None:
            result['NatIpAddress'] = self.nat_ip_address

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatIpAddress') is not None:
            self.nat_ip_address = m.get('NatIpAddress')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeRCInstancesResponseBodyRCInstancesTags(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeRCInstancesResponseBodyRCInstancesTagResources(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

