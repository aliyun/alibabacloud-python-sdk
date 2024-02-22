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


class CreateDocumentTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
    ):
        self.agent_key = agent_key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateDocumentTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class CreateDocumentTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDocumentTagResponseBody = None,
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
            temp_model = CreateDocumentTagResponseBody()
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


class DeleteDocRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        doc_id: str = None,
    ):
        self.agent_key = agent_key
        self.doc_id = doc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        return self


class DeleteDocResponseBody(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        request_id: str = None,
    ):
        self.doc_id = doc_id
        # Id of the request
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


class DeleteDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDocResponseBody = None,
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
            temp_model = DeleteDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDocumentTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        tag_id: str = None,
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


class DeleteDocumentTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DeleteDocumentTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDocumentTagResponseBody = None,
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
            temp_model = DeleteDocumentTagResponseBody()
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


class DescribeDocRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        doc_id: str = None,
    ):
        self.agent_key = agent_key
        self.doc_id = doc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        return self


class DescribeDocResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_id: str = None,
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


class DescribeDocResponseBody(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        fail_reason: str = None,
        name: str = None,
        owner_id: str = None,
        request_id: str = None,
        size: str = None,
        status: str = None,
        tags: List[DescribeDocResponseBodyTags] = None,
        type: str = None,
        upload_time: str = None,
    ):
        self.doc_id = doc_id
        self.fail_reason = fail_reason
        self.name = name
        self.owner_id = owner_id
        # Id of the request
        self.request_id = request_id
        self.size = size
        self.status = status
        self.tags = tags
        self.type = type
        self.upload_time = upload_time

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDocResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class DescribeDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDocResponseBody = None,
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
            temp_model = DescribeDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDocumentImportJobRequest(TeaModel):
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


class DescribeDocumentImportJobResponseBodyDocs(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        fail_reason: str = None,
        name: str = None,
        status: str = None,
    ):
        self.doc_id = doc_id
        self.fail_reason = fail_reason
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDocumentImportJobResponseBody(TeaModel):
    def __init__(
        self,
        docs: List[DescribeDocumentImportJobResponseBodyDocs] = None,
        job_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.docs = docs
        # Id of the request
        self.job_id = job_id
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['Docs'].append(k.to_map() if k else None)
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.docs = []
        if m.get('Docs') is not None:
            for k in m.get('Docs'):
                temp_model = DescribeDocumentImportJobResponseBodyDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDocumentImportJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDocumentImportJobResponseBody = None,
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
            temp_model = DescribeDocumentImportJobResponseBody()
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


class GetText2ImageJobRequest(TeaModel):
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


class GetText2ImageJobResponseBodyImages(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        url: str = None,
    ):
        self.code = code
        self.message = message
        self.url = url

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
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class GetText2ImageJobResponseBodyTaskMetrics(TeaModel):
    def __init__(
        self,
        failed: int = None,
        succeeded: int = None,
        total: int = None,
    ):
        self.failed = failed
        self.succeeded = succeeded
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetText2ImageJobResponseBodyUsage(TeaModel):
    def __init__(
        self,
        image_count: int = None,
    ):
        self.image_count = image_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        return self


class GetText2ImageJobResponseBody(TeaModel):
    def __init__(
        self,
        images: List[GetText2ImageJobResponseBodyImages] = None,
        request_id: str = None,
        task_id: str = None,
        task_metrics: GetText2ImageJobResponseBodyTaskMetrics = None,
        task_status: str = None,
        usage: List[GetText2ImageJobResponseBodyUsage] = None,
    ):
        self.images = images
        self.request_id = request_id
        self.task_id = task_id
        self.task_metrics = task_metrics
        self.task_status = task_status
        self.usage = usage

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.task_metrics:
            self.task_metrics.validate()
        if self.usage:
            for k in self.usage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_metrics is not None:
            result['TaskMetrics'] = self.task_metrics.to_map()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        result['Usage'] = []
        if self.usage is not None:
            for k in self.usage:
                result['Usage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = GetText2ImageJobResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskMetrics') is not None:
            temp_model = GetText2ImageJobResponseBodyTaskMetrics()
            self.task_metrics = temp_model.from_map(m['TaskMetrics'])
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        self.usage = []
        if m.get('Usage') is not None:
            for k in m.get('Usage'):
                temp_model = GetText2ImageJobResponseBodyUsage()
                self.usage.append(temp_model.from_map(k))
        return self


class GetText2ImageJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetText2ImageJobResponseBody = None,
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
            temp_model = GetText2ImageJobResponseBody()
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


class ListDocsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        store_id: str = None,
        tag_ids: List[str] = None,
    ):
        self.agent_key = agent_key
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
        self.store_id = store_id
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListDocsShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        store_id: str = None,
        tag_ids_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
        self.store_id = store_id
        self.tag_ids_shrink = tag_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')
        return self


class ListDocsResponseBodyDocsTags(TeaModel):
    def __init__(
        self,
        tag_id: str = None,
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


class ListDocsResponseBodyDocs(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        fail_reason: str = None,
        name: str = None,
        owner_id: str = None,
        size: str = None,
        status: str = None,
        tags: List[ListDocsResponseBodyDocsTags] = None,
        type: str = None,
        upload_time: str = None,
    ):
        self.doc_id = doc_id
        self.fail_reason = fail_reason
        self.name = name
        self.owner_id = owner_id
        self.size = size
        self.status = status
        self.tags = tags
        self.type = type
        self.upload_time = upload_time

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListDocsResponseBodyDocsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class ListDocsResponseBody(TeaModel):
    def __init__(
        self,
        docs: List[ListDocsResponseBodyDocs] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.docs = docs
        self.page_no = page_no
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['Docs'].append(k.to_map() if k else None)
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
        self.docs = []
        if m.get('Docs') is not None:
            for k in m.get('Docs'):
                temp_model = ListDocsResponseBodyDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDocsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDocsResponseBody = None,
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
            temp_model = ListDocsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDocumentTagsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        tag_id: str = None,
    ):
        self.agent_key = agent_key
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
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
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListDocumentTagsResponseBodyTagList(TeaModel):
    def __init__(
        self,
        name: str = None,
        tag_id: str = None,
    ):
        self.name = name
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListDocumentTagsResponseBody(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_list: List[ListDocumentTagsResponseBodyTagList] = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.tag_list = tag_list
        self.total = total

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = ListDocumentTagsResponseBodyTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDocumentTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDocumentTagsResponseBody = None,
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
            temp_model = ListDocumentTagsResponseBody()
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


class SubmitDocumentImportJobRequestDocs(TeaModel):
    def __init__(
        self,
        name: str = None,
        owner_id: str = None,
        store_id: str = None,
        tag_ids: List[str] = None,
        type: str = None,
        url: str = None,
    ):
        self.name = name
        self.owner_id = owner_id
        self.store_id = store_id
        self.tag_ids = tag_ids
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class SubmitDocumentImportJobRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        docs: List[SubmitDocumentImportJobRequestDocs] = None,
    ):
        self.agent_key = agent_key
        self.docs = docs

    def validate(self):
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        result['Docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['Docs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        self.docs = []
        if m.get('Docs') is not None:
            for k in m.get('Docs'):
                temp_model = SubmitDocumentImportJobRequestDocs()
                self.docs.append(temp_model.from_map(k))
        return self


class SubmitDocumentImportJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        # Id of the request
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


class SubmitDocumentImportJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocumentImportJobResponseBody = None,
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
            temp_model = SubmitDocumentImportJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitText2ImageJobRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        app_id: str = None,
        n: int = None,
        negative_prompt: str = None,
        prompt: str = None,
        seed: int = None,
        size: str = None,
        style: str = None,
    ):
        self.agent_key = agent_key
        self.app_id = app_id
        self.n = n
        self.negative_prompt = negative_prompt
        self.prompt = prompt
        self.seed = seed
        self.size = size
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.n is not None:
            result['N'] = self.n
        if self.negative_prompt is not None:
            result['NegativePrompt'] = self.negative_prompt
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.size is not None:
            result['Size'] = self.size
        if self.style is not None:
            result['Style'] = self.style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('NegativePrompt') is not None:
            self.negative_prompt = m.get('NegativePrompt')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        return self


class SubmitText2ImageJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class SubmitText2ImageJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitText2ImageJobResponseBody = None,
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
            temp_model = SubmitText2ImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDocAttributeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        del_all_tags: bool = None,
        doc_id: str = None,
        name: str = None,
        tag_ids: List[str] = None,
    ):
        self.agent_key = agent_key
        self.del_all_tags = del_all_tags
        self.doc_id = doc_id
        self.name = name
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.del_all_tags is not None:
            result['DelAllTags'] = self.del_all_tags
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DelAllTags') is not None:
            self.del_all_tags = m.get('DelAllTags')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class UpdateDocAttributeShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        del_all_tags: bool = None,
        doc_id: str = None,
        name: str = None,
        tag_ids_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.del_all_tags = del_all_tags
        self.doc_id = doc_id
        self.name = name
        self.tag_ids_shrink = tag_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.del_all_tags is not None:
            result['DelAllTags'] = self.del_all_tags
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DelAllTags') is not None:
            self.del_all_tags = m.get('DelAllTags')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')
        return self


class UpdateDocAttributeResponseBody(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        request_id: str = None,
    ):
        self.doc_id = doc_id
        # Id of the request
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


class UpdateDocAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDocAttributeResponseBody = None,
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
            temp_model = UpdateDocAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDocumentTagRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        tag_id: str = None,
    ):
        self.agent_key = agent_key
        self.name = name
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
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class UpdateDocumentTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class UpdateDocumentTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDocumentTagResponseBody = None,
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
            temp_model = UpdateDocumentTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


