# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class InsertClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster: main_models.InsertClusterResponseBodyCluster = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the cluster that was created.
        self.cluster = cluster
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = main_models.InsertClusterResponseBodyCluster()
            self.cluster = temp_model.from_map(m.get('Cluster'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InsertClusterResponseBodyCluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: int = None,
        iaas_provider: str = None,
        network_mode: int = None,
        oversold_factor: int = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The type of the cluster. Valid values:
        # 
        # *   2: ECS cluster
        # *   3: self-managed Kubernetes cluster in EDAS
        # *   5: Kubernetes cluster
        self.cluster_type = cluster_type
        # The provider of the IaaS resources that are used in the cluster.
        self.iaas_provider = iaas_provider
        # The network type of the cluster. Valid values:
        # 
        # *   1: classic network
        # *   2\\. VPC
        self.network_mode = network_mode
        # **This parameter is deprecated.** The CPU overcommit ratio supported by the Docker cluster. Valid values:
        # 
        # *   2: 1:2, which means that resources are overcommitted by 1:2.
        # *   4: 1:4, which means that resources are overcommitted by 1:4.
        # *   8: 1:8, which means that resources are overcommitted by 1:8.
        self.oversold_factor = oversold_factor
        # The ID of the region in which the cluster resides.
        self.region_id = region_id
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.iaas_provider is not None:
            result['IaasProvider'] = self.iaas_provider

        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode

        if self.oversold_factor is not None:
            result['OversoldFactor'] = self.oversold_factor

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('IaasProvider') is not None:
            self.iaas_provider = m.get('IaasProvider')

        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')

        if m.get('OversoldFactor') is not None:
            self.oversold_factor = m.get('OversoldFactor')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

