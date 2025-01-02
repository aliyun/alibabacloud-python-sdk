# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class OpenApiMultiResponseDataInferenceJobList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        prompt_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        self.prompt_id = prompt_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id
        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')
        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')
        return self


class OpenApiMultiResponseData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        image_url: List[str] = None,
        inference_image_count: int = None,
        inference_job_list: List[OpenApiMultiResponseDataInferenceJobList] = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        name: str = None,
        object_type: str = None,
    ):
        self.create_time = create_time
        self.id = id
        self.image_url = image_url
        self.inference_image_count = inference_image_count
        self.inference_job_list = inference_job_list
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        self.name = name
        self.object_type = object_type

    def validate(self):
        if self.inference_job_list:
            for k in self.inference_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.inference_image_count is not None:
            result['inferenceImageCount'] = self.inference_image_count
        result['inferenceJobList'] = []
        if self.inference_job_list is not None:
            for k in self.inference_job_list:
                result['inferenceJobList'].append(k.to_map() if k else None)
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.object_type is not None:
            result['objectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('inferenceImageCount') is not None:
            self.inference_image_count = m.get('inferenceImageCount')
        self.inference_job_list = []
        if m.get('inferenceJobList') is not None:
            for k in m.get('inferenceJobList'):
                temp_model = OpenApiMultiResponseDataInferenceJobList()
                self.inference_job_list.append(temp_model.from_map(k))
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        return self


class OpenApiMultiResponse(TeaModel):
    def __init__(
        self,
        data: List[OpenApiMultiResponseData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = OpenApiMultiResponseData()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class OpenApiSingleResponseData(TeaModel):
    def __init__(
        self,
        model_train_status: str = None,
    ):
        self.model_train_status = model_train_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_train_status is not None:
            result['modelTrainStatus'] = self.model_train_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelTrainStatus') is not None:
            self.model_train_status = m.get('modelTrainStatus')
        return self


class OpenApiSingleResponse(TeaModel):
    def __init__(
        self,
        data: OpenApiSingleResponseData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = OpenApiSingleResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class Personalizedtxt2imgAddInferenceJobCmd(TeaModel):
    def __init__(
        self,
        image_number: int = None,
        model_id: str = None,
        prompt: str = None,
        seed: int = None,
    ):
        self.image_number = image_number
        # This parameter is required.
        self.model_id = model_id
        # This parameter is required.
        self.prompt = prompt
        self.seed = seed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_number is not None:
            result['imageNumber'] = self.image_number
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.seed is not None:
            result['seed'] = self.seed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageNumber') is not None:
            self.image_number = m.get('imageNumber')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('seed') is not None:
            self.seed = m.get('seed')
        return self


class Personalizedtxt2imgAddModelTrainJobCmd(TeaModel):
    def __init__(
        self,
        image_url: List[str] = None,
        name: str = None,
        object_type: str = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.name is not None:
            result['name'] = self.name
        if self.object_type is not None:
            result['objectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        return self


class Personalizedtxt2imgInferenceJobInfoDTO(TeaModel):
    def __init__(
        self,
        create_user_id: str = None,
        id: str = None,
        job_status: str = None,
        model_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_user_id = create_user_id
        self.id = id
        self.job_status = job_status
        self.model_id = model_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_user_id is not None:
            result['createUserId'] = self.create_user_id
        if self.id is not None:
            result['id'] = self.id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createUserId') is not None:
            self.create_user_id = m.get('createUserId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')
        return self


class Personalizedtxt2imgModelTrainJobInfoDTO(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        image_url: List[str] = None,
        inference_job_list: List[Personalizedtxt2imgInferenceJobInfoDTO] = None,
        job_status: str = None,
        name: str = None,
        object_type: str = None,
        id: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.image_url = image_url
        self.inference_job_list = inference_job_list
        self.job_status = job_status
        self.name = name
        self.object_type = object_type
        self.id = id

    def validate(self):
        if self.inference_job_list:
            for k in self.inference_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        result['InferenceJobList'] = []
        if self.inference_job_list is not None:
            for k in self.inference_job_list:
                result['InferenceJobList'].append(k.to_map() if k else None)
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.name is not None:
            result['Name'] = self.name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        self.inference_job_list = []
        if m.get('InferenceJobList') is not None:
            for k in m.get('InferenceJobList'):
                temp_model = Personalizedtxt2imgInferenceJobInfoDTO()
                self.inference_job_list.append(temp_model.from_map(k))
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class AITeacherExpansionPracticeTaskGenerateRequest(TeaModel):
    def __init__(
        self,
        grade: str = None,
        key_sentences: List[str] = None,
        key_words: List[str] = None,
        learning_object: str = None,
        text_content: str = None,
        textbook: str = None,
        topic: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.grade = grade
        self.key_sentences = key_sentences
        self.key_words = key_words
        self.learning_object = learning_object
        # This parameter is required.
        self.text_content = text_content
        self.textbook = textbook
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grade is not None:
            result['grade'] = self.grade
        if self.key_sentences is not None:
            result['keySentences'] = self.key_sentences
        if self.key_words is not None:
            result['keyWords'] = self.key_words
        if self.learning_object is not None:
            result['learningObject'] = self.learning_object
        if self.text_content is not None:
            result['textContent'] = self.text_content
        if self.textbook is not None:
            result['textbook'] = self.textbook
        if self.topic is not None:
            result['topic'] = self.topic
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('keySentences') is not None:
            self.key_sentences = m.get('keySentences')
        if m.get('keyWords') is not None:
            self.key_words = m.get('keyWords')
        if m.get('learningObject') is not None:
            self.learning_object = m.get('learningObject')
        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')
        if m.get('textbook') is not None:
            self.textbook = m.get('textbook')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class AITeacherExpansionPracticeTaskGenerateResponseBodyDataRoleSet(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class AITeacherExpansionPracticeTaskGenerateResponseBodyDataTaskContent(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class AITeacherExpansionPracticeTaskGenerateResponseBodyData(TeaModel):
    def __init__(
        self,
        background_description: str = None,
        role_set: AITeacherExpansionPracticeTaskGenerateResponseBodyDataRoleSet = None,
        start_sentence: str = None,
        task_content: List[AITeacherExpansionPracticeTaskGenerateResponseBodyDataTaskContent] = None,
        task_type: str = None,
    ):
        self.background_description = background_description
        self.role_set = role_set
        self.start_sentence = start_sentence
        self.task_content = task_content
        self.task_type = task_type

    def validate(self):
        if self.role_set:
            self.role_set.validate()
        if self.task_content:
            for k in self.task_content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_description is not None:
            result['backgroundDescription'] = self.background_description
        if self.role_set is not None:
            result['roleSet'] = self.role_set.to_map()
        if self.start_sentence is not None:
            result['startSentence'] = self.start_sentence
        result['taskContent'] = []
        if self.task_content is not None:
            for k in self.task_content:
                result['taskContent'].append(k.to_map() if k else None)
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backgroundDescription') is not None:
            self.background_description = m.get('backgroundDescription')
        if m.get('roleSet') is not None:
            temp_model = AITeacherExpansionPracticeTaskGenerateResponseBodyDataRoleSet()
            self.role_set = temp_model.from_map(m['roleSet'])
        if m.get('startSentence') is not None:
            self.start_sentence = m.get('startSentence')
        self.task_content = []
        if m.get('taskContent') is not None:
            for k in m.get('taskContent'):
                temp_model = AITeacherExpansionPracticeTaskGenerateResponseBodyDataTaskContent()
                self.task_content.append(temp_model.from_map(k))
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class AITeacherExpansionPracticeTaskGenerateResponseBody(TeaModel):
    def __init__(
        self,
        data: AITeacherExpansionPracticeTaskGenerateResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AITeacherExpansionPracticeTaskGenerateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AITeacherExpansionPracticeTaskGenerateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AITeacherExpansionPracticeTaskGenerateResponseBody = None,
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
            temp_model = AITeacherExpansionPracticeTaskGenerateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AITeacherSyncPracticeTaskGenerateRequest(TeaModel):
    def __init__(
        self,
        grade: str = None,
        key_sentences: List[str] = None,
        key_words: List[str] = None,
        learning_object: str = None,
        text_content: str = None,
        textbook: str = None,
        topic: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.grade = grade
        self.key_sentences = key_sentences
        self.key_words = key_words
        self.learning_object = learning_object
        # This parameter is required.
        self.text_content = text_content
        self.textbook = textbook
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grade is not None:
            result['grade'] = self.grade
        if self.key_sentences is not None:
            result['keySentences'] = self.key_sentences
        if self.key_words is not None:
            result['keyWords'] = self.key_words
        if self.learning_object is not None:
            result['learningObject'] = self.learning_object
        if self.text_content is not None:
            result['textContent'] = self.text_content
        if self.textbook is not None:
            result['textbook'] = self.textbook
        if self.topic is not None:
            result['topic'] = self.topic
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('keySentences') is not None:
            self.key_sentences = m.get('keySentences')
        if m.get('keyWords') is not None:
            self.key_words = m.get('keyWords')
        if m.get('learningObject') is not None:
            self.learning_object = m.get('learningObject')
        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')
        if m.get('textbook') is not None:
            self.textbook = m.get('textbook')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class AITeacherSyncPracticeTaskGenerateResponseBodyDataTaskContent(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class AITeacherSyncPracticeTaskGenerateResponseBodyData(TeaModel):
    def __init__(
        self,
        task_content: List[AITeacherSyncPracticeTaskGenerateResponseBodyDataTaskContent] = None,
        task_type: str = None,
    ):
        self.task_content = task_content
        self.task_type = task_type

    def validate(self):
        if self.task_content:
            for k in self.task_content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['taskContent'] = []
        if self.task_content is not None:
            for k in self.task_content:
                result['taskContent'].append(k.to_map() if k else None)
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_content = []
        if m.get('taskContent') is not None:
            for k in m.get('taskContent'):
                temp_model = AITeacherSyncPracticeTaskGenerateResponseBodyDataTaskContent()
                self.task_content.append(temp_model.from_map(k))
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class AITeacherSyncPracticeTaskGenerateResponseBody(TeaModel):
    def __init__(
        self,
        data: AITeacherSyncPracticeTaskGenerateResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AITeacherSyncPracticeTaskGenerateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AITeacherSyncPracticeTaskGenerateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AITeacherSyncPracticeTaskGenerateResponseBody = None,
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
            temp_model = AITeacherSyncPracticeTaskGenerateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponseBodyData(TeaModel):
    def __init__(
        self,
        free_concurrency_count: int = None,
        free_count: int = None,
        service_code: str = None,
        service_name: str = None,
    ):
        self.free_concurrency_count = free_concurrency_count
        self.free_count = free_count
        self.service_code = service_code
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_concurrency_count is not None:
            result['FreeConcurrencyCount'] = self.free_concurrency_count
        if self.free_count is not None:
            result['FreeCount'] = self.free_count
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeConcurrencyCount') is not None:
            self.free_concurrency_count = m.get('FreeConcurrencyCount')
        if m.get('FreeCount') is not None:
            self.free_count = m.get('FreeCount')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponseBody = None,
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
            temp_model = AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponseBodyData(TeaModel):
    def __init__(
        self,
        free_concurrency_count: int = None,
        free_count: int = None,
        service_code: str = None,
        service_name: str = None,
    ):
        self.free_concurrency_count = free_concurrency_count
        self.free_count = free_count
        self.service_code = service_code
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_concurrency_count is not None:
            result['FreeConcurrencyCount'] = self.free_concurrency_count
        if self.free_count is not None:
            result['FreeCount'] = self.free_count
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeConcurrencyCount') is not None:
            self.free_concurrency_count = m.get('FreeConcurrencyCount')
        if m.get('FreeCount') is not None:
            self.free_count = m.get('FreeCount')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponseBody = None,
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
            temp_model = AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherExpansionDialogueRequestDialogueTasks(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        assistant_translate: str = None,
        order: int = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        self.assistant_translate = assistant_translate
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.assistant_translate is not None:
            result['assistantTranslate'] = self.assistant_translate
        if self.order is not None:
            result['order'] = self.order
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('assistantTranslate') is not None:
            self.assistant_translate = m.get('assistantTranslate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteAITeacherExpansionDialogueRequestRecords(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        order: int = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.order is not None:
            result['order'] = self.order
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ExecuteAITeacherExpansionDialogueRequestRoleInfo(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteAITeacherExpansionDialogueRequest(TeaModel):
    def __init__(
        self,
        background: str = None,
        dialogue_tasks: List[ExecuteAITeacherExpansionDialogueRequestDialogueTasks] = None,
        language_code: str = None,
        records: List[ExecuteAITeacherExpansionDialogueRequestRecords] = None,
        role_info: ExecuteAITeacherExpansionDialogueRequestRoleInfo = None,
        start_sentence: str = None,
        topic: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.background = background
        # This parameter is required.
        self.dialogue_tasks = dialogue_tasks
        self.language_code = language_code
        self.records = records
        # This parameter is required.
        self.role_info = role_info
        self.start_sentence = start_sentence
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.dialogue_tasks:
            for k in self.dialogue_tasks:
                if k:
                    k.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()
        if self.role_info:
            self.role_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background is not None:
            result['background'] = self.background
        result['dialogueTasks'] = []
        if self.dialogue_tasks is not None:
            for k in self.dialogue_tasks:
                result['dialogueTasks'].append(k.to_map() if k else None)
        if self.language_code is not None:
            result['languageCode'] = self.language_code
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.role_info is not None:
            result['roleInfo'] = self.role_info.to_map()
        if self.start_sentence is not None:
            result['startSentence'] = self.start_sentence
        if self.topic is not None:
            result['topic'] = self.topic
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('background') is not None:
            self.background = m.get('background')
        self.dialogue_tasks = []
        if m.get('dialogueTasks') is not None:
            for k in m.get('dialogueTasks'):
                temp_model = ExecuteAITeacherExpansionDialogueRequestDialogueTasks()
                self.dialogue_tasks.append(temp_model.from_map(k))
        if m.get('languageCode') is not None:
            self.language_code = m.get('languageCode')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = ExecuteAITeacherExpansionDialogueRequestRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('roleInfo') is not None:
            temp_model = ExecuteAITeacherExpansionDialogueRequestRoleInfo()
            self.role_info = temp_model.from_map(m['roleInfo'])
        if m.get('startSentence') is not None:
            self.start_sentence = m.get('startSentence')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherExpansionDialogueResponseBodyData(TeaModel):
    def __init__(
        self,
        chinese_result: str = None,
        english_result: str = None,
        is_finish: bool = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        question_index: int = None,
    ):
        self.chinese_result = chinese_result
        self.english_result = english_result
        self.is_finish = is_finish
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        self.question_index = question_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chinese_result is not None:
            result['chineseResult'] = self.chinese_result
        if self.english_result is not None:
            result['englishResult'] = self.english_result
        if self.is_finish is not None:
            result['isFinish'] = self.is_finish
        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.question_index is not None:
            result['questionIndex'] = self.question_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chineseResult') is not None:
            self.chinese_result = m.get('chineseResult')
        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('questionIndex') is not None:
            self.question_index = m.get('questionIndex')
        return self


class ExecuteAITeacherExpansionDialogueResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteAITeacherExpansionDialogueResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ExecuteAITeacherExpansionDialogueResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExecuteAITeacherExpansionDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherExpansionDialogueResponseBody = None,
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
            temp_model = ExecuteAITeacherExpansionDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherExpansionDialogueRefineRequestDialogueTasks(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        assistant_translate: str = None,
        order: int = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        self.assistant_translate = assistant_translate
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.assistant_translate is not None:
            result['assistantTranslate'] = self.assistant_translate
        if self.order is not None:
            result['order'] = self.order
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('assistantTranslate') is not None:
            self.assistant_translate = m.get('assistantTranslate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteAITeacherExpansionDialogueRefineRequestRecords(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        order: int = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.order is not None:
            result['order'] = self.order
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ExecuteAITeacherExpansionDialogueRefineRequestRoleInfo(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteAITeacherExpansionDialogueRefineRequest(TeaModel):
    def __init__(
        self,
        background: str = None,
        dialogue_tasks: List[ExecuteAITeacherExpansionDialogueRefineRequestDialogueTasks] = None,
        language_code: str = None,
        records: List[ExecuteAITeacherExpansionDialogueRefineRequestRecords] = None,
        role_info: ExecuteAITeacherExpansionDialogueRefineRequestRoleInfo = None,
        start_sentence: str = None,
        topic: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.background = background
        # This parameter is required.
        self.dialogue_tasks = dialogue_tasks
        self.language_code = language_code
        # This parameter is required.
        self.records = records
        # This parameter is required.
        self.role_info = role_info
        self.start_sentence = start_sentence
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.dialogue_tasks:
            for k in self.dialogue_tasks:
                if k:
                    k.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()
        if self.role_info:
            self.role_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background is not None:
            result['background'] = self.background
        result['dialogueTasks'] = []
        if self.dialogue_tasks is not None:
            for k in self.dialogue_tasks:
                result['dialogueTasks'].append(k.to_map() if k else None)
        if self.language_code is not None:
            result['languageCode'] = self.language_code
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.role_info is not None:
            result['roleInfo'] = self.role_info.to_map()
        if self.start_sentence is not None:
            result['startSentence'] = self.start_sentence
        if self.topic is not None:
            result['topic'] = self.topic
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('background') is not None:
            self.background = m.get('background')
        self.dialogue_tasks = []
        if m.get('dialogueTasks') is not None:
            for k in m.get('dialogueTasks'):
                temp_model = ExecuteAITeacherExpansionDialogueRefineRequestDialogueTasks()
                self.dialogue_tasks.append(temp_model.from_map(k))
        if m.get('languageCode') is not None:
            self.language_code = m.get('languageCode')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = ExecuteAITeacherExpansionDialogueRefineRequestRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('roleInfo') is not None:
            temp_model = ExecuteAITeacherExpansionDialogueRefineRequestRoleInfo()
            self.role_info = temp_model.from_map(m['roleInfo'])
        if m.get('startSentence') is not None:
            self.start_sentence = m.get('startSentence')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherExpansionDialogueRefineResponseBodyData(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ExecuteAITeacherExpansionDialogueRefineResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteAITeacherExpansionDialogueRefineResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ExecuteAITeacherExpansionDialogueRefineResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExecuteAITeacherExpansionDialogueRefineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherExpansionDialogueRefineResponseBody = None,
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
            temp_model = ExecuteAITeacherExpansionDialogueRefineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherExpansionDialogueTranslateRequestDialogueTasks(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        assistant_translate: str = None,
        order: int = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        self.assistant_translate = assistant_translate
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.assistant_translate is not None:
            result['assistantTranslate'] = self.assistant_translate
        if self.order is not None:
            result['order'] = self.order
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('assistantTranslate') is not None:
            self.assistant_translate = m.get('assistantTranslate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteAITeacherExpansionDialogueTranslateRequestRecords(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        order: int = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.order is not None:
            result['order'] = self.order
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ExecuteAITeacherExpansionDialogueTranslateRequestRoleInfo(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteAITeacherExpansionDialogueTranslateRequest(TeaModel):
    def __init__(
        self,
        background: str = None,
        dialogue_tasks: List[ExecuteAITeacherExpansionDialogueTranslateRequestDialogueTasks] = None,
        records: List[ExecuteAITeacherExpansionDialogueTranslateRequestRecords] = None,
        role_info: ExecuteAITeacherExpansionDialogueTranslateRequestRoleInfo = None,
        start_sentence: str = None,
        topic: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.background = background
        # This parameter is required.
        self.dialogue_tasks = dialogue_tasks
        self.records = records
        # This parameter is required.
        self.role_info = role_info
        self.start_sentence = start_sentence
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.dialogue_tasks:
            for k in self.dialogue_tasks:
                if k:
                    k.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()
        if self.role_info:
            self.role_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background is not None:
            result['background'] = self.background
        result['dialogueTasks'] = []
        if self.dialogue_tasks is not None:
            for k in self.dialogue_tasks:
                result['dialogueTasks'].append(k.to_map() if k else None)
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.role_info is not None:
            result['roleInfo'] = self.role_info.to_map()
        if self.start_sentence is not None:
            result['startSentence'] = self.start_sentence
        if self.topic is not None:
            result['topic'] = self.topic
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('background') is not None:
            self.background = m.get('background')
        self.dialogue_tasks = []
        if m.get('dialogueTasks') is not None:
            for k in m.get('dialogueTasks'):
                temp_model = ExecuteAITeacherExpansionDialogueTranslateRequestDialogueTasks()
                self.dialogue_tasks.append(temp_model.from_map(k))
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = ExecuteAITeacherExpansionDialogueTranslateRequestRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('roleInfo') is not None:
            temp_model = ExecuteAITeacherExpansionDialogueTranslateRequestRoleInfo()
            self.role_info = temp_model.from_map(m['roleInfo'])
        if m.get('startSentence') is not None:
            self.start_sentence = m.get('startSentence')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherExpansionDialogueTranslateResponseBodyData(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ExecuteAITeacherExpansionDialogueTranslateResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteAITeacherExpansionDialogueTranslateResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ExecuteAITeacherExpansionDialogueTranslateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExecuteAITeacherExpansionDialogueTranslateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherExpansionDialogueTranslateResponseBody = None,
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
            temp_model = ExecuteAITeacherExpansionDialogueTranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherGrammarCheckRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherGrammarCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        analysis: str = None,
        correction: str = None,
        correction_status: str = None,
        error_reason: str = None,
    ):
        self.analysis = analysis
        self.correction = correction
        self.correction_status = correction_status
        self.error_reason = error_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis is not None:
            result['analysis'] = self.analysis
        if self.correction is not None:
            result['correction'] = self.correction
        if self.correction_status is not None:
            result['correctionStatus'] = self.correction_status
        if self.error_reason is not None:
            result['errorReason'] = self.error_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')
        if m.get('correction') is not None:
            self.correction = m.get('correction')
        if m.get('correctionStatus') is not None:
            self.correction_status = m.get('correctionStatus')
        if m.get('errorReason') is not None:
            self.error_reason = m.get('errorReason')
        return self


class ExecuteAITeacherGrammarCheckResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteAITeacherGrammarCheckResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ExecuteAITeacherGrammarCheckResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExecuteAITeacherGrammarCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherGrammarCheckResponseBody = None,
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
            temp_model = ExecuteAITeacherGrammarCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherSyncDialogueRequestDialogueTasks(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        assistant_translate: str = None,
        order: int = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        self.assistant_translate = assistant_translate
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.assistant_translate is not None:
            result['assistantTranslate'] = self.assistant_translate
        if self.order is not None:
            result['order'] = self.order
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('assistantTranslate') is not None:
            self.assistant_translate = m.get('assistantTranslate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteAITeacherSyncDialogueRequestRecords(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        order: int = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.order is not None:
            result['order'] = self.order
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ExecuteAITeacherSyncDialogueRequest(TeaModel):
    def __init__(
        self,
        dialogue_tasks: List[ExecuteAITeacherSyncDialogueRequestDialogueTasks] = None,
        language_code: str = None,
        records: List[ExecuteAITeacherSyncDialogueRequestRecords] = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.dialogue_tasks = dialogue_tasks
        self.language_code = language_code
        self.records = records
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.dialogue_tasks:
            for k in self.dialogue_tasks:
                if k:
                    k.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dialogueTasks'] = []
        if self.dialogue_tasks is not None:
            for k in self.dialogue_tasks:
                result['dialogueTasks'].append(k.to_map() if k else None)
        if self.language_code is not None:
            result['languageCode'] = self.language_code
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue_tasks = []
        if m.get('dialogueTasks') is not None:
            for k in m.get('dialogueTasks'):
                temp_model = ExecuteAITeacherSyncDialogueRequestDialogueTasks()
                self.dialogue_tasks.append(temp_model.from_map(k))
        if m.get('languageCode') is not None:
            self.language_code = m.get('languageCode')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = ExecuteAITeacherSyncDialogueRequestRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherSyncDialogueResponseBodyData(TeaModel):
    def __init__(
        self,
        english_result: str = None,
        is_finish: bool = None,
        is_on_topic: bool = None,
        question_index: int = None,
    ):
        self.english_result = english_result
        self.is_finish = is_finish
        self.is_on_topic = is_on_topic
        self.question_index = question_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.english_result is not None:
            result['englishResult'] = self.english_result
        if self.is_finish is not None:
            result['isFinish'] = self.is_finish
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.question_index is not None:
            result['questionIndex'] = self.question_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('questionIndex') is not None:
            self.question_index = m.get('questionIndex')
        return self


class ExecuteAITeacherSyncDialogueResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteAITeacherSyncDialogueResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ExecuteAITeacherSyncDialogueResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExecuteAITeacherSyncDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherSyncDialogueResponseBody = None,
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
            temp_model = ExecuteAITeacherSyncDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherSyncDialogueTranslateRequestDialogueTasks(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        assistant_translate: str = None,
        order: int = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        self.assistant_translate = assistant_translate
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.assistant_translate is not None:
            result['assistantTranslate'] = self.assistant_translate
        if self.order is not None:
            result['order'] = self.order
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('assistantTranslate') is not None:
            self.assistant_translate = m.get('assistantTranslate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteAITeacherSyncDialogueTranslateRequestRecords(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        order: int = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.order is not None:
            result['order'] = self.order
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ExecuteAITeacherSyncDialogueTranslateRequest(TeaModel):
    def __init__(
        self,
        dialogue_tasks: List[ExecuteAITeacherSyncDialogueTranslateRequestDialogueTasks] = None,
        records: List[ExecuteAITeacherSyncDialogueTranslateRequestRecords] = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.dialogue_tasks = dialogue_tasks
        self.records = records
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.dialogue_tasks:
            for k in self.dialogue_tasks:
                if k:
                    k.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dialogueTasks'] = []
        if self.dialogue_tasks is not None:
            for k in self.dialogue_tasks:
                result['dialogueTasks'].append(k.to_map() if k else None)
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue_tasks = []
        if m.get('dialogueTasks') is not None:
            for k in m.get('dialogueTasks'):
                temp_model = ExecuteAITeacherSyncDialogueTranslateRequestDialogueTasks()
                self.dialogue_tasks.append(temp_model.from_map(k))
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = ExecuteAITeacherSyncDialogueTranslateRequestRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherSyncDialogueTranslateResponseBodyData(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ExecuteAITeacherSyncDialogueTranslateResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteAITeacherSyncDialogueTranslateResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ExecuteAITeacherSyncDialogueTranslateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExecuteAITeacherSyncDialogueTranslateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherSyncDialogueTranslateResponseBody = None,
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
            temp_model = ExecuteAITeacherSyncDialogueTranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAITeacherExpansionDialogueSuggestionRequestDialogueTasks(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        assistant_translate: str = None,
        order: int = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        self.assistant_translate = assistant_translate
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.assistant_translate is not None:
            result['assistantTranslate'] = self.assistant_translate
        if self.order is not None:
            result['order'] = self.order
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('assistantTranslate') is not None:
            self.assistant_translate = m.get('assistantTranslate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class GetAITeacherExpansionDialogueSuggestionRequestRecords(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        order: int = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.order is not None:
            result['order'] = self.order
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class GetAITeacherExpansionDialogueSuggestionRequestRoleInfo(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class GetAITeacherExpansionDialogueSuggestionRequest(TeaModel):
    def __init__(
        self,
        background: str = None,
        dialogue_tasks: List[GetAITeacherExpansionDialogueSuggestionRequestDialogueTasks] = None,
        language_code: str = None,
        records: List[GetAITeacherExpansionDialogueSuggestionRequestRecords] = None,
        role_info: GetAITeacherExpansionDialogueSuggestionRequestRoleInfo = None,
        start_sentence: str = None,
        topic: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.background = background
        # This parameter is required.
        self.dialogue_tasks = dialogue_tasks
        self.language_code = language_code
        # This parameter is required.
        self.records = records
        # This parameter is required.
        self.role_info = role_info
        self.start_sentence = start_sentence
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.dialogue_tasks:
            for k in self.dialogue_tasks:
                if k:
                    k.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()
        if self.role_info:
            self.role_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background is not None:
            result['background'] = self.background
        result['dialogueTasks'] = []
        if self.dialogue_tasks is not None:
            for k in self.dialogue_tasks:
                result['dialogueTasks'].append(k.to_map() if k else None)
        if self.language_code is not None:
            result['languageCode'] = self.language_code
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.role_info is not None:
            result['roleInfo'] = self.role_info.to_map()
        if self.start_sentence is not None:
            result['startSentence'] = self.start_sentence
        if self.topic is not None:
            result['topic'] = self.topic
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('background') is not None:
            self.background = m.get('background')
        self.dialogue_tasks = []
        if m.get('dialogueTasks') is not None:
            for k in m.get('dialogueTasks'):
                temp_model = GetAITeacherExpansionDialogueSuggestionRequestDialogueTasks()
                self.dialogue_tasks.append(temp_model.from_map(k))
        if m.get('languageCode') is not None:
            self.language_code = m.get('languageCode')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetAITeacherExpansionDialogueSuggestionRequestRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('roleInfo') is not None:
            temp_model = GetAITeacherExpansionDialogueSuggestionRequestRoleInfo()
            self.role_info = temp_model.from_map(m['roleInfo'])
        if m.get('startSentence') is not None:
            self.start_sentence = m.get('startSentence')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetAITeacherExpansionDialogueSuggestionResponseBodyData(TeaModel):
    def __init__(
        self,
        chinese_result: str = None,
        english_result: str = None,
    ):
        self.chinese_result = chinese_result
        self.english_result = english_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chinese_result is not None:
            result['chineseResult'] = self.chinese_result
        if self.english_result is not None:
            result['englishResult'] = self.english_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chineseResult') is not None:
            self.chinese_result = m.get('chineseResult')
        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')
        return self


class GetAITeacherExpansionDialogueSuggestionResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAITeacherExpansionDialogueSuggestionResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetAITeacherExpansionDialogueSuggestionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetAITeacherExpansionDialogueSuggestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAITeacherExpansionDialogueSuggestionResponseBody = None,
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
            temp_model = GetAITeacherExpansionDialogueSuggestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAITeacherSyncDialogueSuggestionRequestDialogueTasks(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        assistant_translate: str = None,
        order: int = None,
        user: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        self.assistant_translate = assistant_translate
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.assistant_translate is not None:
            result['assistantTranslate'] = self.assistant_translate
        if self.order is not None:
            result['order'] = self.order
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('assistantTranslate') is not None:
            self.assistant_translate = m.get('assistantTranslate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class GetAITeacherSyncDialogueSuggestionRequestRecords(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_off_topic_control: bool = None,
        is_on_topic: bool = None,
        order: int = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.is_off_topic_control = is_off_topic_control
        self.is_on_topic = is_on_topic
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.is_off_topic_control is not None:
            result['isOffTopicControl'] = self.is_off_topic_control
        if self.is_on_topic is not None:
            result['isOnTopic'] = self.is_on_topic
        if self.order is not None:
            result['order'] = self.order
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('isOffTopicControl') is not None:
            self.is_off_topic_control = m.get('isOffTopicControl')
        if m.get('isOnTopic') is not None:
            self.is_on_topic = m.get('isOnTopic')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class GetAITeacherSyncDialogueSuggestionRequest(TeaModel):
    def __init__(
        self,
        dialogue_tasks: List[GetAITeacherSyncDialogueSuggestionRequestDialogueTasks] = None,
        language_code: str = None,
        records: List[GetAITeacherSyncDialogueSuggestionRequestRecords] = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.dialogue_tasks = dialogue_tasks
        self.language_code = language_code
        # This parameter is required.
        self.records = records
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.dialogue_tasks:
            for k in self.dialogue_tasks:
                if k:
                    k.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dialogueTasks'] = []
        if self.dialogue_tasks is not None:
            for k in self.dialogue_tasks:
                result['dialogueTasks'].append(k.to_map() if k else None)
        if self.language_code is not None:
            result['languageCode'] = self.language_code
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue_tasks = []
        if m.get('dialogueTasks') is not None:
            for k in m.get('dialogueTasks'):
                temp_model = GetAITeacherSyncDialogueSuggestionRequestDialogueTasks()
                self.dialogue_tasks.append(temp_model.from_map(k))
        if m.get('languageCode') is not None:
            self.language_code = m.get('languageCode')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetAITeacherSyncDialogueSuggestionRequestRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetAITeacherSyncDialogueSuggestionResponseBodyData(TeaModel):
    def __init__(
        self,
        chinese_result: str = None,
        english_result: str = None,
    ):
        self.chinese_result = chinese_result
        self.english_result = english_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chinese_result is not None:
            result['chineseResult'] = self.chinese_result
        if self.english_result is not None:
            result['englishResult'] = self.english_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chineseResult') is not None:
            self.chinese_result = m.get('chineseResult')
        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')
        return self


class GetAITeacherSyncDialogueSuggestionResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAITeacherSyncDialogueSuggestionResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetAITeacherSyncDialogueSuggestionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetAITeacherSyncDialogueSuggestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAITeacherSyncDialogueSuggestionResponseBody = None,
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
            temp_model = GetAITeacherSyncDialogueSuggestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PersonalizedTextToImageAddInferenceJobRequest(TeaModel):
    def __init__(
        self,
        image_number: int = None,
        image_url: List[str] = None,
        prompt: str = None,
        seed: int = None,
        strength: float = None,
        train_steps: int = None,
    ):
        self.image_number = image_number
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.prompt = prompt
        self.seed = seed
        self.strength = strength
        self.train_steps = train_steps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_number is not None:
            result['imageNumber'] = self.image_number
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.seed is not None:
            result['seed'] = self.seed
        if self.strength is not None:
            result['strength'] = self.strength
        if self.train_steps is not None:
            result['trainSteps'] = self.train_steps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageNumber') is not None:
            self.image_number = m.get('imageNumber')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('seed') is not None:
            self.seed = m.get('seed')
        if m.get('strength') is not None:
            self.strength = m.get('strength')
        if m.get('trainSteps') is not None:
            self.train_steps = m.get('trainSteps')
        return self


class PersonalizedTextToImageAddInferenceJobResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        prompt_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        # promptId
        self.prompt_id = prompt_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id
        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')
        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')
        return self


class PersonalizedTextToImageAddInferenceJobResponseBody(TeaModel):
    def __init__(
        self,
        data: PersonalizedTextToImageAddInferenceJobResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = PersonalizedTextToImageAddInferenceJobResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class PersonalizedTextToImageAddInferenceJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PersonalizedTextToImageAddInferenceJobResponseBody = None,
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
            temp_model = PersonalizedTextToImageAddInferenceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PersonalizedTextToImageQueryImageAssetRequest(TeaModel):
    def __init__(
        self,
        encode_format: str = None,
        image_id: str = None,
    ):
        self.encode_format = encode_format
        # This parameter is required.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_format is not None:
            result['encodeFormat'] = self.encode_format
        if self.image_id is not None:
            result['imageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encodeFormat') is not None:
            self.encode_format = m.get('encodeFormat')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        return self


class PersonalizedTextToImageQueryImageAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Any = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest(TeaModel):
    def __init__(
        self,
        inference_job_id: str = None,
    ):
        # This parameter is required.
        self.inference_job_id = inference_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inference_job_id is not None:
            result['inferenceJobId'] = self.inference_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inferenceJobId') is not None:
            self.inference_job_id = m.get('inferenceJobId')
        return self


class PersonalizedTextToImageQueryPreModelInferenceJobInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        prompt_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        # promptId
        self.prompt_id = prompt_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id
        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')
        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')
        return self


class PersonalizedTextToImageQueryPreModelInferenceJobInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = PersonalizedTextToImageQueryPreModelInferenceJobInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponseBody = None,
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
            temp_model = PersonalizedTextToImageQueryPreModelInferenceJobInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Personalizedtxt2imgAddInferenceJobRequest(TeaModel):
    def __init__(
        self,
        image_number: int = None,
        model_id: str = None,
        prompt: str = None,
        seed: int = None,
    ):
        self.image_number = image_number
        # This parameter is required.
        self.model_id = model_id
        # This parameter is required.
        self.prompt = prompt
        self.seed = seed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_number is not None:
            result['imageNumber'] = self.image_number
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.seed is not None:
            result['seed'] = self.seed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageNumber') is not None:
            self.image_number = m.get('imageNumber')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('seed') is not None:
            self.seed = m.get('seed')
        return self


class Personalizedtxt2imgAddInferenceJobResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        prompt_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        self.prompt_id = prompt_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id
        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')
        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')
        return self


class Personalizedtxt2imgAddInferenceJobResponseBody(TeaModel):
    def __init__(
        self,
        data: Personalizedtxt2imgAddInferenceJobResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Personalizedtxt2imgAddInferenceJobResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class Personalizedtxt2imgAddInferenceJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Personalizedtxt2imgAddInferenceJobResponseBody = None,
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
            temp_model = Personalizedtxt2imgAddInferenceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Personalizedtxt2imgAddModelTrainJobRequest(TeaModel):
    def __init__(
        self,
        image_url: List[str] = None,
        name: str = None,
        object_type: str = None,
        train_steps: int = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.object_type = object_type
        self.train_steps = train_steps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.name is not None:
            result['name'] = self.name
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.train_steps is not None:
            result['trainSteps'] = self.train_steps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('trainSteps') is not None:
            self.train_steps = m.get('trainSteps')
        return self


class Personalizedtxt2imgAddModelTrainJobResponseBodyDataInferenceJobList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        prompt_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        self.prompt_id = prompt_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id
        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')
        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')
        return self


class Personalizedtxt2imgAddModelTrainJobResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        image_url: List[str] = None,
        inference_image_count: int = None,
        inference_job_list: List[Personalizedtxt2imgAddModelTrainJobResponseBodyDataInferenceJobList] = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        name: str = None,
        object_type: str = None,
    ):
        self.create_time = create_time
        self.id = id
        self.image_url = image_url
        self.inference_image_count = inference_image_count
        self.inference_job_list = inference_job_list
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        self.name = name
        self.object_type = object_type

    def validate(self):
        if self.inference_job_list:
            for k in self.inference_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.inference_image_count is not None:
            result['inferenceImageCount'] = self.inference_image_count
        result['inferenceJobList'] = []
        if self.inference_job_list is not None:
            for k in self.inference_job_list:
                result['inferenceJobList'].append(k.to_map() if k else None)
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.object_type is not None:
            result['objectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('inferenceImageCount') is not None:
            self.inference_image_count = m.get('inferenceImageCount')
        self.inference_job_list = []
        if m.get('inferenceJobList') is not None:
            for k in m.get('inferenceJobList'):
                temp_model = Personalizedtxt2imgAddModelTrainJobResponseBodyDataInferenceJobList()
                self.inference_job_list.append(temp_model.from_map(k))
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        return self


class Personalizedtxt2imgAddModelTrainJobResponseBody(TeaModel):
    def __init__(
        self,
        data: Personalizedtxt2imgAddModelTrainJobResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Personalizedtxt2imgAddModelTrainJobResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class Personalizedtxt2imgAddModelTrainJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Personalizedtxt2imgAddModelTrainJobResponseBody = None,
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
            temp_model = Personalizedtxt2imgAddModelTrainJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Personalizedtxt2imgQueryImageAssetRequest(TeaModel):
    def __init__(
        self,
        encode_format: str = None,
        image_id: str = None,
        model_id: str = None,
        prompt_id: str = None,
    ):
        self.encode_format = encode_format
        # This parameter is required.
        self.image_id = image_id
        # This parameter is required.
        self.model_id = model_id
        # This parameter is required.
        self.prompt_id = prompt_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_format is not None:
            result['encodeFormat'] = self.encode_format
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encodeFormat') is not None:
            self.encode_format = m.get('encodeFormat')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')
        return self


class Personalizedtxt2imgQueryImageAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Any = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class Personalizedtxt2imgQueryInferenceJobInfoRequest(TeaModel):
    def __init__(
        self,
        inference_job_id: str = None,
    ):
        # This parameter is required.
        self.inference_job_id = inference_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inference_job_id is not None:
            result['inferenceJobId'] = self.inference_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inferenceJobId') is not None:
            self.inference_job_id = m.get('inferenceJobId')
        return self


class Personalizedtxt2imgQueryInferenceJobInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        prompt_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        self.prompt_id = prompt_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id
        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')
        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')
        return self


class Personalizedtxt2imgQueryInferenceJobInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: Personalizedtxt2imgQueryInferenceJobInfoResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Personalizedtxt2imgQueryInferenceJobInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class Personalizedtxt2imgQueryInferenceJobInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Personalizedtxt2imgQueryInferenceJobInfoResponseBody = None,
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
            temp_model = Personalizedtxt2imgQueryInferenceJobInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Personalizedtxt2imgQueryModelTrainJobListResponseBodyDataInferenceJobList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        prompt_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        self.prompt_id = prompt_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id
        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')
        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')
        return self


class Personalizedtxt2imgQueryModelTrainJobListResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        image_url: List[str] = None,
        inference_image_count: int = None,
        inference_job_list: List[Personalizedtxt2imgQueryModelTrainJobListResponseBodyDataInferenceJobList] = None,
        job_status: str = None,
        job_train_progress: float = None,
        model_id: str = None,
        name: str = None,
        object_type: str = None,
    ):
        self.create_time = create_time
        self.id = id
        self.image_url = image_url
        self.inference_image_count = inference_image_count
        self.inference_job_list = inference_job_list
        self.job_status = job_status
        self.job_train_progress = job_train_progress
        self.model_id = model_id
        self.name = name
        self.object_type = object_type

    def validate(self):
        if self.inference_job_list:
            for k in self.inference_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.inference_image_count is not None:
            result['inferenceImageCount'] = self.inference_image_count
        result['inferenceJobList'] = []
        if self.inference_job_list is not None:
            for k in self.inference_job_list:
                result['inferenceJobList'].append(k.to_map() if k else None)
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.job_train_progress is not None:
            result['jobTrainProgress'] = self.job_train_progress
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.name is not None:
            result['name'] = self.name
        if self.object_type is not None:
            result['objectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('inferenceImageCount') is not None:
            self.inference_image_count = m.get('inferenceImageCount')
        self.inference_job_list = []
        if m.get('inferenceJobList') is not None:
            for k in m.get('inferenceJobList'):
                temp_model = Personalizedtxt2imgQueryModelTrainJobListResponseBodyDataInferenceJobList()
                self.inference_job_list.append(temp_model.from_map(k))
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('jobTrainProgress') is not None:
            self.job_train_progress = m.get('jobTrainProgress')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        return self


class Personalizedtxt2imgQueryModelTrainJobListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Personalizedtxt2imgQueryModelTrainJobListResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Personalizedtxt2imgQueryModelTrainJobListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class Personalizedtxt2imgQueryModelTrainJobListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Personalizedtxt2imgQueryModelTrainJobListResponseBody = None,
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
            temp_model = Personalizedtxt2imgQueryModelTrainJobListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Personalizedtxt2imgQueryModelTrainStatusRequest(TeaModel):
    def __init__(
        self,
        model_id: str = None,
    ):
        # This parameter is required.
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['modelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        return self


class Personalizedtxt2imgQueryModelTrainStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        model_train_status: str = None,
    ):
        self.model_train_status = model_train_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_train_status is not None:
            result['modelTrainStatus'] = self.model_train_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelTrainStatus') is not None:
            self.model_train_status = m.get('modelTrainStatus')
        return self


class Personalizedtxt2imgQueryModelTrainStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: Personalizedtxt2imgQueryModelTrainStatusResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Personalizedtxt2imgQueryModelTrainStatusResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class Personalizedtxt2imgQueryModelTrainStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Personalizedtxt2imgQueryModelTrainStatusResponseBody = None,
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
            temp_model = Personalizedtxt2imgQueryModelTrainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


