# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class QueryLocationDateClustersResponseBody(DaraModel):
    def __init__(
        self,
        location_date_clusters: List[main_models.LocationDateCluster] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of spatiotemporal clusters.
        self.location_date_clusters = location_date_clusters
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.location_date_clusters:
            for v1 in self.location_date_clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LocationDateClusters'] = []
        if self.location_date_clusters is not None:
            for k1 in self.location_date_clusters:
                result['LocationDateClusters'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.location_date_clusters = []
        if m.get('LocationDateClusters') is not None:
            for k1 in m.get('LocationDateClusters'):
                temp_model = main_models.LocationDateCluster()
                self.location_date_clusters.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

