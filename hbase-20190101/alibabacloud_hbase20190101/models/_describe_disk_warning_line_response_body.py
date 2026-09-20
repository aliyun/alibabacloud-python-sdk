# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiskWarningLineResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        warning_line: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The disk capacity alert threshold. For example, if the value is 75, an alert is triggered when disk usage exceeds 75%. If no value is returned, the user has not configured this parameter, and the system default value is 80%.
        self.warning_line = warning_line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.warning_line is not None:
            result['WarningLine'] = self.warning_line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WarningLine') is not None:
            self.warning_line = m.get('WarningLine')

        return self

