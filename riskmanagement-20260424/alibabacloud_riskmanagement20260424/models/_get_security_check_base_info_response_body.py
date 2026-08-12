# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetSecurityCheckBaseInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSecurityCheckBaseInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # >  200: Success. Other codes (500, 400, etc.): Error codes.
        self.code = code
        # The query result.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        # - **true**: Successful.
        # - **false**: Failed.
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
            temp_model = main_models.GetSecurityCheckBaseInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSecurityCheckBaseInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        task_completed: bool = None,
    ):
        # Indicates whether the security check is enabled.
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enabled = enabled
        # Indicates whether the security check is completed.
        # 
        # - **true**: Completed.
        # - **false**: Not completed.
        self.task_completed = task_completed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.task_completed is not None:
            result['TaskCompleted'] = self.task_completed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('TaskCompleted') is not None:
            self.task_completed = m.get('TaskCompleted')

        return self

