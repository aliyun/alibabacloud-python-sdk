# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Any, Dict, BinaryIO


class AyncTradeDocumentPackageExtractSmartAppRequest(TeaModel):
    def __init__(
        self,
        custom_extraction_range: List[str] = None,
        file_name: str = None,
        file_url: str = None,
        option: str = None,
        template_name: str = None,
    ):
        self.custom_extraction_range = custom_extraction_range
        self.file_name = file_name
        # This parameter is required.
        self.file_url = file_url
        self.option = option
        self.template_name = template_name

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
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.option is not None:
            result['Option'] = self.option
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExtractionRange') is not None:
            self.custom_extraction_range = m.get('CustomExtractionRange')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class AyncTradeDocumentPackageExtractSmartAppShrinkRequest(TeaModel):
    def __init__(
        self,
        custom_extraction_range_shrink: str = None,
        file_name: str = None,
        file_url: str = None,
        option: str = None,
        template_name: str = None,
    ):
        self.custom_extraction_range_shrink = custom_extraction_range_shrink
        self.file_name = file_name
        # This parameter is required.
        self.file_url = file_url
        self.option = option
        self.template_name = template_name

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
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.option is not None:
            result['Option'] = self.option
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExtractionRange') is not None:
            self.custom_extraction_range_shrink = m.get('CustomExtractionRange')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class AyncTradeDocumentPackageExtractSmartAppResponseBody(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        data: Any = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.data = data
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AyncTradeDocumentPackageExtractSmartAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AyncTradeDocumentPackageExtractSmartAppResponseBody = None,
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
            temp_model = AyncTradeDocumentPackageExtractSmartAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocParserResultRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        layout_num: int = None,
        layout_step_size: int = None,
    ):
        self.id = id
        self.layout_num = layout_num
        self.layout_step_size = layout_step_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.layout_num is not None:
            result['LayoutNum'] = self.layout_num
        if self.layout_step_size is not None:
            result['LayoutStepSize'] = self.layout_step_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LayoutNum') is not None:
            self.layout_num = m.get('LayoutNum')
        if m.get('LayoutStepSize') is not None:
            self.layout_step_size = m.get('LayoutStepSize')
        return self


class GetDocParserResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
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


class GetDocParserResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocParserResultResponseBody = None,
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
            temp_model = GetDocParserResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocStructureResultRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        image_strategy: str = None,
        reveal_markdown: bool = None,
        use_url_response_body: bool = None,
    ):
        self.id = id
        self.image_strategy = image_strategy
        self.reveal_markdown = reveal_markdown
        self.use_url_response_body = use_url_response_body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.image_strategy is not None:
            result['ImageStrategy'] = self.image_strategy
        if self.reveal_markdown is not None:
            result['RevealMarkdown'] = self.reveal_markdown
        if self.use_url_response_body is not None:
            result['UseUrlResponseBody'] = self.use_url_response_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageStrategy') is not None:
            self.image_strategy = m.get('ImageStrategy')
        if m.get('RevealMarkdown') is not None:
            self.reveal_markdown = m.get('RevealMarkdown')
        if m.get('UseUrlResponseBody') is not None:
            self.use_url_response_body = m.get('UseUrlResponseBody')
        return self


class GetDocStructureResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed: bool = None,
        data: Dict[str, Any] = None,
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


class GetDocStructureResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocStructureResultResponseBody = None,
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
            temp_model = GetDocStructureResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentCompareResultRequest(TeaModel):
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


class GetDocumentCompareResultResponseBody(TeaModel):
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


class GetDocumentCompareResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentCompareResultResponseBody = None,
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
            temp_model = GetDocumentCompareResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentConvertResultRequest(TeaModel):
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


class GetDocumentConvertResultResponseBodyData(TeaModel):
    def __init__(
        self,
        md_5: str = None,
        size: int = None,
        type: str = None,
        url: str = None,
    ):
        self.md_5 = md_5
        self.size = size
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetDocumentConvertResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed: bool = None,
        data: List[GetDocumentConvertResultResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        # This parameter is required.
        self.completed = completed
        self.data = data
        self.message = message
        self.request_id = request_id
        # This parameter is required.
        self.status = status

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed is not None:
            result['Completed'] = self.completed
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDocumentConvertResultResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDocumentConvertResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentConvertResultResponseBody = None,
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
            temp_model = GetDocumentConvertResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentExtractResultRequest(TeaModel):
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


class GetDocumentExtractResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed: bool = None,
        data: Dict[str, Any] = None,
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


class GetDocumentExtractResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentExtractResultResponseBody = None,
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
            temp_model = GetDocumentExtractResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPageNumRequest(TeaModel):
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


class GetPageNumResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
    ):
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class GetPageNumResponseBody(TeaModel):
    def __init__(
        self,
        data: GetPageNumResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetPageNumResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPageNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPageNumResponseBody = None,
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
            temp_model = GetPageNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableUnderstandingResultRequest(TeaModel):
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


class GetTableUnderstandingResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed: bool = None,
        data: Dict[str, Any] = None,
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


class GetTableUnderstandingResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableUnderstandingResultResponseBody = None,
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
            temp_model = GetTableUnderstandingResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDocParserStatusRequest(TeaModel):
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


class QueryDocParserStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        image_count: int = None,
        number_of_successful_parsing: int = None,
        page_count_estimate: int = None,
        paragraph_count: int = None,
        status: str = None,
        table_count: int = None,
        tokens: int = None,
    ):
        self.image_count = image_count
        self.number_of_successful_parsing = number_of_successful_parsing
        self.page_count_estimate = page_count_estimate
        self.paragraph_count = paragraph_count
        self.status = status
        self.table_count = table_count
        self.tokens = tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.number_of_successful_parsing is not None:
            result['NumberOfSuccessfulParsing'] = self.number_of_successful_parsing
        if self.page_count_estimate is not None:
            result['PageCountEstimate'] = self.page_count_estimate
        if self.paragraph_count is not None:
            result['ParagraphCount'] = self.paragraph_count
        if self.status is not None:
            result['Status'] = self.status
        if self.table_count is not None:
            result['TableCount'] = self.table_count
        if self.tokens is not None:
            result['Tokens'] = self.tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('NumberOfSuccessfulParsing') is not None:
            self.number_of_successful_parsing = m.get('NumberOfSuccessfulParsing')
        if m.get('PageCountEstimate') is not None:
            self.page_count_estimate = m.get('PageCountEstimate')
        if m.get('ParagraphCount') is not None:
            self.paragraph_count = m.get('ParagraphCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')
        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')
        return self


class QueryDocParserStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDocParserStatusResponseBodyData = None,
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
            temp_model = QueryDocParserStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDocParserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDocParserStatusResponseBody = None,
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
            temp_model = QueryDocParserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertImageToExcelJobRequest(TeaModel):
    def __init__(
        self,
        force_merge_excel: bool = None,
        image_name_extension: str = None,
        image_names: List[str] = None,
        image_urls: List[str] = None,
    ):
        self.force_merge_excel = force_merge_excel
        self.image_name_extension = image_name_extension
        self.image_names = image_names
        self.image_urls = image_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_merge_excel is not None:
            result['ForceMergeExcel'] = self.force_merge_excel
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceMergeExcel') is not None:
            self.force_merge_excel = m.get('ForceMergeExcel')
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class SubmitConvertImageToExcelJobShrinkRequest(TeaModel):
    def __init__(
        self,
        force_merge_excel: bool = None,
        image_name_extension: str = None,
        image_names_shrink: str = None,
        image_urls_shrink: str = None,
    ):
        self.force_merge_excel = force_merge_excel
        self.image_name_extension = image_name_extension
        self.image_names_shrink = image_names_shrink
        self.image_urls_shrink = image_urls_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_merge_excel is not None:
            result['ForceMergeExcel'] = self.force_merge_excel
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.image_urls_shrink is not None:
            result['ImageUrls'] = self.image_urls_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceMergeExcel') is not None:
            self.force_merge_excel = m.get('ForceMergeExcel')
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls_shrink = m.get('ImageUrls')
        return self


class SubmitConvertImageToExcelJobResponseBodyData(TeaModel):
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


class SubmitConvertImageToExcelJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitConvertImageToExcelJobResponseBodyData = None,
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
            temp_model = SubmitConvertImageToExcelJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertImageToExcelJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitConvertImageToExcelJobResponseBody = None,
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
            temp_model = SubmitConvertImageToExcelJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertImageToMarkdownJobRequest(TeaModel):
    def __init__(
        self,
        image_name_extension: str = None,
        image_names: List[str] = None,
        image_urls: List[str] = None,
    ):
        self.image_name_extension = image_name_extension
        self.image_names = image_names
        self.image_urls = image_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class SubmitConvertImageToMarkdownJobShrinkRequest(TeaModel):
    def __init__(
        self,
        image_name_extension: str = None,
        image_names_shrink: str = None,
        image_urls_shrink: str = None,
    ):
        self.image_name_extension = image_name_extension
        self.image_names_shrink = image_names_shrink
        self.image_urls_shrink = image_urls_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.image_urls_shrink is not None:
            result['ImageUrls'] = self.image_urls_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls_shrink = m.get('ImageUrls')
        return self


class SubmitConvertImageToMarkdownJobResponseBodyData(TeaModel):
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


class SubmitConvertImageToMarkdownJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitConvertImageToMarkdownJobResponseBodyData = None,
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
            temp_model = SubmitConvertImageToMarkdownJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertImageToMarkdownJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitConvertImageToMarkdownJobResponseBody = None,
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
            temp_model = SubmitConvertImageToMarkdownJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertImageToPdfJobRequest(TeaModel):
    def __init__(
        self,
        image_name_extension: str = None,
        image_names: List[str] = None,
        image_urls: List[str] = None,
    ):
        self.image_name_extension = image_name_extension
        self.image_names = image_names
        self.image_urls = image_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class SubmitConvertImageToPdfJobShrinkRequest(TeaModel):
    def __init__(
        self,
        image_name_extension: str = None,
        image_names_shrink: str = None,
        image_urls_shrink: str = None,
    ):
        self.image_name_extension = image_name_extension
        self.image_names_shrink = image_names_shrink
        self.image_urls_shrink = image_urls_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.image_urls_shrink is not None:
            result['ImageUrls'] = self.image_urls_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls_shrink = m.get('ImageUrls')
        return self


class SubmitConvertImageToPdfJobResponseBodyData(TeaModel):
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


class SubmitConvertImageToPdfJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitConvertImageToPdfJobResponseBodyData = None,
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
            temp_model = SubmitConvertImageToPdfJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertImageToPdfJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitConvertImageToPdfJobResponseBody = None,
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
            temp_model = SubmitConvertImageToPdfJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertImageToWordJobRequest(TeaModel):
    def __init__(
        self,
        image_name_extension: str = None,
        image_names: List[str] = None,
        image_urls: List[str] = None,
    ):
        self.image_name_extension = image_name_extension
        self.image_names = image_names
        self.image_urls = image_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class SubmitConvertImageToWordJobShrinkRequest(TeaModel):
    def __init__(
        self,
        image_name_extension: str = None,
        image_names_shrink: str = None,
        image_urls_shrink: str = None,
    ):
        self.image_name_extension = image_name_extension
        self.image_names_shrink = image_names_shrink
        self.image_urls_shrink = image_urls_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_name_extension is not None:
            result['ImageNameExtension'] = self.image_name_extension
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.image_urls_shrink is not None:
            result['ImageUrls'] = self.image_urls_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageNameExtension') is not None:
            self.image_name_extension = m.get('ImageNameExtension')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('ImageUrls') is not None:
            self.image_urls_shrink = m.get('ImageUrls')
        return self


class SubmitConvertImageToWordJobResponseBodyData(TeaModel):
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


class SubmitConvertImageToWordJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitConvertImageToWordJobResponseBodyData = None,
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
            temp_model = SubmitConvertImageToWordJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertImageToWordJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitConvertImageToWordJobResponseBody = None,
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
            temp_model = SubmitConvertImageToWordJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertPdfToExcelJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        force_export_inner_image: bool = None,
        force_merge_excel: bool = None,
    ):
        self.file_name = file_name
        self.file_url = file_url
        self.force_export_inner_image = force_export_inner_image
        self.force_merge_excel = force_merge_excel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image
        if self.force_merge_excel is not None:
            result['ForceMergeExcel'] = self.force_merge_excel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')
        if m.get('ForceMergeExcel') is not None:
            self.force_merge_excel = m.get('ForceMergeExcel')
        return self


class SubmitConvertPdfToExcelJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        force_export_inner_image: bool = None,
        force_merge_excel: bool = None,
    ):
        self.file_name = file_name
        self.file_url_object = file_url_object
        self.force_export_inner_image = force_export_inner_image
        self.force_merge_excel = force_merge_excel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image
        if self.force_merge_excel is not None:
            result['ForceMergeExcel'] = self.force_merge_excel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')
        if m.get('ForceMergeExcel') is not None:
            self.force_merge_excel = m.get('ForceMergeExcel')
        return self


class SubmitConvertPdfToExcelJobResponseBodyData(TeaModel):
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


class SubmitConvertPdfToExcelJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitConvertPdfToExcelJobResponseBodyData = None,
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
            temp_model = SubmitConvertPdfToExcelJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertPdfToExcelJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitConvertPdfToExcelJobResponseBody = None,
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
            temp_model = SubmitConvertPdfToExcelJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertPdfToImageJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
    ):
        self.file_name = file_name
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitConvertPdfToImageJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
    ):
        self.file_name = file_name
        self.file_url_object = file_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitConvertPdfToImageJobResponseBodyData(TeaModel):
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


class SubmitConvertPdfToImageJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitConvertPdfToImageJobResponseBodyData = None,
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
            temp_model = SubmitConvertPdfToImageJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertPdfToImageJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitConvertPdfToImageJobResponseBody = None,
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
            temp_model = SubmitConvertPdfToImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertPdfToMarkdownJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
    ):
        self.file_name = file_name
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitConvertPdfToMarkdownJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
    ):
        self.file_name = file_name
        self.file_url_object = file_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitConvertPdfToMarkdownJobResponseBodyData(TeaModel):
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


class SubmitConvertPdfToMarkdownJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitConvertPdfToMarkdownJobResponseBodyData = None,
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
            temp_model = SubmitConvertPdfToMarkdownJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertPdfToMarkdownJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitConvertPdfToMarkdownJobResponseBody = None,
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
            temp_model = SubmitConvertPdfToMarkdownJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitConvertPdfToWordJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        force_export_inner_image: bool = None,
    ):
        self.file_name = file_name
        self.file_url = file_url
        self.force_export_inner_image = force_export_inner_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')
        return self


class SubmitConvertPdfToWordJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        force_export_inner_image: bool = None,
    ):
        self.file_name = file_name
        self.file_url_object = file_url_object
        self.force_export_inner_image = force_export_inner_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.force_export_inner_image is not None:
            result['ForceExportInnerImage'] = self.force_export_inner_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ForceExportInnerImage') is not None:
            self.force_export_inner_image = m.get('ForceExportInnerImage')
        return self


class SubmitConvertPdfToWordJobResponseBodyData(TeaModel):
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


class SubmitConvertPdfToWordJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitConvertPdfToWordJobResponseBodyData = None,
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
            temp_model = SubmitConvertPdfToWordJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitConvertPdfToWordJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitConvertPdfToWordJobResponseBody = None,
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
            temp_model = SubmitConvertPdfToWordJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDigitalDocStructureJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        image_strategy: str = None,
        reveal_markdown: bool = None,
        use_url_response_body: bool = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.image_strategy = image_strategy
        self.reveal_markdown = reveal_markdown
        self.use_url_response_body = use_url_response_body

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
        if self.image_strategy is not None:
            result['ImageStrategy'] = self.image_strategy
        if self.reveal_markdown is not None:
            result['RevealMarkdown'] = self.reveal_markdown
        if self.use_url_response_body is not None:
            result['UseUrlResponseBody'] = self.use_url_response_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ImageStrategy') is not None:
            self.image_strategy = m.get('ImageStrategy')
        if m.get('RevealMarkdown') is not None:
            self.reveal_markdown = m.get('RevealMarkdown')
        if m.get('UseUrlResponseBody') is not None:
            self.use_url_response_body = m.get('UseUrlResponseBody')
        return self


class SubmitDigitalDocStructureJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        image_strategy: str = None,
        reveal_markdown: bool = None,
        use_url_response_body: bool = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.image_strategy = image_strategy
        self.reveal_markdown = reveal_markdown
        self.use_url_response_body = use_url_response_body

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
        if self.image_strategy is not None:
            result['ImageStrategy'] = self.image_strategy
        if self.reveal_markdown is not None:
            result['RevealMarkdown'] = self.reveal_markdown
        if self.use_url_response_body is not None:
            result['UseUrlResponseBody'] = self.use_url_response_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('ImageStrategy') is not None:
            self.image_strategy = m.get('ImageStrategy')
        if m.get('RevealMarkdown') is not None:
            self.reveal_markdown = m.get('RevealMarkdown')
        if m.get('UseUrlResponseBody') is not None:
            self.use_url_response_body = m.get('UseUrlResponseBody')
        return self


class SubmitDigitalDocStructureJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        id: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        self.data = data
        self.id = id
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
        if self.data is not None:
            result['Data'] = self.data
        if self.id is not None:
            result['Id'] = self.id
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SubmitDigitalDocStructureJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDigitalDocStructureJobResponseBody = None,
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
            temp_model = SubmitDigitalDocStructureJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocParserJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        formula_enhancement: bool = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.formula_enhancement = formula_enhancement

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
        if self.formula_enhancement is not None:
            result['FormulaEnhancement'] = self.formula_enhancement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FormulaEnhancement') is not None:
            self.formula_enhancement = m.get('FormulaEnhancement')
        return self


class SubmitDocParserJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        formula_enhancement: bool = None,
    ):
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.formula_enhancement = formula_enhancement

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
        if self.formula_enhancement is not None:
            result['FormulaEnhancement'] = self.formula_enhancement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('FormulaEnhancement') is not None:
            self.formula_enhancement = m.get('FormulaEnhancement')
        return self


class SubmitDocParserJobResponseBodyData(TeaModel):
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


class SubmitDocParserJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitDocParserJobResponseBodyData = None,
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
            temp_model = SubmitDocParserJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDocParserJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocParserJobResponseBody = None,
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
            temp_model = SubmitDocParserJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocStructureJobRequest(TeaModel):
    def __init__(
        self,
        allow_ppt_format: bool = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
        formula_enhancement: bool = None,
        structure_type: str = None,
    ):
        self.allow_ppt_format = allow_ppt_format
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url = file_url
        self.formula_enhancement = formula_enhancement
        self.structure_type = structure_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_ppt_format is not None:
            result['AllowPptFormat'] = self.allow_ppt_format
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.formula_enhancement is not None:
            result['FormulaEnhancement'] = self.formula_enhancement
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPptFormat') is not None:
            self.allow_ppt_format = m.get('AllowPptFormat')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FormulaEnhancement') is not None:
            self.formula_enhancement = m.get('FormulaEnhancement')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        return self


class SubmitDocStructureJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        allow_ppt_format: bool = None,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
        formula_enhancement: bool = None,
        structure_type: str = None,
    ):
        self.allow_ppt_format = allow_ppt_format
        self.file_name = file_name
        self.file_name_extension = file_name_extension
        self.file_url_object = file_url_object
        self.formula_enhancement = formula_enhancement
        self.structure_type = structure_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_ppt_format is not None:
            result['AllowPptFormat'] = self.allow_ppt_format
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        if self.formula_enhancement is not None:
            result['FormulaEnhancement'] = self.formula_enhancement
        if self.structure_type is not None:
            result['StructureType'] = self.structure_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPptFormat') is not None:
            self.allow_ppt_format = m.get('AllowPptFormat')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        if m.get('FormulaEnhancement') is not None:
            self.formula_enhancement = m.get('FormulaEnhancement')
        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')
        return self


class SubmitDocStructureJobResponseBodyData(TeaModel):
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


class SubmitDocStructureJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitDocStructureJobResponseBodyData = None,
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
            temp_model = SubmitDocStructureJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDocStructureJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocStructureJobResponseBody = None,
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
            temp_model = SubmitDocStructureJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocumentExtractJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
    ):
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
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitDocumentExtractJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
    ):
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
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitDocumentExtractJobResponseBodyData(TeaModel):
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


class SubmitDocumentExtractJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitDocumentExtractJobResponseBodyData = None,
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
            temp_model = SubmitDocumentExtractJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDocumentExtractJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocumentExtractJobResponseBody = None,
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
            temp_model = SubmitDocumentExtractJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTableUnderstandingJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url: str = None,
    ):
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
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitTableUnderstandingJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_name_extension: str = None,
        file_url_object: BinaryIO = None,
    ):
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
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_name_extension is not None:
            result['FileNameExtension'] = self.file_name_extension
        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileNameExtension') is not None:
            self.file_name_extension = m.get('FileNameExtension')
        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')
        return self


class SubmitTableUnderstandingJobResponseBodyData(TeaModel):
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


class SubmitTableUnderstandingJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTableUnderstandingJobResponseBodyData = None,
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
            temp_model = SubmitTableUnderstandingJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitTableUnderstandingJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTableUnderstandingJobResponseBody = None,
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
            temp_model = SubmitTableUnderstandingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


