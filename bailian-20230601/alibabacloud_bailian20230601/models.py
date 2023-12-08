# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddEnterpriseTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        tag_name: str = None,
    ):
        self.agent_key = agent_key
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class AddEnterpriseTagResponseBodyData(TeaModel):
    def __init__(
        self,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class AddEnterpriseTagResponseBody(TeaModel):
    def __init__(
        self,
        data: AddEnterpriseTagResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AddEnterpriseTagResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddEnterpriseTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddEnterpriseTagResponseBody = None,
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
            temp_model = AddEnterpriseTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelFineTuneJobRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        job_id: str = None,
    ):
        self.agent_key = agent_key
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CancelFineTuneJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelFineTuneJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelFineTuneJobResponseBody = None,
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
            temp_model = CancelFineTuneJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFineTuneJobRequestHyperParameters(TeaModel):
    def __init__(
        self,
        batch_size: int = None,
        epochs: int = None,
        learning_rate: str = None,
        prompt_loss_weight: float = None,
    ):
        self.batch_size = batch_size
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.prompt_loss_weight = prompt_loss_weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.epochs is not None:
            result['Epochs'] = self.epochs
        if self.learning_rate is not None:
            result['LearningRate'] = self.learning_rate
        if self.prompt_loss_weight is not None:
            result['PromptLossWeight'] = self.prompt_loss_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Epochs') is not None:
            self.epochs = m.get('Epochs')
        if m.get('LearningRate') is not None:
            self.learning_rate = m.get('LearningRate')
        if m.get('PromptLossWeight') is not None:
            self.prompt_loss_weight = m.get('PromptLossWeight')
        return self


class CreateFineTuneJobRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        base_model: str = None,
        hyper_parameters: CreateFineTuneJobRequestHyperParameters = None,
        model_name: str = None,
        training_files: List[str] = None,
        training_type: str = None,
        validation_files: List[str] = None,
    ):
        self.agent_key = agent_key
        self.base_model = base_model
        self.hyper_parameters = hyper_parameters
        self.model_name = model_name
        self.training_files = training_files
        self.training_type = training_type
        self.validation_files = validation_files

    def validate(self):
        if self.hyper_parameters:
            self.hyper_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.base_model is not None:
            result['BaseModel'] = self.base_model
        if self.hyper_parameters is not None:
            result['HyperParameters'] = self.hyper_parameters.to_map()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.training_files is not None:
            result['TrainingFiles'] = self.training_files
        if self.training_type is not None:
            result['TrainingType'] = self.training_type
        if self.validation_files is not None:
            result['ValidationFiles'] = self.validation_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BaseModel') is not None:
            self.base_model = m.get('BaseModel')
        if m.get('HyperParameters') is not None:
            temp_model = CreateFineTuneJobRequestHyperParameters()
            self.hyper_parameters = temp_model.from_map(m['HyperParameters'])
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('TrainingFiles') is not None:
            self.training_files = m.get('TrainingFiles')
        if m.get('TrainingType') is not None:
            self.training_type = m.get('TrainingType')
        if m.get('ValidationFiles') is not None:
            self.validation_files = m.get('ValidationFiles')
        return self


class CreateFineTuneJobShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        base_model: str = None,
        hyper_parameters_shrink: str = None,
        model_name: str = None,
        training_files_shrink: str = None,
        training_type: str = None,
        validation_files_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.base_model = base_model
        self.hyper_parameters_shrink = hyper_parameters_shrink
        self.model_name = model_name
        self.training_files_shrink = training_files_shrink
        self.training_type = training_type
        self.validation_files_shrink = validation_files_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.base_model is not None:
            result['BaseModel'] = self.base_model
        if self.hyper_parameters_shrink is not None:
            result['HyperParameters'] = self.hyper_parameters_shrink
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.training_files_shrink is not None:
            result['TrainingFiles'] = self.training_files_shrink
        if self.training_type is not None:
            result['TrainingType'] = self.training_type
        if self.validation_files_shrink is not None:
            result['ValidationFiles'] = self.validation_files_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BaseModel') is not None:
            self.base_model = m.get('BaseModel')
        if m.get('HyperParameters') is not None:
            self.hyper_parameters_shrink = m.get('HyperParameters')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('TrainingFiles') is not None:
            self.training_files_shrink = m.get('TrainingFiles')
        if m.get('TrainingType') is not None:
            self.training_type = m.get('TrainingType')
        if m.get('ValidationFiles') is not None:
            self.validation_files_shrink = m.get('ValidationFiles')
        return self


class CreateFineTuneJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateFineTuneJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFineTuneJobResponseBody = None,
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
            temp_model = CreateFineTuneJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        model: str = None,
    ):
        self.agent_key = agent_key
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        model_service_id: str = None,
        request_id: str = None,
    ):
        self.model_service_id = model_service_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceResponseBody = None,
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTextEmbeddingsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        input: List[str] = None,
        text_type: str = None,
    ):
        self.agent_key = agent_key
        self.input = input
        self.text_type = text_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.input is not None:
            result['Input'] = self.input
        if self.text_type is not None:
            result['TextType'] = self.text_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('TextType') is not None:
            self.text_type = m.get('TextType')
        return self


class CreateTextEmbeddingsShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        input_shrink: str = None,
        text_type: str = None,
    ):
        self.agent_key = agent_key
        self.input_shrink = input_shrink
        self.text_type = text_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.text_type is not None:
            result['TextType'] = self.text_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('TextType') is not None:
            self.text_type = m.get('TextType')
        return self


class CreateTextEmbeddingsResponseBodyDataEmbeddings(TeaModel):
    def __init__(
        self,
        embedding: List[float] = None,
        text_index: int = None,
    ):
        self.embedding = embedding
        self.text_index = text_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embedding is not None:
            result['Embedding'] = self.embedding
        if self.text_index is not None:
            result['TextIndex'] = self.text_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Embedding') is not None:
            self.embedding = m.get('Embedding')
        if m.get('TextIndex') is not None:
            self.text_index = m.get('TextIndex')
        return self


class CreateTextEmbeddingsResponseBodyData(TeaModel):
    def __init__(
        self,
        embeddings: List[CreateTextEmbeddingsResponseBodyDataEmbeddings] = None,
    ):
        self.embeddings = embeddings

    def validate(self):
        if self.embeddings:
            for k in self.embeddings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Embeddings'] = []
        if self.embeddings is not None:
            for k in self.embeddings:
                result['Embeddings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.embeddings = []
        if m.get('Embeddings') is not None:
            for k in m.get('Embeddings'):
                temp_model = CreateTextEmbeddingsResponseBodyDataEmbeddings()
                self.embeddings.append(temp_model.from_map(k))
        return self


class CreateTextEmbeddingsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTextEmbeddingsResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateTextEmbeddingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTextEmbeddingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTextEmbeddingsResponseBody = None,
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
            temp_model = CreateTextEmbeddingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTokenRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class CreateTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        expired_time: int = None,
        token: str = None,
    ):
        self.expired_time = expired_time
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTokenResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTokenResponseBody = None,
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
            temp_model = CreateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelEnterpriseTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        tag_id: int = None,
    ):
        self.agent_key = agent_key
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DelEnterpriseTagResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DelEnterpriseTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DelEnterpriseTagResponseBody = None,
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
            temp_model = DelEnterpriseTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnterpriseDataRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class DeleteEnterpriseDataResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEnterpriseDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEnterpriseDataResponseBody = None,
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
            temp_model = DeleteEnterpriseDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFineTuneJobRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        job_id: str = None,
    ):
        self.agent_key = agent_key
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteFineTuneJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFineTuneJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFineTuneJobResponseBody = None,
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
            temp_model = DeleteFineTuneJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        model_service_id: str = None,
    ):
        self.agent_key = agent_key
        self.model_service_id = model_service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(
        self,
        model_service_id: str = None,
        request_id: str = None,
    ):
        self.model_service_id = model_service_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceResponseBody = None,
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFineTuneJobRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        job_id: str = None,
    ):
        self.agent_key = agent_key
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeFineTuneJobResponseBodyHyperParameters(TeaModel):
    def __init__(
        self,
        batch_size: int = None,
        epochs: int = None,
        learning_rate: str = None,
        prompt_loss_weight: float = None,
    ):
        self.batch_size = batch_size
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.prompt_loss_weight = prompt_loss_weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.epochs is not None:
            result['Epochs'] = self.epochs
        if self.learning_rate is not None:
            result['LearningRate'] = self.learning_rate
        if self.prompt_loss_weight is not None:
            result['PromptLossWeight'] = self.prompt_loss_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Epochs') is not None:
            self.epochs = m.get('Epochs')
        if m.get('LearningRate') is not None:
            self.learning_rate = m.get('LearningRate')
        if m.get('PromptLossWeight') is not None:
            self.prompt_loss_weight = m.get('PromptLossWeight')
        return self


class DescribeFineTuneJobResponseBody(TeaModel):
    def __init__(
        self,
        base_model: str = None,
        fine_tuned_model: str = None,
        hyper_parameters: DescribeFineTuneJobResponseBodyHyperParameters = None,
        job_id: str = None,
        message: str = None,
        model_name: str = None,
        request_id: str = None,
        status: str = None,
        training_files: List[str] = None,
        training_type: str = None,
        validation_files: List[str] = None,
    ):
        self.base_model = base_model
        self.fine_tuned_model = fine_tuned_model
        self.hyper_parameters = hyper_parameters
        self.job_id = job_id
        self.message = message
        self.model_name = model_name
        self.request_id = request_id
        self.status = status
        self.training_files = training_files
        self.training_type = training_type
        self.validation_files = validation_files

    def validate(self):
        if self.hyper_parameters:
            self.hyper_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_model is not None:
            result['BaseModel'] = self.base_model
        if self.fine_tuned_model is not None:
            result['FineTunedModel'] = self.fine_tuned_model
        if self.hyper_parameters is not None:
            result['HyperParameters'] = self.hyper_parameters.to_map()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.training_files is not None:
            result['TrainingFiles'] = self.training_files
        if self.training_type is not None:
            result['TrainingType'] = self.training_type
        if self.validation_files is not None:
            result['ValidationFiles'] = self.validation_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseModel') is not None:
            self.base_model = m.get('BaseModel')
        if m.get('FineTunedModel') is not None:
            self.fine_tuned_model = m.get('FineTunedModel')
        if m.get('HyperParameters') is not None:
            temp_model = DescribeFineTuneJobResponseBodyHyperParameters()
            self.hyper_parameters = temp_model.from_map(m['HyperParameters'])
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingFiles') is not None:
            self.training_files = m.get('TrainingFiles')
        if m.get('TrainingType') is not None:
            self.training_type = m.get('TrainingType')
        if m.get('ValidationFiles') is not None:
            self.validation_files = m.get('ValidationFiles')
        return self


class DescribeFineTuneJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFineTuneJobResponseBody = None,
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
            temp_model = DescribeFineTuneJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        model_service_id: str = None,
    ):
        self.agent_key = agent_key
        self.model_service_id = model_service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')
        return self


class DescribeServiceResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_service_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.app_id = app_id
        self.model_service_id = model_service_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceResponseBody = None,
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
            temp_model = DescribeServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDataByDataIdRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
        owner_id: int = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetEnterpriseDataByDataIdResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        data_name: str = None,
        data_size: str = None,
        data_status: str = None,
        data_status_code: int = None,
        data_type: str = None,
        data_type_code: int = None,
        status_detail: str = None,
        store_type: str = None,
        tags: str = None,
        upload_time: str = None,
    ):
        self.data_id = data_id
        self.data_name = data_name
        self.data_size = data_size
        self.data_status = data_status
        self.data_status_code = data_status_code
        self.data_type = data_type
        self.data_type_code = data_type_code
        self.status_detail = status_detail
        self.store_type = store_type
        self.tags = tags
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.data_name is not None:
            result['DataName'] = self.data_name
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data_status is not None:
            result['DataStatus'] = self.data_status
        if self.data_status_code is not None:
            result['DataStatusCode'] = self.data_status_code
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_type_code is not None:
            result['DataTypeCode'] = self.data_type_code
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.store_type is not None:
            result['StoreType'] = self.store_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DataStatus') is not None:
            self.data_status = m.get('DataStatus')
        if m.get('DataStatusCode') is not None:
            self.data_status_code = m.get('DataStatusCode')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataTypeCode') is not None:
            self.data_type_code = m.get('DataTypeCode')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class GetEnterpriseDataByDataIdResponseBody(TeaModel):
    def __init__(
        self,
        data: GetEnterpriseDataByDataIdResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetEnterpriseDataByDataIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEnterpriseDataByDataIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnterpriseDataByDataIdResponseBody = None,
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
            temp_model = GetEnterpriseDataByDataIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDataChunkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetEnterpriseDataChunkResponseBodyData(TeaModel):
    def __init__(
        self,
        text: str = None,
        title: str = None,
        title_path: str = None,
    ):
        self.text = text
        self.title = title
        self.title_path = title_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.title_path is not None:
            result['TitlePath'] = self.title_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TitlePath') is not None:
            self.title_path = m.get('TitlePath')
        return self


class GetEnterpriseDataChunkResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetEnterpriseDataChunkResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetEnterpriseDataChunkResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEnterpriseDataChunkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnterpriseDataChunkResponseBody = None,
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
            temp_model = GetEnterpriseDataChunkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDataPageImageRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetEnterpriseDataPageImageResponseBodyData(TeaModel):
    def __init__(
        self,
        height: int = None,
        image_url: str = None,
        page_id: str = None,
        width: int = None,
    ):
        self.height = height
        self.image_url = image_url
        self.page_id = page_id
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.page_id is not None:
            result['PageId'] = self.page_id
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetEnterpriseDataPageImageResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetEnterpriseDataPageImageResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetEnterpriseDataPageImageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEnterpriseDataPageImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnterpriseDataPageImageResponseBody = None,
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
            temp_model = GetEnterpriseDataPageImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDataParseResultRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetEnterpriseDataParseResultResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEnterpriseDataParseResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnterpriseDataParseResultResponseBody = None,
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
            temp_model = GetEnterpriseDataParseResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileStoreUploadPolicyRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        file_name: str = None,
        file_store_id: int = None,
        user_id: str = None,
    ):
        self.agent_key = agent_key
        self.file_name = file_name
        self.file_store_id = file_store_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_store_id is not None:
            result['FileStoreId'] = self.file_store_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStoreId') is not None:
            self.file_store_id = m.get('FileStoreId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetFileStoreUploadPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.key = key
        self.policy = policy
        self.security_token = security_token
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.key is not None:
            result['Key'] = self.key
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetFileStoreUploadPolicyResponseBody(TeaModel):
    def __init__(
        self,
        data: GetFileStoreUploadPolicyResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetFileStoreUploadPolicyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFileStoreUploadPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileStoreUploadPolicyResponseBody = None,
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
            temp_model = GetFileStoreUploadPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImportTaskResultRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        self.agent_key = agent_key
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetImportTaskResultResponseBodyDataDetails(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        data_name: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        self.data_id = data_id
        self.data_name = data_name
        self.error_msg = error_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.data_name is not None:
            result['DataName'] = self.data_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImportTaskResultResponseBodyData(TeaModel):
    def __init__(
        self,
        details: List[GetImportTaskResultResponseBodyDataDetails] = None,
        task_id: str = None,
        task_status: int = None,
        task_status_text: str = None,
    ):
        self.details = details
        self.task_id = task_id
        self.task_status = task_status
        self.task_status_text = task_status_text

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_text is not None:
            result['TaskStatusText'] = self.task_status_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = GetImportTaskResultResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusText') is not None:
            self.task_status_text = m.get('TaskStatusText')
        return self


class GetImportTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetImportTaskResultResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetImportTaskResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImportTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImportTaskResultResponseBody = None,
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
            temp_model = GetImportTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPromptRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        prompt_id: str = None,
        vars: str = None,
    ):
        self.agent_key = agent_key
        self.prompt_id = prompt_id
        self.vars = vars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.prompt_id is not None:
            result['PromptId'] = self.prompt_id
        if self.vars is not None:
            result['Vars'] = self.vars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PromptId') is not None:
            self.prompt_id = m.get('PromptId')
        if m.get('Vars') is not None:
            self.vars = m.get('Vars')
        return self


class GetPromptResponseBodyData(TeaModel):
    def __init__(
        self,
        prompt_content: str = None,
        prompt_id: str = None,
    ):
        self.prompt_content = prompt_content
        self.prompt_id = prompt_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt_content is not None:
            result['PromptContent'] = self.prompt_content
        if self.prompt_id is not None:
            result['PromptId'] = self.prompt_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromptContent') is not None:
            self.prompt_content = m.get('PromptContent')
        if m.get('PromptId') is not None:
            self.prompt_id = m.get('PromptId')
        return self


class GetPromptResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPromptResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPromptResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPromptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPromptResponseBody = None,
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
            temp_model = GetPromptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportEnterpriseDocumentRequestDocumentList(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        file_can_download: bool = None,
        file_link: str = None,
        file_name: str = None,
        file_preview_link: str = None,
    ):
        self.biz_id = biz_id
        self.file_can_download = file_can_download
        self.file_link = file_link
        self.file_name = file_name
        self.file_preview_link = file_preview_link

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.file_can_download is not None:
            result['FileCanDownload'] = self.file_can_download
        if self.file_link is not None:
            result['FileLink'] = self.file_link
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_preview_link is not None:
            result['FilePreviewLink'] = self.file_preview_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FileCanDownload') is not None:
            self.file_can_download = m.get('FileCanDownload')
        if m.get('FileLink') is not None:
            self.file_link = m.get('FileLink')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePreviewLink') is not None:
            self.file_preview_link = m.get('FilePreviewLink')
        return self


class ImportEnterpriseDocumentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_type: int = None,
        document_list: List[ImportEnterpriseDocumentRequestDocumentList] = None,
        owner_id: int = None,
        store_id: int = None,
        tags: List[str] = None,
    ):
        self.agent_key = agent_key
        self.data_type = data_type
        self.document_list = document_list
        self.owner_id = owner_id
        self.store_id = store_id
        self.tags = tags

    def validate(self):
        if self.document_list:
            for k in self.document_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_type is not None:
            result['DataType'] = self.data_type
        result['DocumentList'] = []
        if self.document_list is not None:
            for k in self.document_list:
                result['DocumentList'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        self.document_list = []
        if m.get('DocumentList') is not None:
            for k in m.get('DocumentList'):
                temp_model = ImportEnterpriseDocumentRequestDocumentList()
                self.document_list.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ImportEnterpriseDocumentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_type: int = None,
        document_list_shrink: str = None,
        owner_id: int = None,
        store_id: int = None,
        tags_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.data_type = data_type
        self.document_list_shrink = document_list_shrink
        self.owner_id = owner_id
        self.store_id = store_id
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.document_list_shrink is not None:
            result['DocumentList'] = self.document_list_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DocumentList') is not None:
            self.document_list_shrink = m.get('DocumentList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ImportEnterpriseDocumentResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportEnterpriseDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportEnterpriseDocumentResponseBody = None,
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
            temp_model = ImportEnterpriseDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportUserDocumentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        file_name: str = None,
        file_store_id: int = None,
        oss_path: str = None,
        store_id: int = None,
        user_id: str = None,
    ):
        self.agent_key = agent_key
        self.file_name = file_name
        self.file_store_id = file_store_id
        self.oss_path = oss_path
        self.store_id = store_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_store_id is not None:
            result['FileStoreId'] = self.file_store_id
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStoreId') is not None:
            self.file_store_id = m.get('FileStoreId')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ImportUserDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        data_status: int = None,
    ):
        self.data_id = data_id
        self.data_status = data_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.data_status is not None:
            result['DataStatus'] = self.data_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DataStatus') is not None:
            self.data_status = m.get('DataStatus')
        return self


class ImportUserDocumentResponseBody(TeaModel):
    def __init__(
        self,
        data: ImportUserDocumentResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ImportUserDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportUserDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportUserDocumentResponseBody = None,
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
            temp_model = ImportUserDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFineTuneJobsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFineTuneJobsResponseBodyJobsHyperParameters(TeaModel):
    def __init__(
        self,
        batch_size: int = None,
        epochs: int = None,
        learning_rate: str = None,
        prompt_loss_weight: float = None,
    ):
        self.batch_size = batch_size
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.prompt_loss_weight = prompt_loss_weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.epochs is not None:
            result['Epochs'] = self.epochs
        if self.learning_rate is not None:
            result['LearningRate'] = self.learning_rate
        if self.prompt_loss_weight is not None:
            result['PromptLossWeight'] = self.prompt_loss_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Epochs') is not None:
            self.epochs = m.get('Epochs')
        if m.get('LearningRate') is not None:
            self.learning_rate = m.get('LearningRate')
        if m.get('PromptLossWeight') is not None:
            self.prompt_loss_weight = m.get('PromptLossWeight')
        return self


class ListFineTuneJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        base_model: str = None,
        fine_tuned_model: str = None,
        hyper_parameters: ListFineTuneJobsResponseBodyJobsHyperParameters = None,
        job_id: str = None,
        message: str = None,
        model_name: str = None,
        status: str = None,
        training_files: List[str] = None,
        training_type: str = None,
        validation_files: List[str] = None,
    ):
        self.base_model = base_model
        self.fine_tuned_model = fine_tuned_model
        self.hyper_parameters = hyper_parameters
        self.job_id = job_id
        self.message = message
        self.model_name = model_name
        self.status = status
        self.training_files = training_files
        self.training_type = training_type
        self.validation_files = validation_files

    def validate(self):
        if self.hyper_parameters:
            self.hyper_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_model is not None:
            result['BaseModel'] = self.base_model
        if self.fine_tuned_model is not None:
            result['FineTunedModel'] = self.fine_tuned_model
        if self.hyper_parameters is not None:
            result['HyperParameters'] = self.hyper_parameters.to_map()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.status is not None:
            result['Status'] = self.status
        if self.training_files is not None:
            result['TrainingFiles'] = self.training_files
        if self.training_type is not None:
            result['TrainingType'] = self.training_type
        if self.validation_files is not None:
            result['ValidationFiles'] = self.validation_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseModel') is not None:
            self.base_model = m.get('BaseModel')
        if m.get('FineTunedModel') is not None:
            self.fine_tuned_model = m.get('FineTunedModel')
        if m.get('HyperParameters') is not None:
            temp_model = ListFineTuneJobsResponseBodyJobsHyperParameters()
            self.hyper_parameters = temp_model.from_map(m['HyperParameters'])
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingFiles') is not None:
            self.training_files = m.get('TrainingFiles')
        if m.get('TrainingType') is not None:
            self.training_type = m.get('TrainingType')
        if m.get('ValidationFiles') is not None:
            self.validation_files = m.get('ValidationFiles')
        return self


class ListFineTuneJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[ListFineTuneJobsResponseBodyJobs] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.jobs = jobs
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListFineTuneJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFineTuneJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFineTuneJobsResponseBody = None,
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
            temp_model = ListFineTuneJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListServicesResponseBodyModelServices(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_service_id: str = None,
        status: str = None,
    ):
        self.app_id = app_id
        self.model_service_id = model_service_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        model_services: List[ListServicesResponseBodyModelServices] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.model_services = model_services
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.model_services:
            for k in self.model_services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModelServices'] = []
        if self.model_services is not None:
            for k in self.model_services:
                result['ModelServices'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_services = []
        if m.get('ModelServices') is not None:
            for k in m.get('ModelServices'):
                temp_model = ListServicesResponseBodyModelServices()
                self.model_services.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEnterpriseDataListRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_name: str = None,
        page_no: int = None,
        page_size: int = None,
        store_type: str = None,
        tags: List[str] = None,
    ):
        self.agent_key = agent_key
        self.data_name = data_name
        self.page_no = page_no
        self.page_size = page_size
        self.store_type = store_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_name is not None:
            result['DataName'] = self.data_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_type is not None:
            result['StoreType'] = self.store_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class QueryEnterpriseDataListShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_name: str = None,
        page_no: int = None,
        page_size: int = None,
        store_type: str = None,
        tags_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.data_name = data_name
        self.page_no = page_no
        self.page_size = page_size
        self.store_type = store_type
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_name is not None:
            result['DataName'] = self.data_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_type is not None:
            result['StoreType'] = self.store_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class QueryEnterpriseDataListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        data_name: str = None,
        data_size: str = None,
        data_status: str = None,
        data_status_code: int = None,
        data_type: str = None,
        data_type_code: int = None,
        status_detail: str = None,
        store_type: str = None,
        tags: str = None,
        upload_time: str = None,
    ):
        self.data_id = data_id
        self.data_name = data_name
        self.data_size = data_size
        self.data_status = data_status
        self.data_status_code = data_status_code
        self.data_type = data_type
        self.data_type_code = data_type_code
        self.status_detail = status_detail
        self.store_type = store_type
        self.tags = tags
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.data_name is not None:
            result['DataName'] = self.data_name
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data_status is not None:
            result['DataStatus'] = self.data_status
        if self.data_status_code is not None:
            result['DataStatusCode'] = self.data_status_code
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_type_code is not None:
            result['DataTypeCode'] = self.data_type_code
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.store_type is not None:
            result['StoreType'] = self.store_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DataStatus') is not None:
            self.data_status = m.get('DataStatus')
        if m.get('DataStatusCode') is not None:
            self.data_status_code = m.get('DataStatusCode')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataTypeCode') is not None:
            self.data_type_code = m.get('DataTypeCode')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class QueryEnterpriseDataListResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryEnterpriseDataListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEnterpriseDataListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryEnterpriseDataListResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryEnterpriseDataListResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryEnterpriseDataListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEnterpriseDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEnterpriseDataListResponseBody = None,
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
            temp_model = QueryEnterpriseDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEnterpriseDataTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class QueryEnterpriseDataTagResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.data_id = data_id
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class QueryEnterpriseDataTagResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryEnterpriseDataTagResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryEnterpriseDataTagResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEnterpriseDataTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEnterpriseDataTagResponseBody = None,
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
            temp_model = QueryEnterpriseDataTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEnterpriseTagListRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryEnterpriseTagListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class QueryEnterpriseTagListResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryEnterpriseTagListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEnterpriseTagListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryEnterpriseTagListResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryEnterpriseTagListResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryEnterpriseTagListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEnterpriseTagListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEnterpriseTagListResponseBody = None,
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
            temp_model = QueryEnterpriseTagListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserDocumentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
        user_id: str = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryUserDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        data_status: int = None,
    ):
        self.data_id = data_id
        self.data_status = data_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.data_status is not None:
            result['DataStatus'] = self.data_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DataStatus') is not None:
            self.data_status = m.get('DataStatus')
        return self


class QueryUserDocumentResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryUserDocumentResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryUserDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserDocumentResponseBody = None,
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
            temp_model = QueryUserDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEnterpriseDataRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id_list: List[str] = None,
        enable_rank: bool = None,
        owner_id: int = None,
        query: str = None,
        store_id: int = None,
        tag_id_list: List[int] = None,
    ):
        self.agent_key = agent_key
        self.data_id_list = data_id_list
        self.enable_rank = enable_rank
        self.owner_id = owner_id
        self.query = query
        self.store_id = store_id
        self.tag_id_list = tag_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id_list is not None:
            result['DataIdList'] = self.data_id_list
        if self.enable_rank is not None:
            result['EnableRank'] = self.enable_rank
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.query is not None:
            result['Query'] = self.query
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataIdList') is not None:
            self.data_id_list = m.get('DataIdList')
        if m.get('EnableRank') is not None:
            self.enable_rank = m.get('EnableRank')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        return self


class SearchEnterpriseDataShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id_list_shrink: str = None,
        enable_rank: bool = None,
        owner_id: int = None,
        query: str = None,
        store_id: int = None,
        tag_id_list_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.data_id_list_shrink = data_id_list_shrink
        self.enable_rank = enable_rank
        self.owner_id = owner_id
        self.query = query
        self.store_id = store_id
        self.tag_id_list_shrink = tag_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id_list_shrink is not None:
            result['DataIdList'] = self.data_id_list_shrink
        if self.enable_rank is not None:
            result['EnableRank'] = self.enable_rank
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.query is not None:
            result['Query'] = self.query
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.tag_id_list_shrink is not None:
            result['TagIdList'] = self.tag_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataIdList') is not None:
            self.data_id_list_shrink = m.get('DataIdList')
        if m.get('EnableRank') is not None:
            self.enable_rank = m.get('EnableRank')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('TagIdList') is not None:
            self.tag_id_list_shrink = m.get('TagIdList')
        return self


class SearchEnterpriseDataResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        data_name: str = None,
        score: str = None,
        source: str = None,
        text: str = None,
        title: str = None,
        title_path: str = None,
    ):
        self.data_id = data_id
        self.data_name = data_name
        self.score = score
        self.source = source
        self.text = text
        self.title = title
        self.title_path = title_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.data_name is not None:
            result['DataName'] = self.data_name
        if self.score is not None:
            result['Score'] = self.score
        if self.source is not None:
            result['Source'] = self.source
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.title_path is not None:
            result['TitlePath'] = self.title_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TitlePath') is not None:
            self.title_path = m.get('TitlePath')
        return self


class SearchEnterpriseDataResponseBody(TeaModel):
    def __init__(
        self,
        data: List[SearchEnterpriseDataResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchEnterpriseDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchEnterpriseDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchEnterpriseDataResponseBody = None,
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
            temp_model = SearchEnterpriseDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnterpriseDataInfoRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_id: str = None,
        data_id: str = None,
        data_name: str = None,
        file_preview_link: str = None,
    ):
        self.agent_key = agent_key
        self.biz_id = biz_id
        self.data_id = data_id
        self.data_name = data_name
        self.file_preview_link = file_preview_link

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.data_name is not None:
            result['DataName'] = self.data_name
        if self.file_preview_link is not None:
            result['FilePreviewLink'] = self.file_preview_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')
        if m.get('FilePreviewLink') is not None:
            self.file_preview_link = m.get('FilePreviewLink')
        return self


class UpdateEnterpriseDataInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEnterpriseDataInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnterpriseDataInfoResponseBody = None,
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
            temp_model = UpdateEnterpriseDataInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnterpriseDataTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
        tags: List[int] = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateEnterpriseDataTagShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        data_id: str = None,
        tags_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.data_id = data_id
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdateEnterpriseDataTagResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEnterpriseDataTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnterpriseDataTagResponseBody = None,
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
            temp_model = UpdateEnterpriseDataTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnterpriseTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.agent_key = agent_key
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class UpdateEnterpriseTagResponseBodyData(TeaModel):
    def __init__(
        self,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class UpdateEnterpriseTagResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateEnterpriseTagResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateEnterpriseTagResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEnterpriseTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnterpriseTagResponseBody = None,
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
            temp_model = UpdateEnterpriseTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


