# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeElasticPlanAttributeRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_plan_name: str = None,
    ):
        # The ID of the cluster.
        # > Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the elastic plan.
        # > Call the [DescribeElasticPlans](https://help.aliyun.com/document_detail/601334.html) operation to query the name of the elastic plan for the cluster.
        # 
        # This parameter is required.
        self.elastic_plan_name = elastic_plan_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')

        return self

