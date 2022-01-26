# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateComputeTaskRequest(TeaModel):
    def __init__(
        self,
        algorithm_code_list: str = None,
        device_code_list: str = None,
        project_id: str = None,
        region_id: str = None,
        task_name: str = None,
        vcs_id: str = None,
    ):
        self.algorithm_code_list = algorithm_code_list
        self.device_code_list = device_code_list
        self.project_id = project_id
        self.region_id = region_id
        self.task_name = task_name
        self.vcs_id = vcs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_code_list is not None:
            result['AlgorithmCodeList'] = self.algorithm_code_list
        if self.device_code_list is not None:
            result['DeviceCodeList'] = self.device_code_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmCodeList') is not None:
            self.algorithm_code_list = m.get('AlgorithmCodeList')
        if m.get('DeviceCodeList') is not None:
            self.device_code_list = m.get('DeviceCodeList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class CreateComputeTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateComputeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateComputeTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateComputeTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateComputeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateComputeTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateComputeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        area_code: str = None,
        project_name: str = None,
        region_id: str = None,
        time_zone_code: str = None,
        vcs_id: str = None,
    ):
        self.area_code = area_code
        self.project_name = project_name
        self.region_id = region_id
        self.time_zone_code = time_zone_code
        self.vcs_id = vcs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.time_zone_code is not None:
            result['TimeZoneCode'] = self.time_zone_code
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TimeZoneCode') is not None:
            self.time_zone_code = m.get('TimeZoneCode')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class CreateProjectResponseBodyData(TeaModel):
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
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateProjectResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeComputeTasksRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        project_id: str = None,
        region_id: str = None,
        search_key: str = None,
        vcs_id: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.project_id = project_id
        self.region_id = region_id
        self.search_key = search_key
        self.vcs_id = vcs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class DescribeComputeTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        device_num: int = None,
        image_size: float = None,
        runtime: str = None,
        structured_size: float = None,
        task_id: str = None,
        task_name: str = None,
        task_status: str = None,
        vector_size: float = None,
    ):
        self.algorithm_name = algorithm_name
        self.device_num = device_num
        self.image_size = image_size
        self.runtime = runtime
        self.structured_size = structured_size
        self.task_id = task_id
        self.task_name = task_name
        self.task_status = task_status
        self.vector_size = vector_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.structured_size is not None:
            result['StructuredSize'] = self.structured_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.vector_size is not None:
            result['VectorSize'] = self.vector_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('StructuredSize') is not None:
            self.structured_size = m.get('StructuredSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('VectorSize') is not None:
            self.vector_size = m.get('VectorSize')
        return self


class DescribeComputeTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeComputeTasksResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeComputeTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeComputeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeComputeTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeComputeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDevicesRequest(TeaModel):
    def __init__(
        self,
        filter_key: str = None,
        page_num: int = None,
        page_size: int = None,
        project_id: str = None,
        region_id: str = None,
        search_key: str = None,
        vcs_id: str = None,
    ):
        self.filter_key = filter_key
        self.page_num = page_num
        self.page_size = page_size
        self.project_id = project_id
        self.region_id = region_id
        self.search_key = search_key
        self.vcs_id = vcs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class DescribeDevicesResponseBodyData(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        device_id: str = None,
        device_name: str = None,
        device_type: str = None,
        frame_rate: str = None,
        image_size: float = None,
        location: str = None,
        owner: str = None,
        pull_stream_status: str = None,
        real_time_data_rate: str = None,
        structured_size: float = None,
        vector_size: float = None,
    ):
        self.device_code = device_code
        self.device_id = device_id
        self.device_name = device_name
        self.device_type = device_type
        self.frame_rate = frame_rate
        self.image_size = image_size
        self.location = location
        self.owner = owner
        self.pull_stream_status = pull_stream_status
        self.real_time_data_rate = real_time_data_rate
        self.structured_size = structured_size
        self.vector_size = vector_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.location is not None:
            result['Location'] = self.location
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.pull_stream_status is not None:
            result['PullStreamStatus'] = self.pull_stream_status
        if self.real_time_data_rate is not None:
            result['RealTimeDataRate'] = self.real_time_data_rate
        if self.structured_size is not None:
            result['StructuredSize'] = self.structured_size
        if self.vector_size is not None:
            result['VectorSize'] = self.vector_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PullStreamStatus') is not None:
            self.pull_stream_status = m.get('PullStreamStatus')
        if m.get('RealTimeDataRate') is not None:
            self.real_time_data_rate = m.get('RealTimeDataRate')
        if m.get('StructuredSize') is not None:
            self.structured_size = m.get('StructuredSize')
        if m.get('VectorSize') is not None:
            self.vector_size = m.get('VectorSize')
        return self


class DescribeDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeDevicesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDevicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectsRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        project_name: str = None,
        region_id: str = None,
        vcs_id: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.project_name = project_name
        self.region_id = region_id
        self.vcs_id = vcs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class DescribeProjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        gb_id: str = None,
        gb_ip: str = None,
        gb_port: str = None,
        image_size: float = None,
        package_pattern: str = None,
        project_code: str = None,
        project_id: str = None,
        project_name: str = None,
        protocol: str = None,
        status: str = None,
        structured_size: float = None,
        vector_size: float = None,
    ):
        self.algorithm_name = algorithm_name
        self.gb_id = gb_id
        self.gb_ip = gb_ip
        self.gb_port = gb_port
        self.image_size = image_size
        self.package_pattern = package_pattern
        self.project_code = project_code
        self.project_id = project_id
        self.project_name = project_name
        self.protocol = protocol
        self.status = status
        self.structured_size = structured_size
        self.vector_size = vector_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.package_pattern is not None:
            result['PackagePattern'] = self.package_pattern
        if self.project_code is not None:
            result['ProjectCode'] = self.project_code
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.structured_size is not None:
            result['StructuredSize'] = self.structured_size
        if self.vector_size is not None:
            result['VectorSize'] = self.vector_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('PackagePattern') is not None:
            self.package_pattern = m.get('PackagePattern')
        if m.get('ProjectCode') is not None:
            self.project_code = m.get('ProjectCode')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructuredSize') is not None:
            self.structured_size = m.get('StructuredSize')
        if m.get('VectorSize') is not None:
            self.vector_size = m.get('VectorSize')
        return self


class DescribeProjectsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeProjectsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeProjectsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPictureSearchResultsRequest(TeaModel):
    def __init__(
        self,
        algorithm_type: str = None,
        begin_time: str = None,
        device_list: str = None,
        end_time: str = None,
        page_num: int = None,
        picture_contents: str = None,
        region_id: str = None,
        top_num: int = None,
        vcs_id: str = None,
    ):
        self.algorithm_type = algorithm_type
        self.begin_time = begin_time
        self.device_list = device_list
        self.end_time = end_time
        self.page_num = page_num
        self.picture_contents = picture_contents
        self.region_id = region_id
        self.top_num = top_num
        self.vcs_id = vcs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.picture_contents is not None:
            result['PictureContents'] = self.picture_contents
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_num is not None:
            result['TopNum'] = self.top_num
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PictureContents') is not None:
            self.picture_contents = m.get('PictureContents')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopNum') is not None:
            self.top_num = m.get('TopNum')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class GetPictureSearchResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        left_upper_corner_xcoordinate: str = None,
        left_upper_corner_ycoordinate: str = None,
        location_mark_time: str = None,
        picture_id_1: str = None,
        picture_id_2: str = None,
        picture_url_1: str = None,
        picture_url_2: str = None,
        right_lower_corner_xcoordinate: str = None,
        right_lower_corner_ycoordinate: str = None,
        similarity: float = None,
    ):
        self.device_id = device_id
        self.left_upper_corner_xcoordinate = left_upper_corner_xcoordinate
        self.left_upper_corner_ycoordinate = left_upper_corner_ycoordinate
        self.location_mark_time = location_mark_time
        self.picture_id_1 = picture_id_1
        self.picture_id_2 = picture_id_2
        self.picture_url_1 = picture_url_1
        self.picture_url_2 = picture_url_2
        self.right_lower_corner_xcoordinate = right_lower_corner_xcoordinate
        self.right_lower_corner_ycoordinate = right_lower_corner_ycoordinate
        self.similarity = similarity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.left_upper_corner_xcoordinate is not None:
            result['LeftUpperCornerXCoordinate'] = self.left_upper_corner_xcoordinate
        if self.left_upper_corner_ycoordinate is not None:
            result['LeftUpperCornerYCoordinate'] = self.left_upper_corner_ycoordinate
        if self.location_mark_time is not None:
            result['LocationMarkTime'] = self.location_mark_time
        if self.picture_id_1 is not None:
            result['PictureId1'] = self.picture_id_1
        if self.picture_id_2 is not None:
            result['PictureId2'] = self.picture_id_2
        if self.picture_url_1 is not None:
            result['PictureUrl1'] = self.picture_url_1
        if self.picture_url_2 is not None:
            result['PictureUrl2'] = self.picture_url_2
        if self.right_lower_corner_xcoordinate is not None:
            result['RightLowerCornerXCoordinate'] = self.right_lower_corner_xcoordinate
        if self.right_lower_corner_ycoordinate is not None:
            result['RightLowerCornerYCoordinate'] = self.right_lower_corner_ycoordinate
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('LeftUpperCornerXCoordinate') is not None:
            self.left_upper_corner_xcoordinate = m.get('LeftUpperCornerXCoordinate')
        if m.get('LeftUpperCornerYCoordinate') is not None:
            self.left_upper_corner_ycoordinate = m.get('LeftUpperCornerYCoordinate')
        if m.get('LocationMarkTime') is not None:
            self.location_mark_time = m.get('LocationMarkTime')
        if m.get('PictureId1') is not None:
            self.picture_id_1 = m.get('PictureId1')
        if m.get('PictureId2') is not None:
            self.picture_id_2 = m.get('PictureId2')
        if m.get('PictureUrl1') is not None:
            self.picture_url_1 = m.get('PictureUrl1')
        if m.get('PictureUrl2') is not None:
            self.picture_url_2 = m.get('PictureUrl2')
        if m.get('RightLowerCornerXCoordinate') is not None:
            self.right_lower_corner_xcoordinate = m.get('RightLowerCornerXCoordinate')
        if m.get('RightLowerCornerYCoordinate') is not None:
            self.right_lower_corner_ycoordinate = m.get('RightLowerCornerYCoordinate')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        return self


class GetPictureSearchResultsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetPictureSearchResultsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetPictureSearchResultsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPictureSearchResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPictureSearchResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPictureSearchResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportDevicesRequest(TeaModel):
    def __init__(
        self,
        device_list: str = None,
        project_id: str = None,
        region_id: str = None,
        vcs_id: str = None,
    ):
        self.device_list = device_list
        self.project_id = project_id
        self.region_id = region_id
        self.vcs_id = vcs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class ImportDevicesResponseBodyDataFailure(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        device_id: str = None,
    ):
        self.device_code = device_code
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class ImportDevicesResponseBodyDataSuccess(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        device_id: str = None,
    ):
        self.device_code = device_code
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class ImportDevicesResponseBodyData(TeaModel):
    def __init__(
        self,
        failure: List[ImportDevicesResponseBodyDataFailure] = None,
        success: List[ImportDevicesResponseBodyDataSuccess] = None,
    ):
        self.failure = failure
        self.success = success

    def validate(self):
        if self.failure:
            for k in self.failure:
                if k:
                    k.validate()
        if self.success:
            for k in self.success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Failure'] = []
        if self.failure is not None:
            for k in self.failure:
                result['Failure'].append(k.to_map() if k else None)
        result['Success'] = []
        if self.success is not None:
            for k in self.success:
                result['Success'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failure = []
        if m.get('Failure') is not None:
            for k in m.get('Failure'):
                temp_model = ImportDevicesResponseBodyDataFailure()
                self.failure.append(temp_model.from_map(k))
        self.success = []
        if m.get('Success') is not None:
            for k in m.get('Success'):
                temp_model = ImportDevicesResponseBodyDataSuccess()
                self.success.append(temp_model.from_map(k))
        return self


class ImportDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ImportDevicesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ImportDevicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


