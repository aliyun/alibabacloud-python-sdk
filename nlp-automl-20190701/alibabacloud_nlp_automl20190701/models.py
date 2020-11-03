# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class PredictMTModelByDocRequest(TeaModel):
    def __init__(self, file_content=None, file_type=None, model_id=None, need_xliff=None, model_version=None):
        self.file_content = file_content  # type: str
        self.file_type = file_type      # type: str
        self.model_id = model_id        # type: int
        self.need_xliff = need_xliff    # type: bool
        self.model_version = model_version  # type: str

    def validate(self):
        self.validate_required(self.file_content, 'file_content')
        self.validate_required(self.file_type, 'file_type')
        self.validate_required(self.model_id, 'model_id')
        self.validate_required(self.model_version, 'model_version')

    def to_map(self):
        result = {}
        result['FileContent'] = self.file_content
        result['FileType'] = self.file_type
        result['ModelId'] = self.model_id
        result['NeedXLIFF'] = self.need_xliff
        result['ModelVersion'] = self.model_version
        return result

    def from_map(self, map={}):
        self.file_content = map.get('FileContent')
        self.file_type = map.get('FileType')
        self.model_id = map.get('ModelId')
        self.need_xliff = map.get('NeedXLIFF')
        self.model_version = map.get('ModelVersion')
        return self


class PredictMTModelByDocResponse(TeaModel):
    def __init__(self, request_id=None, doc_id=None):
        self.request_id = request_id    # type: str
        self.doc_id = doc_id            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.doc_id, 'doc_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DocId'] = self.doc_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.doc_id = map.get('DocId')
        return self


class BindIntervenePackageAndModelRequest(TeaModel):
    def __init__(self, package_id=None, model_id=None, model_version=None, project_id=None):
        self.package_id = package_id    # type: int
        self.model_id = model_id        # type: int
        self.model_version = model_version  # type: str
        self.project_id = project_id    # type: int

    def validate(self):
        self.validate_required(self.package_id, 'package_id')
        self.validate_required(self.model_id, 'model_id')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['PackageId'] = self.package_id
        result['ModelId'] = self.model_id
        result['ModelVersion'] = self.model_version
        result['ProjectId'] = self.project_id
        return result

    def from_map(self, map={}):
        self.package_id = map.get('PackageId')
        self.model_id = map.get('ModelId')
        self.model_version = map.get('ModelVersion')
        self.project_id = map.get('ProjectId')
        return self


class BindIntervenePackageAndModelResponse(TeaModel):
    def __init__(self, code=None, message=None, success=None, request_id=None):
        self.code = code                # type: int
        self.message = message          # type: int
        self.success = success          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.request_id = map.get('RequestId')
        return self


class AddMtIntervenePackageRequest(TeaModel):
    def __init__(self, package_name=None, source_language=None, target_language=None, project_id=None,
                 source_type=None):
        self.package_name = package_name  # type: str
        self.source_language = source_language  # type: str
        self.target_language = target_language  # type: str
        self.project_id = project_id    # type: int
        self.source_type = source_type  # type: str

    def validate(self):
        self.validate_required(self.package_name, 'package_name')
        self.validate_required(self.source_language, 'source_language')
        self.validate_required(self.target_language, 'target_language')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['PackageName'] = self.package_name
        result['SourceLanguage'] = self.source_language
        result['TargetLanguage'] = self.target_language
        result['ProjectId'] = self.project_id
        result['SourceType'] = self.source_type
        return result

    def from_map(self, map={}):
        self.package_name = map.get('PackageName')
        self.source_language = map.get('SourceLanguage')
        self.target_language = map.get('TargetLanguage')
        self.project_id = map.get('ProjectId')
        self.source_type = map.get('SourceType')
        return self


class AddMtIntervenePackageResponse(TeaModel):
    def __init__(self, code=None, message=None, package_id=None, request_id=None):
        self.code = code                # type: int
        self.message = message          # type: int
        self.package_id = package_id    # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.package_id, 'package_id')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['PackageId'] = self.package_id
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.package_id = map.get('PackageId')
        self.request_id = map.get('RequestId')
        return self


class GetPredictDocRequest(TeaModel):
    def __init__(self, doc_id=None, product=None):
        self.doc_id = doc_id            # type: int
        self.product = product          # type: str

    def validate(self):
        self.validate_required(self.doc_id, 'doc_id')

    def to_map(self):
        result = {}
        result['DocId'] = self.doc_id
        result['Product'] = self.product
        return result

    def from_map(self, map={}):
        self.doc_id = map.get('DocId')
        self.product = map.get('Product')
        return self


class GetPredictDocResponse(TeaModel):
    def __init__(self, request_id=None, result_content=None, status=None, xliffinfo=None):
        self.request_id = request_id    # type: str
        self.result_content = result_content  # type: str
        self.status = status            # type: int
        self.xliffinfo = xliffinfo      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_content, 'result_content')
        self.validate_required(self.status, 'status')
        self.validate_required(self.xliffinfo, 'xliffinfo')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ResultContent'] = self.result_content
        result['Status'] = self.status
        result['XLIFFInfo'] = self.xliffinfo
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.result_content = map.get('ResultContent')
        self.status = map.get('Status')
        self.xliffinfo = map.get('XLIFFInfo')
        return self


class AddMTInterveneWordRequest(TeaModel):
    def __init__(self, source_text=None, target_text=None, project_id=None, package_id=None):
        self.source_text = source_text  # type: str
        self.target_text = target_text  # type: str
        self.project_id = project_id    # type: str
        self.package_id = package_id    # type: str

    def validate(self):
        self.validate_required(self.source_text, 'source_text')
        self.validate_required(self.project_id, 'project_id')

    def to_map(self):
        result = {}
        result['SourceText'] = self.source_text
        result['TargetText'] = self.target_text
        result['ProjectId'] = self.project_id
        result['PackageId'] = self.package_id
        return result

    def from_map(self, map={}):
        self.source_text = map.get('SourceText')
        self.target_text = map.get('TargetText')
        self.project_id = map.get('ProjectId')
        self.package_id = map.get('PackageId')
        return self


class AddMTInterveneWordResponse(TeaModel):
    def __init__(self, code=None, message=None, word_id=None, request_id=None):
        self.code = code                # type: int
        self.message = message          # type: int
        self.word_id = word_id          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.word_id, 'word_id')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['WordId'] = self.word_id
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.word_id = map.get('WordId')
        self.request_id = map.get('RequestId')
        return self


class PredictMTModelRequest(TeaModel):
    def __init__(self, model_id=None, model_version=None, content=None, product=None):
        self.model_id = model_id        # type: str
        self.model_version = model_version  # type: str
        self.content = content          # type: str
        self.product = product          # type: str

    def validate(self):
        self.validate_required(self.model_id, 'model_id')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['ModelId'] = self.model_id
        result['ModelVersion'] = self.model_version
        result['Content'] = self.content
        result['Product'] = self.product
        return result

    def from_map(self, map={}):
        self.model_id = map.get('ModelId')
        self.model_version = map.get('ModelVersion')
        self.content = map.get('Content')
        self.product = map.get('Product')
        return self


class PredictMTModelResponse(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code                # type: int
        self.message = message          # type: int
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['Data'] = self.data
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.data = map.get('Data')
        self.request_id = map.get('RequestId')
        return self


class InvokeActionRequest(TeaModel):
    def __init__(self, invoke_product=None, invoke_region=None, invoke_action=None, invoke_params=None):
        self.invoke_product = invoke_product  # type: str
        self.invoke_region = invoke_region  # type: str
        self.invoke_action = invoke_action  # type: str
        self.invoke_params = invoke_params  # type: str

    def validate(self):
        self.validate_required(self.invoke_action, 'invoke_action')
        self.validate_required(self.invoke_params, 'invoke_params')

    def to_map(self):
        result = {}
        result['InvokeProduct'] = self.invoke_product
        result['InvokeRegion'] = self.invoke_region
        result['InvokeAction'] = self.invoke_action
        result['InvokeParams'] = self.invoke_params
        return result

    def from_map(self, map={}):
        self.invoke_product = map.get('InvokeProduct')
        self.invoke_region = map.get('InvokeRegion')
        self.invoke_action = map.get('InvokeAction')
        self.invoke_params = map.get('InvokeParams')
        return self


class InvokeActionResponse(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code                # type: int
        self.message = message          # type: int
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['Data'] = self.data
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.data = map.get('Data')
        self.request_id = map.get('RequestId')
        return self
