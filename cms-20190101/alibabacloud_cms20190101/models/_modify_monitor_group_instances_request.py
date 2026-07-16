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
        # The list of instances. You can specify up to 2,000 instances.
        # 
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
        # The cloud service to which the resource instance belongs. The following cloud services are supported:
        # 
        # - ECS (including Alibaba Cloud and third-party hosts)
        # 
        # - ApsaraDB RDS
        # 
        # - AnalyticDB
        # 
        # - SLB
        # 
        # - VPC (Elastic IP)
        # 
        # - API Gateway
        # 
        # - Alibaba Cloud CDN
        # 
        # - Container Service for Swarm
        # 
        # - DCDN
        # 
        # - Anti-DDoS
        # 
        # - EIP
        # 
        # - Elasticsearch
        # 
        # - E-MapReduce
        # 
        # - Auto Scaling
        # 
        # - ApsaraDB for HBase
        # 
        # - IoT Edge
        # 
        # - Kubernetes pod
        # 
        # - ApsaraDB for Redis (sharded cluster)
        # 
        # - ApsaraDB for Redis (read/write splitting)
        # 
        # - ApsaraDB for Redis (Standard Edition)
        # 
        # - ApsaraDB for Memcache
        # 
        # - MNS
        # 
        # - ApsaraDB for MongoDB (replica set)
        # 
        # - ApsaraDB for MongoDB (sharded cluster)
        # 
        # - ApsaraDB for MongoDB (sharded cluster)
        # 
        # - MNS topic
        # 
        # - OCS (ApsaraDB for Memcache of earlier versions)
        # 
        # - OpenSearch
        # 
        # - OSS
        # 
        # - PolarDB
        # 
        # - HybridDB for MySQL
        # 
        # - Internet Shared Bandwidth
        # 
        # - SLS
        # 
        # - VPN Gateway
        # 
        # This parameter is required.
        self.category = category
        # The ID of the resource instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The region ID.
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

