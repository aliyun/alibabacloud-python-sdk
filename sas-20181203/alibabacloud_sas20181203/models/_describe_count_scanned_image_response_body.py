# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCountScannedImageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scanned_count: int = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of images that are scanned.
        self.scanned_count = scanned_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scanned_count is not None:
            result['ScannedCount'] = self.scanned_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScannedCount') is not None:
            self.scanned_count = m.get('ScannedCount')

        return self

