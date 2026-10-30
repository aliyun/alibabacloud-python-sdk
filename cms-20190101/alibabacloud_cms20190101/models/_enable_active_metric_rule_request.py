# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableActiveMetricRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        product: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value of this parameter on the client side. Make sure that the value is unique across different requests. The value can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # Specifies whether to check the availability of the webhook.
        self.dry_run = dry_run
        # The name of the Alibaba Cloud service that supports one-click alert rules. Valid values:
        # 
        # * ecs: Elastic Compute Service (ECS).
        # * rds: ApsaraDB RDS.
        # * slb: Server Load Balancer (SLB).
        # * redis_standard: Standard architecture of open-source Redis.
        # * redis_sharding: Cluster architecture of open-source Redis.
        # * redis_splitrw: Read/write splitting architecture of open-source Redis.
        # * mongodb: ApsaraDB for MongoDB (replica set).
        # * mongodb_sharding: ApsaraDB for MongoDB (sharded cluster).
        # * hbase: ApsaraDB for HBase.
        # * elasticsearch: Elasticsearch.
        # * opensearch: OpenSearch.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

