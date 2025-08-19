# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class SubmitDocParserJobAdvanceRequest(DaraModel):
    def __init__(
        self,
        enhancement_mode: str = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        formula_enhancement: bool = None,
        llm_enhancement: bool = None,
        option: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        output_html_table: bool = None,
        page_index: str = None,
    ):
        self.enhancement_mode = enhancement_mode
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.formula_enhancement = formula_enhancement
        self.llm_enhancement = llm_enhancement
        self.option = option
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.output_html_table = output_html_table
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enhancement_mode is not None:
            result['EnhancementMode'] = self.enhancement_mode

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension

        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object

        if self.formula_enhancement is not None:
            result['FormulaEnhancement'] = self.formula_enhancement

        if self.llm_enhancement is not None:
            result['LlmEnhancement'] = self.llm_enhancement

        if self.option is not None:
            result['Option'] = self.option

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.output_html_table is not None:
            result['OutputHtmlTable'] = self.output_html_table

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnhancementMode') is not None:
            self.enhancement_mode = m.get('EnhancementMode')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')

        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')

        if m.get('FormulaEnhancement') is not None:
            self.formula_enhancement = m.get('FormulaEnhancement')

        if m.get('LlmEnhancement') is not None:
            self.llm_enhancement = m.get('LlmEnhancement')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OutputHtmlTable') is not None:
            self.output_html_table = m.get('OutputHtmlTable')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        return self

