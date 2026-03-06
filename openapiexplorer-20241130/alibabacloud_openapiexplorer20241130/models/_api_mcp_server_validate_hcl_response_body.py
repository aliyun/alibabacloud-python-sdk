# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from darabonba.model import DaraModel

class ApiMcpServerValidateHclResponseBody(DaraModel):
    def __init__(
        self,
        diagnostic_report: Any = None,
        errors: List[str] = None,
        hash: str = None,
        is_valid: bool = None,
        parameters: List[Any] = None,
        request_id: str = None,
        warnings: List[str] = None,
    ):
        # The diagnostic report of the code.
        self.diagnostic_report = diagnostic_report
        # The list of error messages.
        self.errors = errors
        # The unique identifier of the Terraform HCL code.
        self.hash = hash
        # Indicates whether the code is valid.
        self.is_valid = is_valid
        # The list of parameters.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id
        # The list of warning messages.
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnostic_report is not None:
            result['diagnosticReport'] = self.diagnostic_report

        if self.errors is not None:
            result['errors'] = self.errors

        if self.hash is not None:
            result['hash'] = self.hash

        if self.is_valid is not None:
            result['isValid'] = self.is_valid

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.warnings is not None:
            result['warnings'] = self.warnings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diagnosticReport') is not None:
            self.diagnostic_report = m.get('diagnosticReport')

        if m.get('errors') is not None:
            self.errors = m.get('errors')

        if m.get('hash') is not None:
            self.hash = m.get('hash')

        if m.get('isValid') is not None:
            self.is_valid = m.get('isValid')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('warnings') is not None:
            self.warnings = m.get('warnings')

        return self

