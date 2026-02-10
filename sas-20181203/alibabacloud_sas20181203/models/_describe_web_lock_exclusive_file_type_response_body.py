# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeWebLockExclusiveFileTypeResponseBody(DaraModel):
    def __init__(
        self,
        exclusive_file_type: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the types of the files that are excluded from web tamper proofing.
        self.exclusive_file_type = exclusive_file_type
        # The request ID.
        self.request_id = request_id
        # The total number of types of the files that are excluded from web tamper proofing.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclusive_file_type is not None:
            result['ExclusiveFileType'] = self.exclusive_file_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExclusiveFileType') is not None:
            self.exclusive_file_type = m.get('ExclusiveFileType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

