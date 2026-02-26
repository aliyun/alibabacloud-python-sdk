# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class SearchImageFigureClusterResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.SearchImageFigureClusterResponseBodyClusters] = None,
        request_id: str = None,
    ):
        # The face clusters.
        self.clusters = clusters
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.SearchImageFigureClusterResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SearchImageFigureClusterResponseBodyClusters(DaraModel):
    def __init__(
        self,
        boundary: main_models.Boundary = None,
        cluster_id: str = None,
        similarity: float = None,
    ):
        # The bounding box of the face.
        self.boundary = boundary
        # The ID of the face cluster that contains faces similar to the face within the bounding box.
        self.cluster_id = cluster_id
        # The similarity between the face within the bounding box and the face cluster. Valid value: 0 to 1.
        self.similarity = similarity

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = main_models.Boundary()
            self.boundary = temp_model.from_map(m.get('Boundary'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        return self

