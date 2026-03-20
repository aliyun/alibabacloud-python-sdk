# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class ExecuteWorkflowResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ExecuteWorkflowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # If the request is successful, the ID of the workflow instance is returned.
        self.data = data
        # The error message that is returned only if the corresponding error occurs.
        self.message = message
        # The request ID.
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ExecuteWorkflowResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ExecuteWorkflowResponseBodyData(DaraModel):
    def __init__(
        self,
        wf_instance_id: int = None,
    ):
        # The workflow instance ID.
        self.wf_instance_id = wf_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.wf_instance_id is not None:
            result['WfInstanceId'] = self.wf_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WfInstanceId') is not None:
            self.wf_instance_id = m.get('WfInstanceId')

        return self

