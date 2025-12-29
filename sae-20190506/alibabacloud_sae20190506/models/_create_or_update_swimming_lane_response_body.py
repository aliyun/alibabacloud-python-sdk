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
        # The HTTP status code or the error code. Valid values:
        # 
        # *   **2xx**: Success.
        # *   **3xx**: Redirection.
        # *   **4xx**: Request error.
        # *   **5xx**: Server error.
        self.code = code
        # The returned information.
        self.data = data
        # The status code. Value values:
        # 
        # *   If the request was successful, **ErrorCode** is not returned.
        # *   If the request failed, **ErrorCode** is returned. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # The message returned. Value description:
        # 
        # *   If the request was successful, a success message is returned.
        # *   An error code is returned if the request failed.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Whether the creation or update was successful. Valid values:
        # 
        # *   true: created.
        # *   false: failed to create.
        self.success = success
        # The ID of the trace. The ID is used to query the details of a request.
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
        # The ID of the lane.
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

