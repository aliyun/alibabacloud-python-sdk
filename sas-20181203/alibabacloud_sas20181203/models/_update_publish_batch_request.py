# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePublishBatchRequest(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        batch_name: str = None,
        interval: int = None,
        operation_base: int = None,
    ):
        # The ID of the release batch.
        self.batch_id = batch_id
        # The name of the release batch.
        self.batch_name = batch_name
        # The interval between two release batches.
        self.interval = interval
        # The asset selection dimension. Valid values:
        # 
        # *   **0**: instance
        # *   **1**: machine group
        # *   **2**: VPC-based instance ID
        self.operation_base = operation_base

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.batch_name is not None:
            result['BatchName'] = self.batch_name

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.operation_base is not None:
            result['OperationBase'] = self.operation_base

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('BatchName') is not None:
            self.batch_name = m.get('BatchName')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OperationBase') is not None:
            self.operation_base = m.get('OperationBase')

        return self

