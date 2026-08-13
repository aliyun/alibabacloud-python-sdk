# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ConfigDataAgentMemoryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ConfigDataAgentMemoryResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned when the request fails.
        self.error_code = error_code
        # The error message returned when the request fails.
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ConfigDataAgentMemoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ConfigDataAgentMemoryResponseBodyData(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        recall_enabled: bool = None,
    ):
        # Specifies whether to enable memory generation. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        self.enabled = enabled
        # Indicates whether memory recall usage is enabled. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        self.recall_enabled = recall_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.recall_enabled is not None:
            result['RecallEnabled'] = self.recall_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('RecallEnabled') is not None:
            self.recall_enabled = m.get('RecallEnabled')

        return self

