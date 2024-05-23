# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class MachineTranslateECommerceRequest(TeaModel):
    def __init__(
        self,
        content_format: str = None,
        source_language: str = None,
        source_text: str = None,
        target_language: str = None,
    ):
        # This parameter is required.
        self.content_format = content_format
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.source_text = source_text
        # This parameter is required.
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_format is not None:
            result['ContentFormat'] = self.content_format
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentFormat') is not None:
            self.content_format = m.get('ContentFormat')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class MachineTranslateECommerceResponseBodyResultCode(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class MachineTranslateECommerceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: MachineTranslateECommerceResponseBodyResultCode = None,
        success: bool = None,
        translate_text: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.success = success
        self.translate_text = translate_text

    def validate(self):
        if self.result_code:
            self.result_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.translate_text is not None:
            result['TranslateText'] = self.translate_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            temp_model = MachineTranslateECommerceResponseBodyResultCode()
            self.result_code = temp_model.from_map(m['ResultCode'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TranslateText') is not None:
            self.translate_text = m.get('TranslateText')
        return self


class MachineTranslateECommerceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MachineTranslateECommerceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MachineTranslateECommerceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MachineTranslateGeneralRequest(TeaModel):
    def __init__(
        self,
        content_format: str = None,
        source_language: str = None,
        source_text: str = None,
        target_language: str = None,
    ):
        # This parameter is required.
        self.content_format = content_format
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.source_text = source_text
        # This parameter is required.
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_format is not None:
            result['ContentFormat'] = self.content_format
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentFormat') is not None:
            self.content_format = m.get('ContentFormat')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class MachineTranslateGeneralResponseBodyResultCode(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class MachineTranslateGeneralResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: MachineTranslateGeneralResponseBodyResultCode = None,
        success: bool = None,
        translate_text: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.success = success
        self.translate_text = translate_text

    def validate(self):
        if self.result_code:
            self.result_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.translate_text is not None:
            result['TranslateText'] = self.translate_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            temp_model = MachineTranslateGeneralResponseBodyResultCode()
            self.result_code = temp_model.from_map(m['ResultCode'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TranslateText') is not None:
            self.translate_text = m.get('TranslateText')
        return self


class MachineTranslateGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MachineTranslateGeneralResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MachineTranslateGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


