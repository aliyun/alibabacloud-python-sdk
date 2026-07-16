# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeWebLockInclusiveFileTypeResponseBody(DaraModel):
    def __init__(
        self,
        inclusive_file_type: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of file types supported by tamper-proofing protection.
        self.inclusive_file_type = inclusive_file_type
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The total number of file types supported by tamper-proofing protection.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inclusive_file_type is not None:
            result['InclusiveFileType'] = self.inclusive_file_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InclusiveFileType') is not None:
            self.inclusive_file_type = m.get('InclusiveFileType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

