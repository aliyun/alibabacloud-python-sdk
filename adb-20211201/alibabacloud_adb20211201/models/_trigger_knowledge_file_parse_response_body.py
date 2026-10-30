# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class TriggerKnowledgeFileParseResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TriggerKnowledgeFileParseResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TriggerKnowledgeFileParseResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TriggerKnowledgeFileParseResponseBodyData(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        message: str = None,
        previous_status: str = None,
        process_status: str = None,
        success: bool = None,
    ):
        # The ID of the file submitted for reparsing, which is a decimal string. This parameter is returned only when the request is successful.
        self.file_id = file_id
        # The description of the operation result. If the operation fails, this parameter indicates the cause or the security error code.
        self.message = message
        # The status before submission. Valid values: PENDING, COMPLETED, FAILED, SKIPPED, and DUPLICATED. This parameter is returned only when the request is successful.
        self.previous_status = previous_status
        # The status after submission. The value is fixed to PENDING. This parameter is returned only when the request is successful.
        self.process_status = process_status
        # Indicates whether the operation is successful. If the operation fails, the Data parameter contains only the Success and Message parameters.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.message is not None:
            result['Message'] = self.message

        if self.previous_status is not None:
            result['PreviousStatus'] = self.previous_status

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PreviousStatus') is not None:
            self.previous_status = m.get('PreviousStatus')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

