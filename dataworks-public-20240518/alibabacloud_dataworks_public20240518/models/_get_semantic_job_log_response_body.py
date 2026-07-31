# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetSemanticJobLogResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetSemanticJobLogResponseBodyData] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of log segments returned by the executor. The current POP contract does not expose sqlIndex or offset externally. Log segments are returned based on the default behavior of the operation.
        self.data = data
        # The request ID. Used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetSemanticJobLogResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSemanticJobLogResponseBodyData(DaraModel):
    def __init__(
        self,
        log_content: str = None,
        log_end: bool = None,
    ):
        # The raw log text returned in this response.
        self.log_content = log_content
        # Indicates whether the current log segment has been read to the end. A value of true indicates that no more content follows this segment.
        self.log_end = log_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_content is not None:
            result['LogContent'] = self.log_content

        if self.log_end is not None:
            result['LogEnd'] = self.log_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')

        if m.get('LogEnd') is not None:
            self.log_end = m.get('LogEnd')

        return self

