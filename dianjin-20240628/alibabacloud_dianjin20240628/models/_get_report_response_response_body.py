# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetReportResponseResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        out_request_no: str = None,
        report_url: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.out_request_no = out_request_no
        self.report_url = report_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.out_request_no is not None:
            result['outRequestNo'] = self.out_request_no

        if self.report_url is not None:
            result['reportUrl'] = self.report_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('outRequestNo') is not None:
            self.out_request_no = m.get('outRequestNo')

        if m.get('reportUrl') is not None:
            self.report_url = m.get('reportUrl')

        return self

