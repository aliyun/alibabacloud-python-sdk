# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GrantHonorResponseBody(DaraModel):
    def __init__(
        self,
        failed_user_ids: List[str] = None,
        request_id: str = None,
        success_user_ids: List[str] = None,
    ):
        self.failed_user_ids = failed_user_ids
        # requestId
        self.request_id = request_id
        self.success_user_ids = success_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_user_ids is not None:
            result['failedUserIds'] = self.failed_user_ids

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success_user_ids is not None:
            result['successUserIds'] = self.success_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedUserIds') is not None:
            self.failed_user_ids = m.get('failedUserIds')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('successUserIds') is not None:
            self.success_user_ids = m.get('successUserIds')

        return self

