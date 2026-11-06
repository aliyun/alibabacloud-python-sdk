# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterResourceUsageResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dbcluster_id: str = None,
        engine: str = None,
        engine_version: str = None,
        node_items: List[main_models.DescribeAIDBClusterResourceUsageResponseBodyNodeItems] = None,
        request_id: str = None,
    ):
        # The time when the cluster was created, in ISO 8601 UTC format.
        self.create_time = create_time
        # The ID of the AI database cluster.
        self.dbcluster_id = dbcluster_id
        # The database engine of the cluster.
        self.engine = engine
        # The DPI engine version of the cluster.
        self.engine_version = engine_version
        # The resource usage information of the nodes in the cluster.
        self.node_items = node_items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.node_items:
            for v1 in self.node_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        result['NodeItems'] = []
        if self.node_items is not None:
            for k1 in self.node_items:
                result['NodeItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        self.node_items = []
        if m.get('NodeItems') is not None:
            for k1 in m.get('NodeItems'):
                temp_model = main_models.DescribeAIDBClusterResourceUsageResponseBodyNodeItems()
                self.node_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAIDBClusterResourceUsageResponseBodyNodeItems(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        cpuused: str = None,
        dbnode_id: str = None,
        gpu: str = None,
        gpumodel: str = None,
        gpuused: str = None,
        memory: str = None,
        memory_used: str = None,
        pod_items: List[main_models.DescribeAIDBClusterResourceUsageResponseBodyNodeItemsPodItems] = None,
        vnode_id: str = None,
    ):
        # The total CPU capacity of the node.
        self.cpu = cpu
        # The used CPU capacity of the node.
        self.cpuused = cpuused
        # The ID of the database node.
        self.dbnode_id = dbnode_id
        # The total GPU capacity of the node.
        self.gpu = gpu
        # The GPU model of the node.
        self.gpumodel = gpumodel
        # The used GPU capacity of the node.
        self.gpuused = gpuused
        # The total memory capacity of the node.
        self.memory = memory
        # The used memory capacity of the node.
        self.memory_used = memory_used
        # The resource information of the pods on the node.
        self.pod_items = pod_items
        # The ID of the virtual node associated with the database node.
        self.vnode_id = vnode_id

    def validate(self):
        if self.pod_items:
            for v1 in self.pod_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.cpuused is not None:
            result['CPUUsed'] = self.cpuused

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gpumodel is not None:
            result['GPUModel'] = self.gpumodel

        if self.gpuused is not None:
            result['GPUUsed'] = self.gpuused

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used

        result['PodItems'] = []
        if self.pod_items is not None:
            for k1 in self.pod_items:
                result['PodItems'].append(k1.to_map() if k1 else None)

        if self.vnode_id is not None:
            result['VNodeId'] = self.vnode_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('CPUUsed') is not None:
            self.cpuused = m.get('CPUUsed')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUModel') is not None:
            self.gpumodel = m.get('GPUModel')

        if m.get('GPUUsed') is not None:
            self.gpuused = m.get('GPUUsed')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')

        self.pod_items = []
        if m.get('PodItems') is not None:
            for k1 in m.get('PodItems'):
                temp_model = main_models.DescribeAIDBClusterResourceUsageResponseBodyNodeItemsPodItems()
                self.pod_items.append(temp_model.from_map(k1))

        if m.get('VNodeId') is not None:
            self.vnode_id = m.get('VNodeId')

        return self

class DescribeAIDBClusterResourceUsageResponseBodyNodeItemsPodItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        name_space: str = None,
        pod_ip: str = None,
        resource_request: str = None,
        status: str = None,
    ):
        # The time when the pod was created, in ISO 8601 UTC format.
        self.create_time = create_time
        # The name of the pod.
        self.name = name
        # The namespace to which the pod belongs.
        self.name_space = name_space
        # The IP address of the pod.
        self.pod_ip = pod_ip
        # The requested resources of the pod.
        self.resource_request = resource_request
        # The status of the pod.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.name_space is not None:
            result['NameSpace'] = self.name_space

        if self.pod_ip is not None:
            result['PodIP'] = self.pod_ip

        if self.resource_request is not None:
            result['ResourceRequest'] = self.resource_request

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')

        if m.get('PodIP') is not None:
            self.pod_ip = m.get('PodIP')

        if m.get('ResourceRequest') is not None:
            self.resource_request = m.get('ResourceRequest')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

