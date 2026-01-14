# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeParseSettingShrinkRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        file_type: str = None,
        parser: str = None,
        parser_config_shrink: str = None,
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
        self.parser_config_shrink = parser_config_shrink

    def validate(self):
        pass

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

        if self.parser_config_shrink is not None:
            result['ParserConfig'] = self.parser_config_shrink

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
            self.parser_config_shrink = m.get('ParserConfig')

        return self

