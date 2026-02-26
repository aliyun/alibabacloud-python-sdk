# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class QueryFigureClustersResponseBody(DaraModel):
    def __init__(
        self,
        figure_clusters: List[main_models.FigureCluster] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The face groups.
        self.figure_clusters = figure_clusters
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of face groups that matches the current query conditions.
        self.total_count = total_count

    def validate(self):
        if self.figure_clusters:
            for v1 in self.figure_clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FigureClusters'] = []
        if self.figure_clusters is not None:
            for k1 in self.figure_clusters:
                result['FigureClusters'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figure_clusters = []
        if m.get('FigureClusters') is not None:
            for k1 in m.get('FigureClusters'):
                temp_model = main_models.FigureCluster()
                self.figure_clusters.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

