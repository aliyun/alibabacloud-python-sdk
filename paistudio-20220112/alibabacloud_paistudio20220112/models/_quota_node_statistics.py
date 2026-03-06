# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class QuotaNodeStatistics(DaraModel):
    def __init__(
        self,
        actual_min_hyper_node_num: int = None,
        actual_min_node_num: int = None,
        allocated_hyper_node_details: List[main_models.AllocatedHyperNodeDetail] = None,
        allocated_hyper_node_num: int = None,
        allocated_node_num: int = None,
        empty_node_num: int = None,
    ):
        self.actual_min_hyper_node_num = actual_min_hyper_node_num
        self.actual_min_node_num = actual_min_node_num
        self.allocated_hyper_node_details = allocated_hyper_node_details
        self.allocated_hyper_node_num = allocated_hyper_node_num
        self.allocated_node_num = allocated_node_num
        self.empty_node_num = empty_node_num

    def validate(self):
        if self.allocated_hyper_node_details:
            for v1 in self.allocated_hyper_node_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_min_hyper_node_num is not None:
            result['ActualMinHyperNodeNum'] = self.actual_min_hyper_node_num

        if self.actual_min_node_num is not None:
            result['ActualMinNodeNum'] = self.actual_min_node_num

        result['AllocatedHyperNodeDetails'] = []
        if self.allocated_hyper_node_details is not None:
            for k1 in self.allocated_hyper_node_details:
                result['AllocatedHyperNodeDetails'].append(k1.to_map() if k1 else None)

        if self.allocated_hyper_node_num is not None:
            result['AllocatedHyperNodeNum'] = self.allocated_hyper_node_num

        if self.allocated_node_num is not None:
            result['AllocatedNodeNum'] = self.allocated_node_num

        if self.empty_node_num is not None:
            result['EmptyNodeNum'] = self.empty_node_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualMinHyperNodeNum') is not None:
            self.actual_min_hyper_node_num = m.get('ActualMinHyperNodeNum')

        if m.get('ActualMinNodeNum') is not None:
            self.actual_min_node_num = m.get('ActualMinNodeNum')

        self.allocated_hyper_node_details = []
        if m.get('AllocatedHyperNodeDetails') is not None:
            for k1 in m.get('AllocatedHyperNodeDetails'):
                temp_model = main_models.AllocatedHyperNodeDetail()
                self.allocated_hyper_node_details.append(temp_model.from_map(k1))

        if m.get('AllocatedHyperNodeNum') is not None:
            self.allocated_hyper_node_num = m.get('AllocatedHyperNodeNum')

        if m.get('AllocatedNodeNum') is not None:
            self.allocated_node_num = m.get('AllocatedNodeNum')

        if m.get('EmptyNodeNum') is not None:
            self.empty_node_num = m.get('EmptyNodeNum')

        return self

