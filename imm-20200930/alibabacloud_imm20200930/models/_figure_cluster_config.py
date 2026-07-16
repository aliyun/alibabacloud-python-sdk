# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FigureClusterConfig(DaraModel):
    def __init__(
        self,
        auto_clustering: bool = None,
        auto_generate: bool = None,
        enabled_features: List[str] = None,
        min_entity_count: int = None,
    ):
        # Whether to automatically group similar figures into clusters.
        self.auto_clustering = auto_clustering
        # Whether to automatically generate metadata for each cluster, such as a representative cover image.
        self.auto_generate = auto_generate
        # An array of strings specifying the clustering strategies to use.
        self.enabled_features = enabled_features
        # The minimum number of figures required to form a cluster.
        self.min_entity_count = min_entity_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_clustering is not None:
            result['AutoClustering'] = self.auto_clustering

        if self.auto_generate is not None:
            result['AutoGenerate'] = self.auto_generate

        if self.enabled_features is not None:
            result['EnabledFeatures'] = self.enabled_features

        if self.min_entity_count is not None:
            result['MinEntityCount'] = self.min_entity_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoClustering') is not None:
            self.auto_clustering = m.get('AutoClustering')

        if m.get('AutoGenerate') is not None:
            self.auto_generate = m.get('AutoGenerate')

        if m.get('EnabledFeatures') is not None:
            self.enabled_features = m.get('EnabledFeatures')

        if m.get('MinEntityCount') is not None:
            self.min_entity_count = m.get('MinEntityCount')

        return self

