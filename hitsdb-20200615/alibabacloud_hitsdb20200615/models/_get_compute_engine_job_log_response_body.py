# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetComputeEngineJobLogResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        job_id: str = None,
        logs: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.job_id = job_id
        self.logs = logs
        self.page_number = page_number
        self.page_size = page_size
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

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.logs is not None:
            result['Logs'] = self.logs

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Logs') is not None:
            self.logs = m.get('Logs')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

