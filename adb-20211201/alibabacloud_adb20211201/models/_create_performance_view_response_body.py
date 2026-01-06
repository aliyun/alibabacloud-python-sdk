# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePerformanceViewResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        create_status: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        # 
        # >  This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The creation result. Valid values:
        # 
        # *   **SUCCESS**
        # *   **FAILED**
        self.create_status = create_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.create_status is not None:
            result['CreateStatus'] = self.create_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('CreateStatus') is not None:
            self.create_status = m.get('CreateStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

