# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafkastreaming20260202 import models as main_models
from darabonba.model import DaraModel

class CheckSqlContentResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CheckSqlContentResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CheckSqlContentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CheckSqlContentResponseBodyData(DaraModel):
    def __init__(
        self,
        error_list: List[main_models.CheckSqlContentResponseBodyDataErrorList] = None,
        valid: bool = None,
    ):
        self.error_list = error_list
        self.valid = valid

    def validate(self):
        if self.error_list:
            for v1 in self.error_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorList'] = []
        if self.error_list is not None:
            for k1 in self.error_list:
                result['ErrorList'].append(k1.to_map() if k1 else None)

        if self.valid is not None:
            result['Valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_list = []
        if m.get('ErrorList') is not None:
            for k1 in m.get('ErrorList'):
                temp_model = main_models.CheckSqlContentResponseBodyDataErrorList()
                self.error_list.append(temp_model.from_map(k1))

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        return self



class CheckSqlContentResponseBodyDataErrorList(DaraModel):
    def __init__(
        self,
        code_snippet: str = None,
        column_number: int = None,
        end_column_number: int = None,
        end_line_number: int = None,
        error_type: str = None,
        line_number: int = None,
        message: str = None,
    ):
        self.code_snippet = code_snippet
        self.column_number = column_number
        self.end_column_number = end_column_number
        self.end_line_number = end_line_number
        self.error_type = error_type
        self.line_number = line_number
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_snippet is not None:
            result['CodeSnippet'] = self.code_snippet

        if self.column_number is not None:
            result['ColumnNumber'] = self.column_number

        if self.end_column_number is not None:
            result['EndColumnNumber'] = self.end_column_number

        if self.end_line_number is not None:
            result['EndLineNumber'] = self.end_line_number

        if self.error_type is not None:
            result['ErrorType'] = self.error_type

        if self.line_number is not None:
            result['LineNumber'] = self.line_number

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeSnippet') is not None:
            self.code_snippet = m.get('CodeSnippet')

        if m.get('ColumnNumber') is not None:
            self.column_number = m.get('ColumnNumber')

        if m.get('EndColumnNumber') is not None:
            self.end_column_number = m.get('EndColumnNumber')

        if m.get('EndLineNumber') is not None:
            self.end_line_number = m.get('EndLineNumber')

        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')

        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

