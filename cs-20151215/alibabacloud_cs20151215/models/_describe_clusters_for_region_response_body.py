# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClustersForRegionResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.DescribeClustersForRegionResponseBodyClusters] = None,
        page_info: main_models.DescribeClustersForRegionResponseBodyPageInfo = None,
    ):
        # A list of clusters.
        self.clusters = clusters
        # The pagination information.
        self.page_info = page_info

    def validate(self):
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['clusters'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('clusters') is not None:
            for k1 in m.get('clusters'):
                temp_model = main_models.DescribeClustersForRegionResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('page_info') is not None:
            temp_model = main_models.DescribeClustersForRegionResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        return self

class DescribeClustersForRegionResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The returned page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries that match the query.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

class DescribeClustersForRegionResponseBodyClusters(DaraModel):
    def __init__(
        self,
        cluster_domain: str = None,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        container_cidr: str = None,
        created: str = None,
        current_version: str = None,
        deletion_protection: bool = None,
        init_version: str = None,
        ip_stack: str = None,
        name: str = None,
        next_version: str = None,
        profile: str = None,
        proxy_mode: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        service_cidr: str = None,
        size: int = None,
        state: str = None,
        tags: List[main_models.Tag] = None,
        timezone: str = None,
        updated: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
    ):
        # The cluster domain.
        self.cluster_domain = cluster_domain
        # The cluster ID.
        self.cluster_id = cluster_id
        # The specification of the cluster. Valid values:
        # 
        # - `ack.standard`: Basic Edition
        # 
        # - `ack.pro.small`: Pro Edition
        # 
        # - `ack.pro.xlarge`: Pro XL
        # 
        # - `ack.pro.2xlarge`: Pro 2XL
        # 
        # - `ack.pro.4xlarge`: Pro 4XL. This specification is available only to allowlisted users.
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three specifications available for the <props="china">[ACK Pro provisioned control plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro provisioned control plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). These specifications ensure a high and deterministic level of API concurrency and Pod scheduling capabilities by pre-allocating and dedicating control plane resources. They are suitable for AI training and inference, large-scale clusters, and mission-critical workloads.
        # 
        # For information about the <props="china">[cluster management fee](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[cluster management fee](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee) for Pro Edition and ACK Pro provisioned control plane specifications, see the linked topic.
        self.cluster_spec = cluster_spec
        # The type of the cluster. Valid values:
        # 
        # - `Kubernetes`: an ACK dedicated cluster.
        # 
        # - `ManagedKubernetes`: an ACK managed cluster. This type includes ACK managed clusters (Pro and Basic editions), ACK Serverless clusters (Pro and Basic editions), ACK Edge clusters (Pro and Basic editions), and ACK Lingjun clusters (Pro edition).
        # 
        # - `ExternalKubernetes`: a registered cluster.
        self.cluster_type = cluster_type
        # The CIDR block for Pods in the cluster.
        self.container_cidr = container_cidr
        # The time the cluster was created.
        self.created = created
        # The current version of the cluster.
        self.current_version = current_version
        # Specifies whether deletion protection is enabled for the cluster. If enabled, you cannot delete the cluster from the console or by an API call. Valid values:
        # 
        # - `true`: Deletion protection is enabled.
        # 
        # - `false`: Deletion protection is disabled.
        self.deletion_protection = deletion_protection
        # The initial version of the cluster.
        self.init_version = init_version
        # The IP stack of the cluster.
        self.ip_stack = ip_stack
        # The cluster name.
        self.name = name
        # The available upgrade version.
        self.next_version = next_version
        # The subtype of the cluster. Valid values:
        # 
        # - `Default`: An ACK managed cluster (Pro and Basic editions).
        # 
        # - `Edge`: An ACK Edge cluster (Pro and Basic editions).
        # 
        # - `Serverless`: An ACK Serverless cluster (Pro and Basic editions).
        # 
        # - `LingJun`: An ACK Lingjun cluster (Pro edition).
        self.profile = profile
        # The kube-proxy proxy mode of the cluster.
        self.proxy_mode = proxy_mode
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        # The security group ID of the cluster.
        self.security_group_id = security_group_id
        # The CIDR block for the service network.
        # 
        # This parameter is required.
        self.service_cidr = service_cidr
        # The number of nodes in the cluster.
        self.size = size
        # The state of the cluster. Valid values:
        # 
        # - `initial`: The cluster is being created.
        # 
        # - `failed`: Cluster creation failed.
        # 
        # - `running`: The cluster is running.
        # 
        # - `updating`: The cluster is being updated.
        # 
        # - `upgrading`: The cluster is being upgraded.
        # 
        # - `removing`: Nodes are being removed from the cluster.
        # 
        # - `draining`: Node draining is in progress.
        # 
        # - `scaling`: The cluster is being scaled.
        # 
        # - `inactive`: The cluster is inactive.
        # 
        # - `unavailable`: The cluster is unavailable.
        # 
        # - `deleting`: The cluster is being deleted.
        # 
        # - `deleted`: The cluster is deleted.
        # 
        # - `delete_failed`: Cluster deletion failed.
        # 
        # - `waiting`: The cluster is waiting for a connection.
        # 
        # - `disconnected`: The cluster is disconnected.
        self.state = state
        # The tags attached to the cluster.
        self.tags = tags
        # The time zone of the cluster.
        self.timezone = timezone
        # The time the cluster was last updated.
        self.updated = updated
        # The VPC ID of the cluster.
        self.vpc_id = vpc_id
        # The IDs of the vSwitches for the control plane.
        self.vswitch_ids = vswitch_ids

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
        if self.cluster_domain is not None:
            result['cluster_domain'] = self.cluster_domain

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.container_cidr is not None:
            result['container_cidr'] = self.container_cidr

        if self.created is not None:
            result['created'] = self.created

        if self.current_version is not None:
            result['current_version'] = self.current_version

        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection

        if self.init_version is not None:
            result['init_version'] = self.init_version

        if self.ip_stack is not None:
            result['ip_stack'] = self.ip_stack

        if self.name is not None:
            result['name'] = self.name

        if self.next_version is not None:
            result['next_version'] = self.next_version

        if self.profile is not None:
            result['profile'] = self.profile

        if self.proxy_mode is not None:
            result['proxy_mode'] = self.proxy_mode

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id

        if self.service_cidr is not None:
            result['service_cidr'] = self.service_cidr

        if self.size is not None:
            result['size'] = self.size

        if self.state is not None:
            result['state'] = self.state

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.updated is not None:
            result['updated'] = self.updated

        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_domain') is not None:
            self.cluster_domain = m.get('cluster_domain')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('container_cidr') is not None:
            self.container_cidr = m.get('container_cidr')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')

        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')

        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')

        if m.get('ip_stack') is not None:
            self.ip_stack = m.get('ip_stack')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')

        if m.get('profile') is not None:
            self.profile = m.get('profile')

        if m.get('proxy_mode') is not None:
            self.proxy_mode = m.get('proxy_mode')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')

        if m.get('service_cidr') is not None:
            self.service_cidr = m.get('service_cidr')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('state') is not None:
            self.state = m.get('state')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')

        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')

        return self

