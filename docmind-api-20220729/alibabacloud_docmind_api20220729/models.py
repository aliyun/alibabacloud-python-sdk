# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, Any, List


class ExtractFeedbackRequest(TeaModel):
    def __init__(
        self,
        feedback_url: str = None,
    ):
        self.feedback_url = feedback_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback_url is not None:
            result['FeedbackUrl'] = self.feedback_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeedbackUrl') is not None:
            self.feedback_url = m.get('FeedbackUrl')
        return self


class ExtractFeedbackAdvanceRequest(TeaModel):
    def __init__(
        self,
        feedback_url_object: BinaryIO = None,
    ):
        self.feedback_url_object = feedback_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback_url_object is not None:
            result['FeedbackUrl'] = self.feedback_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeedbackUrl') is not None:
            self.feedback_url_object = m.get('FeedbackUrl')
        return self


class ExtractFeedbackResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ExtractFeedbackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ExtractFeedbackResponseBodyData = None,
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
            temp_model = ExtractFeedbackResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtractFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExtractFeedbackResponseBody = None,
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
            temp_model = ExtractFeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSingleDocumentExtractResultRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetSingleDocumentExtractResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed: bool = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        self.completed = completed
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetSingleDocumentExtractResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSingleDocumentExtractResultResponseBody = None,
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
            temp_model = GetSingleDocumentExtractResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReClassifyTradeDocumentExtractRequestPageUpdateInfoModels(TeaModel):
    def __init__(
        self,
        att_type_code: str = None,
        page_id: str = None,
    ):
        self.att_type_code = att_type_code
        self.page_id = page_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.att_type_code is not None:
            result['AttTypeCode'] = self.att_type_code
        if self.page_id is not None:
            result['PageId'] = self.page_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttTypeCode') is not None:
            self.att_type_code = m.get('AttTypeCode')
        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')
        return self


class ReClassifyTradeDocumentExtractRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        page_update_info_models: List[ReClassifyTradeDocumentExtractRequestPageUpdateInfoModels] = None,
    ):
        self.biz_id = biz_id
        self.page_update_info_models = page_update_info_models

    def validate(self):
        if self.page_update_info_models:
            for k in self.page_update_info_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        result['PageUpdateInfoModels'] = []
        if self.page_update_info_models is not None:
            for k in self.page_update_info_models:
                result['PageUpdateInfoModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        self.page_update_info_models = []
        if m.get('PageUpdateInfoModels') is not None:
            for k in m.get('PageUpdateInfoModels'):
                temp_model = ReClassifyTradeDocumentExtractRequestPageUpdateInfoModels()
                self.page_update_info_models.append(temp_model.from_map(k))
        return self


class ReClassifyTradeDocumentExtractShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        page_update_info_models_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.page_update_info_models_shrink = page_update_info_models_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_update_info_models_shrink is not None:
            result['PageUpdateInfoModels'] = self.page_update_info_models_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageUpdateInfoModels') is not None:
            self.page_update_info_models_shrink = m.get('PageUpdateInfoModels')
        return self


class ReClassifyTradeDocumentExtractResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ReClassifyTradeDocumentExtractResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReClassifyTradeDocumentExtractResponseBodyData = None,
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
            temp_model = ReClassifyTradeDocumentExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReClassifyTradeDocumentExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReClassifyTradeDocumentExtractResponseBody = None,
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
            temp_model = ReClassifyTradeDocumentExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryTradeDocumentExtractRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class RetryTradeDocumentExtractResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RetryTradeDocumentExtractResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RetryTradeDocumentExtractResponseBodyData = None,
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
            temp_model = RetryTradeDocumentExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RetryTradeDocumentExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetryTradeDocumentExtractResponseBody = None,
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
            temp_model = RetryTradeDocumentExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAirWaybillExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitAirWaybillExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitAirWaybillExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitAirWaybillExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitAirWaybillExtractJobResponseBodyData = None,
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
            temp_model = SubmitAirWaybillExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitAirWaybillExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitAirWaybillExtractJobResponseBody = None,
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
            temp_model = SubmitAirWaybillExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitBillOfLadingExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitBillOfLadingExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitBillOfLadingExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitBillOfLadingExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitBillOfLadingExtractJobResponseBodyData = None,
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
            temp_model = SubmitBillOfLadingExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitBillOfLadingExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitBillOfLadingExtractJobResponseBody = None,
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
            temp_model = SubmitBillOfLadingExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitBookingNoteExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitBookingNoteExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitBookingNoteExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitBookingNoteExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitBookingNoteExtractJobResponseBodyData = None,
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
            temp_model = SubmitBookingNoteExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitBookingNoteExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitBookingNoteExtractJobResponseBody = None,
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
            temp_model = SubmitBookingNoteExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCertificateOfOriginExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitCertificateOfOriginExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitCertificateOfOriginExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitCertificateOfOriginExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitCertificateOfOriginExtractJobResponseBodyData = None,
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
            temp_model = SubmitCertificateOfOriginExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitCertificateOfOriginExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitCertificateOfOriginExtractJobResponseBody = None,
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
            temp_model = SubmitCertificateOfOriginExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitContainerLoadPlanExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitContainerLoadPlanExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitContainerLoadPlanExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitContainerLoadPlanExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitContainerLoadPlanExtractJobResponseBodyData = None,
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
            temp_model = SubmitContainerLoadPlanExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitContainerLoadPlanExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitContainerLoadPlanExtractJobResponseBody = None,
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
            temp_model = SubmitContainerLoadPlanExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitExportDeclarationSheetExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitExportDeclarationSheetExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitExportDeclarationSheetExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitExportDeclarationSheetExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitExportDeclarationSheetExtractJobResponseBodyData = None,
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
            temp_model = SubmitExportDeclarationSheetExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitExportDeclarationSheetExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitExportDeclarationSheetExtractJobResponseBody = None,
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
            temp_model = SubmitExportDeclarationSheetExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitGeneralContractExtractJobRequest(TeaModel):
    def __init__(
        self,
        contract_model: str = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
    ):
        self.contract_model = contract_model
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contract_model is not None:
            result['ContractModel'] = self.contract_model
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContractModel') is not None:
            self.contract_model = m.get('ContractModel')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitGeneralContractExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        contract_model: str = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
    ):
        self.contract_model = contract_model
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contract_model is not None:
            result['ContractModel'] = self.contract_model
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContractModel') is not None:
            self.contract_model = m.get('ContractModel')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitGeneralContractExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitGeneralContractExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitGeneralContractExtractJobResponseBodyData = None,
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
            temp_model = SubmitGeneralContractExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitGeneralContractExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitGeneralContractExtractJobResponseBody = None,
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
            temp_model = SubmitGeneralContractExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitImportDeclarationSheetExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitImportDeclarationSheetExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitImportDeclarationSheetExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitImportDeclarationSheetExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitImportDeclarationSheetExtractJobResponseBodyData = None,
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
            temp_model = SubmitImportDeclarationSheetExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitImportDeclarationSheetExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitImportDeclarationSheetExtractJobResponseBody = None,
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
            temp_model = SubmitImportDeclarationSheetExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInvoiceExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitInvoiceExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitInvoiceExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitInvoiceExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitInvoiceExtractJobResponseBodyData = None,
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
            temp_model = SubmitInvoiceExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitInvoiceExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitInvoiceExtractJobResponseBody = None,
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
            temp_model = SubmitInvoiceExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPackingListExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitPackingListExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitPackingListExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitPackingListExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitPackingListExtractJobResponseBodyData = None,
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
            temp_model = SubmitPackingListExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitPackingListExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitPackingListExtractJobResponseBody = None,
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
            temp_model = SubmitPackingListExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSalesConfirmationExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitSalesConfirmationExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitSalesConfirmationExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitSalesConfirmationExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitSalesConfirmationExtractJobResponseBodyData = None,
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
            temp_model = SubmitSalesConfirmationExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitSalesConfirmationExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSalesConfirmationExtractJobResponseBody = None,
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
            temp_model = SubmitSalesConfirmationExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSeaWaybillExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitSeaWaybillExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        parser_config_id: int = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.parser_config_id = parser_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.parser_config_id is not None:
            result['ParserConfigId'] = self.parser_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ParserConfigId') is not None:
            self.parser_config_id = m.get('ParserConfigId')
        return self


class SubmitSeaWaybillExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitSeaWaybillExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitSeaWaybillExtractJobResponseBodyData = None,
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
            temp_model = SubmitSeaWaybillExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitSeaWaybillExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSeaWaybillExtractJobResponseBody = None,
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
            temp_model = SubmitSeaWaybillExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTradeDocumentPackageExtractJobRequest(TeaModel):
    def __init__(
        self,
        custom_extraction_range: List[str] = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
    ):
        self.custom_extraction_range = custom_extraction_range
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_extraction_range is not None:
            result['CustomExtractionRange'] = self.custom_extraction_range
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExtractionRange') is not None:
            self.custom_extraction_range = m.get('CustomExtractionRange')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitTradeDocumentPackageExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        custom_extraction_range: List[str] = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
    ):
        self.custom_extraction_range = custom_extraction_range
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_extraction_range is not None:
            result['CustomExtractionRange'] = self.custom_extraction_range
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExtractionRange') is not None:
            self.custom_extraction_range = m.get('CustomExtractionRange')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitTradeDocumentPackageExtractJobShrinkRequest(TeaModel):
    def __init__(
        self,
        custom_extraction_range_shrink: str = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
    ):
        self.custom_extraction_range_shrink = custom_extraction_range_shrink
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_extraction_range_shrink is not None:
            result['CustomExtractionRange'] = self.custom_extraction_range_shrink
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExtractionRange') is not None:
            self.custom_extraction_range_shrink = m.get('CustomExtractionRange')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitTradeDocumentPackageExtractJobResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SubmitTradeDocumentPackageExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTradeDocumentPackageExtractJobResponseBodyData = None,
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
            temp_model = SubmitTradeDocumentPackageExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitTradeDocumentPackageExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTradeDocumentPackageExtractJobResponseBody = None,
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
            temp_model = SubmitTradeDocumentPackageExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


