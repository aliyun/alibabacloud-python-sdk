# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FileSmartCluster(DaraModel):
    def __init__(
        self,
        similarity: float = None,
        smart_cluster_id: str = None,
    ):
        # Similarity
        self.similarity = similarity
        # SmartClusterId
        self.smart_cluster_id = smart_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.similarity is not None:
            result['Similarity'] = self.similarity

        if self.smart_cluster_id is not None:
            result['SmartClusterId'] = self.smart_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        if m.get('SmartClusterId') is not None:
            self.smart_cluster_id = m.get('SmartClusterId')

        return self

