# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CreateAIJobRequestInputsDes(TeaModel):
    def __init__(
        self,
        band_no: str = None,
        data_id: str = None,
    ):
        self.band_no = band_no
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_no is not None:
            result['BandNo'] = self.band_no
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandNo') is not None:
            self.band_no = m.get('BandNo')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class CreateAIJobRequestInputsSrc(TeaModel):
    def __init__(
        self,
        band_no: str = None,
        data_id: str = None,
    ):
        self.band_no = band_no
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_no is not None:
            result['BandNo'] = self.band_no
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandNo') is not None:
            self.band_no = m.get('BandNo')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class CreateAIJobRequestInputs(TeaModel):
    def __init__(
        self,
        des: CreateAIJobRequestInputsDes = None,
        idx: int = None,
        src: CreateAIJobRequestInputsSrc = None,
    ):
        self.des = des
        self.idx = idx
        self.src = src

    def validate(self):
        if self.des:
            self.des.validate()
        if self.src:
            self.src.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.des is not None:
            result['Des'] = self.des.to_map()
        if self.idx is not None:
            result['Idx'] = self.idx
        if self.src is not None:
            result['Src'] = self.src.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Des') is not None:
            temp_model = CreateAIJobRequestInputsDes()
            self.des = temp_model.from_map(m['Des'])
        if m.get('Idx') is not None:
            self.idx = m.get('Idx')
        if m.get('Src') is not None:
            temp_model = CreateAIJobRequestInputsSrc()
            self.src = temp_model.from_map(m['Src'])
        return self


class CreateAIJobRequest(TeaModel):
    def __init__(
        self,
        app: str = None,
        area_threshold: float = None,
        confidence: float = None,
        inputs: List[CreateAIJobRequestInputs] = None,
        job_name: str = None,
        model_project_id: int = None,
        model_version: str = None,
        project_id: int = None,
        shape_data_id: str = None,
        shape_wkt: str = None,
    ):
        self.app = app
        self.area_threshold = area_threshold
        self.confidence = confidence
        self.inputs = inputs
        self.job_name = job_name
        self.model_project_id = model_project_id
        self.model_version = model_version
        self.project_id = project_id
        self.shape_data_id = shape_data_id
        self.shape_wkt = shape_wkt

    def validate(self):
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.area_threshold is not None:
            result['AreaThreshold'] = self.area_threshold
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.model_project_id is not None:
            result['ModelProjectId'] = self.model_project_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.shape_data_id is not None:
            result['ShapeDataId'] = self.shape_data_id
        if self.shape_wkt is not None:
            result['ShapeWkt'] = self.shape_wkt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('AreaThreshold') is not None:
            self.area_threshold = m.get('AreaThreshold')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = CreateAIJobRequestInputs()
                self.inputs.append(temp_model.from_map(k))
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('ModelProjectId') is not None:
            self.model_project_id = m.get('ModelProjectId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ShapeDataId') is not None:
            self.shape_data_id = m.get('ShapeDataId')
        if m.get('ShapeWkt') is not None:
            self.shape_wkt = m.get('ShapeWkt')
        return self


class CreateAIJobShrinkRequest(TeaModel):
    def __init__(
        self,
        app: str = None,
        area_threshold: float = None,
        confidence: float = None,
        inputs_shrink: str = None,
        job_name: str = None,
        model_project_id: int = None,
        model_version: str = None,
        project_id: int = None,
        shape_data_id: str = None,
        shape_wkt: str = None,
    ):
        self.app = app
        self.area_threshold = area_threshold
        self.confidence = confidence
        self.inputs_shrink = inputs_shrink
        self.job_name = job_name
        self.model_project_id = model_project_id
        self.model_version = model_version
        self.project_id = project_id
        self.shape_data_id = shape_data_id
        self.shape_wkt = shape_wkt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.area_threshold is not None:
            result['AreaThreshold'] = self.area_threshold
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.inputs_shrink is not None:
            result['Inputs'] = self.inputs_shrink
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.model_project_id is not None:
            result['ModelProjectId'] = self.model_project_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.shape_data_id is not None:
            result['ShapeDataId'] = self.shape_data_id
        if self.shape_wkt is not None:
            result['ShapeWkt'] = self.shape_wkt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('AreaThreshold') is not None:
            self.area_threshold = m.get('AreaThreshold')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Inputs') is not None:
            self.inputs_shrink = m.get('Inputs')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('ModelProjectId') is not None:
            self.model_project_id = m.get('ModelProjectId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ShapeDataId') is not None:
            self.shape_data_id = m.get('ShapeDataId')
        if m.get('ShapeWkt') is not None:
            self.shape_wkt = m.get('ShapeWkt')
        return self


class CreateAIJobResponseBodyJobs(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        name: str = None,
        success: bool = None,
    ):
        self.job_id = job_id
        self.name = name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAIJobResponseBody(TeaModel):
    def __init__(
        self,
        app: str = None,
        jobs: List[CreateAIJobResponseBodyJobs] = None,
        project_id: int = None,
        request_id: str = None,
    ):
        self.app = app
        self.jobs = jobs
        self.project_id = project_id
        self.request_id = request_id

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
        if self.app is not None:
            result['App'] = self.app
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = CreateAIJobResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAIJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAIJobResponseBody = None,
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
            temp_model = CreateAIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobsRequest(TeaModel):
    def __init__(
        self,
        job_ids: List[int] = None,
    ):
        self.job_ids = job_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class DeleteJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        job_ids_shrink: str = None,
    ):
        self.job_ids_shrink = job_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_ids_shrink is not None:
            result['JobIds'] = self.job_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids_shrink = m.get('JobIds')
        return self


class DeleteJobsResponseBody(TeaModel):
    def __init__(
        self,
        num: int = None,
        request_id: str = None,
    ):
        self.num = num
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteJobsResponseBody = None,
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
            temp_model = DeleteJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadDataRequest(TeaModel):
    def __init__(
        self,
        band_no: str = None,
        data_id: str = None,
    ):
        self.band_no = band_no
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_no is not None:
            result['BandNo'] = self.band_no
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandNo') is not None:
            self.band_no = m.get('BandNo')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class DownloadDataResponseBody(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        download_url: str = None,
        finished: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        self.data_id = data_id
        self.download_url = download_url
        self.finished = finished
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DownloadDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadDataResponseBody = None,
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
            temp_model = DownloadDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobsRequest(TeaModel):
    def __init__(
        self,
        job_ids: List[int] = None,
    ):
        self.job_ids = job_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class GetJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        job_ids_shrink: str = None,
    ):
        self.job_ids_shrink = job_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_ids_shrink is not None:
            result['JobIds'] = self.job_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids_shrink = m.get('JobIds')
        return self


class GetJobsResponseBodyList(TeaModel):
    def __init__(
        self,
        app: str = None,
        job_id: int = None,
        job_name: str = None,
        job_type: int = None,
        out_data_id: int = None,
        out_data_type: int = None,
        out_date_type: int = None,
        progress: str = None,
        request_id: str = None,
        status: int = None,
        submit_date: int = None,
    ):
        self.app = app
        self.job_id = job_id
        self.job_name = job_name
        self.job_type = job_type
        self.out_data_id = out_data_id
        self.out_data_type = out_data_type
        self.out_date_type = out_date_type
        self.progress = progress
        self.request_id = request_id
        self.status = status
        self.submit_date = submit_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.out_data_id is not None:
            result['OutDataId'] = self.out_data_id
        if self.out_data_type is not None:
            result['OutDataType'] = self.out_data_type
        if self.out_date_type is not None:
            result['OutDateType'] = self.out_date_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_date is not None:
            result['SubmitDate'] = self.submit_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('OutDataId') is not None:
            self.out_data_id = m.get('OutDataId')
        if m.get('OutDataType') is not None:
            self.out_data_type = m.get('OutDataType')
        if m.get('OutDateType') is not None:
            self.out_date_type = m.get('OutDateType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitDate') is not None:
            self.submit_date = m.get('SubmitDate')
        return self


class GetJobsResponseBody(TeaModel):
    def __init__(
        self,
        list: List[GetJobsResponseBodyList] = None,
        request_id: str = None,
    ):
        self.list = list
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetJobsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobsResponseBody = None,
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
            temp_model = GetJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasRequest(TeaModel):
    def __init__(
        self,
        cloudage_max: int = None,
        cloudage_min: int = None,
        date_end: str = None,
        date_start: str = None,
        page_number: int = None,
        page_size: int = None,
        region_wkt: str = None,
        source_type_list: List[str] = None,
    ):
        self.cloudage_max = cloudage_max
        self.cloudage_min = cloudage_min
        self.date_end = date_end
        self.date_start = date_start
        self.page_number = page_number
        self.page_size = page_size
        self.region_wkt = region_wkt
        self.source_type_list = source_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloudage_max is not None:
            result['CloudageMax'] = self.cloudage_max
        if self.cloudage_min is not None:
            result['CloudageMin'] = self.cloudage_min
        if self.date_end is not None:
            result['DateEnd'] = self.date_end
        if self.date_start is not None:
            result['DateStart'] = self.date_start
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_wkt is not None:
            result['RegionWkt'] = self.region_wkt
        if self.source_type_list is not None:
            result['SourceTypeList'] = self.source_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudageMax') is not None:
            self.cloudage_max = m.get('CloudageMax')
        if m.get('CloudageMin') is not None:
            self.cloudage_min = m.get('CloudageMin')
        if m.get('DateEnd') is not None:
            self.date_end = m.get('DateEnd')
        if m.get('DateStart') is not None:
            self.date_start = m.get('DateStart')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionWkt') is not None:
            self.region_wkt = m.get('RegionWkt')
        if m.get('SourceTypeList') is not None:
            self.source_type_list = m.get('SourceTypeList')
        return self


class ListDatasShrinkRequest(TeaModel):
    def __init__(
        self,
        cloudage_max: int = None,
        cloudage_min: int = None,
        date_end: str = None,
        date_start: str = None,
        page_number: int = None,
        page_size: int = None,
        region_wkt: str = None,
        source_type_list_shrink: str = None,
    ):
        self.cloudage_max = cloudage_max
        self.cloudage_min = cloudage_min
        self.date_end = date_end
        self.date_start = date_start
        self.page_number = page_number
        self.page_size = page_size
        self.region_wkt = region_wkt
        self.source_type_list_shrink = source_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloudage_max is not None:
            result['CloudageMax'] = self.cloudage_max
        if self.cloudage_min is not None:
            result['CloudageMin'] = self.cloudage_min
        if self.date_end is not None:
            result['DateEnd'] = self.date_end
        if self.date_start is not None:
            result['DateStart'] = self.date_start
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_wkt is not None:
            result['RegionWkt'] = self.region_wkt
        if self.source_type_list_shrink is not None:
            result['SourceTypeList'] = self.source_type_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudageMax') is not None:
            self.cloudage_max = m.get('CloudageMax')
        if m.get('CloudageMin') is not None:
            self.cloudage_min = m.get('CloudageMin')
        if m.get('DateEnd') is not None:
            self.date_end = m.get('DateEnd')
        if m.get('DateStart') is not None:
            self.date_start = m.get('DateStart')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionWkt') is not None:
            self.region_wkt = m.get('RegionWkt')
        if m.get('SourceTypeList') is not None:
            self.source_type_list_shrink = m.get('SourceTypeList')
        return self


class ListDatasResponseBodyListRasterBands(TeaModel):
    def __init__(
        self,
        band_no: str = None,
        height: int = None,
        resolution: float = None,
        width: int = None,
    ):
        self.band_no = band_no
        self.height = height
        self.resolution = resolution
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_no is not None:
            result['BandNo'] = self.band_no
        if self.height is not None:
            result['Height'] = self.height
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandNo') is not None:
            self.band_no = m.get('BandNo')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ListDatasResponseBodyListRaster(TeaModel):
    def __init__(
        self,
        acquisition_date_end: str = None,
        acquisition_date_start: str = None,
        bands: List[ListDatasResponseBodyListRasterBands] = None,
        bbox: List[float] = None,
        cloud_coverage: int = None,
        name: str = None,
        source_type: str = None,
        stac_id: str = None,
    ):
        self.acquisition_date_end = acquisition_date_end
        self.acquisition_date_start = acquisition_date_start
        self.bands = bands
        self.bbox = bbox
        self.cloud_coverage = cloud_coverage
        self.name = name
        self.source_type = source_type
        self.stac_id = stac_id

    def validate(self):
        if self.bands:
            for k in self.bands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acquisition_date_end is not None:
            result['AcquisitionDateEnd'] = self.acquisition_date_end
        if self.acquisition_date_start is not None:
            result['AcquisitionDateStart'] = self.acquisition_date_start
        result['Bands'] = []
        if self.bands is not None:
            for k in self.bands:
                result['Bands'].append(k.to_map() if k else None)
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.cloud_coverage is not None:
            result['CloudCoverage'] = self.cloud_coverage
        if self.name is not None:
            result['Name'] = self.name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.stac_id is not None:
            result['StacId'] = self.stac_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcquisitionDateEnd') is not None:
            self.acquisition_date_end = m.get('AcquisitionDateEnd')
        if m.get('AcquisitionDateStart') is not None:
            self.acquisition_date_start = m.get('AcquisitionDateStart')
        self.bands = []
        if m.get('Bands') is not None:
            for k in m.get('Bands'):
                temp_model = ListDatasResponseBodyListRasterBands()
                self.bands.append(temp_model.from_map(k))
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('CloudCoverage') is not None:
            self.cloud_coverage = m.get('CloudCoverage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StacId') is not None:
            self.stac_id = m.get('StacId')
        return self


class ListDatasResponseBodyList(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        raster: ListDatasResponseBodyListRaster = None,
    ):
        self.data_id = data_id
        self.raster = raster

    def validate(self):
        if self.raster:
            self.raster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.raster is not None:
            result['Raster'] = self.raster.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Raster') is not None:
            temp_model = ListDatasResponseBodyListRaster()
            self.raster = temp_model.from_map(m['Raster'])
        return self


class ListDatasResponseBody(TeaModel):
    def __init__(
        self,
        list: List[ListDatasResponseBodyList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListDatasResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasResponseBody = None,
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
            temp_model = ListDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserRasterDatasRequest(TeaModel):
    def __init__(
        self,
        acquisition_date: str = None,
        from_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resolution: float = None,
        upload_date: str = None,
    ):
        self.acquisition_date = acquisition_date
        self.from_type = from_type
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.resolution = resolution
        self.upload_date = upload_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acquisition_date is not None:
            result['AcquisitionDate'] = self.acquisition_date
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.upload_date is not None:
            result['UploadDate'] = self.upload_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcquisitionDate') is not None:
            self.acquisition_date = m.get('AcquisitionDate')
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('UploadDate') is not None:
            self.upload_date = m.get('UploadDate')
        return self


class ListUserRasterDatasResponseBodyListRasterBands(TeaModel):
    def __init__(
        self,
        band_no: str = None,
        height: int = None,
        resolution: float = None,
        width: int = None,
    ):
        self.band_no = band_no
        self.height = height
        self.resolution = resolution
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_no is not None:
            result['BandNo'] = self.band_no
        if self.height is not None:
            result['Height'] = self.height
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandNo') is not None:
            self.band_no = m.get('BandNo')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ListUserRasterDatasResponseBodyListRaster(TeaModel):
    def __init__(
        self,
        acquisition_date_end: str = None,
        acquisition_date_start: str = None,
        bands: List[ListUserRasterDatasResponseBodyListRasterBands] = None,
        bbox: List[float] = None,
        cloud_coverage: int = None,
        name: str = None,
        source_type: str = None,
        stac_id: str = None,
    ):
        self.acquisition_date_end = acquisition_date_end
        self.acquisition_date_start = acquisition_date_start
        self.bands = bands
        self.bbox = bbox
        self.cloud_coverage = cloud_coverage
        self.name = name
        self.source_type = source_type
        self.stac_id = stac_id

    def validate(self):
        if self.bands:
            for k in self.bands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acquisition_date_end is not None:
            result['AcquisitionDateEnd'] = self.acquisition_date_end
        if self.acquisition_date_start is not None:
            result['AcquisitionDateStart'] = self.acquisition_date_start
        result['Bands'] = []
        if self.bands is not None:
            for k in self.bands:
                result['Bands'].append(k.to_map() if k else None)
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.cloud_coverage is not None:
            result['CloudCoverage'] = self.cloud_coverage
        if self.name is not None:
            result['Name'] = self.name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.stac_id is not None:
            result['StacId'] = self.stac_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcquisitionDateEnd') is not None:
            self.acquisition_date_end = m.get('AcquisitionDateEnd')
        if m.get('AcquisitionDateStart') is not None:
            self.acquisition_date_start = m.get('AcquisitionDateStart')
        self.bands = []
        if m.get('Bands') is not None:
            for k in m.get('Bands'):
                temp_model = ListUserRasterDatasResponseBodyListRasterBands()
                self.bands.append(temp_model.from_map(k))
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('CloudCoverage') is not None:
            self.cloud_coverage = m.get('CloudCoverage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StacId') is not None:
            self.stac_id = m.get('StacId')
        return self


class ListUserRasterDatasResponseBodyList(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        raster: ListUserRasterDatasResponseBodyListRaster = None,
    ):
        self.data_id = data_id
        self.raster = raster

    def validate(self):
        if self.raster:
            self.raster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.raster is not None:
            result['Raster'] = self.raster.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Raster') is not None:
            temp_model = ListUserRasterDatasResponseBodyListRaster()
            self.raster = temp_model.from_map(m['Raster'])
        return self


class ListUserRasterDatasResponseBody(TeaModel):
    def __init__(
        self,
        list: List[ListUserRasterDatasResponseBodyList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListUserRasterDatasResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserRasterDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserRasterDatasResponseBody = None,
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
            temp_model = ListUserRasterDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserVectorDatasRequest(TeaModel):
    def __init__(
        self,
        from_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        upload_date: str = None,
    ):
        self.from_type = from_type
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.upload_date = upload_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_type is not None:
            result['FromType'] = self.from_type
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.upload_date is not None:
            result['UploadDate'] = self.upload_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UploadDate') is not None:
            self.upload_date = m.get('UploadDate')
        return self


class ListUserVectorDatasResponseBodyListVector(TeaModel):
    def __init__(
        self,
        bbox: List[float] = None,
        name: str = None,
        stac_id: str = None,
    ):
        self.bbox = bbox
        self.name = name
        self.stac_id = stac_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.name is not None:
            result['Name'] = self.name
        if self.stac_id is not None:
            result['StacId'] = self.stac_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StacId') is not None:
            self.stac_id = m.get('StacId')
        return self


class ListUserVectorDatasResponseBodyList(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        vector: ListUserVectorDatasResponseBodyListVector = None,
    ):
        self.data_id = data_id
        self.vector = vector

    def validate(self):
        if self.vector:
            self.vector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.vector is not None:
            result['Vector'] = self.vector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Vector') is not None:
            temp_model = ListUserVectorDatasResponseBodyListVector()
            self.vector = temp_model.from_map(m['Vector'])
        return self


class ListUserVectorDatasResponseBody(TeaModel):
    def __init__(
        self,
        list: List[ListUserVectorDatasResponseBodyList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListUserVectorDatasResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserVectorDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserVectorDatasResponseBody = None,
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
            temp_model = ListUserVectorDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


