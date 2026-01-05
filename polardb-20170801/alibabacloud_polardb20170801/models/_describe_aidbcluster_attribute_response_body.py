# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterAttributeResponseBody(DaraModel):
    def __init__(
        self,
        ai_node_type: str = None,
        creation_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        dbnodes: List[main_models.DescribeAIDBClusterAttributeResponseBodyDBNodes] = None,
        dbversion: str = None,
        ecs_security_group_id: str = None,
        endpoint_list: List[main_models.DescribeAIDBClusterAttributeResponseBodyEndpointList] = None,
        expire_time: str = None,
        expired: bool = None,
        internal_ip: str = None,
        kvcache_instance_id: str = None,
        kube_cluster_id: str = None,
        lock_mode: str = None,
        max_qpm: str = None,
        model_name: str = None,
        model_type: str = None,
        pay_type: str = None,
        public_ip: str = None,
        region_id: str = None,
        request_id: str = None,
        run_type: str = None,
        storage_type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        volumes: List[main_models.DescribeAIDBClusterAttributeResponseBodyVolumes] = None,
        zone_id: str = None,
        zone_ids: str = None,
    ):
        self.ai_node_type = ai_node_type
        self.creation_time = creation_time
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_status = dbcluster_status
        self.dbnodes = dbnodes
        self.dbversion = dbversion
        self.ecs_security_group_id = ecs_security_group_id
        self.endpoint_list = endpoint_list
        self.expire_time = expire_time
        self.expired = expired
        self.internal_ip = internal_ip
        self.kvcache_instance_id = kvcache_instance_id
        self.kube_cluster_id = kube_cluster_id
        self.lock_mode = lock_mode
        self.max_qpm = max_qpm
        self.model_name = model_name
        self.model_type = model_type
        self.pay_type = pay_type
        self.public_ip = public_ip
        self.region_id = region_id
        # Id of the request
        self.request_id = request_id
        self.run_type = run_type
        self.storage_type = storage_type
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.volumes = volumes
        self.zone_id = zone_id
        self.zone_ids = zone_ids

    def validate(self):
        if self.dbnodes:
            for v1 in self.dbnodes:
                 if v1:
                    v1.validate()
        if self.endpoint_list:
            for v1 in self.endpoint_list:
                 if v1:
                    v1.validate()
        if self.volumes:
            for v1 in self.volumes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_node_type is not None:
            result['AiNodeType'] = self.ai_node_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k1 in self.dbnodes:
                result['DBNodes'].append(k1.to_map() if k1 else None)

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.ecs_security_group_id is not None:
            result['EcsSecurityGroupId'] = self.ecs_security_group_id

        result['EndpointList'] = []
        if self.endpoint_list is not None:
            for k1 in self.endpoint_list:
                result['EndpointList'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.kvcache_instance_id is not None:
            result['KVCacheInstanceId'] = self.kvcache_instance_id

        if self.kube_cluster_id is not None:
            result['KubeClusterId'] = self.kube_cluster_id

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.max_qpm is not None:
            result['MaxQPM'] = self.max_qpm

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.run_type is not None:
            result['RunType'] = self.run_type

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        result['Volumes'] = []
        if self.volumes is not None:
            for k1 in self.volumes:
                result['Volumes'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiNodeType') is not None:
            self.ai_node_type = m.get('AiNodeType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k1 in m.get('DBNodes'):
                temp_model = main_models.DescribeAIDBClusterAttributeResponseBodyDBNodes()
                self.dbnodes.append(temp_model.from_map(k1))

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('EcsSecurityGroupId') is not None:
            self.ecs_security_group_id = m.get('EcsSecurityGroupId')

        self.endpoint_list = []
        if m.get('EndpointList') is not None:
            for k1 in m.get('EndpointList'):
                temp_model = main_models.DescribeAIDBClusterAttributeResponseBodyEndpointList()
                self.endpoint_list.append(temp_model.from_map(k1))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('KVCacheInstanceId') is not None:
            self.kvcache_instance_id = m.get('KVCacheInstanceId')

        if m.get('KubeClusterId') is not None:
            self.kube_cluster_id = m.get('KubeClusterId')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaxQPM') is not None:
            self.max_qpm = m.get('MaxQPM')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunType') is not None:
            self.run_type = m.get('RunType')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        self.volumes = []
        if m.get('Volumes') is not None:
            for k1 in m.get('Volumes'):
                temp_model = main_models.DescribeAIDBClusterAttributeResponseBodyVolumes()
                self.volumes.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

class DescribeAIDBClusterAttributeResponseBodyVolumes(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
        size_gb: str = None,
        storage_category: str = None,
        storage_type: str = None,
    ):
        self.mount_path = mount_path
        self.name = name
        self.size_gb = size_gb
        self.storage_category = storage_category
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.name is not None:
            result['Name'] = self.name

        if self.size_gb is not None:
            result['SizeGB'] = self.size_gb

        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SizeGB') is not None:
            self.size_gb = m.get('SizeGB')

        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeAIDBClusterAttributeResponseBodyEndpointList(DaraModel):
    def __init__(
        self,
        net_info_items: List[main_models.DescribeAIDBClusterAttributeResponseBodyEndpointListNetInfoItems] = None,
    ):
        self.net_info_items = net_info_items

    def validate(self):
        if self.net_info_items:
            for v1 in self.net_info_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetInfoItems'] = []
        if self.net_info_items is not None:
            for k1 in self.net_info_items:
                result['NetInfoItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.net_info_items = []
        if m.get('NetInfoItems') is not None:
            for k1 in m.get('NetInfoItems'):
                temp_model = main_models.DescribeAIDBClusterAttributeResponseBodyEndpointListNetInfoItems()
                self.net_info_items.append(temp_model.from_map(k1))

        return self

class DescribeAIDBClusterAttributeResponseBodyEndpointListNetInfoItems(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        net_type: str = None,
        port: str = None,
    ):
        self.connection_string = connection_string
        self.net_type = net_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class DescribeAIDBClusterAttributeResponseBodyDBNodes(DaraModel):
    def __init__(
        self,
        child_volumes: List[main_models.DescribeAIDBClusterAttributeResponseBodyDBNodesChildVolumes] = None,
        cpu_cores: str = None,
        creation_time: str = None,
        dbnode_class: str = None,
        dbnode_description: str = None,
        dbnode_id: str = None,
        dbnode_status: str = None,
        gpu: str = None,
        link_ip: str = None,
        memory_size: str = None,
        public_ip: str = None,
        vnode_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.child_volumes = child_volumes
        self.cpu_cores = cpu_cores
        self.creation_time = creation_time
        self.dbnode_class = dbnode_class
        self.dbnode_description = dbnode_description
        self.dbnode_id = dbnode_id
        self.dbnode_status = dbnode_status
        self.gpu = gpu
        self.link_ip = link_ip
        self.memory_size = memory_size
        self.public_ip = public_ip
        self.vnode_id = vnode_id
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.child_volumes:
            for v1 in self.child_volumes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChildVolumes'] = []
        if self.child_volumes is not None:
            for k1 in self.child_volumes:
                result['ChildVolumes'].append(k1.to_map() if k1 else None)

        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_description is not None:
            result['DBNodeDescription'] = self.dbnode_description

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.dbnode_status is not None:
            result['DBNodeStatus'] = self.dbnode_status

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.link_ip is not None:
            result['LinkIP'] = self.link_ip

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.vnode_id is not None:
            result['VNodeId'] = self.vnode_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_volumes = []
        if m.get('ChildVolumes') is not None:
            for k1 in m.get('ChildVolumes'):
                temp_model = main_models.DescribeAIDBClusterAttributeResponseBodyDBNodesChildVolumes()
                self.child_volumes.append(temp_model.from_map(k1))

        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeDescription') is not None:
            self.dbnode_description = m.get('DBNodeDescription')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('DBNodeStatus') is not None:
            self.dbnode_status = m.get('DBNodeStatus')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('LinkIP') is not None:
            self.link_ip = m.get('LinkIP')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('VNodeId') is not None:
            self.vnode_id = m.get('VNodeId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAIDBClusterAttributeResponseBodyDBNodesChildVolumes(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
        size_gb: str = None,
        storage_category: str = None,
        storage_type: str = None,
    ):
        self.mount_path = mount_path
        self.name = name
        self.size_gb = size_gb
        self.storage_category = storage_category
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.name is not None:
            result['Name'] = self.name

        if self.size_gb is not None:
            result['SizeGB'] = self.size_gb

        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SizeGB') is not None:
            self.size_gb = m.get('SizeGB')

        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

