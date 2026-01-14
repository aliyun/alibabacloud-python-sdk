# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class GetAvailableParserTypesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAvailableParserTypesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true
        # *   false
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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAvailableParserTypesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAvailableParserTypesResponseBodyData(DaraModel):
    def __init__(
        self,
        file_type: str = None,
        parser_list: List[main_models.GetAvailableParserTypesResponseBodyDataParserList] = None,
    ):
        # The file type, which is the same as the FileType in the input parameter.
        self.file_type = file_type
        # The list of supported parsers
        self.parser_list = parser_list

    def validate(self):
        if self.parser_list:
            for v1 in self.parser_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_type is not None:
            result['FileType'] = self.file_type

        result['ParserList'] = []
        if self.parser_list is not None:
            for k1 in self.parser_list:
                result['ParserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        self.parser_list = []
        if m.get('ParserList') is not None:
            for k1 in m.get('ParserList'):
                temp_model = main_models.GetAvailableParserTypesResponseBodyDataParserList()
                self.parser_list.append(temp_model.from_map(k1))

        return self

class GetAvailableParserTypesResponseBodyDataParserList(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        parser: str = None,
    ):
        # The display name of the parsing method.
        self.display_name = display_name
        # The parser code. Valid values:
        # 
        # *   DOCMIND (Intelligent parsing)
        # *   DOCMIND_DIGITAL (Digital parsing)
        # *   DOCMIND_LLM_VERSION (LLM parsing)
        # *   DASH_QWEN_VL_PARSER (Qwen VL parsing)
        self.parser = parser

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.parser is not None:
            result['Parser'] = self.parser

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        return self

