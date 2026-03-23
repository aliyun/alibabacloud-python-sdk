# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImportTaskValidationResponseBody(DaraModel):
    def __init__(
        self,
        detail: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # Job details.
        self.detail = detail
        # ID of the request
        self.request_id = request_id
        # Job status. The parameter is invalid.
        self.status = status
        # Indicates whether the request succeeded. The values have the following meanings:
        # 
        # - **true**: Succeeded
        # - **false**: Failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

