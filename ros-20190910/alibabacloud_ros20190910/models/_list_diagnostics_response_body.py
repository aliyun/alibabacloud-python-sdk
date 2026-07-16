# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListDiagnosticsResponseBody(DaraModel):
    def __init__(
        self,
        diagnostics: List[main_models.ListDiagnosticsResponseBodyDiagnostics] = None,
        http_status_code: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The items that are diagnosed.
        self.diagnostics = diagnostics
        # The HTTP status code returned. The value 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.diagnostics:
            for v1 in self.diagnostics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Diagnostics'] = []
        if self.diagnostics is not None:
            for k1 in self.diagnostics:
                result['Diagnostics'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.diagnostics = []
        if m.get('Diagnostics') is not None:
            for k1 in m.get('Diagnostics'):
                temp_model = main_models.ListDiagnosticsResponseBodyDiagnostics()
                self.diagnostics.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDiagnosticsResponseBodyDiagnostics(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        diagnostic_key: str = None,
        diagnostic_product: str = None,
        report_id: str = None,
        status: str = None,
    ):
        # The time when the diagnostic report was generated.
        self.create_time = create_time
        # The keyword in the diagnosis.
        self.diagnostic_key = diagnostic_key
        # The product that is diagnosed.
        self.diagnostic_product = diagnostic_product
        # The ID of the diagnostic report.
        self.report_id = report_id
        # The diagnosis status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.diagnostic_key is not None:
            result['DiagnosticKey'] = self.diagnostic_key

        if self.diagnostic_product is not None:
            result['DiagnosticProduct'] = self.diagnostic_product

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DiagnosticKey') is not None:
            self.diagnostic_key = m.get('DiagnosticKey')

        if m.get('DiagnosticProduct') is not None:
            self.diagnostic_product = m.get('DiagnosticProduct')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

