# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_docmind_api20220711 import models as main_models
from darabonba.model import DaraModel

class SubmitDocParserJobRequest(DaraModel):
    def __init__(
        self,
        custom_oss_config: main_models.SubmitDocParserJobRequestCustomOssConfig = None,
        enable_event_callback: bool = None,
        enhancement_mode: str = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        formula_enhancement: bool = None,
        llmparam: main_models.SubmitDocParserJobRequestLLMParam = None,
        llm_enhancement: bool = None,
        multimedia_parameters: main_models.SubmitDocParserJobRequestMultimediaParameters = None,
        need_header_footer: bool = None,
        option: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        output_html_table: bool = None,
        page_index: str = None,
    ):
        self.custom_oss_config = custom_oss_config
        self.enable_event_callback = enable_event_callback
        self.enhancement_mode = enhancement_mode
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.formula_enhancement = formula_enhancement
        self.llmparam = llmparam
        self.llm_enhancement = llm_enhancement
        self.multimedia_parameters = multimedia_parameters
        self.need_header_footer = need_header_footer
        self.option = option
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.output_html_table = output_html_table
        self.page_index = page_index

    def validate(self):
        if self.custom_oss_config:
            self.custom_oss_config.validate()
        if self.llmparam:
            self.llmparam.validate()
        if self.multimedia_parameters:
            self.multimedia_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_oss_config is not None:
            result['CustomOssConfig'] = self.custom_oss_config.to_map()

        if self.enable_event_callback is not None:
            result['EnableEventCallback'] = self.enable_event_callback

        if self.enhancement_mode is not None:
            result['EnhancementMode'] = self.enhancement_mode

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.formula_enhancement is not None:
            result['FormulaEnhancement'] = self.formula_enhancement

        if self.llmparam is not None:
            result['LLMParam'] = self.llmparam.to_map()

        if self.llm_enhancement is not None:
            result['LlmEnhancement'] = self.llm_enhancement

        if self.multimedia_parameters is not None:
            result['MultimediaParameters'] = self.multimedia_parameters.to_map()

        if self.need_header_footer is not None:
            result['NeedHeaderFooter'] = self.need_header_footer

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
        if m.get('CustomOssConfig') is not None:
            temp_model = main_models.SubmitDocParserJobRequestCustomOssConfig()
            self.custom_oss_config = temp_model.from_map(m.get('CustomOssConfig'))

        if m.get('EnableEventCallback') is not None:
            self.enable_event_callback = m.get('EnableEventCallback')

        if m.get('EnhancementMode') is not None:
            self.enhancement_mode = m.get('EnhancementMode')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('FormulaEnhancement') is not None:
            self.formula_enhancement = m.get('FormulaEnhancement')

        if m.get('LLMParam') is not None:
            temp_model = main_models.SubmitDocParserJobRequestLLMParam()
            self.llmparam = temp_model.from_map(m.get('LLMParam'))

        if m.get('LlmEnhancement') is not None:
            self.llm_enhancement = m.get('LlmEnhancement')

        if m.get('MultimediaParameters') is not None:
            temp_model = main_models.SubmitDocParserJobRequestMultimediaParameters()
            self.multimedia_parameters = temp_model.from_map(m.get('MultimediaParameters'))

        if m.get('NeedHeaderFooter') is not None:
            self.need_header_footer = m.get('NeedHeaderFooter')

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

class SubmitDocParserJobRequestMultimediaParameters(DaraModel):
    def __init__(
        self,
        enable_synopsis_parse: bool = None,
        vl_parse_prompt: str = None,
    ):
        self.enable_synopsis_parse = enable_synopsis_parse
        self.vl_parse_prompt = vl_parse_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_synopsis_parse is not None:
            result['EnableSynopsisParse'] = self.enable_synopsis_parse

        if self.vl_parse_prompt is not None:
            result['VlParsePrompt'] = self.vl_parse_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSynopsisParse') is not None:
            self.enable_synopsis_parse = m.get('EnableSynopsisParse')

        if m.get('VlParsePrompt') is not None:
            self.vl_parse_prompt = m.get('VlParsePrompt')

        return self

class SubmitDocParserJobRequestLLMParam(DaraModel):
    def __init__(
        self,
        model: str = None,
        prompt: str = None,
    ):
        self.model = model
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['Model'] = self.model

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        return self

class SubmitDocParserJobRequestCustomOssConfig(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        access_key_secret: str = None,
        sts_token: str = None,
    ):
        self.access_id = access_id
        self.access_key_secret = access_key_secret
        self.sts_token = sts_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.sts_token is not None:
            result['StsToken'] = self.sts_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')

        return self

