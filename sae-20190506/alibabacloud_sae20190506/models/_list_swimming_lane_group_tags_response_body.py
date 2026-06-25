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
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: A client error occurred.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The data returned.
        self.data = data
        # The error code.
        # 
        # - This parameter is not returned if the request succeeds.
        # 
        # - This parameter is returned if the request fails. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The response message.
        # 
        # - If the request is successful, **success** is returned.
        # 
        # - If the request fails, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.success = success
        # The trace ID that is used to query the details of a request.
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
        # The swimming lane tag.
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

