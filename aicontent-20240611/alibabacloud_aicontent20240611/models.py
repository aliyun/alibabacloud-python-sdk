# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AliyunConsoleServiceInfoDTO(TeaModel):
    def __init__(
        self,
        buy_url: str = None,
        document_url: str = None,
        free_concurrency_count: int = None,
        free_count: int = None,
        service_code: str = None,
        service_name: str = None,
    ):
        self.buy_url = buy_url
        self.document_url = document_url
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
        if self.buy_url is not None:
            result['buyUrl'] = self.buy_url
        if self.document_url is not None:
            result['documentUrl'] = self.document_url
        if self.free_concurrency_count is not None:
            result['freeConcurrencyCount'] = self.free_concurrency_count
        if self.free_count is not None:
            result['freeCount'] = self.free_count
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buyUrl') is not None:
            self.buy_url = m.get('buyUrl')
        if m.get('documentUrl') is not None:
            self.document_url = m.get('documentUrl')
        if m.get('freeConcurrencyCount') is not None:
            self.free_concurrency_count = m.get('freeConcurrencyCount')
        if m.get('freeCount') is not None:
            self.free_count = m.get('freeCount')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


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


class OralEvaluationStatisticsCallsCountRequest(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
        end_time: str = None,
        granularity: str = None,
        project_id: str = None,
        start_time: str = None,
    ):
        self.application_access_id = application_access_id
        self.end_time = end_time
        self.granularity = granularity
        self.project_id = project_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.granularity is not None:
            result['granularity'] = self.granularity
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class OralEvaluationStatisticsCallsCountResponseProjectDataApplicationDataData(TeaModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.count = count
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class OralEvaluationStatisticsCallsCountResponseProjectDataApplicationData(TeaModel):
    def __init__(
        self,
        data: List[OralEvaluationStatisticsCallsCountResponseProjectDataApplicationDataData] = None,
        application_access_id: str = None,
    ):
        self.data = data
        # This parameter is required.
        self.application_access_id = application_access_id

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
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OralEvaluationStatisticsCallsCountResponseProjectDataApplicationDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        return self


class OralEvaluationStatisticsCallsCountResponseProjectData(TeaModel):
    def __init__(
        self,
        application_data: List[OralEvaluationStatisticsCallsCountResponseProjectDataApplicationData] = None,
        application_internal_id: str = None,
    ):
        self.application_data = application_data
        # This parameter is required.
        self.application_internal_id = application_internal_id

    def validate(self):
        if self.application_data:
            for k in self.application_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationData'] = []
        if self.application_data is not None:
            for k in self.application_data:
                result['ApplicationData'].append(k.to_map() if k else None)
        if self.application_internal_id is not None:
            result['applicationInternalId'] = self.application_internal_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_data = []
        if m.get('ApplicationData') is not None:
            for k in m.get('ApplicationData'):
                temp_model = OralEvaluationStatisticsCallsCountResponseProjectDataApplicationData()
                self.application_data.append(temp_model.from_map(k))
        if m.get('applicationInternalId') is not None:
            self.application_internal_id = m.get('applicationInternalId')
        return self


class OralEvaluationStatisticsCallsCountResponse(TeaModel):
    def __init__(
        self,
        project_data: OralEvaluationStatisticsCallsCountResponseProjectData = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.project_data = project_data
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.project_data:
            self.project_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_data is not None:
            result['projectData'] = self.project_data.to_map()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectData') is not None:
            temp_model = OralEvaluationStatisticsCallsCountResponseProjectData()
            self.project_data = temp_model.from_map(m['projectData'])
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class OralEvaluationStatisticsConcurrentCountRequest(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
        end_time: str = None,
        granularity: str = None,
        project_id: str = None,
        start_time: str = None,
    ):
        self.application_access_id = application_access_id
        self.end_time = end_time
        self.granularity = granularity
        self.project_id = project_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.granularity is not None:
            result['granularity'] = self.granularity
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class OralEvaluationStatisticsConcurrentCountResponseProjectDataApplicationDataData(TeaModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.count = count
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class OralEvaluationStatisticsConcurrentCountResponseProjectDataApplicationData(TeaModel):
    def __init__(
        self,
        data: List[OralEvaluationStatisticsConcurrentCountResponseProjectDataApplicationDataData] = None,
        application_access_id: str = None,
    ):
        self.data = data
        # This parameter is required.
        self.application_access_id = application_access_id

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
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OralEvaluationStatisticsConcurrentCountResponseProjectDataApplicationDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        return self


class OralEvaluationStatisticsConcurrentCountResponseProjectData(TeaModel):
    def __init__(
        self,
        application_data: List[OralEvaluationStatisticsConcurrentCountResponseProjectDataApplicationData] = None,
        application_internal_id: str = None,
    ):
        self.application_data = application_data
        # This parameter is required.
        self.application_internal_id = application_internal_id

    def validate(self):
        if self.application_data:
            for k in self.application_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationData'] = []
        if self.application_data is not None:
            for k in self.application_data:
                result['ApplicationData'].append(k.to_map() if k else None)
        if self.application_internal_id is not None:
            result['applicationInternalId'] = self.application_internal_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_data = []
        if m.get('ApplicationData') is not None:
            for k in m.get('ApplicationData'):
                temp_model = OralEvaluationStatisticsConcurrentCountResponseProjectDataApplicationData()
                self.application_data.append(temp_model.from_map(k))
        if m.get('applicationInternalId') is not None:
            self.application_internal_id = m.get('applicationInternalId')
        return self


class OralEvaluationStatisticsConcurrentCountResponse(TeaModel):
    def __init__(
        self,
        project_data: OralEvaluationStatisticsConcurrentCountResponseProjectData = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.project_data = project_data
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.project_data:
            self.project_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_data is not None:
            result['projectData'] = self.project_data.to_map()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectData') is not None:
            temp_model = OralEvaluationStatisticsConcurrentCountResponseProjectData()
            self.project_data = temp_model.from_map(m['projectData'])
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class OralEvaluationStatisticsErrorCountRequest(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
        end_time: str = None,
        error_code: List[str] = None,
        granularity: str = None,
        project_id: str = None,
        start_time: str = None,
    ):
        self.application_access_id = application_access_id
        self.end_time = end_time
        self.error_code = error_code
        self.granularity = granularity
        self.project_id = project_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.granularity is not None:
            result['granularity'] = self.granularity
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataDataData(TeaModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.count = count
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataData(TeaModel):
    def __init__(
        self,
        data: List[OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataDataData] = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class OralEvaluationStatisticsErrorCountResponseProjectDataApplicationData(TeaModel):
    def __init__(
        self,
        data: List[OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataData] = None,
        application_access_id: str = None,
    ):
        self.data = data
        # This parameter is required.
        self.application_access_id = application_access_id

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
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OralEvaluationStatisticsErrorCountResponseProjectDataApplicationDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        return self


class OralEvaluationStatisticsErrorCountResponseProjectData(TeaModel):
    def __init__(
        self,
        application_data: List[OralEvaluationStatisticsErrorCountResponseProjectDataApplicationData] = None,
        application_internal_id: str = None,
    ):
        self.application_data = application_data
        # This parameter is required.
        self.application_internal_id = application_internal_id

    def validate(self):
        if self.application_data:
            for k in self.application_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationData'] = []
        if self.application_data is not None:
            for k in self.application_data:
                result['ApplicationData'].append(k.to_map() if k else None)
        if self.application_internal_id is not None:
            result['applicationInternalId'] = self.application_internal_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_data = []
        if m.get('ApplicationData') is not None:
            for k in m.get('ApplicationData'):
                temp_model = OralEvaluationStatisticsErrorCountResponseProjectDataApplicationData()
                self.application_data.append(temp_model.from_map(k))
        if m.get('applicationInternalId') is not None:
            self.application_internal_id = m.get('applicationInternalId')
        return self


class OralEvaluationStatisticsErrorCountResponse(TeaModel):
    def __init__(
        self,
        project_data: OralEvaluationStatisticsErrorCountResponseProjectData = None,
        project_id: str = None,
    ):
        self.project_data = project_data
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.project_data:
            self.project_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_data is not None:
            result['ProjectData'] = self.project_data.to_map()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectData') is not None:
            temp_model = OralEvaluationStatisticsErrorCountResponseProjectData()
            self.project_data = temp_model.from_map(m['ProjectData'])
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
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


class AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AliyunConsoleServiceInfoDTO] = None,
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
                temp_model = AliyunConsoleServiceInfoDTO()
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


class CountOralEvaluationStatisticsCallsRequest(TeaModel):
    def __init__(
        self,
        body: OralEvaluationStatisticsCallsCountRequest = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = OralEvaluationStatisticsCallsCountRequest()
            self.body = temp_model.from_map(m['body'])
        return self


class CountOralEvaluationStatisticsCallsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[OralEvaluationStatisticsCallsCountResponse] = None,
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
                temp_model = OralEvaluationStatisticsCallsCountResponse()
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


class CountOralEvaluationStatisticsCallsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CountOralEvaluationStatisticsCallsResponseBody = None,
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
            temp_model = CountOralEvaluationStatisticsCallsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountOralEvaluationStatisticsConcurrentRequest(TeaModel):
    def __init__(
        self,
        body: OralEvaluationStatisticsConcurrentCountRequest = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = OralEvaluationStatisticsConcurrentCountRequest()
            self.body = temp_model.from_map(m['body'])
        return self


class CountOralEvaluationStatisticsConcurrentResponseBody(TeaModel):
    def __init__(
        self,
        data: List[OralEvaluationStatisticsConcurrentCountResponse] = None,
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
                temp_model = OralEvaluationStatisticsConcurrentCountResponse()
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


class CountOralEvaluationStatisticsConcurrentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CountOralEvaluationStatisticsConcurrentResponseBody = None,
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
            temp_model = CountOralEvaluationStatisticsConcurrentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountOralEvaluationStatisticsErrorRequest(TeaModel):
    def __init__(
        self,
        body: OralEvaluationStatisticsErrorCountRequest = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = OralEvaluationStatisticsErrorCountRequest()
            self.body = temp_model.from_map(m['body'])
        return self


class CountOralEvaluationStatisticsErrorResponseBody(TeaModel):
    def __init__(
        self,
        data: List[OralEvaluationStatisticsErrorCountResponse] = None,
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
                temp_model = OralEvaluationStatisticsErrorCountResponse()
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


class CountOralEvaluationStatisticsErrorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CountOralEvaluationStatisticsErrorResponseBody = None,
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
            temp_model = CountOralEvaluationStatisticsErrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessWarrantRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_sign: str = None,
        timestamp: str = None,
        user_client_ip: str = None,
        user_id: str = None,
        warrant_available: int = None,
    ):
        self.app_id = app_id
        self.request_sign = request_sign
        self.timestamp = timestamp
        self.user_client_ip = user_client_ip
        self.user_id = user_id
        self.warrant_available = warrant_available

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.request_sign is not None:
            result['requestSign'] = self.request_sign
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.user_client_ip is not None:
            result['userClientIp'] = self.user_client_ip
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.warrant_available is not None:
            result['warrantAvailable'] = self.warrant_available
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('requestSign') is not None:
            self.request_sign = m.get('requestSign')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('userClientIp') is not None:
            self.user_client_ip = m.get('userClientIp')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('warrantAvailable') is not None:
            self.warrant_available = m.get('warrantAvailable')
        return self


class CreateAccessWarrantResponseBodyData(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        access_warrant_id: str = None,
        application_access_id: str = None,
        create_time: str = None,
        expire_time: str = None,
        user_id: str = None,
    ):
        self.access_token = access_token
        self.access_warrant_id = access_warrant_id
        self.application_access_id = application_access_id
        self.create_time = create_time
        self.expire_time = expire_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_warrant_id is not None:
            result['AccessWarrantId'] = self.access_warrant_id
        if self.application_access_id is not None:
            result['ApplicationAccessId'] = self.application_access_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessWarrantId') is not None:
            self.access_warrant_id = m.get('AccessWarrantId')
        if m.get('ApplicationAccessId') is not None:
            self.application_access_id = m.get('ApplicationAccessId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateAccessWarrantResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateAccessWarrantResponseBodyData = None,
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
            temp_model = CreateAccessWarrantResponseBodyData()
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


class CreateAccessWarrantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessWarrantResponseBody = None,
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
            temp_model = CreateAccessWarrantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        project_type: str = None,
    ):
        self.project_name = project_name
        self.project_type = project_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.project_type is not None:
            result['projectType'] = self.project_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('projectType') is not None:
            self.project_type = m.get('projectType')
        return self


class CreateProjectResponseBodyDataProjectAppsApplicationAccessIds(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
        application_access_secret: str = None,
    ):
        self.application_access_id = application_access_id
        self.application_access_secret = application_access_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        if self.application_access_secret is not None:
            result['applicationAccessSecret'] = self.application_access_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        if m.get('applicationAccessSecret') is not None:
            self.application_access_secret = m.get('applicationAccessSecret')
        return self


class CreateProjectResponseBodyDataProjectApps(TeaModel):
    def __init__(
        self,
        application_access_ids: List[CreateProjectResponseBodyDataProjectAppsApplicationAccessIds] = None,
        id: str = None,
        project_id: str = None,
    ):
        self.application_access_ids = application_access_ids
        self.id = id
        self.project_id = project_id

    def validate(self):
        if self.application_access_ids:
            for k in self.application_access_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationAccessIds'] = []
        if self.application_access_ids is not None:
            for k in self.application_access_ids:
                result['ApplicationAccessIds'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_access_ids = []
        if m.get('ApplicationAccessIds') is not None:
            for k in m.get('ApplicationAccessIds'):
                temp_model = CreateProjectResponseBodyDataProjectAppsApplicationAccessIds()
                self.application_access_ids.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateProjectResponseBodyDataProjectSDK(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        demo_url: str = None,
        deploy_mode: str = None,
        develop_language: str = None,
        doc_url: str = None,
        sdk_name: str = None,
        sdk_url: str = None,
        sdk_version: str = None,
    ):
        self.create_time = create_time
        self.demo_url = demo_url
        self.deploy_mode = deploy_mode
        self.develop_language = develop_language
        self.doc_url = doc_url
        self.sdk_name = sdk_name
        self.sdk_url = sdk_url
        self.sdk_version = sdk_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.demo_url is not None:
            result['DemoUrl'] = self.demo_url
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.develop_language is not None:
            result['DevelopLanguage'] = self.develop_language
        if self.doc_url is not None:
            result['DocUrl'] = self.doc_url
        if self.sdk_name is not None:
            result['SdkName'] = self.sdk_name
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DemoUrl') is not None:
            self.demo_url = m.get('DemoUrl')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DevelopLanguage') is not None:
            self.develop_language = m.get('DevelopLanguage')
        if m.get('DocUrl') is not None:
            self.doc_url = m.get('DocUrl')
        if m.get('SdkName') is not None:
            self.sdk_name = m.get('SdkName')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        return self


class CreateProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        project_apps: List[CreateProjectResponseBodyDataProjectApps] = None,
        project_id: str = None,
        project_name: str = None,
        project_sdk: List[CreateProjectResponseBodyDataProjectSDK] = None,
        project_type: str = None,
    ):
        self.create_time = create_time
        self.project_apps = project_apps
        self.project_id = project_id
        self.project_name = project_name
        self.project_sdk = project_sdk
        self.project_type = project_type

    def validate(self):
        if self.project_apps:
            for k in self.project_apps:
                if k:
                    k.validate()
        if self.project_sdk:
            for k in self.project_sdk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['ProjectApps'] = []
        if self.project_apps is not None:
            for k in self.project_apps:
                result['ProjectApps'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['ProjectSDK'] = []
        if self.project_sdk is not None:
            for k in self.project_sdk:
                result['ProjectSDK'].append(k.to_map() if k else None)
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.project_apps = []
        if m.get('ProjectApps') is not None:
            for k in m.get('ProjectApps'):
                temp_model = CreateProjectResponseBodyDataProjectApps()
                self.project_apps.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.project_sdk = []
        if m.get('ProjectSDK') is not None:
            for k in m.get('ProjectSDK'):
                temp_model = CreateProjectResponseBodyDataProjectSDK()
                self.project_sdk.append(temp_model.from_map(k))
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateProjectResponseBodyData = None,
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
            temp_model = CreateProjectResponseBodyData()
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


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest(TeaModel):
    def __init__(
        self,
        essay_outline: str = None,
        essay_requirements: str = None,
        essay_topic: str = None,
        essay_type: str = None,
        essay_word_count: int = None,
        grade: int = None,
        response_mode: str = None,
        user_id: str = None,
    ):
        self.essay_outline = essay_outline
        # This parameter is required.
        self.essay_requirements = essay_requirements
        # This parameter is required.
        self.essay_topic = essay_topic
        # This parameter is required.
        self.essay_type = essay_type
        self.essay_word_count = essay_word_count
        # This parameter is required.
        self.grade = grade
        # This parameter is required.
        self.response_mode = response_mode
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.essay_outline is not None:
            result['essayOutline'] = self.essay_outline
        if self.essay_requirements is not None:
            result['essayRequirements'] = self.essay_requirements
        if self.essay_topic is not None:
            result['essayTopic'] = self.essay_topic
        if self.essay_type is not None:
            result['essayType'] = self.essay_type
        if self.essay_word_count is not None:
            result['essayWordCount'] = self.essay_word_count
        if self.grade is not None:
            result['grade'] = self.grade
        if self.response_mode is not None:
            result['responseMode'] = self.response_mode
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('essayOutline') is not None:
            self.essay_outline = m.get('essayOutline')
        if m.get('essayRequirements') is not None:
            self.essay_requirements = m.get('essayRequirements')
        if m.get('essayTopic') is not None:
            self.essay_topic = m.get('essayTopic')
        if m.get('essayType') is not None:
            self.essay_type = m.get('essayType')
        if m.get('essayWordCount') is not None:
            self.essay_word_count = m.get('essayWordCount')
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('responseMode') is not None:
            self.response_mode = m.get('responseMode')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        event: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.event = event
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.event is not None:
            result['event'] = self.event
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponseBody = None,
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
            temp_model = ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest(TeaModel):
    def __init__(
        self,
        essay_outline: str = None,
        essay_requirements: str = None,
        essay_topic: str = None,
        essay_type: str = None,
        essay_word_count: int = None,
        grade: int = None,
        response_mode: str = None,
        user_id: str = None,
    ):
        self.essay_outline = essay_outline
        # This parameter is required.
        self.essay_requirements = essay_requirements
        # This parameter is required.
        self.essay_topic = essay_topic
        # This parameter is required.
        self.essay_type = essay_type
        self.essay_word_count = essay_word_count
        # This parameter is required.
        self.grade = grade
        # This parameter is required.
        self.response_mode = response_mode
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.essay_outline is not None:
            result['essayOutline'] = self.essay_outline
        if self.essay_requirements is not None:
            result['essayRequirements'] = self.essay_requirements
        if self.essay_topic is not None:
            result['essayTopic'] = self.essay_topic
        if self.essay_type is not None:
            result['essayType'] = self.essay_type
        if self.essay_word_count is not None:
            result['essayWordCount'] = self.essay_word_count
        if self.grade is not None:
            result['grade'] = self.grade
        if self.response_mode is not None:
            result['responseMode'] = self.response_mode
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('essayOutline') is not None:
            self.essay_outline = m.get('essayOutline')
        if m.get('essayRequirements') is not None:
            self.essay_requirements = m.get('essayRequirements')
        if m.get('essayTopic') is not None:
            self.essay_topic = m.get('essayTopic')
        if m.get('essayType') is not None:
            self.essay_type = m.get('essayType')
        if m.get('essayWordCount') is not None:
            self.essay_word_count = m.get('essayWordCount')
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('responseMode') is not None:
            self.response_mode = m.get('responseMode')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        event: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.event = event
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.event is not None:
            result['event'] = self.event
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponseBody = None,
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
            temp_model = ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteAITeacherEnglishParaphraseChatMessageRequest(TeaModel):
    def __init__(
        self,
        chat_id: str = None,
        content: str = None,
        grade: int = None,
        question_id: str = None,
        question_info: str = None,
        response_mode: str = None,
        user_answer: str = None,
        user_id: str = None,
    ):
        self.chat_id = chat_id
        # This parameter is required.
        self.content = content
        self.grade = grade
        self.question_id = question_id
        # This parameter is required.
        self.question_info = question_info
        # This parameter is required.
        self.response_mode = response_mode
        # This parameter is required.
        self.user_answer = user_answer
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.content is not None:
            result['content'] = self.content
        if self.grade is not None:
            result['grade'] = self.grade
        if self.question_id is not None:
            result['questionId'] = self.question_id
        if self.question_info is not None:
            result['questionInfo'] = self.question_info
        if self.response_mode is not None:
            result['responseMode'] = self.response_mode
        if self.user_answer is not None:
            result['userAnswer'] = self.user_answer
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('questionId') is not None:
            self.question_id = m.get('questionId')
        if m.get('questionInfo') is not None:
            self.question_info = m.get('questionInfo')
        if m.get('responseMode') is not None:
            self.response_mode = m.get('responseMode')
        if m.get('userAnswer') is not None:
            self.user_answer = m.get('userAnswer')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ExecuteAITeacherEnglishParaphraseChatMessageResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        event: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.event = event
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.event is not None:
            result['event'] = self.event
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExecuteAITeacherEnglishParaphraseChatMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteAITeacherEnglishParaphraseChatMessageResponseBody = None,
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
            temp_model = ExecuteAITeacherEnglishParaphraseChatMessageResponseBody()
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


class ExecuteHundredThousandWhysDialogueRequestMessages(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
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
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ExecuteHundredThousandWhysDialogueRequest(TeaModel):
    def __init__(
        self,
        age_group: str = None,
        chat_id: str = None,
        device_id: str = None,
        mac_address: str = None,
        messages: List[ExecuteHundredThousandWhysDialogueRequestMessages] = None,
    ):
        self.age_group = age_group
        self.chat_id = chat_id
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.mac_address = mac_address
        # This parameter is required.
        self.messages = messages

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age_group is not None:
            result['ageGroup'] = self.age_group
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        result['messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['messages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ageGroup') is not None:
            self.age_group = m.get('ageGroup')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        self.messages = []
        if m.get('messages') is not None:
            for k in m.get('messages'):
                temp_model = ExecuteHundredThousandWhysDialogueRequestMessages()
                self.messages.append(temp_model.from_map(k))
        return self


class ExecuteHundredThousandWhysDialogueResponseBodyChoicesDelta(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
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
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ExecuteHundredThousandWhysDialogueResponseBodyChoices(TeaModel):
    def __init__(
        self,
        delta: ExecuteHundredThousandWhysDialogueResponseBodyChoicesDelta = None,
        finish_reason: str = None,
        index: int = None,
    ):
        self.delta = delta
        self.finish_reason = finish_reason
        self.index = index

    def validate(self):
        if self.delta:
            self.delta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delta is not None:
            result['delta'] = self.delta.to_map()
        if self.finish_reason is not None:
            result['finish_reason'] = self.finish_reason
        if self.index is not None:
            result['index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delta') is not None:
            temp_model = ExecuteHundredThousandWhysDialogueResponseBodyChoicesDelta()
            self.delta = temp_model.from_map(m['delta'])
        if m.get('finish_reason') is not None:
            self.finish_reason = m.get('finish_reason')
        if m.get('index') is not None:
            self.index = m.get('index')
        return self


class ExecuteHundredThousandWhysDialogueResponseBody(TeaModel):
    def __init__(
        self,
        choices: List[ExecuteHundredThousandWhysDialogueResponseBodyChoices] = None,
        created: int = None,
        id: str = None,
        model: str = None,
        object: str = None,
        request_id: str = None,
    ):
        self.choices = choices
        self.created = created
        self.id = id
        self.model = model
        self.object = object
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.model is not None:
            result['model'] = self.model
        if self.object is not None:
            result['object'] = self.object
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = ExecuteHundredThousandWhysDialogueResponseBodyChoices()
                self.choices.append(temp_model.from_map(k))
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('object') is not None:
            self.object = m.get('object')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExecuteHundredThousandWhysDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteHundredThousandWhysDialogueResponseBody = None,
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
            temp_model = ExecuteHundredThousandWhysDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantDialogueRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
        user_message: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario
        # This parameter is required.
        self.user_message = user_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.user_message is not None:
            result['userMessage'] = self.user_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('userMessage') is not None:
            self.user_message = m.get('userMessage')
        return self


class ExecuteTextbookAssistantDialogueResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        chinese_result: str = None,
        english_result: str = None,
        is_finish: bool = None,
        is_task_completed: bool = None,
    ):
        self.chinese_result = chinese_result
        self.english_result = english_result
        self.is_finish = is_finish
        self.is_task_completed = is_task_completed

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
        if self.is_task_completed is not None:
            result['isTaskCompleted'] = self.is_task_completed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chineseResult') is not None:
            self.chinese_result = m.get('chineseResult')
        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        if m.get('isTaskCompleted') is not None:
            self.is_task_completed = m.get('isTaskCompleted')
        return self


class ExecuteTextbookAssistantDialogueResponseBodyData(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        chat_id: str = None,
        result: ExecuteTextbookAssistantDialogueResponseBodyDataResult = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.chat_id = chat_id
        self.result = result
        self.user = user

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('result') is not None:
            temp_model = ExecuteTextbookAssistantDialogueResponseBodyDataResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteTextbookAssistantDialogueResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteTextbookAssistantDialogueResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            temp_model = ExecuteTextbookAssistantDialogueResponseBodyData()
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


class ExecuteTextbookAssistantDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantDialogueResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantDifficultyRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        assistant: str = None,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        return self


class ExecuteTextbookAssistantDifficultyResponseBodyDataResult(TeaModel):
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


class ExecuteTextbookAssistantDifficultyResponseBodyData(TeaModel):
    def __init__(
        self,
        result: ExecuteTextbookAssistantDifficultyResponseBodyDataResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ExecuteTextbookAssistantDifficultyResponseBodyDataResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ExecuteTextbookAssistantDifficultyResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteTextbookAssistantDifficultyResponseBodyData = None,
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
            temp_model = ExecuteTextbookAssistantDifficultyResponseBodyData()
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


class ExecuteTextbookAssistantDifficultyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantDifficultyResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantDifficultyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantGrammarCheckRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteTextbookAssistantGrammarCheckResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        analysis: str = None,
        correction: str = None,
        correction_status: str = None,
    ):
        self.analysis = analysis
        self.correction = correction
        self.correction_status = correction_status

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')
        if m.get('correction') is not None:
            self.correction = m.get('correction')
        if m.get('correctionStatus') is not None:
            self.correction_status = m.get('correctionStatus')
        return self


class ExecuteTextbookAssistantGrammarCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        result: ExecuteTextbookAssistantGrammarCheckResponseBodyDataResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ExecuteTextbookAssistantGrammarCheckResponseBodyDataResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ExecuteTextbookAssistantGrammarCheckResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteTextbookAssistantGrammarCheckResponseBodyData = None,
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
            temp_model = ExecuteTextbookAssistantGrammarCheckResponseBodyData()
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


class ExecuteTextbookAssistantGrammarCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantGrammarCheckResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantGrammarCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantRefineByContextRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteTextbookAssistantRefineByContextResponseBodyDataResult(TeaModel):
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


class ExecuteTextbookAssistantRefineByContextResponseBodyData(TeaModel):
    def __init__(
        self,
        result: ExecuteTextbookAssistantRefineByContextResponseBodyDataResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ExecuteTextbookAssistantRefineByContextResponseBodyDataResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ExecuteTextbookAssistantRefineByContextResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteTextbookAssistantRefineByContextResponseBodyData = None,
        err_code: str = None,
        err_message: int = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
            temp_model = ExecuteTextbookAssistantRefineByContextResponseBodyData()
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


class ExecuteTextbookAssistantRefineByContextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantRefineByContextResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantRefineByContextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantRetryConversationRequest(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        return self


class ExecuteTextbookAssistantRetryConversationResponseBodyDataResult(TeaModel):
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


class ExecuteTextbookAssistantRetryConversationResponseBodyData(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        chat_id: str = None,
        result: ExecuteTextbookAssistantRetryConversationResponseBodyDataResult = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.chat_id = chat_id
        self.result = result
        self.user = user

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('result') is not None:
            temp_model = ExecuteTextbookAssistantRetryConversationResponseBodyDataResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteTextbookAssistantRetryConversationResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteTextbookAssistantRetryConversationResponseBodyData = None,
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
            temp_model = ExecuteTextbookAssistantRetryConversationResponseBodyData()
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


class ExecuteTextbookAssistantRetryConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantRetryConversationResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantRetryConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantSseDialogueRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
        user_message: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario
        # This parameter is required.
        self.user_message = user_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.user_message is not None:
            result['userMessage'] = self.user_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('userMessage') is not None:
            self.user_message = m.get('userMessage')
        return self


class ExecuteTextbookAssistantSseDialogueResponseBodyData(TeaModel):
    def __init__(
        self,
        english_result: str = None,
        is_finish: bool = None,
    ):
        self.english_result = english_result
        self.is_finish = is_finish

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('englishResult') is not None:
            self.english_result = m.get('englishResult')
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        return self


class ExecuteTextbookAssistantSseDialogueResponseBody(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        chat_id: str = None,
        data: ExecuteTextbookAssistantSseDialogueResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.chat_id = chat_id
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.user = user

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('data') is not None:
            temp_model = ExecuteTextbookAssistantSseDialogueResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteTextbookAssistantSseDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantSseDialogueResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantSseDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantStartConversationRequest(TeaModel):
    def __init__(
        self,
        article_id: str = None,
        auth_token: str = None,
        scenario: str = None,
    ):
        # This parameter is required.
        self.article_id = article_id
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.article_id is not None:
            result['articleId'] = self.article_id
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.scenario is not None:
            result['scenario'] = self.scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('articleId') is not None:
            self.article_id = m.get('articleId')
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        return self


class ExecuteTextbookAssistantStartConversationResponseBodyDataResult(TeaModel):
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


class ExecuteTextbookAssistantStartConversationResponseBodyData(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        chat_id: str = None,
        result: ExecuteTextbookAssistantStartConversationResponseBodyDataResult = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.chat_id = chat_id
        self.result = result
        self.user = user

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('result') is not None:
            temp_model = ExecuteTextbookAssistantStartConversationResponseBodyDataResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ExecuteTextbookAssistantStartConversationResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteTextbookAssistantStartConversationResponseBodyData = None,
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
            temp_model = ExecuteTextbookAssistantStartConversationResponseBodyData()
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


class ExecuteTextbookAssistantStartConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantStartConversationResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantStartConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantSuggestionRequest(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        return self


class ExecuteTextbookAssistantSuggestionResponseBodyDataResult(TeaModel):
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


class ExecuteTextbookAssistantSuggestionResponseBodyData(TeaModel):
    def __init__(
        self,
        result: ExecuteTextbookAssistantSuggestionResponseBodyDataResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ExecuteTextbookAssistantSuggestionResponseBodyDataResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ExecuteTextbookAssistantSuggestionResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteTextbookAssistantSuggestionResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        httpstatus_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.httpstatus_code = httpstatus_code
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
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.httpstatus_code is not None:
            result['httpstatusCode'] = self.httpstatus_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ExecuteTextbookAssistantSuggestionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('httpstatusCode') is not None:
            self.httpstatus_code = m.get('httpstatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExecuteTextbookAssistantSuggestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantSuggestionResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantSuggestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTextbookAssistantTranslateRequest(TeaModel):
    def __init__(
        self,
        assistant: str = None,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
    ):
        # This parameter is required.
        self.assistant = assistant
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assistant is not None:
            result['assistant'] = self.assistant
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        return self


class ExecuteTextbookAssistantTranslateResponseBodyDataResult(TeaModel):
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


class ExecuteTextbookAssistantTranslateResponseBodyData(TeaModel):
    def __init__(
        self,
        result: ExecuteTextbookAssistantTranslateResponseBodyDataResult = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = ExecuteTextbookAssistantTranslateResponseBodyDataResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ExecuteTextbookAssistantTranslateResponseBody(TeaModel):
    def __init__(
        self,
        data: ExecuteTextbookAssistantTranslateResponseBodyData = None,
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
            temp_model = ExecuteTextbookAssistantTranslateResponseBodyData()
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


class ExecuteTextbookAssistantTranslateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTextbookAssistantTranslateResponseBody = None,
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
            temp_model = ExecuteTextbookAssistantTranslateResponseBody()
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


class GetTextbookAssistantTokenRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        model: str = None,
    ):
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.model is not None:
            result['model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('model') is not None:
            self.model = m.get('model')
        return self


class GetTextbookAssistantTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        expire: int = None,
    ):
        self.auth_token = auth_token
        self.expire = expire

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.expire is not None:
            result['expire'] = self.expire
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        return self


class GetTextbookAssistantTokenResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTextbookAssistantTokenResponseBodyData = None,
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
            temp_model = GetTextbookAssistantTokenResponseBodyData()
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


class GetTextbookAssistantTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTextbookAssistantTokenResponseBody = None,
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
            temp_model = GetTextbookAssistantTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTextbookAssistantArticleDetailsRequest(TeaModel):
    def __init__(
        self,
        article_id_list: List[str] = None,
        auth_token: str = None,
    ):
        self.article_id_list = article_id_list
        # This parameter is required.
        self.auth_token = auth_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.article_id_list is not None:
            result['articleIdList'] = self.article_id_list
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('articleIdList') is not None:
            self.article_id_list = m.get('articleIdList')
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        return self


class ListTextbookAssistantArticleDetailsResponseBodyDataQuestionList(TeaModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
        question_translate: str = None,
    ):
        self.answer = answer
        self.question = question
        self.question_translate = question_translate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['answer'] = self.answer
        if self.question is not None:
            result['question'] = self.question
        if self.question_translate is not None:
            result['questionTranslate'] = self.question_translate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')
        if m.get('question') is not None:
            self.question = m.get('question')
        if m.get('questionTranslate') is not None:
            self.question_translate = m.get('questionTranslate')
        return self


class ListTextbookAssistantArticleDetailsResponseBodyDataSceneList(TeaModel):
    def __init__(
        self,
        scene: str = None,
        scene_id: str = None,
        scene_image_list: List[str] = None,
        scene_translate: str = None,
    ):
        self.scene = scene
        self.scene_id = scene_id
        self.scene_image_list = scene_image_list
        self.scene_translate = scene_translate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['scene'] = self.scene
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.scene_image_list is not None:
            result['sceneImageList'] = self.scene_image_list
        if self.scene_translate is not None:
            result['sceneTranslate'] = self.scene_translate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('sceneImageList') is not None:
            self.scene_image_list = m.get('sceneImageList')
        if m.get('sceneTranslate') is not None:
            self.scene_translate = m.get('sceneTranslate')
        return self


class ListTextbookAssistantArticleDetailsResponseBodyDataSentenceList(TeaModel):
    def __init__(
        self,
        sentence_analysis: str = None,
        sentence_id: str = None,
        sentence_text: str = None,
    ):
        self.sentence_analysis = sentence_analysis
        self.sentence_id = sentence_id
        self.sentence_text = sentence_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sentence_analysis is not None:
            result['sentenceAnalysis'] = self.sentence_analysis
        if self.sentence_id is not None:
            result['sentenceId'] = self.sentence_id
        if self.sentence_text is not None:
            result['sentenceText'] = self.sentence_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sentenceAnalysis') is not None:
            self.sentence_analysis = m.get('sentenceAnalysis')
        if m.get('sentenceId') is not None:
            self.sentence_id = m.get('sentenceId')
        if m.get('sentenceText') is not None:
            self.sentence_text = m.get('sentenceText')
        return self


class ListTextbookAssistantArticleDetailsResponseBodyDataTheme(TeaModel):
    def __init__(
        self,
        theme_image_list: List[str] = None,
        theme_name: str = None,
        theme_translate: str = None,
    ):
        self.theme_image_list = theme_image_list
        self.theme_name = theme_name
        self.theme_translate = theme_translate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.theme_image_list is not None:
            result['themeImageList'] = self.theme_image_list
        if self.theme_name is not None:
            result['themeName'] = self.theme_name
        if self.theme_translate is not None:
            result['themeTranslate'] = self.theme_translate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('themeImageList') is not None:
            self.theme_image_list = m.get('themeImageList')
        if m.get('themeName') is not None:
            self.theme_name = m.get('themeName')
        if m.get('themeTranslate') is not None:
            self.theme_translate = m.get('themeTranslate')
        return self


class ListTextbookAssistantArticleDetailsResponseBodyDataTopic(TeaModel):
    def __init__(
        self,
        topic_image_list: List[str] = None,
        topic_name: str = None,
        topic_translate: str = None,
    ):
        self.topic_image_list = topic_image_list
        self.topic_name = topic_name
        self.topic_translate = topic_translate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_image_list is not None:
            result['topicImageList'] = self.topic_image_list
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.topic_translate is not None:
            result['topicTranslate'] = self.topic_translate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topicImageList') is not None:
            self.topic_image_list = m.get('topicImageList')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('topicTranslate') is not None:
            self.topic_translate = m.get('topicTranslate')
        return self


class ListTextbookAssistantArticleDetailsResponseBodyDataWordList(TeaModel):
    def __init__(
        self,
        word_analysis: str = None,
        word_id: str = None,
        word_text: str = None,
    ):
        self.word_analysis = word_analysis
        self.word_id = word_id
        self.word_text = word_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word_analysis is not None:
            result['wordAnalysis'] = self.word_analysis
        if self.word_id is not None:
            result['wordId'] = self.word_id
        if self.word_text is not None:
            result['wordText'] = self.word_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('wordAnalysis') is not None:
            self.word_analysis = m.get('wordAnalysis')
        if m.get('wordId') is not None:
            self.word_id = m.get('wordId')
        if m.get('wordText') is not None:
            self.word_text = m.get('wordText')
        return self


class ListTextbookAssistantArticleDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        article_id: str = None,
        question_list: List[ListTextbookAssistantArticleDetailsResponseBodyDataQuestionList] = None,
        scene_list: List[ListTextbookAssistantArticleDetailsResponseBodyDataSceneList] = None,
        sentence_list: List[ListTextbookAssistantArticleDetailsResponseBodyDataSentenceList] = None,
        target: str = None,
        theme: ListTextbookAssistantArticleDetailsResponseBodyDataTheme = None,
        topic: ListTextbookAssistantArticleDetailsResponseBodyDataTopic = None,
        word_list: List[ListTextbookAssistantArticleDetailsResponseBodyDataWordList] = None,
    ):
        self.article_id = article_id
        self.question_list = question_list
        self.scene_list = scene_list
        self.sentence_list = sentence_list
        self.target = target
        self.theme = theme
        self.topic = topic
        self.word_list = word_list

    def validate(self):
        if self.question_list:
            for k in self.question_list:
                if k:
                    k.validate()
        if self.scene_list:
            for k in self.scene_list:
                if k:
                    k.validate()
        if self.sentence_list:
            for k in self.sentence_list:
                if k:
                    k.validate()
        if self.theme:
            self.theme.validate()
        if self.topic:
            self.topic.validate()
        if self.word_list:
            for k in self.word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.article_id is not None:
            result['articleId'] = self.article_id
        result['questionList'] = []
        if self.question_list is not None:
            for k in self.question_list:
                result['questionList'].append(k.to_map() if k else None)
        result['sceneList'] = []
        if self.scene_list is not None:
            for k in self.scene_list:
                result['sceneList'].append(k.to_map() if k else None)
        result['sentenceList'] = []
        if self.sentence_list is not None:
            for k in self.sentence_list:
                result['sentenceList'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        if self.theme is not None:
            result['theme'] = self.theme.to_map()
        if self.topic is not None:
            result['topic'] = self.topic.to_map()
        result['wordList'] = []
        if self.word_list is not None:
            for k in self.word_list:
                result['wordList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('articleId') is not None:
            self.article_id = m.get('articleId')
        self.question_list = []
        if m.get('questionList') is not None:
            for k in m.get('questionList'):
                temp_model = ListTextbookAssistantArticleDetailsResponseBodyDataQuestionList()
                self.question_list.append(temp_model.from_map(k))
        self.scene_list = []
        if m.get('sceneList') is not None:
            for k in m.get('sceneList'):
                temp_model = ListTextbookAssistantArticleDetailsResponseBodyDataSceneList()
                self.scene_list.append(temp_model.from_map(k))
        self.sentence_list = []
        if m.get('sentenceList') is not None:
            for k in m.get('sentenceList'):
                temp_model = ListTextbookAssistantArticleDetailsResponseBodyDataSentenceList()
                self.sentence_list.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('theme') is not None:
            temp_model = ListTextbookAssistantArticleDetailsResponseBodyDataTheme()
            self.theme = temp_model.from_map(m['theme'])
        if m.get('topic') is not None:
            temp_model = ListTextbookAssistantArticleDetailsResponseBodyDataTopic()
            self.topic = temp_model.from_map(m['topic'])
        self.word_list = []
        if m.get('wordList') is not None:
            for k in m.get('wordList'):
                temp_model = ListTextbookAssistantArticleDetailsResponseBodyDataWordList()
                self.word_list.append(temp_model.from_map(k))
        return self


class ListTextbookAssistantArticleDetailsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListTextbookAssistantArticleDetailsResponseBodyData] = None,
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
                temp_model = ListTextbookAssistantArticleDetailsResponseBodyData()
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


class ListTextbookAssistantArticleDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTextbookAssistantArticleDetailsResponseBody = None,
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
            temp_model = ListTextbookAssistantArticleDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTextbookAssistantArticlesRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        directory_id: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        return self


class ListTextbookAssistantArticlesResponseBodyData(TeaModel):
    def __init__(
        self,
        article_id: str = None,
    ):
        self.article_id = article_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.article_id is not None:
            result['articleId'] = self.article_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('articleId') is not None:
            self.article_id = m.get('articleId')
        return self


class ListTextbookAssistantArticlesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListTextbookAssistantArticlesResponseBodyData] = None,
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
                temp_model = ListTextbookAssistantArticlesResponseBodyData()
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


class ListTextbookAssistantArticlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTextbookAssistantArticlesResponseBody = None,
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
            temp_model = ListTextbookAssistantArticlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTextbookAssistantBookDirectoriesRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        book_id: str = None,
        scenario: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.book_id = book_id
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.book_id is not None:
            result['bookId'] = self.book_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('bookId') is not None:
            self.book_id = m.get('bookId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        return self


class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeTopic(TeaModel):
    def __init__(
        self,
        label_id: str = None,
        label_name: str = None,
    ):
        self.label_id = label_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_id is not None:
            result['labelId'] = self.label_id
        if self.label_name is not None:
            result['labelName'] = self.label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')
        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')
        return self


class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSectionTopic(TeaModel):
    def __init__(
        self,
        label_id: str = None,
        label_name: str = None,
    ):
        self.label_id = label_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_id is not None:
            result['labelId'] = self.label_id
        if self.label_name is not None:
            result['labelName'] = self.label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')
        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')
        return self


class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSection(TeaModel):
    def __init__(
        self,
        children: Any = None,
        directory_id: str = None,
        directory_name: str = None,
        topic: List[ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSectionTopic] = None,
    ):
        self.children = children
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.topic = topic

    def validate(self):
        if self.topic:
            for k in self.topic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.children is not None:
            result['children'] = self.children
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.directory_name is not None:
            result['directoryName'] = self.directory_name
        result['topic'] = []
        if self.topic is not None:
            for k in self.topic:
                result['topic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('children') is not None:
            self.children = m.get('children')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('directoryName') is not None:
            self.directory_name = m.get('directoryName')
        self.topic = []
        if m.get('topic') is not None:
            for k in m.get('topic'):
                temp_model = ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSectionTopic()
                self.topic.append(temp_model.from_map(k))
        return self


class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitTopic(TeaModel):
    def __init__(
        self,
        label_id: str = None,
        label_name: str = None,
    ):
        self.label_id = label_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_id is not None:
            result['labelId'] = self.label_id
        if self.label_name is not None:
            result['labelName'] = self.label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')
        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')
        return self


class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnit(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        directory_name: str = None,
        section: List[ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSection] = None,
        topic: List[ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitTopic] = None,
    ):
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.section = section
        self.topic = topic

    def validate(self):
        if self.section:
            for k in self.section:
                if k:
                    k.validate()
        if self.topic:
            for k in self.topic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.directory_name is not None:
            result['directoryName'] = self.directory_name
        result['section'] = []
        if self.section is not None:
            for k in self.section:
                result['section'].append(k.to_map() if k else None)
        result['topic'] = []
        if self.topic is not None:
            for k in self.topic:
                result['topic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('directoryName') is not None:
            self.directory_name = m.get('directoryName')
        self.section = []
        if m.get('section') is not None:
            for k in m.get('section'):
                temp_model = ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSection()
                self.section.append(temp_model.from_map(k))
        self.topic = []
        if m.get('topic') is not None:
            for k in m.get('topic'):
                temp_model = ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitTopic()
                self.topic.append(temp_model.from_map(k))
        return self


class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTree(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        directory_name: str = None,
        topic: List[ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeTopic] = None,
        unit: List[ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnit] = None,
    ):
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.topic = topic
        self.unit = unit

    def validate(self):
        if self.topic:
            for k in self.topic:
                if k:
                    k.validate()
        if self.unit:
            for k in self.unit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.directory_name is not None:
            result['directoryName'] = self.directory_name
        result['topic'] = []
        if self.topic is not None:
            for k in self.topic:
                result['topic'].append(k.to_map() if k else None)
        result['unit'] = []
        if self.unit is not None:
            for k in self.unit:
                result['unit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('directoryName') is not None:
            self.directory_name = m.get('directoryName')
        self.topic = []
        if m.get('topic') is not None:
            for k in m.get('topic'):
                temp_model = ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeTopic()
                self.topic.append(temp_model.from_map(k))
        self.unit = []
        if m.get('unit') is not None:
            for k in m.get('unit'):
                temp_model = ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnit()
                self.unit.append(temp_model.from_map(k))
        return self


class ListTextbookAssistantBookDirectoriesResponseBodyDataEditionInfo(TeaModel):
    def __init__(
        self,
        book_id: str = None,
        book_volume: str = None,
        edition: str = None,
        grade: str = None,
        impression: str = None,
        isbn: str = None,
        publisher: str = None,
        subject: str = None,
        version: str = None,
    ):
        self.book_id = book_id
        self.book_volume = book_volume
        self.edition = edition
        self.grade = grade
        self.impression = impression
        self.isbn = isbn
        self.publisher = publisher
        self.subject = subject
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.book_id is not None:
            result['bookId'] = self.book_id
        if self.book_volume is not None:
            result['bookVolume'] = self.book_volume
        if self.edition is not None:
            result['edition'] = self.edition
        if self.grade is not None:
            result['grade'] = self.grade
        if self.impression is not None:
            result['impression'] = self.impression
        if self.isbn is not None:
            result['isbn'] = self.isbn
        if self.publisher is not None:
            result['publisher'] = self.publisher
        if self.subject is not None:
            result['subject'] = self.subject
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bookId') is not None:
            self.book_id = m.get('bookId')
        if m.get('bookVolume') is not None:
            self.book_volume = m.get('bookVolume')
        if m.get('edition') is not None:
            self.edition = m.get('edition')
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('impression') is not None:
            self.impression = m.get('impression')
        if m.get('isbn') is not None:
            self.isbn = m.get('isbn')
        if m.get('publisher') is not None:
            self.publisher = m.get('publisher')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListTextbookAssistantBookDirectoriesResponseBodyData(TeaModel):
    def __init__(
        self,
        directory_tree: List[ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTree] = None,
        edition_info: ListTextbookAssistantBookDirectoriesResponseBodyDataEditionInfo = None,
    ):
        self.directory_tree = directory_tree
        self.edition_info = edition_info

    def validate(self):
        if self.directory_tree:
            for k in self.directory_tree:
                if k:
                    k.validate()
        if self.edition_info:
            self.edition_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['directoryTree'] = []
        if self.directory_tree is not None:
            for k in self.directory_tree:
                result['directoryTree'].append(k.to_map() if k else None)
        if self.edition_info is not None:
            result['editionInfo'] = self.edition_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directory_tree = []
        if m.get('directoryTree') is not None:
            for k in m.get('directoryTree'):
                temp_model = ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTree()
                self.directory_tree.append(temp_model.from_map(k))
        if m.get('editionInfo') is not None:
            temp_model = ListTextbookAssistantBookDirectoriesResponseBodyDataEditionInfo()
            self.edition_info = temp_model.from_map(m['editionInfo'])
        return self


class ListTextbookAssistantBookDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTextbookAssistantBookDirectoriesResponseBodyData = None,
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
            temp_model = ListTextbookAssistantBookDirectoriesResponseBodyData()
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


class ListTextbookAssistantBookDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTextbookAssistantBookDirectoriesResponseBody = None,
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
            temp_model = ListTextbookAssistantBookDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTextbookAssistantBooksRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        book_id: str = None,
        grade: str = None,
        max_results: str = None,
        page: str = None,
        version: str = None,
        volume: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        self.book_id = book_id
        self.grade = grade
        self.max_results = max_results
        self.page = page
        self.version = version
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.book_id is not None:
            result['bookId'] = self.book_id
        if self.grade is not None:
            result['grade'] = self.grade
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page is not None:
            result['page'] = self.page
        if self.version is not None:
            result['version'] = self.version
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('bookId') is not None:
            self.book_id = m.get('bookId')
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
        return self


class ListTextbookAssistantBooksResponseBodyDataBookList(TeaModel):
    def __init__(
        self,
        author: str = None,
        book_id: str = None,
        book_name: str = None,
        cover_image: str = None,
        edition: str = None,
        grade: str = None,
        impression: str = None,
        isbn: str = None,
        publisher: str = None,
        subject: str = None,
        version: str = None,
        volume: str = None,
    ):
        self.author = author
        self.book_id = book_id
        self.book_name = book_name
        self.cover_image = cover_image
        self.edition = edition
        self.grade = grade
        self.impression = impression
        self.isbn = isbn
        self.publisher = publisher
        self.subject = subject
        self.version = version
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['author'] = self.author
        if self.book_id is not None:
            result['bookId'] = self.book_id
        if self.book_name is not None:
            result['bookName'] = self.book_name
        if self.cover_image is not None:
            result['coverImage'] = self.cover_image
        if self.edition is not None:
            result['edition'] = self.edition
        if self.grade is not None:
            result['grade'] = self.grade
        if self.impression is not None:
            result['impression'] = self.impression
        if self.isbn is not None:
            result['isbn'] = self.isbn
        if self.publisher is not None:
            result['publisher'] = self.publisher
        if self.subject is not None:
            result['subject'] = self.subject
        if self.version is not None:
            result['version'] = self.version
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('author') is not None:
            self.author = m.get('author')
        if m.get('bookId') is not None:
            self.book_id = m.get('bookId')
        if m.get('bookName') is not None:
            self.book_name = m.get('bookName')
        if m.get('coverImage') is not None:
            self.cover_image = m.get('coverImage')
        if m.get('edition') is not None:
            self.edition = m.get('edition')
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('impression') is not None:
            self.impression = m.get('impression')
        if m.get('isbn') is not None:
            self.isbn = m.get('isbn')
        if m.get('publisher') is not None:
            self.publisher = m.get('publisher')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
        return self


class ListTextbookAssistantBooksResponseBodyDataPaginationData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        max_results: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.max_results = max_results
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTextbookAssistantBooksResponseBodyData(TeaModel):
    def __init__(
        self,
        book_list: List[ListTextbookAssistantBooksResponseBodyDataBookList] = None,
        pagination_data: ListTextbookAssistantBooksResponseBodyDataPaginationData = None,
    ):
        self.book_list = book_list
        self.pagination_data = pagination_data

    def validate(self):
        if self.book_list:
            for k in self.book_list:
                if k:
                    k.validate()
        if self.pagination_data:
            self.pagination_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['bookList'] = []
        if self.book_list is not None:
            for k in self.book_list:
                result['bookList'].append(k.to_map() if k else None)
        if self.pagination_data is not None:
            result['paginationData'] = self.pagination_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.book_list = []
        if m.get('bookList') is not None:
            for k in m.get('bookList'):
                temp_model = ListTextbookAssistantBooksResponseBodyDataBookList()
                self.book_list.append(temp_model.from_map(k))
        if m.get('paginationData') is not None:
            temp_model = ListTextbookAssistantBooksResponseBodyDataPaginationData()
            self.pagination_data = temp_model.from_map(m['paginationData'])
        return self


class ListTextbookAssistantBooksResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTextbookAssistantBooksResponseBodyData = None,
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
            temp_model = ListTextbookAssistantBooksResponseBodyData()
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


class ListTextbookAssistantBooksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTextbookAssistantBooksResponseBody = None,
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
            temp_model = ListTextbookAssistantBooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTextbookAssistantGradeVolumesRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        scenario: str = None,
    ):
        self.auth_token = auth_token
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.scenario is not None:
            result['scenario'] = self.scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        return self


class ListTextbookAssistantGradeVolumesResponseBodyDataGradeVolumes(TeaModel):
    def __init__(
        self,
        grade: str = None,
        volume: str = None,
    ):
        self.grade = grade
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grade is not None:
            result['grade'] = self.grade
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
        return self


class ListTextbookAssistantGradeVolumesResponseBodyData(TeaModel):
    def __init__(
        self,
        grade_volumes: List[ListTextbookAssistantGradeVolumesResponseBodyDataGradeVolumes] = None,
        textbook_version: str = None,
    ):
        self.grade_volumes = grade_volumes
        self.textbook_version = textbook_version

    def validate(self):
        if self.grade_volumes:
            for k in self.grade_volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['gradeVolumes'] = []
        if self.grade_volumes is not None:
            for k in self.grade_volumes:
                result['gradeVolumes'].append(k.to_map() if k else None)
        if self.textbook_version is not None:
            result['textbookVersion'] = self.textbook_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grade_volumes = []
        if m.get('gradeVolumes') is not None:
            for k in m.get('gradeVolumes'):
                temp_model = ListTextbookAssistantGradeVolumesResponseBodyDataGradeVolumes()
                self.grade_volumes.append(temp_model.from_map(k))
        if m.get('textbookVersion') is not None:
            self.textbook_version = m.get('textbookVersion')
        return self


class ListTextbookAssistantGradeVolumesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListTextbookAssistantGradeVolumesResponseBodyData] = None,
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
                temp_model = ListTextbookAssistantGradeVolumesResponseBodyData()
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


class ListTextbookAssistantGradeVolumesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTextbookAssistantGradeVolumesResponseBody = None,
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
            temp_model = ListTextbookAssistantGradeVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTextbookAssistantSceneDetailsRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        scene_id_list: List[str] = None,
    ):
        self.auth_token = auth_token
        self.scene_id_list = scene_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.scene_id_list is not None:
            result['sceneIdList'] = self.scene_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('sceneIdList') is not None:
            self.scene_id_list = m.get('sceneIdList')
        return self


class ListTextbookAssistantSceneDetailsResponseBodyDataRoleList(TeaModel):
    def __init__(
        self,
        introduction: str = None,
        introduction_translate: str = None,
        promoting: str = None,
        promoting_translate: str = None,
        role_name: str = None,
        role_name_translate: str = None,
        role_type: str = None,
    ):
        self.introduction = introduction
        self.introduction_translate = introduction_translate
        self.promoting = promoting
        self.promoting_translate = promoting_translate
        self.role_name = role_name
        self.role_name_translate = role_name_translate
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.introduction is not None:
            result['introduction'] = self.introduction
        if self.introduction_translate is not None:
            result['introductionTranslate'] = self.introduction_translate
        if self.promoting is not None:
            result['promoting'] = self.promoting
        if self.promoting_translate is not None:
            result['promotingTranslate'] = self.promoting_translate
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.role_name_translate is not None:
            result['roleNameTranslate'] = self.role_name_translate
        if self.role_type is not None:
            result['roleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('introduction') is not None:
            self.introduction = m.get('introduction')
        if m.get('introductionTranslate') is not None:
            self.introduction_translate = m.get('introductionTranslate')
        if m.get('promoting') is not None:
            self.promoting = m.get('promoting')
        if m.get('promotingTranslate') is not None:
            self.promoting_translate = m.get('promotingTranslate')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('roleNameTranslate') is not None:
            self.role_name_translate = m.get('roleNameTranslate')
        if m.get('roleType') is not None:
            self.role_type = m.get('roleType')
        return self


class ListTextbookAssistantSceneDetailsResponseBodyDataSceneTaskList(TeaModel):
    def __init__(
        self,
        scene_task: str = None,
        scene_task_translate: str = None,
    ):
        self.scene_task = scene_task
        self.scene_task_translate = scene_task_translate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_task is not None:
            result['sceneTask'] = self.scene_task
        if self.scene_task_translate is not None:
            result['sceneTaskTranslate'] = self.scene_task_translate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneTask') is not None:
            self.scene_task = m.get('sceneTask')
        if m.get('sceneTaskTranslate') is not None:
            self.scene_task_translate = m.get('sceneTaskTranslate')
        return self


class ListTextbookAssistantSceneDetailsResponseBodyDataSentenceList(TeaModel):
    def __init__(
        self,
        sentence_analysis: str = None,
        sentence_id: str = None,
        sentence_text: str = None,
    ):
        self.sentence_analysis = sentence_analysis
        self.sentence_id = sentence_id
        self.sentence_text = sentence_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sentence_analysis is not None:
            result['sentenceAnalysis'] = self.sentence_analysis
        if self.sentence_id is not None:
            result['sentenceId'] = self.sentence_id
        if self.sentence_text is not None:
            result['sentenceText'] = self.sentence_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sentenceAnalysis') is not None:
            self.sentence_analysis = m.get('sentenceAnalysis')
        if m.get('sentenceId') is not None:
            self.sentence_id = m.get('sentenceId')
        if m.get('sentenceText') is not None:
            self.sentence_text = m.get('sentenceText')
        return self


class ListTextbookAssistantSceneDetailsResponseBodyDataTheme(TeaModel):
    def __init__(
        self,
        theme_image_list: List[str] = None,
        theme_name: str = None,
        theme_translate: str = None,
    ):
        self.theme_image_list = theme_image_list
        self.theme_name = theme_name
        self.theme_translate = theme_translate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.theme_image_list is not None:
            result['themeImageList'] = self.theme_image_list
        if self.theme_name is not None:
            result['themeName'] = self.theme_name
        if self.theme_translate is not None:
            result['themeTranslate'] = self.theme_translate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('themeImageList') is not None:
            self.theme_image_list = m.get('themeImageList')
        if m.get('themeName') is not None:
            self.theme_name = m.get('themeName')
        if m.get('themeTranslate') is not None:
            self.theme_translate = m.get('themeTranslate')
        return self


class ListTextbookAssistantSceneDetailsResponseBodyDataTopic(TeaModel):
    def __init__(
        self,
        topic_image_list: List[str] = None,
        topic_name: str = None,
        topic_translate: str = None,
    ):
        self.topic_image_list = topic_image_list
        self.topic_name = topic_name
        self.topic_translate = topic_translate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_image_list is not None:
            result['topicImageList'] = self.topic_image_list
        if self.topic_name is not None:
            result['topicName'] = self.topic_name
        if self.topic_translate is not None:
            result['topicTranslate'] = self.topic_translate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topicImageList') is not None:
            self.topic_image_list = m.get('topicImageList')
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')
        if m.get('topicTranslate') is not None:
            self.topic_translate = m.get('topicTranslate')
        return self


class ListTextbookAssistantSceneDetailsResponseBodyDataWordList(TeaModel):
    def __init__(
        self,
        word_analysis: str = None,
        word_id: str = None,
        word_text: str = None,
    ):
        self.word_analysis = word_analysis
        self.word_id = word_id
        self.word_text = word_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word_analysis is not None:
            result['wordAnalysis'] = self.word_analysis
        if self.word_id is not None:
            result['wordId'] = self.word_id
        if self.word_text is not None:
            result['wordText'] = self.word_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('wordAnalysis') is not None:
            self.word_analysis = m.get('wordAnalysis')
        if m.get('wordId') is not None:
            self.word_id = m.get('wordId')
        if m.get('wordText') is not None:
            self.word_text = m.get('wordText')
        return self


class ListTextbookAssistantSceneDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        role_list: List[ListTextbookAssistantSceneDetailsResponseBodyDataRoleList] = None,
        scene: str = None,
        scene_id: str = None,
        scene_image_list: List[str] = None,
        scene_task_list: List[ListTextbookAssistantSceneDetailsResponseBodyDataSceneTaskList] = None,
        scene_translate: str = None,
        sentence_list: List[ListTextbookAssistantSceneDetailsResponseBodyDataSentenceList] = None,
        target: str = None,
        theme: ListTextbookAssistantSceneDetailsResponseBodyDataTheme = None,
        topic: ListTextbookAssistantSceneDetailsResponseBodyDataTopic = None,
        word_list: List[ListTextbookAssistantSceneDetailsResponseBodyDataWordList] = None,
    ):
        self.role_list = role_list
        self.scene = scene
        self.scene_id = scene_id
        self.scene_image_list = scene_image_list
        self.scene_task_list = scene_task_list
        self.scene_translate = scene_translate
        self.sentence_list = sentence_list
        self.target = target
        self.theme = theme
        self.topic = topic
        self.word_list = word_list

    def validate(self):
        if self.role_list:
            for k in self.role_list:
                if k:
                    k.validate()
        if self.scene_task_list:
            for k in self.scene_task_list:
                if k:
                    k.validate()
        if self.sentence_list:
            for k in self.sentence_list:
                if k:
                    k.validate()
        if self.theme:
            self.theme.validate()
        if self.topic:
            self.topic.validate()
        if self.word_list:
            for k in self.word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['roleList'] = []
        if self.role_list is not None:
            for k in self.role_list:
                result['roleList'].append(k.to_map() if k else None)
        if self.scene is not None:
            result['scene'] = self.scene
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.scene_image_list is not None:
            result['sceneImageList'] = self.scene_image_list
        result['sceneTaskList'] = []
        if self.scene_task_list is not None:
            for k in self.scene_task_list:
                result['sceneTaskList'].append(k.to_map() if k else None)
        if self.scene_translate is not None:
            result['sceneTranslate'] = self.scene_translate
        result['sentenceList'] = []
        if self.sentence_list is not None:
            for k in self.sentence_list:
                result['sentenceList'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        if self.theme is not None:
            result['theme'] = self.theme.to_map()
        if self.topic is not None:
            result['topic'] = self.topic.to_map()
        result['wordList'] = []
        if self.word_list is not None:
            for k in self.word_list:
                result['wordList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_list = []
        if m.get('roleList') is not None:
            for k in m.get('roleList'):
                temp_model = ListTextbookAssistantSceneDetailsResponseBodyDataRoleList()
                self.role_list.append(temp_model.from_map(k))
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('sceneImageList') is not None:
            self.scene_image_list = m.get('sceneImageList')
        self.scene_task_list = []
        if m.get('sceneTaskList') is not None:
            for k in m.get('sceneTaskList'):
                temp_model = ListTextbookAssistantSceneDetailsResponseBodyDataSceneTaskList()
                self.scene_task_list.append(temp_model.from_map(k))
        if m.get('sceneTranslate') is not None:
            self.scene_translate = m.get('sceneTranslate')
        self.sentence_list = []
        if m.get('sentenceList') is not None:
            for k in m.get('sentenceList'):
                temp_model = ListTextbookAssistantSceneDetailsResponseBodyDataSentenceList()
                self.sentence_list.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('theme') is not None:
            temp_model = ListTextbookAssistantSceneDetailsResponseBodyDataTheme()
            self.theme = temp_model.from_map(m['theme'])
        if m.get('topic') is not None:
            temp_model = ListTextbookAssistantSceneDetailsResponseBodyDataTopic()
            self.topic = temp_model.from_map(m['topic'])
        self.word_list = []
        if m.get('wordList') is not None:
            for k in m.get('wordList'):
                temp_model = ListTextbookAssistantSceneDetailsResponseBodyDataWordList()
                self.word_list.append(temp_model.from_map(k))
        return self


class ListTextbookAssistantSceneDetailsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListTextbookAssistantSceneDetailsResponseBodyData] = None,
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
                temp_model = ListTextbookAssistantSceneDetailsResponseBodyData()
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


class ListTextbookAssistantSceneDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTextbookAssistantSceneDetailsResponseBody = None,
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
            temp_model = ListTextbookAssistantSceneDetailsResponseBody()
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


class QueryApplicationAccessIdRequest(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
    ):
        self.application_access_id = application_access_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        return self


class QueryApplicationAccessIdResponseBodyData(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
        application_access_secret: str = None,
    ):
        self.application_access_id = application_access_id
        self.application_access_secret = application_access_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        if self.application_access_secret is not None:
            result['applicationAccessSecret'] = self.application_access_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        if m.get('applicationAccessSecret') is not None:
            self.application_access_secret = m.get('applicationAccessSecret')
        return self


class QueryApplicationAccessIdResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryApplicationAccessIdResponseBodyData = None,
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
            temp_model = QueryApplicationAccessIdResponseBodyData()
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


class QueryApplicationAccessIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryApplicationAccessIdResponseBody = None,
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
            temp_model = QueryApplicationAccessIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class QueryProjectResponseBodyDataProjectAppsApplicationAccessIds(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
        application_access_secret: str = None,
    ):
        self.application_access_id = application_access_id
        self.application_access_secret = application_access_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        if self.application_access_secret is not None:
            result['applicationAccessSecret'] = self.application_access_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        if m.get('applicationAccessSecret') is not None:
            self.application_access_secret = m.get('applicationAccessSecret')
        return self


class QueryProjectResponseBodyDataProjectApps(TeaModel):
    def __init__(
        self,
        application_access_ids: List[QueryProjectResponseBodyDataProjectAppsApplicationAccessIds] = None,
        id: str = None,
        project_id: str = None,
    ):
        self.application_access_ids = application_access_ids
        self.id = id
        self.project_id = project_id

    def validate(self):
        if self.application_access_ids:
            for k in self.application_access_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationAccessIds'] = []
        if self.application_access_ids is not None:
            for k in self.application_access_ids:
                result['ApplicationAccessIds'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_access_ids = []
        if m.get('ApplicationAccessIds') is not None:
            for k in m.get('ApplicationAccessIds'):
                temp_model = QueryProjectResponseBodyDataProjectAppsApplicationAccessIds()
                self.application_access_ids.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryProjectResponseBodyDataProjectSDK(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        demo_url: str = None,
        deploy_mode: str = None,
        develop_language: str = None,
        doc_url: str = None,
        sdk_name: str = None,
        sdk_url: str = None,
        sdk_version: str = None,
    ):
        self.create_time = create_time
        self.demo_url = demo_url
        self.deploy_mode = deploy_mode
        self.develop_language = develop_language
        self.doc_url = doc_url
        self.sdk_name = sdk_name
        self.sdk_url = sdk_url
        self.sdk_version = sdk_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.demo_url is not None:
            result['DemoUrl'] = self.demo_url
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.develop_language is not None:
            result['DevelopLanguage'] = self.develop_language
        if self.doc_url is not None:
            result['DocUrl'] = self.doc_url
        if self.sdk_name is not None:
            result['SdkName'] = self.sdk_name
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DemoUrl') is not None:
            self.demo_url = m.get('DemoUrl')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DevelopLanguage') is not None:
            self.develop_language = m.get('DevelopLanguage')
        if m.get('DocUrl') is not None:
            self.doc_url = m.get('DocUrl')
        if m.get('SdkName') is not None:
            self.sdk_name = m.get('SdkName')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        return self


class QueryProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        project_apps: List[QueryProjectResponseBodyDataProjectApps] = None,
        project_id: str = None,
        project_name: str = None,
        project_sdk: List[QueryProjectResponseBodyDataProjectSDK] = None,
        project_type: str = None,
    ):
        self.create_time = create_time
        self.project_apps = project_apps
        self.project_id = project_id
        self.project_name = project_name
        self.project_sdk = project_sdk
        self.project_type = project_type

    def validate(self):
        if self.project_apps:
            for k in self.project_apps:
                if k:
                    k.validate()
        if self.project_sdk:
            for k in self.project_sdk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['ProjectApps'] = []
        if self.project_apps is not None:
            for k in self.project_apps:
                result['ProjectApps'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['ProjectSDK'] = []
        if self.project_sdk is not None:
            for k in self.project_sdk:
                result['ProjectSDK'].append(k.to_map() if k else None)
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.project_apps = []
        if m.get('ProjectApps') is not None:
            for k in m.get('ProjectApps'):
                temp_model = QueryProjectResponseBodyDataProjectApps()
                self.project_apps.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.project_sdk = []
        if m.get('ProjectSDK') is not None:
            for k in m.get('ProjectSDK'):
                temp_model = QueryProjectResponseBodyDataProjectSDK()
                self.project_sdk.append(temp_model.from_map(k))
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        return self


class QueryProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryProjectResponseBodyData = None,
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
            temp_model = QueryProjectResponseBodyData()
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


class QueryProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProjectResponseBody = None,
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
            temp_model = QueryProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectListResponseBodyDataProjectAppsApplicationAccessIds(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
        application_access_secret: str = None,
    ):
        self.application_access_id = application_access_id
        self.application_access_secret = application_access_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        if self.application_access_secret is not None:
            result['applicationAccessSecret'] = self.application_access_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        if m.get('applicationAccessSecret') is not None:
            self.application_access_secret = m.get('applicationAccessSecret')
        return self


class QueryProjectListResponseBodyDataProjectApps(TeaModel):
    def __init__(
        self,
        application_access_ids: List[QueryProjectListResponseBodyDataProjectAppsApplicationAccessIds] = None,
        id: str = None,
        project_id: str = None,
    ):
        self.application_access_ids = application_access_ids
        self.id = id
        self.project_id = project_id

    def validate(self):
        if self.application_access_ids:
            for k in self.application_access_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationAccessIds'] = []
        if self.application_access_ids is not None:
            for k in self.application_access_ids:
                result['ApplicationAccessIds'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_access_ids = []
        if m.get('ApplicationAccessIds') is not None:
            for k in m.get('ApplicationAccessIds'):
                temp_model = QueryProjectListResponseBodyDataProjectAppsApplicationAccessIds()
                self.application_access_ids.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryProjectListResponseBodyDataProjectSDK(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        demo_url: str = None,
        deploy_mode: str = None,
        develop_language: str = None,
        doc_url: str = None,
        sdk_name: str = None,
        sdk_url: str = None,
        sdk_version: str = None,
    ):
        self.create_time = create_time
        self.demo_url = demo_url
        self.deploy_mode = deploy_mode
        self.develop_language = develop_language
        self.doc_url = doc_url
        self.sdk_name = sdk_name
        self.sdk_url = sdk_url
        self.sdk_version = sdk_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.demo_url is not None:
            result['DemoUrl'] = self.demo_url
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.develop_language is not None:
            result['DevelopLanguage'] = self.develop_language
        if self.doc_url is not None:
            result['DocUrl'] = self.doc_url
        if self.sdk_name is not None:
            result['SdkName'] = self.sdk_name
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DemoUrl') is not None:
            self.demo_url = m.get('DemoUrl')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DevelopLanguage') is not None:
            self.develop_language = m.get('DevelopLanguage')
        if m.get('DocUrl') is not None:
            self.doc_url = m.get('DocUrl')
        if m.get('SdkName') is not None:
            self.sdk_name = m.get('SdkName')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        return self


class QueryProjectListResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        project_apps: List[QueryProjectListResponseBodyDataProjectApps] = None,
        project_id: str = None,
        project_name: str = None,
        project_sdk: List[QueryProjectListResponseBodyDataProjectSDK] = None,
        project_type: str = None,
    ):
        self.create_time = create_time
        self.project_apps = project_apps
        self.project_id = project_id
        self.project_name = project_name
        self.project_sdk = project_sdk
        self.project_type = project_type

    def validate(self):
        if self.project_apps:
            for k in self.project_apps:
                if k:
                    k.validate()
        if self.project_sdk:
            for k in self.project_sdk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['ProjectApps'] = []
        if self.project_apps is not None:
            for k in self.project_apps:
                result['ProjectApps'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['ProjectSDK'] = []
        if self.project_sdk is not None:
            for k in self.project_sdk:
                result['ProjectSDK'].append(k.to_map() if k else None)
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.project_apps = []
        if m.get('ProjectApps') is not None:
            for k in m.get('ProjectApps'):
                temp_model = QueryProjectListResponseBodyDataProjectApps()
                self.project_apps.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.project_sdk = []
        if m.get('ProjectSDK') is not None:
            for k in m.get('ProjectSDK'):
                temp_model = QueryProjectListResponseBodyDataProjectSDK()
                self.project_sdk.append(temp_model.from_map(k))
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        return self


class QueryProjectListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryProjectListResponseBodyData] = None,
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
                temp_model = QueryProjectListResponseBodyData()
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


class QueryProjectListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProjectListResponseBody = None,
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
            temp_model = QueryProjectListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPurchasedServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AliyunConsoleServiceInfoDTO] = None,
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
                temp_model = AliyunConsoleServiceInfoDTO()
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


class QueryPurchasedServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPurchasedServiceResponseBody = None,
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
            temp_model = QueryPurchasedServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        project_name: str = None,
    ):
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class UpdateProjectResponseBodyDataProjectAppsApplicationAccessIds(TeaModel):
    def __init__(
        self,
        application_access_id: str = None,
        application_access_secret: str = None,
    ):
        self.application_access_id = application_access_id
        self.application_access_secret = application_access_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id
        if self.application_access_secret is not None:
            result['applicationAccessSecret'] = self.application_access_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')
        if m.get('applicationAccessSecret') is not None:
            self.application_access_secret = m.get('applicationAccessSecret')
        return self


class UpdateProjectResponseBodyDataProjectApps(TeaModel):
    def __init__(
        self,
        application_access_ids: List[UpdateProjectResponseBodyDataProjectAppsApplicationAccessIds] = None,
        id: str = None,
        project_id: str = None,
    ):
        self.application_access_ids = application_access_ids
        self.id = id
        self.project_id = project_id

    def validate(self):
        if self.application_access_ids:
            for k in self.application_access_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationAccessIds'] = []
        if self.application_access_ids is not None:
            for k in self.application_access_ids:
                result['ApplicationAccessIds'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_access_ids = []
        if m.get('ApplicationAccessIds') is not None:
            for k in m.get('ApplicationAccessIds'):
                temp_model = UpdateProjectResponseBodyDataProjectAppsApplicationAccessIds()
                self.application_access_ids.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateProjectResponseBodyDataProjectSDK(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        demo_url: str = None,
        deploy_mode: str = None,
        develop_language: str = None,
        doc_url: str = None,
        sdk_name: str = None,
        sdk_url: str = None,
        sdk_version: str = None,
    ):
        self.create_time = create_time
        self.demo_url = demo_url
        self.deploy_mode = deploy_mode
        self.develop_language = develop_language
        self.doc_url = doc_url
        self.sdk_name = sdk_name
        self.sdk_url = sdk_url
        self.sdk_version = sdk_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.demo_url is not None:
            result['DemoUrl'] = self.demo_url
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.develop_language is not None:
            result['DevelopLanguage'] = self.develop_language
        if self.doc_url is not None:
            result['DocUrl'] = self.doc_url
        if self.sdk_name is not None:
            result['SdkName'] = self.sdk_name
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DemoUrl') is not None:
            self.demo_url = m.get('DemoUrl')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DevelopLanguage') is not None:
            self.develop_language = m.get('DevelopLanguage')
        if m.get('DocUrl') is not None:
            self.doc_url = m.get('DocUrl')
        if m.get('SdkName') is not None:
            self.sdk_name = m.get('SdkName')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        return self


class UpdateProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        project_apps: List[UpdateProjectResponseBodyDataProjectApps] = None,
        project_id: str = None,
        project_name: str = None,
        project_sdk: List[UpdateProjectResponseBodyDataProjectSDK] = None,
        project_type: str = None,
    ):
        self.create_time = create_time
        self.project_apps = project_apps
        self.project_id = project_id
        self.project_name = project_name
        self.project_sdk = project_sdk
        self.project_type = project_type

    def validate(self):
        if self.project_apps:
            for k in self.project_apps:
                if k:
                    k.validate()
        if self.project_sdk:
            for k in self.project_sdk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['ProjectApps'] = []
        if self.project_apps is not None:
            for k in self.project_apps:
                result['ProjectApps'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['ProjectSDK'] = []
        if self.project_sdk is not None:
            for k in self.project_sdk:
                result['ProjectSDK'].append(k.to_map() if k else None)
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.project_apps = []
        if m.get('ProjectApps') is not None:
            for k in m.get('ProjectApps'):
                temp_model = UpdateProjectResponseBodyDataProjectApps()
                self.project_apps.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.project_sdk = []
        if m.get('ProjectSDK') is not None:
            for k in m.get('ProjectSDK'):
                temp_model = UpdateProjectResponseBodyDataProjectSDK()
                self.project_sdk.append(temp_model.from_map(k))
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateProjectResponseBodyData = None,
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
            temp_model = UpdateProjectResponseBodyData()
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


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectResponseBody = None,
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


