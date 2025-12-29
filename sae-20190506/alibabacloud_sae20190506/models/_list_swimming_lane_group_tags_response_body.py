# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListSwimmingLaneGroupTagsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListSwimmingLaneGroupTagsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code or the error code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: Redirection.
        # *   **4xx**: Request error.
        # *   **5xx**: Server error.
        self.code = code
        # Responses.
        self.data = data
        # Error code. Valid values:
        # 
        # *   If the request is successful, no **ErrorCode** fields are returned.
        # *   Request failed: **ErrorCode** fields are returned. For more information, see **Error codes**.
        self.error_code = error_code
        # Additional information. Valid values:
        # 
        # *   The error message returned because the request is normal and **success** is returned.
        # *   If the request is abnormal, the specific exception error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Whether the data is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: Failed.
        self.success = success
        # The ID of the trace. This parameter is used to query the exact call information.
        self.trace_id = trace_id

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSwimmingLaneGroupTagsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class ListSwimmingLaneGroupTagsResponseBodyData(DaraModel):
    def __init__(
        self,
        metadata: str = None,
        tag: str = None,
    ):
        # The metadata.
        self.metadata = metadata
        # The label of the lane.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

