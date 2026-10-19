# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedClusterInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeDedicatedClusterInstanceListResponseBodyInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of instance information.
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeDedicatedClusterInstanceListResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDedicatedClusterInstanceListResponseBodyInstances(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        character_type: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        connection_domain: str = None,
        create_time: str = None,
        current_band_width: int = None,
        custom_id: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_node_list: List[main_models.DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList] = None,
        instance_status: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        proxy_count: int = None,
        region_id: str = None,
        shard_count: int = None,
        storage_type: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # The default bandwidth of the instance. Unit: MB/s.
        self.band_width = band_width
        # The architecture type. Valid values:
        # * **logic**: Cluster architecture.
        # * **normal**: Standard architecture.
        self.character_type = character_type
        # The dedicated cluster ID.
        self.cluster_id = cluster_id
        # The dedicated cluster name.
        self.cluster_name = cluster_name
        # The direct connection endpoint.
        self.connection_domain = connection_domain
        # The time when the instance was created. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The current bandwidth of the instance. Unit: MB/s. The value is the sum of the default bandwidth and the increased bandwidth.
        self.current_band_width = current_band_width
        # An internal parameter used for instance maintenance.
        self.custom_id = custom_id
        # The database engine. The value is fixed as **redis**.
        self.engine = engine
        # The database engine version. The value is fixed as **5.0**.
        self.engine_version = engine_version
        # The instance type.
        self.instance_class = instance_class
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The list of node information.
        self.instance_node_list = instance_node_list
        # The instance status. Valid values:
        # * **Normal**: Normal.
        # * **Creating**: Creating.
        # * **Changing**: Changing.
        # * **Inactive**: Disabled.
        # * **Flushing**: Purge in progress.
        # * **Released**: Released.
        # * **Transforming**: Transforming.
        # * **Unavailable**: Unavailable.
        # * **Error**: Creation failed.
        # * **Migrating**: Migrating.
        # * **BackupRecovering**: Restoring from backup.
        # * **MinorVersionUpgrading**: Minor version upgrade in progress.
        # * **NetworkModifying**: Changing the network.
        # * **SSLModifying**: Changing SSL configurations.
        # * **MajorVersionUpgrading**: Major engine version upgrade in progress. The instance remains accessible.
        self.instance_status = instance_status
        # The end time of the maintenance window. The time is in the <i>HH:mm</i>Z format. The time is displayed in UTC.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window. The time is in the <i>HH:mm</i>Z format. The time is displayed in UTC.
        self.maintain_start_time = maintain_start_time
        # The number of proxy nodes.
        # > * A value of **0** indicates that the proxy mode is disabled for the instance. A value greater than **0** (such as **1**) indicates that the proxy mode is enabled for the instance.
        # > * This parameter is returned only when the instance uses the [cluster architecture](https://help.aliyun.com/document_detail/52228.html).
        self.proxy_count = proxy_count
        # The region ID.
        self.region_id = region_id
        # The number of data shards.
        # > This parameter is returned only when the instance uses the [cluster architecture](https://help.aliyun.com/document_detail/52228.html).
        self.shard_count = shard_count
        # The storage type. The value is fixed as LOCAL_SSD ([ESSD cloud disk (standard SSD)](https://help.aliyun.com/document_detail/122389.html)).
        self.storage_type = storage_type
        # The VPC ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.instance_node_list:
            for v1 in self.instance_node_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['BandWidth'] = self.band_width

        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_band_width is not None:
            result['CurrentBandWidth'] = self.current_band_width

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        result['InstanceNodeList'] = []
        if self.instance_node_list is not None:
            for k1 in self.instance_node_list:
                result['InstanceNodeList'].append(k1.to_map() if k1 else None)

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.proxy_count is not None:
            result['ProxyCount'] = self.proxy_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')

        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentBandWidth') is not None:
            self.current_band_width = m.get('CurrentBandWidth')

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.instance_node_list = []
        if m.get('InstanceNodeList') is not None:
            for k1 in m.get('InstanceNodeList'):
                temp_model = main_models.DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList()
                self.instance_node_list.append(temp_model.from_map(k1))

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('ProxyCount') is not None:
            self.proxy_count = m.get('ProxyCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDedicatedClusterInstanceListResponseBodyInstancesInstanceNodeList(DaraModel):
    def __init__(
        self,
        dedicated_host_name: str = None,
        instance_id: str = None,
        node_id: int = None,
        node_ip: str = None,
        node_type: str = None,
        port: int = None,
        role: str = None,
        zone_id: str = None,
    ):
        # The host ID in the dedicated cluster.
        self.dedicated_host_name = dedicated_host_name
        # The instance ID.
        self.instance_id = instance_id
        # The node ID.
        self.node_id = node_id
        # The IP address of the node.
        self.node_ip = node_ip
        # The node type. Valid values:
        # * **db**: Data node.
        # * **proxy**: Proxy node.
        # * **normal**: Regular node. This value is returned for instances that use the standard architecture.
        self.node_type = node_type
        # The port of the node.
        self.port = port
        # The node role. Valid values:
        # * **master**: Primary node.
        # * **slave**: Secondary node.
        self.role = role
        # The zone to which the node belongs.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.port is not None:
            result['Port'] = self.port

        if self.role is not None:
            result['Role'] = self.role

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

