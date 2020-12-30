# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreateAsyncPredictRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        content: str = None,
        model_version: str = None,
        detail_tag: str = None,
        top_k: int = None,
        file_type: str = None,
        file_url: str = None,
        file_content: str = None,
        fetch_content: str = None,
        product: str = None,
    ):
        self.model_id = model_id
        self.content = content
        self.model_version = model_version
        self.detail_tag = detail_tag
        self.top_k = top_k
        self.file_type = file_type
        self.file_url = file_url
        self.file_content = file_content
        self.fetch_content = fetch_content
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.content is not None:
            result['Content'] = self.content
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.detail_tag is not None:
            result['DetailTag'] = self.detail_tag
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.file_content is not None:
            result['FileContent'] = self.file_content
        if self.fetch_content is not None:
            result['FetchContent'] = self.fetch_content
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('DetailTag') is not None:
            self.detail_tag = m.get('DetailTag')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')
        if m.get('FetchContent') is not None:
            self.fetch_content = m.get('FetchContent')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class CreateAsyncPredictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        async_predict_id: int = None,
    ):
        self.request_id = request_id
        self.async_predict_id = async_predict_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        return self


class CreateAsyncPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAsyncPredictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAsyncPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        dataset_name: str = None,
        product: str = None,
    ):
        self.project_id = project_id
        self.dataset_name = dataset_name
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class CreateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: int = None,
        success: bool = None,
        dataset_id: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success
        self.dataset_id = dataset_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class CreateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDatasetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetRecordRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_record: str = None,
        project_id: int = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_record = dataset_record
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_record is not None:
            result['DatasetRecord'] = self.dataset_record
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetRecord') is not None:
            self.dataset_record = m.get('DatasetRecord')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateDatasetRecordResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        dataset_record_id: Dict[str, Any] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.dataset_record_id = dataset_record_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dataset_record_id is not None:
            result['DatasetRecordId'] = self.dataset_record_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DatasetRecordId') is not None:
            self.dataset_record_id = m.get('DatasetRecordId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDatasetRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDatasetRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDatasetRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        model_type: str = None,
        project_id: int = None,
        model_name: str = None,
        dataset_id_list: Dict[str, Any] = None,
        test_dataset_id_list: Dict[str, Any] = None,
        is_incremental_train: str = None,
        product: str = None,
    ):
        self.model_id = model_id
        self.model_type = model_type
        self.project_id = project_id
        self.model_name = model_name
        self.dataset_id_list = dataset_id_list
        self.test_dataset_id_list = test_dataset_id_list
        self.is_incremental_train = is_incremental_train
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.dataset_id_list is not None:
            result['DatasetIdList'] = self.dataset_id_list
        if self.test_dataset_id_list is not None:
            result['TestDatasetIdList'] = self.test_dataset_id_list
        if self.is_incremental_train is not None:
            result['IsIncrementalTrain'] = self.is_incremental_train
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('DatasetIdList') is not None:
            self.dataset_id_list = m.get('DatasetIdList')
        if m.get('TestDatasetIdList') is not None:
            self.test_dataset_id_list = m.get('TestDatasetIdList')
        if m.get('IsIncrementalTrain') is not None:
            self.is_incremental_train = m.get('IsIncrementalTrain')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class CreateModelShrinkRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        model_type: str = None,
        project_id: int = None,
        model_name: str = None,
        dataset_id_list_shrink: str = None,
        test_dataset_id_list_shrink: str = None,
        is_incremental_train: str = None,
        product: str = None,
    ):
        self.model_id = model_id
        self.model_type = model_type
        self.project_id = project_id
        self.model_name = model_name
        self.dataset_id_list_shrink = dataset_id_list_shrink
        self.test_dataset_id_list_shrink = test_dataset_id_list_shrink
        self.is_incremental_train = is_incremental_train
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.dataset_id_list_shrink is not None:
            result['DatasetIdList'] = self.dataset_id_list_shrink
        if self.test_dataset_id_list_shrink is not None:
            result['TestDatasetIdList'] = self.test_dataset_id_list_shrink
        if self.is_incremental_train is not None:
            result['IsIncrementalTrain'] = self.is_incremental_train
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('DatasetIdList') is not None:
            self.dataset_id_list_shrink = m.get('DatasetIdList')
        if m.get('TestDatasetIdList') is not None:
            self.test_dataset_id_list_shrink = m.get('TestDatasetIdList')
        if m.get('IsIncrementalTrain') is not None:
            self.is_incremental_train = m.get('IsIncrementalTrain')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class CreateModelResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        project_type: str = None,
        project_name: str = None,
        project_description: str = None,
        product: str = None,
    ):
        self.project_type = project_type
        self.project_name = project_name
        self.project_description = project_description
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        project_id: Dict[str, Any] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.project_id = project_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        project_id: int = None,
        product: str = None,
    ):
        self.model_id = model_id
        self.project_id = project_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class DeleteModelResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployModelRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        opt_type: str = None,
        project_id: int = None,
        model_version: str = None,
        product: str = None,
    ):
        self.model_id = model_id
        self.opt_type = opt_type
        self.project_id = project_id
        self.model_version = model_version
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class DeployModelResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeployModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncPredictRequest(TeaModel):
    def __init__(
        self,
        async_predict_id: int = None,
        product: str = None,
    ):
        self.async_predict_id = async_predict_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class GetAsyncPredictResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        request_id: str = None,
        content: str = None,
        async_predict_id: int = None,
    ):
        self.status = status
        self.request_id = request_id
        self.content = content
        self.async_predict_id = async_predict_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        return self


class GetAsyncPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncPredictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAsyncPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        project_id: int = None,
        model_version: str = None,
        product: str = None,
    ):
        self.model_id = model_id
        self.project_id = project_id
        self.model_version = model_version
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class GetModelResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPredictResultRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        content: str = None,
        model_version: str = None,
        detail_tag: str = None,
        top_k: int = None,
        product: str = None,
    ):
        self.model_id = model_id
        self.content = content
        self.model_version = model_version
        self.detail_tag = detail_tag
        self.top_k = top_k
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.content is not None:
            result['Content'] = self.content
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.detail_tag is not None:
            result['DetailTag'] = self.detail_tag
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('DetailTag') is not None:
            self.detail_tag = m.get('DetailTag')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class GetPredictResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        content: str = None,
    ):
        self.request_id = request_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetPredictResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPredictResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPredictResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        page_size: int = None,
        page_number: int = None,
        product: str = None,
    ):
        self.project_id = project_id
        self.page_size = page_size
        self.page_number = page_number
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class ListDatasetResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDatasetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        page_size: int = None,
        page_number: int = None,
        product: str = None,
    ):
        self.project_id = project_id
        self.page_size = page_size
        self.page_number = page_number
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class ListModelsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListModelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunContactReviewRequest(TeaModel):
    def __init__(
        self,
        contact_scene: str = None,
        contact_path: str = None,
        product: str = None,
    ):
        self.contact_scene = contact_scene
        self.contact_path = contact_path
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_scene is not None:
            result['ContactScene'] = self.contact_scene
        if self.contact_path is not None:
            result['ContactPath'] = self.contact_path
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactScene') is not None:
            self.contact_scene = m.get('ContactScene')
        if m.get('ContactPath') is not None:
            self.contact_path = m.get('ContactPath')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class RunContactReviewResponseBodyContactContentReviewResults(TeaModel):
    def __init__(
        self,
        risk_level: str = None,
        type: str = None,
        value: List[str] = None,
        start_position: List[str] = None,
        modification_suggestion: str = None,
        reason: str = None,
        end_position: List[str] = None,
    ):
        self.risk_level = risk_level
        self.type = type
        self.value = value
        self.start_position = start_position
        self.modification_suggestion = modification_suggestion
        self.reason = reason
        self.end_position = end_position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.start_position is not None:
            result['StartPosition'] = self.start_position
        if self.modification_suggestion is not None:
            result['ModificationSuggestion'] = self.modification_suggestion
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.end_position is not None:
            result['EndPosition'] = self.end_position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('StartPosition') is not None:
            self.start_position = m.get('StartPosition')
        if m.get('ModificationSuggestion') is not None:
            self.modification_suggestion = m.get('ModificationSuggestion')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('EndPosition') is not None:
            self.end_position = m.get('EndPosition')
        return self


class RunContactReviewResponseBodyContactContentStructureResults(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: List[str] = None,
        start_position: List[str] = None,
        name: str = None,
        end_position: List[str] = None,
    ):
        self.type = type
        self.value = value
        self.start_position = start_position
        self.name = name
        self.end_position = end_position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.start_position is not None:
            result['StartPosition'] = self.start_position
        if self.name is not None:
            result['Name'] = self.name
        if self.end_position is not None:
            result['EndPosition'] = self.end_position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('StartPosition') is not None:
            self.start_position = m.get('StartPosition')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EndPosition') is not None:
            self.end_position = m.get('EndPosition')
        return self


class RunContactReviewResponseBodyContactContent(TeaModel):
    def __init__(
        self,
        review_results: List[RunContactReviewResponseBodyContactContentReviewResults] = None,
        structure_results: List[RunContactReviewResponseBodyContactContentStructureResults] = None,
    ):
        self.review_results = review_results
        self.structure_results = structure_results

    def validate(self):
        if self.review_results:
            for k in self.review_results:
                if k:
                    k.validate()
        if self.structure_results:
            for k in self.structure_results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ReviewResults'] = []
        if self.review_results is not None:
            for k in self.review_results:
                result['ReviewResults'].append(k.to_map() if k else None)
        result['StructureResults'] = []
        if self.structure_results is not None:
            for k in self.structure_results:
                result['StructureResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_results = []
        if m.get('ReviewResults') is not None:
            for k in m.get('ReviewResults'):
                temp_model = RunContactReviewResponseBodyContactContentReviewResults()
                self.review_results.append(temp_model.from_map(k))
        self.structure_results = []
        if m.get('StructureResults') is not None:
            for k in m.get('StructureResults'):
                temp_model = RunContactReviewResponseBodyContactContentStructureResults()
                self.structure_results.append(temp_model.from_map(k))
        return self


class RunContactReviewResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        raw_contract_content: str = None,
        contact_content: RunContactReviewResponseBodyContactContent = None,
    ):
        self.request_id = request_id
        self.raw_contract_content = raw_contract_content
        self.contact_content = contact_content

    def validate(self):
        if self.contact_content:
            self.contact_content.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.raw_contract_content is not None:
            result['RawContractContent'] = self.raw_contract_content
        if self.contact_content is not None:
            result['ContactContent'] = self.contact_content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RawContractContent') is not None:
            self.raw_contract_content = m.get('RawContractContent')
        if m.get('ContactContent') is not None:
            temp_model = RunContactReviewResponseBodyContactContent()
            self.contact_content = temp_model.from_map(m['ContactContent'])
        return self


class RunContactReviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunContactReviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunContactReviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunPreTrainServiceRequest(TeaModel):
    def __init__(
        self,
        service_name: str = None,
        service_version: str = None,
        predict_content: str = None,
        product: str = None,
    ):
        self.service_name = service_name
        self.service_version = service_version
        self.predict_content = predict_content
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.predict_content is not None:
            result['PredictContent'] = self.predict_content
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('PredictContent') is not None:
            self.predict_content = m.get('PredictContent')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class RunPreTrainServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        predict_result: str = None,
    ):
        self.request_id = request_id
        self.predict_result = predict_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.predict_result is not None:
            result['PredictResult'] = self.predict_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PredictResult') is not None:
            self.predict_result = m.get('PredictResult')
        return self


class RunPreTrainServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunPreTrainServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunPreTrainServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunSmartCallServiceRequest(TeaModel):
    def __init__(
        self,
        service_name: str = None,
        param_content: str = None,
        robot_id: int = None,
        session_id: str = None,
        product: str = None,
    ):
        self.service_name = service_name
        self.param_content = param_content
        self.robot_id = robot_id
        self.session_id = session_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.param_content is not None:
            result['ParamContent'] = self.param_content
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ParamContent') is not None:
            self.param_content = m.get('ParamContent')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class RunSmartCallServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RunSmartCallServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunSmartCallServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunSmartCallServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


