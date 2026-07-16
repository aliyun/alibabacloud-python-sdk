# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetCacheClusterResponseBody(DaraModel):
    def __init__(
        self,
        cache_clusters: main_models.CacheCluster = None,
        request_id: str = None,
    ):
        # The list of Cache clusters.
        self.cache_clusters = cache_clusters
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.cache_clusters:
            self.cache_clusters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_clusters is not None:
            result['cacheClusters'] = self.cache_clusters.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cacheClusters') is not None:
            temp_model = main_models.CacheCluster()
            self.cache_clusters = temp_model.from_map(m.get('cacheClusters'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

