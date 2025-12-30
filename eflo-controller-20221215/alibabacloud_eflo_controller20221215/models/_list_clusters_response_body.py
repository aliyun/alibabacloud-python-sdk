# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListClustersResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.ListClustersResponseBodyClusters] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The clusters.
        self.clusters = clusters
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['Clusters'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.ListClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClustersResponseBodyClusters(DaraModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components: Any = None,
        computing_ip_version: str = None,
        create_time: str = None,
        hpn_zone: str = None,
        node_count: int = None,
        node_group_count: int = None,
        operating_state: str = None,
        resource_group_id: str = None,
        tags: List[main_models.ListClustersResponseBodyClustersTags] = None,
        task_id: str = None,
        update_time: str = None,
        vpc_id: str = None,
    ):
        # The cluster description.
        self.cluster_description = cluster_description
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The cluster type.
        # 
        # Valid values:
        # 
        # *   AckEdgePro
        # *   ExclusiveBareCluster
        # *   Lite
        self.cluster_type = cluster_type
        # The component information.
        self.components = components
        # The IP type of the computing network.
        self.computing_ip_version = computing_ip_version
        # The creation time.
        self.create_time = create_time
        # The cluster number.
        self.hpn_zone = hpn_zone
        # The number of nodes.
        self.node_count = node_count
        # The number of node groups.
        self.node_group_count = node_group_count
        # The cluster status.
        # 
        # Valid values:
        # 
        # *   running
        # *   expanding
        # *   shrinking
        # *   initializing
        self.operating_state = operating_state
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The job ID.
        self.task_id = task_id
        # The update time.
        self.update_time = update_time
        # The virtual private cloud (VPC) ID.
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
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.components is not None:
            result['Components'] = self.components

        if self.computing_ip_version is not None:
            result['ComputingIpVersion'] = self.computing_ip_version

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_group_count is not None:
            result['NodeGroupCount'] = self.node_group_count

        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Components') is not None:
            self.components = m.get('Components')

        if m.get('ComputingIpVersion') is not None:
            self.computing_ip_version = m.get('ComputingIpVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeGroupCount') is not None:
            self.node_group_count = m.get('NodeGroupCount')

        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListClustersResponseBodyClustersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListClustersResponseBodyClustersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

