# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAlertConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scale_statuses: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The status of the scaling activities that trigger text message, internal message, or email-based notifications.
        self.scale_statuses = scale_statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scale_statuses is not None:
            result['ScaleStatuses'] = self.scale_statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScaleStatuses') is not None:
            self.scale_statuses = m.get('ScaleStatuses')

        return self

