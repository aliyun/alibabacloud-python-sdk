# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class OpenApiMultiResponse(DaraModel):
    def __init__(
        self,
        data: List[main_models.OpenApiMultiResponseData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('data'):
                temp_model = main_models.OpenApiMultiResponseData()
                self.data.append(temp_model.from_map(k1))

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

class OpenApiMultiResponseData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        image_url: List[str] = None,
        inference_image_count: int = None,
        inference_job_list: List[main_models.OpenApiMultiResponseDataInferenceJobList] = None,
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
            for v1 in self.inference_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in self.inference_job_list:
                result['inferenceJobList'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('inferenceJobList'):
                temp_model = main_models.OpenApiMultiResponseDataInferenceJobList()
                self.inference_job_list.append(temp_model.from_map(k1))

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

class OpenApiMultiResponseDataInferenceJobList(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

