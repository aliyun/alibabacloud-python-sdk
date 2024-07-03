# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class AddMTInterveneWordRequest(TeaModel):
    def __init__(
        self,
        package_id: str = None,
        project_id: str = None,
        source_text: str = None,
        target_text: str = None,
    ):
        self.package_id = package_id
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.source_text = source_text
        self.target_text = target_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_text is not None:
            result['SourceText'] = self.source_text
        if self.target_text is not None:
            result['TargetText'] = self.target_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')
        if m.get('TargetText') is not None:
            self.target_text = m.get('TargetText')
        return self


class AddMTInterveneWordResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        word_id: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.word_id = word_id

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
        if self.word_id is not None:
            result['WordId'] = self.word_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WordId') is not None:
            self.word_id = m.get('WordId')
        return self


class AddMTInterveneWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMTInterveneWordResponseBody = None,
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
            temp_model = AddMTInterveneWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPredictDocRequest(TeaModel):
    def __init__(
        self,
        doc_id: int = None,
        product: str = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class GetPredictDocResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_content: str = None,
        status: int = None,
        xliffinfo: str = None,
    ):
        self.request_id = request_id
        self.result_content = result_content
        self.status = status
        self.xliffinfo = xliffinfo

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_content is not None:
            result['ResultContent'] = self.result_content
        if self.status is not None:
            result['Status'] = self.status
        if self.xliffinfo is not None:
            result['XLIFFInfo'] = self.xliffinfo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('XLIFFInfo') is not None:
            self.xliffinfo = m.get('XLIFFInfo')
        return self


class GetPredictDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPredictDocResponseBody = None,
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
            temp_model = GetPredictDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictMTModelByDocRequest(TeaModel):
    def __init__(
        self,
        file_content: str = None,
        file_type: str = None,
        model_id: int = None,
        model_version: str = None,
        need_xliff: bool = None,
    ):
        # This parameter is required.
        self.file_content = file_content
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
        self.model_id = model_id
        # This parameter is required.
        self.model_version = model_version
        self.need_xliff = need_xliff

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_content is not None:
            result['FileContent'] = self.file_content
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.need_xliff is not None:
            result['NeedXLIFF'] = self.need_xliff
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('NeedXLIFF') is not None:
            self.need_xliff = m.get('NeedXLIFF')
        return self


class PredictMTModelByDocResponseBody(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        request_id: str = None,
    ):
        self.doc_id = doc_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PredictMTModelByDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PredictMTModelByDocResponseBody = None,
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
            temp_model = PredictMTModelByDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


