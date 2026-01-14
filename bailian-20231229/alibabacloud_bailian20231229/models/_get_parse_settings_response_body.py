# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class GetParseSettingsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetParseSettingsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data fields.
        self.data = data
        # The error message.
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetParseSettingsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetParseSettingsResponseBodyData(DaraModel):
    def __init__(
        self,
        file_type: str = None,
        parser: str = None,
        parser_config: main_models.GetParseSettingsResponseBodyDataParserConfig = None,
        parser_display_name: str = None,
    ):
        # The file type. Valid values are: pdf, docx, doc, etc. All supported file types in the category are listed here.
        self.file_type = file_type
        # The parser used for files of the current type. Valid values:
        # 
        # *   DOCMIND (Intelligent parsing)
        # *   DOCMIND_DIGITAL (Digital parsing)
        # *   DOCMIND_LLM_VERSION (LLM parsing)
        # *   DASH_QWEN_VL_PARSER (Qwen VL parsing)
        self.parser = parser
        # The parser configuration. Currently, this is available only for Qwen VL parsing.
        self.parser_config = parser_config
        # The display name of the parsing method.
        self.parser_display_name = parser_display_name

    def validate(self):
        if self.parser_config:
            self.parser_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.parser is not None:
            result['Parser'] = self.parser

        if self.parser_config is not None:
            result['ParserConfig'] = self.parser_config.to_map()

        if self.parser_display_name is not None:
            result['ParserDisplayName'] = self.parser_display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('ParserConfig') is not None:
            temp_model = main_models.GetParseSettingsResponseBodyDataParserConfig()
            self.parser_config = temp_model.from_map(m.get('ParserConfig'))

        if m.get('ParserDisplayName') is not None:
            self.parser_display_name = m.get('ParserDisplayName')

        return self

class GetParseSettingsResponseBodyDataParserConfig(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        model_prompt: str = None,
    ):
        # The model name.
        self.model_name = model_name
        # The prompt used for parsing.
        self.model_prompt = model_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_prompt is not None:
            result['ModelPrompt'] = self.model_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelPrompt') is not None:
            self.model_prompt = m.get('ModelPrompt')

        return self

