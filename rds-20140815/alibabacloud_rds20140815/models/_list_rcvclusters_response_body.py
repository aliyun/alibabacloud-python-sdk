# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ListRCVClustersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vclusters: List[main_models.ListRCVClustersResponseBodyVClusters] = None,
    ):
        self.request_id = request_id
        self.vclusters = vclusters

    def validate(self):
        if self.vclusters:
            for v1 in self.vclusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VClusters'] = []
        if self.vclusters is not None:
            for k1 in self.vclusters:
                result['VClusters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vclusters = []
        if m.get('VClusters') is not None:
            for k1 in m.get('VClusters'):
                temp_model = main_models.ListRCVClustersResponseBodyVClusters()
                self.vclusters.append(temp_model.from_map(k1))

        return self

class ListRCVClustersResponseBodyVClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_count: int = None,
        region_id: str = None,
        support_disk_performance_level: List[str] = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.instance_count = instance_count
        self.region_id = region_id
        self.support_disk_performance_level = support_disk_performance_level
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

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.support_disk_performance_level is not None:
            result['SupportDiskPerformanceLevel'] = self.support_disk_performance_level

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupportDiskPerformanceLevel') is not None:
            self.support_disk_performance_level = m.get('SupportDiskPerformanceLevel')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

