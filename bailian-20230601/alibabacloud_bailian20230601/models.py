# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


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


