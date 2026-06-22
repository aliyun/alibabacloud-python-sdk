# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenBackupAutoConfigRequest(DaraModel):
    def __init__(
        self,
        max_batch_size: int = None,
    ):
        # The number of servers included in a single batch when the anti-ransomware managed service automatically generates policies.
        # 
        # > The maximum value is 50. If you specify a value greater than 50, the value is set to 50.
        self.max_batch_size = max_batch_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_batch_size is not None:
            result['MaxBatchSize'] = self.max_batch_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxBatchSize') is not None:
            self.max_batch_size = m.get('MaxBatchSize')

        return self

