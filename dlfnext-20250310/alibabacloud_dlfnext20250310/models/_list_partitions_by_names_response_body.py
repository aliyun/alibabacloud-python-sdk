# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class ListPartitionsByNamesResponseBody(DaraModel):
    def __init__(
        self,
        partitions: List[main_models.Partition] = None,
    ):
        # 分区。
        self.partitions = partitions

    def validate(self):
        if self.partitions:
            for v1 in self.partitions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['partitions'] = []
        if self.partitions is not None:
            for k1 in self.partitions:
                result['partitions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.partitions = []
        if m.get('partitions') is not None:
            for k1 in m.get('partitions'):
                temp_model = main_models.Partition()
                self.partitions.append(temp_model.from_map(k1))

        return self

