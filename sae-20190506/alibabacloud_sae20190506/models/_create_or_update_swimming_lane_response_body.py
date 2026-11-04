# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateOrUpdateSwimmingLaneResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The API status code or POP error code. Valid values:
        # 
        # - **2xx**: Success.
        # - **3xx**: Redirection.
        # - **4xx**: Client error.
        # - **5xx**: Server error.
        self.code = code
        # The returned information.
        self.data = data
        # The error code. Description:
        # 
        # - If the request is successful, the **ErrorCode** parameter is not returned.
        # - If the request fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The additional information. Description:
        # 
        # - If the request is normal, success is returned.
        # - If the request is abnormal, a specific error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Specifies whether the traffic lane is created or updated successfully. Valid values:
        # 
        # - true: The traffic lane is created or updated successfully.
        # - false: The traffic lane fails to be created or updated.
        self.success = success
        # The trace ID used to query call information accurately.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateOrUpdateSwimmingLaneResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class CreateOrUpdateSwimmingLaneResponseBodyData(DaraModel):
    def __init__(
        self,
        lane_id: int = None,
    ):
        # The ID of the traffic lane.
        self.lane_id = lane_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lane_id is not None:
            result['LaneId'] = self.lane_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')

        return self

