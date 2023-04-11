# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List, Any


class CreateDocTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        callback_url: str = None,
        client_token: str = None,
        file_url: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
    ):
        self.callback_url = callback_url
        self.client_token = client_token
        self.file_url = file_url
        self.scene = scene
        self.source_language = source_language
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class CreateDocTranslateTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        callback_url: str = None,
        client_token: str = None,
        file_url_object: BinaryIO = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
    ):
        self.callback_url = callback_url
        self.client_token = client_token
        self.file_url_object = file_url_object
        self.scene = scene
        self.source_language = source_language
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class CreateDocTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDocTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDocTranslateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateDocTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        extra: str = None,
        source_language: str = None,
        target_language: str = None,
        url_list: str = None,
    ):
        self.client_token = client_token
        self.extra = extra
        self.source_language = source_language
        self.target_language = target_language
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        if self.url_list is not None:
            result['UrlList'] = self.url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        if m.get('UrlList') is not None:
            self.url_list = m.get('UrlList')
        return self


class CreateImageTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateImageTranslateTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateImageTranslateTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageTranslateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateImageTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBatchTranslateRequest(TeaModel):
    def __init__(
        self,
        api_type: str = None,
        format_type: str = None,
        scene: str = None,
        source_language: str = None,
        source_text: str = None,
        target_language: str = None,
    ):
        self.api_type = api_type
        self.format_type = format_type
        self.scene = scene
        self.source_language = source_language
        self.source_text = source_text
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class GetBatchTranslateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        translated_list: List[Dict[str, Any]] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.translated_list = translated_list

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.translated_list is not None:
            result['TranslatedList'] = self.translated_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranslatedList') is not None:
            self.translated_list = m.get('TranslatedList')
        return self


class GetBatchTranslateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBatchTranslateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBatchTranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectLanguageRequest(TeaModel):
    def __init__(
        self,
        source_text: str = None,
    ):
        self.source_text = source_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        return self


class GetDetectLanguageResponseBody(TeaModel):
    def __init__(
        self,
        detected_language: str = None,
        request_id: str = None,
    ):
        self.detected_language = detected_language
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detected_language is not None:
            result['DetectedLanguage'] = self.detected_language
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectedLanguage') is not None:
            self.detected_language = m.get('DetectedLanguage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDetectLanguageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDetectLanguageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetDetectLanguageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetDocTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        request_id: str = None,
        status: str = None,
        task_id: str = None,
        translate_error_code: str = None,
        translate_error_message: str = None,
        translate_file_url: str = None,
    ):
        self.page_count = page_count
        self.request_id = request_id
        self.status = status
        self.task_id = task_id
        self.translate_error_code = translate_error_code
        self.translate_error_message = translate_error_message
        self.translate_file_url = translate_file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.translate_error_code is not None:
            result['TranslateErrorCode'] = self.translate_error_code
        if self.translate_error_message is not None:
            result['TranslateErrorMessage'] = self.translate_error_message
        if self.translate_file_url is not None:
            result['TranslateFileUrl'] = self.translate_file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TranslateErrorCode') is not None:
            self.translate_error_code = m.get('TranslateErrorCode')
        if m.get('TranslateErrorMessage') is not None:
            self.translate_error_message = m.get('TranslateErrorMessage')
        if m.get('TranslateFileUrl') is not None:
            self.translate_file_url = m.get('TranslateFileUrl')
        return self


class GetDocTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocTranslateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetDocTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageDiagnoseRequest(TeaModel):
    def __init__(
        self,
        extra: str = None,
        url: str = None,
    ):
        self.extra = extra
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImageDiagnoseResponseBodyData(TeaModel):
    def __init__(
        self,
        language: str = None,
    ):
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetImageDiagnoseResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetImageDiagnoseResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetImageDiagnoseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageDiagnoseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageDiagnoseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetImageDiagnoseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageTranslateRequest(TeaModel):
    def __init__(
        self,
        extra: str = None,
        source_language: str = None,
        target_language: str = None,
        url: str = None,
    ):
        self.extra = extra
        self.source_language = source_language
        self.target_language = target_language
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImageTranslateResponseBodyData(TeaModel):
    def __init__(
        self,
        orc: str = None,
        picture_editor: str = None,
        url: str = None,
    ):
        self.orc = orc
        self.picture_editor = picture_editor
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.orc is not None:
            result['Orc'] = self.orc
        if self.picture_editor is not None:
            result['PictureEditor'] = self.picture_editor
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Orc') is not None:
            self.orc = m.get('Orc')
        if m.get('PictureEditor') is not None:
            self.picture_editor = m.get('PictureEditor')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImageTranslateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetImageTranslateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetImageTranslateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageTranslateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageTranslateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetImageTranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetImageTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        image_data: str = None,
    ):
        self.image_data = image_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        return self


class GetImageTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetImageTranslateTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetImageTranslateTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageTranslateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetImageTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTitleDiagnoseRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        extra: str = None,
        language: str = None,
        platform: str = None,
        title: str = None,
    ):
        self.category_id = category_id
        self.extra = extra
        self.language = language
        self.platform = platform
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.language is not None:
            result['Language'] = self.language
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTitleDiagnoseResponseBodyData(TeaModel):
    def __init__(
        self,
        all_uppercase_words: str = None,
        contain_core_classes: str = None,
        disable_words: str = None,
        duplicate_words: str = None,
        language_quality_score: str = None,
        no_first_uppercase_list: str = None,
        over_length_limit: str = None,
        total_score: str = None,
        word_count: str = None,
        word_spelled_correct_error: str = None,
    ):
        self.all_uppercase_words = all_uppercase_words
        self.contain_core_classes = contain_core_classes
        self.disable_words = disable_words
        self.duplicate_words = duplicate_words
        self.language_quality_score = language_quality_score
        self.no_first_uppercase_list = no_first_uppercase_list
        self.over_length_limit = over_length_limit
        self.total_score = total_score
        self.word_count = word_count
        self.word_spelled_correct_error = word_spelled_correct_error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_uppercase_words is not None:
            result['AllUppercaseWords'] = self.all_uppercase_words
        if self.contain_core_classes is not None:
            result['ContainCoreClasses'] = self.contain_core_classes
        if self.disable_words is not None:
            result['DisableWords'] = self.disable_words
        if self.duplicate_words is not None:
            result['DuplicateWords'] = self.duplicate_words
        if self.language_quality_score is not None:
            result['LanguageQualityScore'] = self.language_quality_score
        if self.no_first_uppercase_list is not None:
            result['NoFirstUppercaseList'] = self.no_first_uppercase_list
        if self.over_length_limit is not None:
            result['OverLengthLimit'] = self.over_length_limit
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        if self.word_count is not None:
            result['WordCount'] = self.word_count
        if self.word_spelled_correct_error is not None:
            result['WordSpelledCorrectError'] = self.word_spelled_correct_error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllUppercaseWords') is not None:
            self.all_uppercase_words = m.get('AllUppercaseWords')
        if m.get('ContainCoreClasses') is not None:
            self.contain_core_classes = m.get('ContainCoreClasses')
        if m.get('DisableWords') is not None:
            self.disable_words = m.get('DisableWords')
        if m.get('DuplicateWords') is not None:
            self.duplicate_words = m.get('DuplicateWords')
        if m.get('LanguageQualityScore') is not None:
            self.language_quality_score = m.get('LanguageQualityScore')
        if m.get('NoFirstUppercaseList') is not None:
            self.no_first_uppercase_list = m.get('NoFirstUppercaseList')
        if m.get('OverLengthLimit') is not None:
            self.over_length_limit = m.get('OverLengthLimit')
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')
        if m.get('WordSpelledCorrectError') is not None:
            self.word_spelled_correct_error = m.get('WordSpelledCorrectError')
        return self


class GetTitleDiagnoseResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTitleDiagnoseResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTitleDiagnoseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTitleDiagnoseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTitleDiagnoseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTitleDiagnoseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTitleGenerateRequest(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        category_id: str = None,
        extra: str = None,
        hot_words: str = None,
        language: str = None,
        platform: str = None,
        title: str = None,
    ):
        self.attributes = attributes
        self.category_id = category_id
        self.extra = extra
        self.hot_words = hot_words
        self.language = language
        self.platform = platform
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.hot_words is not None:
            result['HotWords'] = self.hot_words
        if self.language is not None:
            result['Language'] = self.language
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('HotWords') is not None:
            self.hot_words = m.get('HotWords')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTitleGenerateResponseBodyData(TeaModel):
    def __init__(
        self,
        titles: str = None,
    ):
        self.titles = titles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.titles is not None:
            result['Titles'] = self.titles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        return self


class GetTitleGenerateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTitleGenerateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTitleGenerateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTitleGenerateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTitleGenerateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTitleGenerateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTitleIntelligenceRequest(TeaModel):
    def __init__(
        self,
        cat_level_three_id: int = None,
        cat_level_two_id: int = None,
        extra: str = None,
        keywords: str = None,
        platform: str = None,
    ):
        self.cat_level_three_id = cat_level_three_id
        self.cat_level_two_id = cat_level_two_id
        self.extra = extra
        self.keywords = keywords
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cat_level_three_id is not None:
            result['CatLevelThreeId'] = self.cat_level_three_id
        if self.cat_level_two_id is not None:
            result['CatLevelTwoId'] = self.cat_level_two_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatLevelThreeId') is not None:
            self.cat_level_three_id = m.get('CatLevelThreeId')
        if m.get('CatLevelTwoId') is not None:
            self.cat_level_two_id = m.get('CatLevelTwoId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class GetTitleIntelligenceResponseBodyData(TeaModel):
    def __init__(
        self,
        titles: str = None,
    ):
        self.titles = titles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.titles is not None:
            result['Titles'] = self.titles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        return self


class GetTitleIntelligenceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTitleIntelligenceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTitleIntelligenceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTitleIntelligenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTitleIntelligenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTitleIntelligenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranslateImageBatchResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTranslateImageBatchResultResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        code: int = None,
        final_image_url: str = None,
        in_painting_url: str = None,
        message: str = None,
        source_image_url: str = None,
        success: bool = None,
        template_json: str = None,
    ):
        self.code = code
        self.final_image_url = final_image_url
        self.in_painting_url = in_painting_url
        self.message = message
        self.source_image_url = source_image_url
        self.success = success
        self.template_json = template_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.final_image_url is not None:
            result['FinalImageUrl'] = self.final_image_url
        if self.in_painting_url is not None:
            result['InPaintingUrl'] = self.in_painting_url
        if self.message is not None:
            result['Message'] = self.message
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.success is not None:
            result['Success'] = self.success
        if self.template_json is not None:
            result['TemplateJson'] = self.template_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FinalImageUrl') is not None:
            self.final_image_url = m.get('FinalImageUrl')
        if m.get('InPaintingUrl') is not None:
            self.in_painting_url = m.get('InPaintingUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateJson') is not None:
            self.template_json = m.get('TemplateJson')
        return self


class GetTranslateImageBatchResultResponseBodyData(TeaModel):
    def __init__(
        self,
        result: List[GetTranslateImageBatchResultResponseBodyDataResult] = None,
        status: str = None,
    ):
        self.result = result
        self.status = status

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetTranslateImageBatchResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTranslateImageBatchResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTranslateImageBatchResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTranslateImageBatchResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTranslateImageBatchResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTranslateImageBatchResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTranslateImageBatchResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranslateReportRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        begin_time: str = None,
        end_time: str = None,
        group: str = None,
    ):
        self.api_name = api_name
        self.begin_time = begin_time
        self.end_time = end_time
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class GetTranslateReportResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTranslateReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTranslateReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTranslateReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenAlimtServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        type: str = None,
    ):
        self.owner_id = owner_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OpenAlimtServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenAlimtServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenAlimtServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = OpenAlimtServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateRequest(TeaModel):
    def __init__(
        self,
        context: str = None,
        format_type: str = None,
        scene: str = None,
        source_language: str = None,
        source_text: str = None,
        target_language: str = None,
    ):
        self.context = context
        self.format_type = format_type
        self.scene = scene
        self.source_language = source_language
        self.source_text = source_text
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['Context'] = self.context
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateResponseBodyData(TeaModel):
    def __init__(
        self,
        translated: str = None,
        word_count: str = None,
    ):
        self.translated = translated
        self.word_count = word_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translated is not None:
            result['Translated'] = self.translated
        if self.word_count is not None:
            result['WordCount'] = self.word_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Translated') is not None:
            self.translated = m.get('Translated')
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')
        return self


class TranslateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TranslateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TranslateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TranslateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_type: str = None,
        image_url: str = None,
        result_type: str = None,
        source_language: str = None,
        target_language: str = None,
    ):
        self.certificate_type = certificate_type
        self.image_url = image_url
        self.result_type = result_type
        self.source_language = source_language
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateCertificateAdvanceRequest(TeaModel):
    def __init__(
        self,
        certificate_type: str = None,
        image_url_object: BinaryIO = None,
        result_type: str = None,
        source_language: str = None,
        target_language: str = None,
    ):
        self.certificate_type = certificate_type
        self.image_url_object = image_url_object
        self.result_type = result_type
        self.source_language = source_language
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateCertificateResponseBodyDataTranslatedValues(TeaModel):
    def __init__(
        self,
        key: str = None,
        key_translation: str = None,
        value: str = None,
        value_translation: str = None,
    ):
        self.key = key
        self.key_translation = key_translation
        self.value = value
        self.value_translation = value_translation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_translation is not None:
            result['KeyTranslation'] = self.key_translation
        if self.value is not None:
            result['Value'] = self.value
        if self.value_translation is not None:
            result['ValueTranslation'] = self.value_translation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyTranslation') is not None:
            self.key_translation = m.get('KeyTranslation')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueTranslation') is not None:
            self.value_translation = m.get('ValueTranslation')
        return self


class TranslateCertificateResponseBodyData(TeaModel):
    def __init__(
        self,
        translated_values: List[TranslateCertificateResponseBodyDataTranslatedValues] = None,
    ):
        self.translated_values = translated_values

    def validate(self):
        if self.translated_values:
            for k in self.translated_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TranslatedValues'] = []
        if self.translated_values is not None:
            for k in self.translated_values:
                result['TranslatedValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.translated_values = []
        if m.get('TranslatedValues') is not None:
            for k in m.get('TranslatedValues'):
                temp_model = TranslateCertificateResponseBodyDataTranslatedValues()
                self.translated_values.append(temp_model.from_map(k))
        return self


class TranslateCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: TranslateCertificateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = TranslateCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TranslateCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TranslateCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateECommerceRequest(TeaModel):
    def __init__(
        self,
        context: str = None,
        format_type: str = None,
        scene: str = None,
        source_language: str = None,
        source_text: str = None,
        target_language: str = None,
    ):
        self.context = context
        self.format_type = format_type
        self.scene = scene
        self.source_language = source_language
        self.source_text = source_text
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['Context'] = self.context
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateECommerceResponseBodyData(TeaModel):
    def __init__(
        self,
        translated: str = None,
        word_count: str = None,
    ):
        self.translated = translated
        self.word_count = word_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translated is not None:
            result['Translated'] = self.translated
        if self.word_count is not None:
            result['WordCount'] = self.word_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Translated') is not None:
            self.translated = m.get('Translated')
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')
        return self


class TranslateECommerceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TranslateECommerceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TranslateECommerceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateECommerceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TranslateECommerceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TranslateECommerceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateGeneralRequest(TeaModel):
    def __init__(
        self,
        context: str = None,
        format_type: str = None,
        scene: str = None,
        source_language: str = None,
        source_text: str = None,
        target_language: str = None,
    ):
        self.context = context
        self.format_type = format_type
        self.scene = scene
        self.source_language = source_language
        self.source_text = source_text
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['Context'] = self.context
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateGeneralResponseBodyData(TeaModel):
    def __init__(
        self,
        translated: str = None,
        word_count: str = None,
    ):
        self.translated = translated
        self.word_count = word_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translated is not None:
            result['Translated'] = self.translated
        if self.word_count is not None:
            result['WordCount'] = self.word_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Translated') is not None:
            self.translated = m.get('Translated')
        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')
        return self


class TranslateGeneralResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TranslateGeneralResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TranslateGeneralResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TranslateGeneralResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TranslateGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateImageRequest(TeaModel):
    def __init__(
        self,
        ext: str = None,
        field: str = None,
        image_base_64: str = None,
        image_url: str = None,
        source_language: str = None,
        target_language: str = None,
    ):
        self.ext = ext
        self.field = field
        self.image_base_64 = image_base_64
        self.image_url = image_url
        self.source_language = source_language
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.field is not None:
            result['Field'] = self.field
        if self.image_base_64 is not None:
            result['ImageBase64'] = self.image_base_64
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('ImageBase64') is not None:
            self.image_base_64 = m.get('ImageBase64')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateImageResponseBodyData(TeaModel):
    def __init__(
        self,
        final_image_url: str = None,
        in_painting_url: str = None,
        template_json: str = None,
    ):
        self.final_image_url = final_image_url
        self.in_painting_url = in_painting_url
        self.template_json = template_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.final_image_url is not None:
            result['FinalImageUrl'] = self.final_image_url
        if self.in_painting_url is not None:
            result['InPaintingUrl'] = self.in_painting_url
        if self.template_json is not None:
            result['TemplateJson'] = self.template_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinalImageUrl') is not None:
            self.final_image_url = m.get('FinalImageUrl')
        if m.get('InPaintingUrl') is not None:
            self.in_painting_url = m.get('InPaintingUrl')
        if m.get('TemplateJson') is not None:
            self.template_json = m.get('TemplateJson')
        return self


class TranslateImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TranslateImageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TranslateImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TranslateImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TranslateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateImageBatchRequest(TeaModel):
    def __init__(
        self,
        custom_task_id: str = None,
        ext: str = None,
        field: str = None,
        image_urls: str = None,
        source_language: str = None,
        target_language: str = None,
    ):
        self.custom_task_id = custom_task_id
        self.ext = ext
        self.field = field
        self.image_urls = image_urls
        self.source_language = source_language
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.field is not None:
            result['Field'] = self.field
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')
        return self


class TranslateImageBatchResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TranslateImageBatchResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TranslateImageBatchResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TranslateImageBatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateImageBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TranslateImageBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TranslateImageBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


