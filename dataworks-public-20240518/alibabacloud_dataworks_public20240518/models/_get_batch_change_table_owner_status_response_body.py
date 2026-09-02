# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetBatchChangeTableOwnerStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetBatchChangeTableOwnerStatusResponseBodyData = None,
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
            temp_model = main_models.GetBatchChangeTableOwnerStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBatchChangeTableOwnerStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        details: List[main_models.GetBatchChangeTableOwnerStatusResponseBodyDataDetails] = None,
        failed_count: int = None,
        ongoing_count: int = None,
        status: str = None,
        success_count: int = None,
        total_count: int = None,
    ):
        self.batch_id = batch_id
        self.details = details
        self.failed_count = failed_count
        self.ongoing_count = ongoing_count
        self.status = status
        self.success_count = success_count
        self.total_count = total_count

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.ongoing_count is not None:
            result['OngoingCount'] = self.ongoing_count

        if self.status is not None:
            result['Status'] = self.status

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.GetBatchChangeTableOwnerStatusResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('OngoingCount') is not None:
            self.ongoing_count = m.get('OngoingCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetBatchChangeTableOwnerStatusResponseBodyDataDetails(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        status: str = None,
        table_meta_entity_id: str = None,
    ):
        self.error_message = error_message
        self.status = status
        self.table_meta_entity_id = table_meta_entity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.status is not None:
            result['Status'] = self.status

        if self.table_meta_entity_id is not None:
            result['TableMetaEntityId'] = self.table_meta_entity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableMetaEntityId') is not None:
            self.table_meta_entity_id = m.get('TableMetaEntityId')

        return self

