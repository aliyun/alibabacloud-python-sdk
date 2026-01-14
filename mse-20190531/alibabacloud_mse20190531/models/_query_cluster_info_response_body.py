# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryClusterInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryClusterInfoResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The message returned.
        # 
        # *   If the request is successful, a success message is returned.
        # *   If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.QueryClusterInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryClusterInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        acl_entry_list: str = None,
        acl_id: str = None,
        app_version: str = None,
        can_update: bool = None,
        charge_type: str = None,
        cluster_alias_name: str = None,
        cluster_name: str = None,
        cluster_specification: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        connection_type: str = None,
        cpu: int = None,
        create_time: str = None,
        disk_capacity: int = None,
        disk_type: str = None,
        eip_instance_id: str = None,
        end_date: str = None,
        expect_zones: List[str] = None,
        health_status: str = None,
        init_cost_time: int = None,
        init_status: str = None,
        instance_count: int = None,
        instance_id: str = None,
        instance_models: List[main_models.QueryClusterInfoResponseBodyDataInstanceModels] = None,
        internet_address: str = None,
        internet_domain: str = None,
        internet_port: str = None,
        intranet_address: str = None,
        intranet_domain: str = None,
        intranet_port: str = None,
        maintenance_period: main_models.QueryClusterInfoResponseBodyDataMaintenancePeriod = None,
        memory_capacity: int = None,
        mse_version: str = None,
        net_type: str = None,
        pay_info: str = None,
        pub_network_flow: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_type: str = None,
        tags: Dict[str, Any] = None,
        v_switch_id: str = None,
        version_code: str = None,
        version_lifecycle: str = None,
        vpc_id: str = None,
    ):
        # The public IP address whitelist.
        self.acl_entry_list = acl_entry_list
        # The ID of the instance in the public IP address whitelist.
        self.acl_id = acl_id
        # The version of the instance.
        self.app_version = app_version
        self.can_update = can_update
        # The billing method, such as subscription or pay-as-you-go.
        self.charge_type = charge_type
        # The alias of the instance.
        self.cluster_alias_name = cluster_alias_name
        # The full name of the instance.
        self.cluster_name = cluster_name
        # The engine specifications.
        self.cluster_specification = cluster_specification
        # The type of the instance. Valid values: ZooKeeper, Nacos-Ans, and Eureka.
        self.cluster_type = cluster_type
        # The version of the order.
        self.cluster_version = cluster_version
        # A deprecated parameter.
        self.connection_type = connection_type
        # A deprecated parameter.
        self.cpu = cpu
        # The time when the instance was created.
        self.create_time = create_time
        # A deprecated parameter.
        self.disk_capacity = disk_capacity
        # A deprecated parameter.
        self.disk_type = disk_type
        # The ID of the instance that is associated with the Elastic IP Address (EIP).
        self.eip_instance_id = eip_instance_id
        # The time when the subscription instance expires.
        self.end_date = end_date
        # The zones to which the current cluster can be distributed.
        self.expect_zones = expect_zones
        # The status of the instance.
        self.health_status = health_status
        # The time that is required to initialize the instance. Unit: milliseconds.
        self.init_cost_time = init_cost_time
        # The initial status of the instance.
        self.init_status = init_status
        # The number of instance nodes.
        self.instance_count = instance_count
        # The ID of the instance
        self.instance_id = instance_id
        # The reserved structure.
        self.instance_models = instance_models
        # A reserved parameter.
        self.internet_address = internet_address
        # The public endpoint.
        self.internet_domain = internet_domain
        # The instance ports that are accessible over the Internet.
        self.internet_port = internet_port
        # A reserved parameter.
        self.intranet_address = intranet_address
        # The internal endpoint.
        self.intranet_domain = intranet_domain
        # The instance ports that are accessible over an internal network.
        self.intranet_port = intranet_port
        # The O\\&M time window.
        self.maintenance_period = maintenance_period
        # A deprecated parameter.
        self.memory_capacity = memory_capacity
        # The version of the instance.
        self.mse_version = mse_version
        # The network connection type of the instance.
        self.net_type = net_type
        # The billing method.
        self.pay_info = pay_info
        # The public bandwidth. Unit: Mbit/s.\\
        # Valid values: 0 to 5000. The value 0 indicates no access to the Internet.
        self.pub_network_flow = pub_network_flow
        # The ID of the region.
        self.region_id = region_id
        # The ID of the security group to which the elastic network interface (ENI) is connected.
        self.security_group_id = security_group_id
        # The type of the security group to which the ENI is connected.
        self.security_group_type = security_group_type
        # The tag.
        self.tags = tags
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        self.version_code = version_code
        self.version_lifecycle = version_lifecycle
        # The ID of the VPC where the instance resides.
        self.vpc_id = vpc_id

    def validate(self):
        if self.instance_models:
            for v1 in self.instance_models:
                 if v1:
                    v1.validate()
        if self.maintenance_period:
            self.maintenance_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list

        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.can_update is not None:
            result['CanUpdate'] = self.can_update

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.expect_zones is not None:
            result['ExpectZones'] = self.expect_zones

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.init_cost_time is not None:
            result['InitCostTime'] = self.init_cost_time

        if self.init_status is not None:
            result['InitStatus'] = self.init_status

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['InstanceModels'] = []
        if self.instance_models is not None:
            for k1 in self.instance_models:
                result['InstanceModels'].append(k1.to_map() if k1 else None)

        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address

        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain

        if self.internet_port is not None:
            result['InternetPort'] = self.internet_port

        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address

        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain

        if self.intranet_port is not None:
            result['IntranetPort'] = self.intranet_port

        if self.maintenance_period is not None:
            result['MaintenancePeriod'] = self.maintenance_period.to_map()

        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity

        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.pay_info is not None:
            result['PayInfo'] = self.pay_info

        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_type is not None:
            result['SecurityGroupType'] = self.security_group_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        if self.version_lifecycle is not None:
            result['VersionLifecycle'] = self.version_lifecycle

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')

        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('CanUpdate') is not None:
            self.can_update = m.get('CanUpdate')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExpectZones') is not None:
            self.expect_zones = m.get('ExpectZones')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InitCostTime') is not None:
            self.init_cost_time = m.get('InitCostTime')

        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.instance_models = []
        if m.get('InstanceModels') is not None:
            for k1 in m.get('InstanceModels'):
                temp_model = main_models.QueryClusterInfoResponseBodyDataInstanceModels()
                self.instance_models.append(temp_model.from_map(k1))

        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')

        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')

        if m.get('InternetPort') is not None:
            self.internet_port = m.get('InternetPort')

        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')

        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')

        if m.get('IntranetPort') is not None:
            self.intranet_port = m.get('IntranetPort')

        if m.get('MaintenancePeriod') is not None:
            temp_model = main_models.QueryClusterInfoResponseBodyDataMaintenancePeriod()
            self.maintenance_period = temp_model.from_map(m.get('MaintenancePeriod'))

        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('PayInfo') is not None:
            self.pay_info = m.get('PayInfo')

        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupType') is not None:
            self.security_group_type = m.get('SecurityGroupType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        if m.get('VersionLifecycle') is not None:
            self.version_lifecycle = m.get('VersionLifecycle')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class QueryClusterInfoResponseBodyDataMaintenancePeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The start time of the O\\&M time window.
        self.end_time = end_time
        # The end time of the O\\&M time window.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class QueryClusterInfoResponseBodyDataInstanceModels(DaraModel):
    def __init__(
        self,
        creation_timestamp: str = None,
        health_status: str = None,
        internet_ip: str = None,
        ip: str = None,
        pod_name: str = None,
        role: str = None,
        single_tunnel_vip: str = None,
        zone: str = None,
    ):
        # A reserved parameter.
        self.creation_timestamp = creation_timestamp
        # A reserved parameter.
        self.health_status = health_status
        # A reserved parameter.
        self.internet_ip = internet_ip
        # A reserved parameter.
        self.ip = ip
        # A reserved parameter.
        self.pod_name = pod_name
        # A reserved parameter.
        self.role = role
        # A reserved parameter.
        self.single_tunnel_vip = single_tunnel_vip
        # A reserved parameter.
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_timestamp is not None:
            result['CreationTimestamp'] = self.creation_timestamp

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.role is not None:
            result['Role'] = self.role

        if self.single_tunnel_vip is not None:
            result['SingleTunnelVip'] = self.single_tunnel_vip

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTimestamp') is not None:
            self.creation_timestamp = m.get('CreationTimestamp')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SingleTunnelVip') is not None:
            self.single_tunnel_vip = m.get('SingleTunnelVip')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

