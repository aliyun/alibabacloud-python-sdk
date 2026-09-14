# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateComputeResourceAuthUserMappingsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateComputeResourceAuthUserMappingsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data object.
        self.data = data
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.UpdateComputeResourceAuthUserMappingsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateComputeResourceAuthUserMappingsResponseBodyData(DaraModel):
    def __init__(
        self,
        change_record_id: int = None,
        status: str = None,
    ):
        # The change record ID.
        self.change_record_id = change_record_id
        # Indicates whether the operation succeeded. Valid values:
        # - success: The update succeeded.
        # - fail: The update failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_record_id is not None:
            result['ChangeRecordId'] = self.change_record_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeRecordId') is not None:
            self.change_record_id = m.get('ChangeRecordId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

