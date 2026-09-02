# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class SubmitBatchChangeTableOwnerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SubmitBatchChangeTableOwnerResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SubmitBatchChangeTableOwnerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SubmitBatchChangeTableOwnerResponseBodyData(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        status: str = None,
        total_count: int = None,
    ):
        self.batch_id = batch_id
        self.status = status
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

