# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindInstanceDomainsResponseBody(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        request_id: str = None,
        success_count: int = None,
    ):
        # The number of domain names that failed to be unbound from the instance.
        self.failed_count = failed_count
        # The request ID.
        self.request_id = request_id
        # The number of domain names that are unbound from the instance.
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

