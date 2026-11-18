# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class BatchConfigRuntimeChannelResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.BatchConfigRuntimeChannelResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of batch configuration results. Each channel configuration item corresponds to one result.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The number of configuration results, which is the same as the number of configuration items in ChannelConfigs.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.BatchConfigRuntimeChannelResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class BatchConfigRuntimeChannelResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        runtime_id: str = None,
        success: bool = None,
    ):
        # The third-party channel code.
        self.code = code
        # The error code returned when the configuration fails. This parameter is returned only when Success is false.
        self.error_code = error_code
        # The error description returned when the configuration fails. This parameter is returned only when Success is false.
        self.message = message
        # The agent runtime ID.
        self.runtime_id = runtime_id
        # Indicates whether the channel configuration item is configured successfully. Valid values:
        # 
        # - true: The configuration is successful.
        # - false: The configuration fails. For the cause of the failure, see ErrorCode and Message.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

