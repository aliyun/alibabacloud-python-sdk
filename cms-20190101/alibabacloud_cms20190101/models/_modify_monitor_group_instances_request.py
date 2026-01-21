# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class ModifyMonitorGroupInstancesRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        instances: List[main_models.ModifyMonitorGroupInstancesRequestInstances] = None,
        region_id: str = None,
    ):
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # This parameter is required.
        self.instances = instances
        self.region_id = region_id

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
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ModifyMonitorGroupInstancesRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyMonitorGroupInstancesRequestInstances(DaraModel):
    def __init__(
        self,
        category: str = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The abbreviation of the name of the service to which the instances to be added to the application group belong. Valid values:
        # 
        # *   ECS: Elastic Compute Service (ECS) instances provided by Alibaba Cloud and hosts not provided by Alibaba Cloud
        # 
        # *   RDS: ApsaraDB for RDS
        # 
        # *   ADS: AnalyticDB
        # 
        # *   SLB: Server Load Balancer (SLB)
        # 
        # *   VPC: Virtual Private Cloud (VPC)
        # 
        # *   APIGATEWAY: API Gateway
        # 
        # *   CDN: Alibaba Cloud Content Delivery Network (CDN)
        # 
        # *   CS: Container Service for Swarm
        # 
        # *   DCDN: Dynamic Route for CDN
        # 
        # *   DDoS: Anti-DDoS Pro
        # 
        # *   EIP: Elastic IP Address (EIP)
        # 
        # *   ELASTICSEARCH: Elasticsearch
        # 
        # *   EMR: E-MapReduce
        # 
        # *   ESS: Auto Scaling
        # 
        # *   HBASE: ApsaraDB for Hbase
        # 
        # *   IOT_EDGE: IoT Edge
        # 
        # *   K8S_POD: pods in Container Service for Kubernetes
        # 
        # *   KVSTORE_SHARDING: ApsaraDB for Redis of the cluster architecture
        # 
        # *   KVSTORE_SPLITRW: ApsaraDB for Redis of the read/write splitting architecture
        # 
        # *   KVSTORE_STANDARD: ApsaraDB for Redis of the standard architecture
        # 
        # *   MEMCACHE: ApsaraDB for Memcache
        # 
        # *   MNS: Message Service (MNS)
        # 
        # *   MONGODB: ApsaraDB for MongoDB of the replica set architecture
        # 
        # *   MONGODB_CLUSTER: ApsaraDB for MongoDB of the cluster architecture
        # 
        # *   MONGODB_SHARDING: ApsaraDB for MongoDB of the sharded cluster architecture
        # 
        # *   MQ_TOPIC: MNS topics
        # 
        # *   OCS: ApsaraDB for Memcache of earlier versions
        # 
        # *   OPENSEARCH: Open Search
        # 
        # *   OSS: Object Storage Service (OSS)
        # 
        # *   POLARDB: PolarDB
        # 
        # *   PETADATA: HybridDB for MySQL
        # 
        # *   SCDN: Secure Content Delivery Network (SCDN)
        # 
        # *   SHAREBANDWIDTHPACKAGES: EIP Bandwidth Plan
        # 
        # *   SLS: Log Service
        # 
        # *   VPN: VPN Gateway
        # 
        #     Valid values of N: 1 to 2000.
        # 
        # This parameter is required.
        self.category = category
        # The ID of the instance. Valid values of N: 1 to 2000.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the instance. Valid values of N: 1 to 2000.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The ID of the region where the instance resides. Valid values of N: 1 to 2000.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

