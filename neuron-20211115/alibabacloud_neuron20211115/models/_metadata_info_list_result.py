# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MetadataInfoListResult(DaraModel):
    def __init__(
        self,
        metadata_infos: List[main_models.MetadataInfo] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.metadata_infos = metadata_infos
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.metadata_infos:
            for v1 in self.metadata_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['metadataInfos'] = []
        if self.metadata_infos is not None:
            for k1 in self.metadata_infos:
                result['metadataInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metadata_infos = []
        if m.get('metadataInfos') is not None:
            for k1 in m.get('metadataInfos'):
                temp_model = main_models.MetadataInfo()
                self.metadata_infos.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

