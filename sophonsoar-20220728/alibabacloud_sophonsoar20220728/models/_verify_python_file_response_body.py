# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class VerifyPythonFileResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        syntax: List[main_models.VerifyPythonFileResponseBodySyntax] = None,
    ):
        # The request ID. Alibaba Cloud generates a unique ID for each request. Use this ID to troubleshoot issues.
        self.request_id = request_id
        # The result set of the Python code verification. If this parameter is empty, the code syntax is correct.
        self.syntax = syntax

    def validate(self):
        if self.syntax:
            for v1 in self.syntax:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Syntax'] = []
        if self.syntax is not None:
            for k1 in self.syntax:
                result['Syntax'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.syntax = []
        if m.get('Syntax') is not None:
            for k1 in m.get('Syntax'):
                temp_model = main_models.VerifyPythonFileResponseBodySyntax()
                self.syntax.append(temp_model.from_map(k1))

        return self

class VerifyPythonFileResponseBodySyntax(DaraModel):
    def __init__(
        self,
        end_column: int = None,
        end_line_number: int = None,
        message: str = None,
        severity: int = None,
        start_column: int = None,
        start_line_number: int = None,
    ):
        # The ending column number of the code that contains an error.
        self.end_column = end_column
        # The ending line number of the code that contains an error.
        self.end_line_number = end_line_number
        # The error message for the code.
        self.message = message
        # The error level of the code.
        # 
        # - 4: General error
        # 
        # - 8: Critical error
        self.severity = severity
        # The starting column number of the code that contains an error.
        self.start_column = start_column
        # The starting line number of the code that contains an error.
        self.start_line_number = start_line_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_column is not None:
            result['EndColumn'] = self.end_column

        if self.end_line_number is not None:
            result['EndLineNumber'] = self.end_line_number

        if self.message is not None:
            result['Message'] = self.message

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_column is not None:
            result['StartColumn'] = self.start_column

        if self.start_line_number is not None:
            result['StartLineNumber'] = self.start_line_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndColumn') is not None:
            self.end_column = m.get('EndColumn')

        if m.get('EndLineNumber') is not None:
            self.end_line_number = m.get('EndLineNumber')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartColumn') is not None:
            self.start_column = m.get('StartColumn')

        if m.get('StartLineNumber') is not None:
            self.start_line_number = m.get('StartLineNumber')

        return self

