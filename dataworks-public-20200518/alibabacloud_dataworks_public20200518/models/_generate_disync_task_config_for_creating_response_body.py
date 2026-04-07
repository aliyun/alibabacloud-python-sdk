# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GenerateDISyncTaskConfigForCreatingResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GenerateDISyncTaskConfigForCreatingResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information returned for the ID of the asynchronous thread.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.GenerateDISyncTaskConfigForCreatingResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GenerateDISyncTaskConfigForCreatingResponseBodyData(DaraModel):
    def __init__(
        self,
        message: str = None,
        process_id: int = None,
        status: str = None,
    ):
        # The reason why the ID of the asynchronous thread fails to be generated. If the ID is successfully generated, no value is returned for this parameter.
        self.message = message
        # The ID of the asynchronous thread. You can call the [QueryDISyncTaskConfigProcessResult](https://help.aliyun.com/document_detail/383465.html) operation to obtain the asynchronously generated parameters based on the ID. The parameters are used to create a synchronization task in Data Integration.
        self.process_id = process_id
        # Indicates whether the ID of the asynchronous thread is generated. Valid values: Valid values:
        # 
        # *   success: indicates that the ID of the asynchronous thread is generated.
        # *   fail: indicates that the ID of the asynchronous thread fails to be generated. You can view the reason for the failure and troubleshoot the issue based on the reason.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

