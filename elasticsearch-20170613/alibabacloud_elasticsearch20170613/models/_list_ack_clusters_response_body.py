# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListAckClustersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListAckClustersResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListAckClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListAckClustersResponseBodyResult(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        name: str = None,
        vpc_id: str = None,
    ):
        # The ID of cluster.
        self.cluster_id = cluster_id
        # The type of the cluster. The value is fixed as ManagedKubernetes.
        self.cluster_type = cluster_type
        # The name of the cluster.
        self.name = name
        # The ID of the VPC to which the cluster belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type

        if self.name is not None:
            result['name'] = self.name

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

