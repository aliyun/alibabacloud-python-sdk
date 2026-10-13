# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportNodeStatusResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_message: str = None,
        report_id: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The error message.
        self.error_message = error_message
        # The fault report ID.
        self.report_id = report_id
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

