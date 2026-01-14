# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRuleStatusResponseBody(DaraModel):
    def __init__(
        self,
        failed_ids: str = None,
        request_id: str = None,
    ):
        # The IDs of sensitive data detection rules whose status failed to be changed. Multiple IDs are separated with commas (,).
        self.failed_ids = failed_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

