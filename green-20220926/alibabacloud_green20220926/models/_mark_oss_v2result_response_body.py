# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MarkOssV2ResultResponseBody(DaraModel):
    def __init__(
        self,
        failure_request_ids: List[str] = None,
        request_id: str = None,
        success_request_ids: List[str] = None,
    ):
        self.failure_request_ids = failure_request_ids
        self.request_id = request_id
        self.success_request_ids = success_request_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_request_ids is not None:
            result['FailureRequestIds'] = self.failure_request_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_request_ids is not None:
            result['SuccessRequestIds'] = self.success_request_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureRequestIds') is not None:
            self.failure_request_ids = m.get('FailureRequestIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessRequestIds') is not None:
            self.success_request_ids = m.get('SuccessRequestIds')

        return self

