# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ClusterSpec(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        data_sources: List[main_models.DataSource] = None,
        image: str = None,
    ):
        self.cluster_type = cluster_type
        self.data_sources = data_sources
        self.image = image

    def validate(self):
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.image is not None:
            result['Image'] = self.image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.DataSource()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        return self

