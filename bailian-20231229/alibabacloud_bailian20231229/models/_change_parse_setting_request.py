# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ChangeParseSettingRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        file_type: str = None,
        parser: str = None,
        parser_config: main_models.ChangeParseSettingRequestParserConfig = None,
    ):
        # The category ID, which is the `CategoryId` returned by **AddCategory**. To view the category ID, click the ID icon next to the category name on the Unstructured Data tab of the [Application Data](https://bailian.console.alibabacloud.com/?tab=app#/data-center) page.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The file type. Valid values: pdf, docx, and doc.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The parser code. Valid values:
        # 
        # *   DOCMIND (Intelligent parsing)
        # *   DOCMIND_DIGITAL (Digital parsing)
        # *   DOCMIND_LLM_VERSION (LLM parsing)
        # *   DASH_QWEN_VL_PARSER (Qwen VL parsing)
        # 
        # This parameter is required.
        self.parser = parser
        # The parser configuration. Currently, this is available only for Qwen VL parsing.
        self.parser_config = parser_config

    def validate(self):
        if self.parser_config:
            self.parser_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.parser is not None:
            result['Parser'] = self.parser

        if self.parser_config is not None:
            result['ParserConfig'] = self.parser_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('ParserConfig') is not None:
            temp_model = main_models.ChangeParseSettingRequestParserConfig()
            self.parser_config = temp_model.from_map(m.get('ParserConfig'))

        return self

class ChangeParseSettingRequestParserConfig(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        model_prompt: str = None,
    ):
        # The model name.
        # 
        # Valid values:
        # 
        # *   qwen-vl-max
        # *   qwen-vl-plus
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
            result['modelName'] = self.model_name

        if self.model_prompt is not None:
            result['modelPrompt'] = self.model_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelPrompt') is not None:
            self.model_prompt = m.get('modelPrompt')

        return self

