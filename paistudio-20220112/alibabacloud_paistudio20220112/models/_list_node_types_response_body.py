# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListNodeTypesResponseBody(DaraModel):
    def __init__(
        self,
        node_types: List[main_models.NodeType] = None,
        request_id: str = None,
        statistics: List[main_models.NodeTypeStatistic] = None,
    ):
        self.node_types = node_types
        self.request_id = request_id
        self.statistics = statistics

    def validate(self):
        if self.node_types:
            for v1 in self.node_types:
                 if v1:
                    v1.validate()
        if self.statistics:
            for v1 in self.statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeTypes'] = []
        if self.node_types is not None:
            for k1 in self.node_types:
                result['NodeTypes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['Statistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_types = []
        if m.get('NodeTypes') is not None:
            for k1 in m.get('NodeTypes'):
                temp_model = main_models.NodeType()
                self.node_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.NodeTypeStatistic()
                self.statistics.append(temp_model.from_map(k1))

        return self

