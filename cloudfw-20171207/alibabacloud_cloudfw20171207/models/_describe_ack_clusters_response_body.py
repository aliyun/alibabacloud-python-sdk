# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAckClustersResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.DescribeAckClustersResponseBodyClusters] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of ACK clusters.
        self.clusters = clusters
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

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

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.DescribeAckClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAckClustersResponseBodyClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        member_uid: str = None,
        network: str = None,
        profile: str = None,
        region_id: str = None,
        state: str = None,
        vpc_id: str = None,
    ):
        # The ID of the ACK cluster.
        self.cluster_id = cluster_id
        # The name of the ACK cluster.
        self.cluster_name = cluster_name
        # The specification of the ACK cluster.
        self.cluster_spec = cluster_spec
        # The type of the ACK cluster. For more information about the valid values, see [DescribeClustersV1](~~DescribeClustersV1~~).
        # 
        # - [DescribeClustersV1](~~DescribeClustersV1~~): Returns a list of ACK clusters in your account that meet specific criteria, such as the cluster type and specifications.
        self.cluster_type = cluster_type
        # The Alibaba Cloud UID of the account to which the ACK cluster resources belong.
        self.member_uid = member_uid
        # The network plugin of the ACK cluster. For more information about the valid values, see [DescribeClustersV1](~~DescribeClustersV1~~).
        # 
        # - [DescribeClustersV1](~~DescribeClustersV1~~): Lists the ACK clusters in your account that meet specified conditions, such as cluster type and specifications.
        self.network = network
        # The subtype of the cluster. This parameter is available only when `ClusterType` is set to `ManagedKubernetes`. For more information about the valid values, see [DescribeClustersV1](~~DescribeClustersV1~~).
        # 
        # - [DescribeClustersV1](~~DescribeClustersV1~~): Lists ACK clusters in your account that meet specified conditions, such as cluster type and specifications.
        self.profile = profile
        # The region ID of the ACK cluster.
        self.region_id = region_id
        # The running status of the ACK cluster. For more information about the valid values, see [DescribeClustersV1](~~DescribeClustersV1~~).
        # 
        # - [DescribeClustersV1](~~DescribeClustersV1~~): Retrieves a list of ACK clusters in your account that meet specified conditions, such as cluster type and specifications.
        self.state = state
        # The ID of the VPC where the ACK cluster is deployed.
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

        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.network is not None:
            result['Network'] = self.network

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.state is not None:
            result['State'] = self.state

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

