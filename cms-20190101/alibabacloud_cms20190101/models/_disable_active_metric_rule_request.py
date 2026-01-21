# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableActiveMetricRuleRequest(DaraModel):
    def __init__(
        self,
        product: str = None,
        region_id: str = None,
    ):
        # The cloud service for which you want to disable proactive alerting. Valid values:
        # 
        # *   ECS: Elastic Compute Service (ECS)
        # *   rds: ApsaraDB RDS
        # *   slb: Server Load Balancer (SLB)
        # *   redis_standard: Redis Open-Source Edition (standard architecture)
        # *   redis_sharding: Redis Open-Source Edition (cluster architecture)
        # *   redis_splitrw: Redis Open-Source Edition (read/write splitting architecture)
        # *   mongodb: ApsaraDB for MongoDB of the replica set architecture
        # *   mongodb_sharding: ApsaraDB for MongoDB of the sharded cluster architecture
        # *   hbase: ApsaraDB for HBase
        # *   elasticsearch: Elasticsearch
        # *   opensearch: OpenSearch
        # 
        # This parameter is required.
        self.product = product
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

