# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCountNotScannedImageResponseBody(DaraModel):
    def __init__(
        self,
        not_scanned_cnt: int = None,
        request_id: str = None,
    ):
        # The number of images that are not scanned.
        self.not_scanned_cnt = not_scanned_cnt
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_scanned_cnt is not None:
            result['NotScannedCnt'] = self.not_scanned_cnt

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotScannedCnt') is not None:
            self.not_scanned_cnt = m.get('NotScannedCnt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

