# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class SearchSimilarImageClustersResponseBody(DaraModel):
    def __init__(
        self,
        next_marker: str = None,
        similar_image_clusters: List[main_models.SearchSimilarImageClustersResponseBodySimilarImageClusters] = None,
    ):
        self.next_marker = next_marker
        self.similar_image_clusters = similar_image_clusters

    def validate(self):
        if self.similar_image_clusters:
            for v1 in self.similar_image_clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker

        result['similar_image_clusters'] = []
        if self.similar_image_clusters is not None:
            for k1 in self.similar_image_clusters:
                result['similar_image_clusters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')

        self.similar_image_clusters = []
        if m.get('similar_image_clusters') is not None:
            for k1 in m.get('similar_image_clusters'):
                temp_model = main_models.SearchSimilarImageClustersResponseBodySimilarImageClusters()
                self.similar_image_clusters.append(temp_model.from_map(k1))

        return self

class SearchSimilarImageClustersResponseBodySimilarImageClusters(DaraModel):
    def __init__(
        self,
        files: List[main_models.File] = None,
    ):
        self.files = files

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['files'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('files') is not None:
            for k1 in m.get('files'):
                temp_model = main_models.File()
                self.files.append(temp_model.from_map(k1))

        return self

