# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AttachStreamRequestStreams(TeaModel):
    def __init__(
        self,
        stream_name: str = None,
        stream_url: str = None,
    ):
        self.stream_name = stream_name
        self.stream_url = stream_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')
        return self


class AttachStreamRequest(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        region_id: str = None,
        instance_id: str = None,
        streams: List[AttachStreamRequestStreams] = None,
    ):
        self.job_group_id = job_group_id
        self.region_id = region_id
        self.instance_id = instance_id
        self.streams = streams

    def validate(self):
        if self.streams:
            for k in self.streams:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = AttachStreamRequestStreams()
                self.streams.append(temp_model.from_map(k))
        return self


class AttachStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachStreamResponseBody = None,
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
            temp_model = AttachStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchModifyCameraStatusRequest(TeaModel):
    def __init__(
        self,
        stream_status: str = None,
        camera_ids: str = None,
        work_group_id: str = None,
        region_id: str = None,
    ):
        self.stream_status = stream_status
        self.camera_ids = camera_ids
        self.work_group_id = work_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        if self.camera_ids is not None:
            result['CameraIds'] = self.camera_ids
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        if m.get('CameraIds') is not None:
            self.camera_ids = m.get('CameraIds')
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchModifyCameraStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchModifyCameraStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchModifyCameraStatusResponseBody = None,
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
            temp_model = BatchModifyCameraStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlgoLibRequest(TeaModel):
    def __init__(
        self,
        algo_lib_name: str = None,
        algo_lib_version: str = None,
        capacity: int = None,
        oss_endpoint: str = None,
        oss_access_key_id: str = None,
        oss_bucket: str = None,
        oss_path: str = None,
        json_text: str = None,
        capability_names: str = None,
        oss_access_key_secret: str = None,
        text: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.algo_lib_name = algo_lib_name
        self.algo_lib_version = algo_lib_version
        self.capacity = capacity
        self.oss_endpoint = oss_endpoint
        self.oss_access_key_id = oss_access_key_id
        self.oss_bucket = oss_bucket
        self.oss_path = oss_path
        self.json_text = json_text
        self.capability_names = capability_names
        self.oss_access_key_secret = oss_access_key_secret
        self.text = text
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.algo_lib_name is not None:
            result['AlgoLibName'] = self.algo_lib_name
        if self.algo_lib_version is not None:
            result['AlgoLibVersion'] = self.algo_lib_version
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.json_text is not None:
            result['JsonText'] = self.json_text
        if self.capability_names is not None:
            result['CapabilityNames'] = self.capability_names
        if self.oss_access_key_secret is not None:
            result['OssAccessKeySecret'] = self.oss_access_key_secret
        if self.text is not None:
            result['Text'] = self.text
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoLibName') is not None:
            self.algo_lib_name = m.get('AlgoLibName')
        if m.get('AlgoLibVersion') is not None:
            self.algo_lib_version = m.get('AlgoLibVersion')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('JsonText') is not None:
            self.json_text = m.get('JsonText')
        if m.get('CapabilityNames') is not None:
            self.capability_names = m.get('CapabilityNames')
        if m.get('OssAccessKeySecret') is not None:
            self.oss_access_key_secret = m.get('OssAccessKeySecret')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAlgoLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        algo_lib_id: str = None,
    ):
        self.request_id = request_id
        self.algo_lib_id = algo_lib_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.algo_lib_id is not None:
            result['AlgoLibId'] = self.algo_lib_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AlgoLibId') is not None:
            self.algo_lib_id = m.get('AlgoLibId')
        return self


class CreateAlgoLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAlgoLibResponseBody = None,
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
            temp_model = CreateAlgoLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCameraRequest(TeaModel):
    def __init__(
        self,
        camera_name: str = None,
        work_group_id: str = None,
        camera_id: str = None,
        location_info: str = None,
        invite_uri: str = None,
        oss_path: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.camera_name = camera_name
        self.work_group_id = work_group_id
        self.camera_id = camera_id
        self.location_info = location_info
        self.invite_uri = invite_uri
        self.oss_path = oss_path
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_name is not None:
            result['CameraName'] = self.camera_name
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.location_info is not None:
            result['LocationInfo'] = self.location_info
        if self.invite_uri is not None:
            result['InviteUri'] = self.invite_uri
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraName') is not None:
            self.camera_name = m.get('CameraName')
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')
        if m.get('InviteUri') is not None:
            self.invite_uri = m.get('InviteUri')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCameraResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        camera_id: str = None,
    ):
        self.request_id = request_id
        self.camera_id = camera_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        return self


class CreateCameraResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCameraResponseBody = None,
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
            temp_model = CreateCameraResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCapabilityRequest(TeaModel):
    def __init__(
        self,
        capability_name: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.capability_name = capability_name
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.capability_name is not None:
            result['CapabilityName'] = self.capability_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapabilityName') is not None:
            self.capability_name = m.get('CapabilityName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCapabilityResponseBody(TeaModel):
    def __init__(
        self,
        capability_id: str = None,
        request_id: str = None,
    ):
        self.capability_id = capability_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.capability_id is not None:
            result['CapabilityId'] = self.capability_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapabilityId') is not None:
            self.capability_id = m.get('CapabilityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCapabilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCapabilityResponseBody = None,
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
            temp_model = CreateCapabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        description: str = None,
        instance_capacity: int = None,
        status: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.description = description
        self.instance_capacity = instance_capacity
        self.status = status
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_capacity is not None:
            result['InstanceCapacity'] = self.instance_capacity
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceCapacity') is not None:
            self.instance_capacity = m.get('InstanceCapacity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobGroupRequestJobGroupParams(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateJobGroupRequest(TeaModel):
    def __init__(
        self,
        job_group_name: str = None,
        resource_profile_id: str = None,
        algo_lib_id: str = None,
        planed_job_count: int = None,
        stream_per_job: int = None,
        job_count: int = None,
        instance_id: str = None,
        region_id: str = None,
        job_group_params: List[CreateJobGroupRequestJobGroupParams] = None,
    ):
        self.job_group_name = job_group_name
        self.resource_profile_id = resource_profile_id
        self.algo_lib_id = algo_lib_id
        self.planed_job_count = planed_job_count
        self.stream_per_job = stream_per_job
        self.job_count = job_count
        self.instance_id = instance_id
        self.region_id = region_id
        self.job_group_params = job_group_params

    def validate(self):
        if self.job_group_params:
            for k in self.job_group_params:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.resource_profile_id is not None:
            result['ResourceProfileId'] = self.resource_profile_id
        if self.algo_lib_id is not None:
            result['AlgoLibId'] = self.algo_lib_id
        if self.planed_job_count is not None:
            result['PlanedJobCount'] = self.planed_job_count
        if self.stream_per_job is not None:
            result['StreamPerJob'] = self.stream_per_job
        if self.job_count is not None:
            result['JobCount'] = self.job_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['JobGroupParams'] = []
        if self.job_group_params is not None:
            for k in self.job_group_params:
                result['JobGroupParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('ResourceProfileId') is not None:
            self.resource_profile_id = m.get('ResourceProfileId')
        if m.get('AlgoLibId') is not None:
            self.algo_lib_id = m.get('AlgoLibId')
        if m.get('PlanedJobCount') is not None:
            self.planed_job_count = m.get('PlanedJobCount')
        if m.get('StreamPerJob') is not None:
            self.stream_per_job = m.get('StreamPerJob')
        if m.get('JobCount') is not None:
            self.job_count = m.get('JobCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.job_group_params = []
        if m.get('JobGroupParams') is not None:
            for k in m.get('JobGroupParams'):
                temp_model = CreateJobGroupRequestJobGroupParams()
                self.job_group_params.append(temp_model.from_map(k))
        return self


class CreateJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        request_id: str = None,
    ):
        self.job_group_id = job_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJobGroupResponseBody = None,
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
            temp_model = CreateJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceProfileRequestResourceProfileParams(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateResourceProfileRequest(TeaModel):
    def __init__(
        self,
        resource_profile_name: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_profile_params: List[CreateResourceProfileRequestResourceProfileParams] = None,
    ):
        self.resource_profile_name = resource_profile_name
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_profile_params = resource_profile_params

    def validate(self):
        if self.resource_profile_params:
            for k in self.resource_profile_params:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_profile_name is not None:
            result['ResourceProfileName'] = self.resource_profile_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ResourceProfileParams'] = []
        if self.resource_profile_params is not None:
            for k in self.resource_profile_params:
                result['ResourceProfileParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceProfileName') is not None:
            self.resource_profile_name = m.get('ResourceProfileName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource_profile_params = []
        if m.get('ResourceProfileParams') is not None:
            for k in m.get('ResourceProfileParams'):
                temp_model = CreateResourceProfileRequestResourceProfileParams()
                self.resource_profile_params.append(temp_model.from_map(k))
        return self


class CreateResourceProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_profile_id: str = None,
    ):
        self.request_id = request_id
        self.resource_profile_id = resource_profile_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_profile_id is not None:
            result['ResourceProfileId'] = self.resource_profile_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceProfileId') is not None:
            self.resource_profile_id = m.get('ResourceProfileId')
        return self


class CreateResourceProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateResourceProfileResponseBody = None,
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
            temp_model = CreateResourceProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkGroupRequest(TeaModel):
    def __init__(
        self,
        work_group_name: str = None,
        protocol: str = None,
        theory_cut_status: str = None,
        description: str = None,
        job_num: int = None,
        topic_num: int = None,
        topic_prefix: str = None,
        account: str = None,
        password: str = None,
        ip: str = None,
        port: int = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.work_group_name = work_group_name
        self.protocol = protocol
        self.theory_cut_status = theory_cut_status
        self.description = description
        self.job_num = job_num
        self.topic_num = topic_num
        self.topic_prefix = topic_prefix
        self.account = account
        self.password = password
        self.ip = ip
        self.port = port
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.work_group_name is not None:
            result['WorkGroupName'] = self.work_group_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.theory_cut_status is not None:
            result['TheoryCutStatus'] = self.theory_cut_status
        if self.description is not None:
            result['Description'] = self.description
        if self.job_num is not None:
            result['JobNum'] = self.job_num
        if self.topic_num is not None:
            result['TopicNum'] = self.topic_num
        if self.topic_prefix is not None:
            result['TopicPrefix'] = self.topic_prefix
        if self.account is not None:
            result['Account'] = self.account
        if self.password is not None:
            result['Password'] = self.password
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkGroupName') is not None:
            self.work_group_name = m.get('WorkGroupName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TheoryCutStatus') is not None:
            self.theory_cut_status = m.get('TheoryCutStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobNum') is not None:
            self.job_num = m.get('JobNum')
        if m.get('TopicNum') is not None:
            self.topic_num = m.get('TopicNum')
        if m.get('TopicPrefix') is not None:
            self.topic_prefix = m.get('TopicPrefix')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateWorkGroupResponseBody(TeaModel):
    def __init__(
        self,
        work_group_id: str = None,
        request_id: str = None,
    ):
        self.work_group_id = work_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWorkGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWorkGroupResponseBody = None,
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
            temp_model = CreateWorkGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlgoLibRequest(TeaModel):
    def __init__(
        self,
        algo_lib_id: str = None,
        region_id: str = None,
    ):
        self.algo_lib_id = algo_lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.algo_lib_id is not None:
            result['AlgoLibId'] = self.algo_lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoLibId') is not None:
            self.algo_lib_id = m.get('AlgoLibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlgoLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlgoLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlgoLibResponseBody = None,
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
            temp_model = DeleteAlgoLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCameraRequest(TeaModel):
    def __init__(
        self,
        camera_id: str = None,
        region_id: str = None,
    ):
        self.camera_id = camera_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCameraResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCameraResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCameraResponseBody = None,
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
            temp_model = DeleteCameraResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCapabilityRequest(TeaModel):
    def __init__(
        self,
        capability_id: str = None,
        region_id: str = None,
    ):
        self.capability_id = capability_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.capability_id is not None:
            result['CapabilityId'] = self.capability_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapabilityId') is not None:
            self.capability_id = m.get('CapabilityId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCapabilityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCapabilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCapabilityResponseBody = None,
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
            temp_model = DeleteCapabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceResponseBody = None,
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobGroupRequest(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.job_group_id = job_group_id
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteJobGroupResponseBody = None,
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
            temp_model = DeleteJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceProfileRequest(TeaModel):
    def __init__(
        self,
        resource_profile_id: str = None,
        region_id: str = None,
    ):
        self.resource_profile_id = resource_profile_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_profile_id is not None:
            result['ResourceProfileId'] = self.resource_profile_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceProfileId') is not None:
            self.resource_profile_id = m.get('ResourceProfileId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteResourceProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteResourceProfileResponseBody = None,
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
            temp_model = DeleteResourceProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkGroupRequest(TeaModel):
    def __init__(
        self,
        work_group_id: str = None,
        region_id: str = None,
    ):
        self.work_group_id = work_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteWorkGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWorkGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWorkGroupResponseBody = None,
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
            temp_model = DeleteWorkGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlgoLibsRequest(TeaModel):
    def __init__(
        self,
        algo_lib_name: str = None,
        capability_name: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        algo_lib_id: str = None,
        region_id: str = None,
    ):
        self.algo_lib_name = algo_lib_name
        self.capability_name = capability_name
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.algo_lib_id = algo_lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.algo_lib_name is not None:
            result['AlgoLibName'] = self.algo_lib_name
        if self.capability_name is not None:
            result['CapabilityName'] = self.capability_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.algo_lib_id is not None:
            result['AlgoLibId'] = self.algo_lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoLibName') is not None:
            self.algo_lib_name = m.get('AlgoLibName')
        if m.get('CapabilityName') is not None:
            self.capability_name = m.get('CapabilityName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlgoLibId') is not None:
            self.algo_lib_id = m.get('AlgoLibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlgoLibsResponseBodyAlgoLibsAlgoLib(TeaModel):
    def __init__(
        self,
        oss_access_key_id: str = None,
        capacity: str = None,
        algo_lib_id: str = None,
        json_text: str = None,
        algo_lib_version: str = None,
        algo_lib_name: str = None,
        text: str = None,
        oss_bucket: str = None,
        capability_names: str = None,
        oss_path: str = None,
        oss_endpoint: str = None,
        upload_time: str = None,
    ):
        self.oss_access_key_id = oss_access_key_id
        self.capacity = capacity
        self.algo_lib_id = algo_lib_id
        self.json_text = json_text
        self.algo_lib_version = algo_lib_version
        self.algo_lib_name = algo_lib_name
        self.text = text
        self.oss_bucket = oss_bucket
        self.capability_names = capability_names
        self.oss_path = oss_path
        self.oss_endpoint = oss_endpoint
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.algo_lib_id is not None:
            result['AlgoLibId'] = self.algo_lib_id
        if self.json_text is not None:
            result['JsonText'] = self.json_text
        if self.algo_lib_version is not None:
            result['AlgoLibVersion'] = self.algo_lib_version
        if self.algo_lib_name is not None:
            result['AlgoLibName'] = self.algo_lib_name
        if self.text is not None:
            result['Text'] = self.text
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.capability_names is not None:
            result['CapabilityNames'] = self.capability_names
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('AlgoLibId') is not None:
            self.algo_lib_id = m.get('AlgoLibId')
        if m.get('JsonText') is not None:
            self.json_text = m.get('JsonText')
        if m.get('AlgoLibVersion') is not None:
            self.algo_lib_version = m.get('AlgoLibVersion')
        if m.get('AlgoLibName') is not None:
            self.algo_lib_name = m.get('AlgoLibName')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('CapabilityNames') is not None:
            self.capability_names = m.get('CapabilityNames')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class DescribeAlgoLibsResponseBodyAlgoLibs(TeaModel):
    def __init__(
        self,
        algo_lib: List[DescribeAlgoLibsResponseBodyAlgoLibsAlgoLib] = None,
    ):
        self.algo_lib = algo_lib

    def validate(self):
        if self.algo_lib:
            for k in self.algo_lib:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AlgoLib'] = []
        if self.algo_lib is not None:
            for k in self.algo_lib:
                result['AlgoLib'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algo_lib = []
        if m.get('AlgoLib') is not None:
            for k in m.get('AlgoLib'):
                temp_model = DescribeAlgoLibsResponseBodyAlgoLibsAlgoLib()
                self.algo_lib.append(temp_model.from_map(k))
        return self


class DescribeAlgoLibsResponseBody(TeaModel):
    def __init__(
        self,
        algo_libs: DescribeAlgoLibsResponseBodyAlgoLibs = None,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.algo_libs = algo_libs
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.algo_libs:
            self.algo_libs.validate()

    def to_map(self):
        result = dict()
        if self.algo_libs is not None:
            result['AlgoLibs'] = self.algo_libs.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoLibs') is not None:
            temp_model = DescribeAlgoLibsResponseBodyAlgoLibs()
            self.algo_libs = temp_model.from_map(m['AlgoLibs'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAlgoLibsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAlgoLibsResponseBody = None,
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
            temp_model = DescribeAlgoLibsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCamerasRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        camera_id: str = None,
        camera_name: str = None,
        stream_status: str = None,
        work_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.camera_id = camera_id
        self.camera_name = camera_name
        self.stream_status = stream_status
        self.work_group_id = work_group_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.camera_name is not None:
            result['CameraName'] = self.camera_name
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('CameraName') is not None:
            self.camera_name = m.get('CameraName')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCamerasResponseBodyCamerasCamera(TeaModel):
    def __init__(
        self,
        stream_status: str = None,
        update_time: str = None,
        camera_id: str = None,
        conf: str = None,
        rtmp_path: str = None,
        invite_uri: str = None,
        camera_name: str = None,
        work_group_id: str = None,
        location: str = None,
    ):
        self.stream_status = stream_status
        self.update_time = update_time
        self.camera_id = camera_id
        self.conf = conf
        self.rtmp_path = rtmp_path
        self.invite_uri = invite_uri
        self.camera_name = camera_name
        self.work_group_id = work_group_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.rtmp_path is not None:
            result['RtmpPath'] = self.rtmp_path
        if self.invite_uri is not None:
            result['InviteUri'] = self.invite_uri
        if self.camera_name is not None:
            result['CameraName'] = self.camera_name
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('RtmpPath') is not None:
            self.rtmp_path = m.get('RtmpPath')
        if m.get('InviteUri') is not None:
            self.invite_uri = m.get('InviteUri')
        if m.get('CameraName') is not None:
            self.camera_name = m.get('CameraName')
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeCamerasResponseBodyCameras(TeaModel):
    def __init__(
        self,
        camera: List[DescribeCamerasResponseBodyCamerasCamera] = None,
    ):
        self.camera = camera

    def validate(self):
        if self.camera:
            for k in self.camera:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Camera'] = []
        if self.camera is not None:
            for k in self.camera:
                result['Camera'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.camera = []
        if m.get('Camera') is not None:
            for k in m.get('Camera'):
                temp_model = DescribeCamerasResponseBodyCamerasCamera()
                self.camera.append(temp_model.from_map(k))
        return self


class DescribeCamerasResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        cameras: DescribeCamerasResponseBodyCameras = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.cameras = cameras

    def validate(self):
        if self.cameras:
            self.cameras.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.cameras is not None:
            result['Cameras'] = self.cameras.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Cameras') is not None:
            temp_model = DescribeCamerasResponseBodyCameras()
            self.cameras = temp_model.from_map(m['Cameras'])
        return self


class DescribeCamerasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCamerasResponseBody = None,
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
            temp_model = DescribeCamerasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCapabilitiesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCapabilitiesResponseBodyCapabilitiesCapability(TeaModel):
    def __init__(
        self,
        capability_id: str = None,
        capability_name: str = None,
    ):
        self.capability_id = capability_id
        self.capability_name = capability_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.capability_id is not None:
            result['CapabilityId'] = self.capability_id
        if self.capability_name is not None:
            result['CapabilityName'] = self.capability_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapabilityId') is not None:
            self.capability_id = m.get('CapabilityId')
        if m.get('CapabilityName') is not None:
            self.capability_name = m.get('CapabilityName')
        return self


class DescribeCapabilitiesResponseBodyCapabilities(TeaModel):
    def __init__(
        self,
        capability: List[DescribeCapabilitiesResponseBodyCapabilitiesCapability] = None,
    ):
        self.capability = capability

    def validate(self):
        if self.capability:
            for k in self.capability:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Capability'] = []
        if self.capability is not None:
            for k in self.capability:
                result['Capability'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.capability = []
        if m.get('Capability') is not None:
            for k in m.get('Capability'):
                temp_model = DescribeCapabilitiesResponseBodyCapabilitiesCapability()
                self.capability.append(temp_model.from_map(k))
        return self


class DescribeCapabilitiesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        capabilities: DescribeCapabilitiesResponseBodyCapabilities = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.capabilities = capabilities

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Capabilities') is not None:
            temp_model = DescribeCapabilitiesResponseBodyCapabilities()
            self.capabilities = temp_model.from_map(m['Capabilities'])
        return self


class DescribeCapabilitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCapabilitiesResponseBody = None,
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
            temp_model = DescribeCapabilitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
        instance_ids: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id
        self.instance_ids = instance_ids
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(
        self,
        status: str = None,
        instance_capacity: int = None,
        description: str = None,
        create_time: str = None,
        instance_name: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.instance_capacity = instance_capacity
        self.description = description
        self.create_time = create_time
        self.instance_name = instance_name
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_capacity is not None:
            result['InstanceCapacity'] = self.instance_capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceCapacity') is not None:
            self.instance_capacity = m.get('InstanceCapacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance: List[DescribeInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: DescribeInstancesResponseBodyInstances = None,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.instances = instances
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobGroupsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        job_group_id: str = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeJobGroupsResponseBodyJobGroupsJobGroupJobGroupParamsJobGroupParam(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeJobGroupsResponseBodyJobGroupsJobGroupJobGroupParams(TeaModel):
    def __init__(
        self,
        job_group_param: List[DescribeJobGroupsResponseBodyJobGroupsJobGroupJobGroupParamsJobGroupParam] = None,
    ):
        self.job_group_param = job_group_param

    def validate(self):
        if self.job_group_param:
            for k in self.job_group_param:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['JobGroupParam'] = []
        if self.job_group_param is not None:
            for k in self.job_group_param:
                result['JobGroupParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_group_param = []
        if m.get('JobGroupParam') is not None:
            for k in m.get('JobGroupParam'):
                temp_model = DescribeJobGroupsResponseBodyJobGroupsJobGroupJobGroupParamsJobGroupParam()
                self.job_group_param.append(temp_model.from_map(k))
        return self


class DescribeJobGroupsResponseBodyJobGroupsJobGroupComputeJobsComputeJob(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        compute_job_name: str = None,
        compute_job_id: str = None,
        compute_job_status: str = None,
        duration: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.compute_job_name = compute_job_name
        self.compute_job_id = compute_job_id
        self.compute_job_status = compute_job_status
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.compute_job_name is not None:
            result['ComputeJobName'] = self.compute_job_name
        if self.compute_job_id is not None:
            result['ComputeJobId'] = self.compute_job_id
        if self.compute_job_status is not None:
            result['ComputeJobStatus'] = self.compute_job_status
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ComputeJobName') is not None:
            self.compute_job_name = m.get('ComputeJobName')
        if m.get('ComputeJobId') is not None:
            self.compute_job_id = m.get('ComputeJobId')
        if m.get('ComputeJobStatus') is not None:
            self.compute_job_status = m.get('ComputeJobStatus')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeJobGroupsResponseBodyJobGroupsJobGroupComputeJobs(TeaModel):
    def __init__(
        self,
        compute_job: List[DescribeJobGroupsResponseBodyJobGroupsJobGroupComputeJobsComputeJob] = None,
    ):
        self.compute_job = compute_job

    def validate(self):
        if self.compute_job:
            for k in self.compute_job:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ComputeJob'] = []
        if self.compute_job is not None:
            for k in self.compute_job:
                result['ComputeJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compute_job = []
        if m.get('ComputeJob') is not None:
            for k in m.get('ComputeJob'):
                temp_model = DescribeJobGroupsResponseBodyJobGroupsJobGroupComputeJobsComputeJob()
                self.compute_job.append(temp_model.from_map(k))
        return self


class DescribeJobGroupsResponseBodyJobGroupsJobGroup(TeaModel):
    def __init__(
        self,
        status: str = None,
        job_group_id: str = None,
        algo_lib_id: str = None,
        job_count: int = None,
        job_group_name: str = None,
        job_group_params: DescribeJobGroupsResponseBodyJobGroupsJobGroupJobGroupParams = None,
        resource_profile_id: str = None,
        stream_per_job: int = None,
        planed_job_count: int = None,
        compute_jobs: DescribeJobGroupsResponseBodyJobGroupsJobGroupComputeJobs = None,
    ):
        self.status = status
        self.job_group_id = job_group_id
        self.algo_lib_id = algo_lib_id
        self.job_count = job_count
        self.job_group_name = job_group_name
        self.job_group_params = job_group_params
        self.resource_profile_id = resource_profile_id
        self.stream_per_job = stream_per_job
        self.planed_job_count = planed_job_count
        self.compute_jobs = compute_jobs

    def validate(self):
        if self.job_group_params:
            self.job_group_params.validate()
        if self.compute_jobs:
            self.compute_jobs.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.algo_lib_id is not None:
            result['AlgoLibId'] = self.algo_lib_id
        if self.job_count is not None:
            result['JobCount'] = self.job_count
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.job_group_params is not None:
            result['JobGroupParams'] = self.job_group_params.to_map()
        if self.resource_profile_id is not None:
            result['ResourceProfileId'] = self.resource_profile_id
        if self.stream_per_job is not None:
            result['StreamPerJob'] = self.stream_per_job
        if self.planed_job_count is not None:
            result['PlanedJobCount'] = self.planed_job_count
        if self.compute_jobs is not None:
            result['ComputeJobs'] = self.compute_jobs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('AlgoLibId') is not None:
            self.algo_lib_id = m.get('AlgoLibId')
        if m.get('JobCount') is not None:
            self.job_count = m.get('JobCount')
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('JobGroupParams') is not None:
            temp_model = DescribeJobGroupsResponseBodyJobGroupsJobGroupJobGroupParams()
            self.job_group_params = temp_model.from_map(m['JobGroupParams'])
        if m.get('ResourceProfileId') is not None:
            self.resource_profile_id = m.get('ResourceProfileId')
        if m.get('StreamPerJob') is not None:
            self.stream_per_job = m.get('StreamPerJob')
        if m.get('PlanedJobCount') is not None:
            self.planed_job_count = m.get('PlanedJobCount')
        if m.get('ComputeJobs') is not None:
            temp_model = DescribeJobGroupsResponseBodyJobGroupsJobGroupComputeJobs()
            self.compute_jobs = temp_model.from_map(m['ComputeJobs'])
        return self


class DescribeJobGroupsResponseBodyJobGroups(TeaModel):
    def __init__(
        self,
        job_group: List[DescribeJobGroupsResponseBodyJobGroupsJobGroup] = None,
    ):
        self.job_group = job_group

    def validate(self):
        if self.job_group:
            for k in self.job_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['JobGroup'] = []
        if self.job_group is not None:
            for k in self.job_group:
                result['JobGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_group = []
        if m.get('JobGroup') is not None:
            for k in m.get('JobGroup'):
                temp_model = DescribeJobGroupsResponseBodyJobGroupsJobGroup()
                self.job_group.append(temp_model.from_map(k))
        return self


class DescribeJobGroupsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        job_groups: DescribeJobGroupsResponseBodyJobGroups = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.job_groups = job_groups

    def validate(self):
        if self.job_groups:
            self.job_groups.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.job_groups is not None:
            result['JobGroups'] = self.job_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('JobGroups') is not None:
            temp_model = DescribeJobGroupsResponseBodyJobGroups()
            self.job_groups = temp_model.from_map(m['JobGroups'])
        return self


class DescribeJobGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJobGroupsResponseBody = None,
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
            temp_model = DescribeJobGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtocolsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeProtocolsResponseBody(TeaModel):
    def __init__(
        self,
        protocols: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.protocols = protocols
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProtocolsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeProtocolsResponseBody = None,
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
            temp_model = DescribeProtocolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceProfilesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        resource_profile_id: str = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.resource_profile_id = resource_profile_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_profile_id is not None:
            result['ResourceProfileId'] = self.resource_profile_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceProfileId') is not None:
            self.resource_profile_id = m.get('ResourceProfileId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeResourceProfilesResponseBodyResourceProfilesResourceProfileResourceProfileParamsResourceProfileParam(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeResourceProfilesResponseBodyResourceProfilesResourceProfileResourceProfileParams(TeaModel):
    def __init__(
        self,
        resource_profile_param: List[DescribeResourceProfilesResponseBodyResourceProfilesResourceProfileResourceProfileParamsResourceProfileParam] = None,
    ):
        self.resource_profile_param = resource_profile_param

    def validate(self):
        if self.resource_profile_param:
            for k in self.resource_profile_param:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ResourceProfileParam'] = []
        if self.resource_profile_param is not None:
            for k in self.resource_profile_param:
                result['ResourceProfileParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_profile_param = []
        if m.get('ResourceProfileParam') is not None:
            for k in m.get('ResourceProfileParam'):
                temp_model = DescribeResourceProfilesResponseBodyResourceProfilesResourceProfileResourceProfileParamsResourceProfileParam()
                self.resource_profile_param.append(temp_model.from_map(k))
        return self


class DescribeResourceProfilesResponseBodyResourceProfilesResourceProfile(TeaModel):
    def __init__(
        self,
        resource_profile_name: str = None,
        resource_profile_id: str = None,
        resource_profile_params: DescribeResourceProfilesResponseBodyResourceProfilesResourceProfileResourceProfileParams = None,
    ):
        self.resource_profile_name = resource_profile_name
        self.resource_profile_id = resource_profile_id
        self.resource_profile_params = resource_profile_params

    def validate(self):
        if self.resource_profile_params:
            self.resource_profile_params.validate()

    def to_map(self):
        result = dict()
        if self.resource_profile_name is not None:
            result['ResourceProfileName'] = self.resource_profile_name
        if self.resource_profile_id is not None:
            result['ResourceProfileId'] = self.resource_profile_id
        if self.resource_profile_params is not None:
            result['ResourceProfileParams'] = self.resource_profile_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceProfileName') is not None:
            self.resource_profile_name = m.get('ResourceProfileName')
        if m.get('ResourceProfileId') is not None:
            self.resource_profile_id = m.get('ResourceProfileId')
        if m.get('ResourceProfileParams') is not None:
            temp_model = DescribeResourceProfilesResponseBodyResourceProfilesResourceProfileResourceProfileParams()
            self.resource_profile_params = temp_model.from_map(m['ResourceProfileParams'])
        return self


class DescribeResourceProfilesResponseBodyResourceProfiles(TeaModel):
    def __init__(
        self,
        resource_profile: List[DescribeResourceProfilesResponseBodyResourceProfilesResourceProfile] = None,
    ):
        self.resource_profile = resource_profile

    def validate(self):
        if self.resource_profile:
            for k in self.resource_profile:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ResourceProfile'] = []
        if self.resource_profile is not None:
            for k in self.resource_profile:
                result['ResourceProfile'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_profile = []
        if m.get('ResourceProfile') is not None:
            for k in m.get('ResourceProfile'):
                temp_model = DescribeResourceProfilesResponseBodyResourceProfilesResourceProfile()
                self.resource_profile.append(temp_model.from_map(k))
        return self


class DescribeResourceProfilesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        resource_profiles: DescribeResourceProfilesResponseBodyResourceProfiles = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.resource_profiles = resource_profiles

    def validate(self):
        if self.resource_profiles:
            self.resource_profiles.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_profiles is not None:
            result['ResourceProfiles'] = self.resource_profiles.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceProfiles') is not None:
            temp_model = DescribeResourceProfilesResponseBodyResourceProfiles()
            self.resource_profiles = temp_model.from_map(m['ResourceProfiles'])
        return self


class DescribeResourceProfilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeResourceProfilesResponseBody = None,
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
            temp_model = DescribeResourceProfilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamsRequest(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.job_group_id = job_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStreamsResponseBodyStreamsStream(TeaModel):
    def __init__(
        self,
        job_group_id: int = None,
        stream_name: str = None,
        compute_job_id: str = None,
        obj_count: int = None,
        delay_ms: int = None,
        stream_url: str = None,
    ):
        self.job_group_id = job_group_id
        self.stream_name = stream_name
        self.compute_job_id = compute_job_id
        self.obj_count = obj_count
        self.delay_ms = delay_ms
        self.stream_url = stream_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.compute_job_id is not None:
            result['ComputeJobId'] = self.compute_job_id
        if self.obj_count is not None:
            result['ObjCount'] = self.obj_count
        if self.delay_ms is not None:
            result['DelayMS'] = self.delay_ms
        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('ComputeJobId') is not None:
            self.compute_job_id = m.get('ComputeJobId')
        if m.get('ObjCount') is not None:
            self.obj_count = m.get('ObjCount')
        if m.get('DelayMS') is not None:
            self.delay_ms = m.get('DelayMS')
        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')
        return self


class DescribeStreamsResponseBodyStreams(TeaModel):
    def __init__(
        self,
        stream: List[DescribeStreamsResponseBodyStreamsStream] = None,
    ):
        self.stream = stream

    def validate(self):
        if self.stream:
            for k in self.stream:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Stream'] = []
        if self.stream is not None:
            for k in self.stream:
                result['Stream'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream = []
        if m.get('Stream') is not None:
            for k in m.get('Stream'):
                temp_model = DescribeStreamsResponseBodyStreamsStream()
                self.stream.append(temp_model.from_map(k))
        return self


class DescribeStreamsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        streams: DescribeStreamsResponseBodyStreams = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.streams = streams

    def validate(self):
        if self.streams:
            self.streams.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.streams is not None:
            result['Streams'] = self.streams.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Streams') is not None:
            temp_model = DescribeStreamsResponseBodyStreams()
            self.streams = temp_model.from_map(m['Streams'])
        return self


class DescribeStreamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStreamsResponseBody = None,
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
            temp_model = DescribeStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkGroupsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        work_group_id: str = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.work_group_id = work_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeWorkGroupsResponseBodyWorkGroupsWorkGroup(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        description: str = None,
        protocol: str = None,
        create_time: str = None,
        instance_id: str = None,
        theory_cut_status: str = None,
        work_group_id: str = None,
        work_group_name: str = None,
    ):
        self.update_time = update_time
        self.description = description
        self.protocol = protocol
        self.create_time = create_time
        self.instance_id = instance_id
        self.theory_cut_status = theory_cut_status
        self.work_group_id = work_group_id
        self.work_group_name = work_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.description is not None:
            result['Description'] = self.description
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.theory_cut_status is not None:
            result['TheoryCutStatus'] = self.theory_cut_status
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.work_group_name is not None:
            result['WorkGroupName'] = self.work_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TheoryCutStatus') is not None:
            self.theory_cut_status = m.get('TheoryCutStatus')
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('WorkGroupName') is not None:
            self.work_group_name = m.get('WorkGroupName')
        return self


class DescribeWorkGroupsResponseBodyWorkGroups(TeaModel):
    def __init__(
        self,
        work_group: List[DescribeWorkGroupsResponseBodyWorkGroupsWorkGroup] = None,
    ):
        self.work_group = work_group

    def validate(self):
        if self.work_group:
            for k in self.work_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['WorkGroup'] = []
        if self.work_group is not None:
            for k in self.work_group:
                result['WorkGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.work_group = []
        if m.get('WorkGroup') is not None:
            for k in m.get('WorkGroup'):
                temp_model = DescribeWorkGroupsResponseBodyWorkGroupsWorkGroup()
                self.work_group.append(temp_model.from_map(k))
        return self


class DescribeWorkGroupsResponseBody(TeaModel):
    def __init__(
        self,
        work_groups: DescribeWorkGroupsResponseBodyWorkGroups = None,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.work_groups = work_groups
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        if self.work_groups:
            self.work_groups.validate()

    def to_map(self):
        result = dict()
        if self.work_groups is not None:
            result['WorkGroups'] = self.work_groups.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkGroups') is not None:
            temp_model = DescribeWorkGroupsResponseBodyWorkGroups()
            self.work_groups = temp_model.from_map(m['WorkGroups'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeWorkGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWorkGroupsResponseBody = None,
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
            temp_model = DescribeWorkGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachStreamRequestStreams(TeaModel):
    def __init__(
        self,
        stream_name: str = None,
    ):
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class DetachStreamRequest(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        region_id: str = None,
        streams: List[DetachStreamRequestStreams] = None,
    ):
        self.job_group_id = job_group_id
        self.region_id = region_id
        self.streams = streams

    def validate(self):
        if self.streams:
            for k in self.streams:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = DetachStreamRequestStreams()
                self.streams.append(temp_model.from_map(k))
        return self


class DetachStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachStreamResponseBody = None,
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
            temp_model = DetachStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCameraConfForCameraRequest(TeaModel):
    def __init__(
        self,
        camera_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.camera_id = camera_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetCameraConfForCameraResponseBodyCameraConf(TeaModel):
    def __init__(
        self,
        context: str = None,
        camera_id: str = None,
        camera_name: str = None,
        id: str = None,
    ):
        self.context = context
        self.camera_id = camera_id
        self.camera_name = camera_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.context is not None:
            result['Context'] = self.context
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.camera_name is not None:
            result['CameraName'] = self.camera_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('CameraName') is not None:
            self.camera_name = m.get('CameraName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetCameraConfForCameraResponseBody(TeaModel):
    def __init__(
        self,
        camera_conf: GetCameraConfForCameraResponseBodyCameraConf = None,
        request_id: str = None,
    ):
        self.camera_conf = camera_conf
        self.request_id = request_id

    def validate(self):
        if self.camera_conf:
            self.camera_conf.validate()

    def to_map(self):
        result = dict()
        if self.camera_conf is not None:
            result['CameraConf'] = self.camera_conf.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraConf') is not None:
            temp_model = GetCameraConfForCameraResponseBodyCameraConf()
            self.camera_conf = temp_model.from_map(m['CameraConf'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCameraConfForCameraResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCameraConfForCameraResponseBody = None,
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
            temp_model = GetCameraConfForCameraResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComputeJobLogRequest(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        job_id: str = None,
        job_log_name: str = None,
        size: int = None,
        region_id: str = None,
    ):
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.job_log_name = job_log_name
        self.size = size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_log_name is not None:
            result['JobLogName'] = self.job_log_name
        if self.size is not None:
            result['Size'] = self.size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobLogName') is not None:
            self.job_log_name = m.get('JobLogName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetComputeJobLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_log: str = None,
    ):
        self.request_id = request_id
        self.job_log = job_log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_log is not None:
            result['JobLog'] = self.job_log
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobLog') is not None:
            self.job_log = m.get('JobLog')
        return self


class GetComputeJobLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetComputeJobLogResponseBody = None,
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
            temp_model = GetComputeJobLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPlayUrlForCameraRequest(TeaModel):
    def __init__(
        self,
        camera_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.camera_id = camera_id
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPlayUrlForCameraResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        play_url: str = None,
    ):
        self.request_id = request_id
        self.play_url = play_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.play_url is not None:
            result['PlayUrl'] = self.play_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PlayUrl') is not None:
            self.play_url = m.get('PlayUrl')
        return self


class GetPlayUrlForCameraResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPlayUrlForCameraResponseBody = None,
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
            temp_model = GetPlayUrlForCameraResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComputeJobLogsRequest(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        compute_job_id: str = None,
        region_id: str = None,
    ):
        self.job_group_id = job_group_id
        self.compute_job_id = compute_job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.compute_job_id is not None:
            result['ComputeJobId'] = self.compute_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('ComputeJobId') is not None:
            self.compute_job_id = m.get('ComputeJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListComputeJobLogsResponseBodyJobLogs(TeaModel):
    def __init__(
        self,
        job_log: List[str] = None,
    ):
        self.job_log = job_log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_log is not None:
            result['JobLog'] = self.job_log
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobLog') is not None:
            self.job_log = m.get('JobLog')
        return self


class ListComputeJobLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_logs: ListComputeJobLogsResponseBodyJobLogs = None,
    ):
        self.request_id = request_id
        self.job_logs = job_logs

    def validate(self):
        if self.job_logs:
            self.job_logs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_logs is not None:
            result['JobLogs'] = self.job_logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobLogs') is not None:
            temp_model = ListComputeJobLogsResponseBodyJobLogs()
            self.job_logs = temp_model.from_map(m['JobLogs'])
        return self


class ListComputeJobLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListComputeJobLogsResponseBody = None,
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
            temp_model = ListComputeJobLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParkingResultsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        camera_ids: str = None,
        instance_id: str = None,
        region_id: str = None,
        vehicle_plate: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.camera_ids = camera_ids
        self.instance_id = instance_id
        self.region_id = region_id
        self.vehicle_plate = vehicle_plate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.camera_ids is not None:
            result['CameraIds'] = self.camera_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vehicle_plate is not None:
            result['VehiclePlate'] = self.vehicle_plate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CameraIds') is not None:
            self.camera_ids = m.get('CameraIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VehiclePlate') is not None:
            self.vehicle_plate = m.get('VehiclePlate')
        return self


class ListParkingResultsResponseBodyResults(TeaModel):
    def __init__(
        self,
        vehicle_type: str = None,
        camera_id: str = None,
        obj_right: int = None,
        obj_type: str = None,
        feature: str = None,
        obj_left: int = None,
        crop_image: str = None,
        obj_top: int = None,
        label: str = None,
        leave_time: str = None,
        obj_bottom: int = None,
        function_type: str = None,
        orig_image: str = None,
        time_stamp: str = None,
        vehicle_plate: str = None,
        entry_time: str = None,
        image_id: str = None,
    ):
        self.vehicle_type = vehicle_type
        self.camera_id = camera_id
        self.obj_right = obj_right
        self.obj_type = obj_type
        self.feature = feature
        self.obj_left = obj_left
        self.crop_image = crop_image
        self.obj_top = obj_top
        self.label = label
        self.leave_time = leave_time
        self.obj_bottom = obj_bottom
        self.function_type = function_type
        self.orig_image = orig_image
        self.time_stamp = time_stamp
        self.vehicle_plate = vehicle_plate
        self.entry_time = entry_time
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.obj_right is not None:
            result['ObjRight'] = self.obj_right
        if self.obj_type is not None:
            result['ObjType'] = self.obj_type
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.obj_left is not None:
            result['ObjLeft'] = self.obj_left
        if self.crop_image is not None:
            result['CropImage'] = self.crop_image
        if self.obj_top is not None:
            result['ObjTop'] = self.obj_top
        if self.label is not None:
            result['Label'] = self.label
        if self.leave_time is not None:
            result['LeaveTime'] = self.leave_time
        if self.obj_bottom is not None:
            result['ObjBottom'] = self.obj_bottom
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.orig_image is not None:
            result['OrigImage'] = self.orig_image
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.vehicle_plate is not None:
            result['VehiclePlate'] = self.vehicle_plate
        if self.entry_time is not None:
            result['EntryTime'] = self.entry_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('ObjRight') is not None:
            self.obj_right = m.get('ObjRight')
        if m.get('ObjType') is not None:
            self.obj_type = m.get('ObjType')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('ObjLeft') is not None:
            self.obj_left = m.get('ObjLeft')
        if m.get('CropImage') is not None:
            self.crop_image = m.get('CropImage')
        if m.get('ObjTop') is not None:
            self.obj_top = m.get('ObjTop')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LeaveTime') is not None:
            self.leave_time = m.get('LeaveTime')
        if m.get('ObjBottom') is not None:
            self.obj_bottom = m.get('ObjBottom')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('OrigImage') is not None:
            self.orig_image = m.get('OrigImage')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('VehiclePlate') is not None:
            self.vehicle_plate = m.get('VehiclePlate')
        if m.get('EntryTime') is not None:
            self.entry_time = m.get('EntryTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ListParkingResultsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        total_page: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        results: List[ListParkingResultsResponseBodyResults] = None,
    ):
        self.total_count = total_count
        self.total_page = total_page
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ListParkingResultsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ListParkingResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListParkingResultsResponseBody = None,
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
            temp_model = ListParkingResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSafetyHelmetResultsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        camera_ids: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.camera_ids = camera_ids
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.camera_ids is not None:
            result['CameraIds'] = self.camera_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CameraIds') is not None:
            self.camera_ids = m.get('CameraIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListSafetyHelmetResultsResponseBodyResults(TeaModel):
    def __init__(
        self,
        camera_id: str = None,
        obj_type: str = None,
        obj_right: int = None,
        feature: str = None,
        obj_left: int = None,
        crop_image: str = None,
        obj_top: int = None,
        label: str = None,
        leave_time: str = None,
        obj_bottom: int = None,
        time_stamp: str = None,
        orig_image: str = None,
        image_id: str = None,
        entry_time: str = None,
    ):
        self.camera_id = camera_id
        self.obj_type = obj_type
        self.obj_right = obj_right
        self.feature = feature
        self.obj_left = obj_left
        self.crop_image = crop_image
        self.obj_top = obj_top
        self.label = label
        self.leave_time = leave_time
        self.obj_bottom = obj_bottom
        self.time_stamp = time_stamp
        self.orig_image = orig_image
        self.image_id = image_id
        self.entry_time = entry_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.obj_type is not None:
            result['ObjType'] = self.obj_type
        if self.obj_right is not None:
            result['ObjRight'] = self.obj_right
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.obj_left is not None:
            result['ObjLeft'] = self.obj_left
        if self.crop_image is not None:
            result['CropImage'] = self.crop_image
        if self.obj_top is not None:
            result['ObjTop'] = self.obj_top
        if self.label is not None:
            result['Label'] = self.label
        if self.leave_time is not None:
            result['LeaveTime'] = self.leave_time
        if self.obj_bottom is not None:
            result['ObjBottom'] = self.obj_bottom
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.orig_image is not None:
            result['OrigImage'] = self.orig_image
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.entry_time is not None:
            result['EntryTime'] = self.entry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('ObjType') is not None:
            self.obj_type = m.get('ObjType')
        if m.get('ObjRight') is not None:
            self.obj_right = m.get('ObjRight')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('ObjLeft') is not None:
            self.obj_left = m.get('ObjLeft')
        if m.get('CropImage') is not None:
            self.crop_image = m.get('CropImage')
        if m.get('ObjTop') is not None:
            self.obj_top = m.get('ObjTop')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LeaveTime') is not None:
            self.leave_time = m.get('LeaveTime')
        if m.get('ObjBottom') is not None:
            self.obj_bottom = m.get('ObjBottom')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('OrigImage') is not None:
            self.orig_image = m.get('OrigImage')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('EntryTime') is not None:
            self.entry_time = m.get('EntryTime')
        return self


class ListSafetyHelmetResultsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        total_page: int = None,
        request_id: str = None,
        page_number: int = None,
        results: List[ListSafetyHelmetResultsResponseBodyResults] = None,
        page_index: int = None,
    ):
        self.total_count = total_count
        self.total_page = total_page
        self.request_id = request_id
        self.page_number = page_number
        self.results = results
        self.page_index = page_index

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ListSafetyHelmetResultsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class ListSafetyHelmetResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSafetyHelmetResultsResponseBody = None,
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
            temp_model = ListSafetyHelmetResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStreamsForCamerasRequest(TeaModel):
    def __init__(
        self,
        camera_ids: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.camera_ids = camera_ids
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_ids is not None:
            result['CameraIds'] = self.camera_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraIds') is not None:
            self.camera_ids = m.get('CameraIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListStreamsForCamerasResponseBodyStreams(TeaModel):
    def __init__(
        self,
        stream: List[str] = None,
    ):
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class ListStreamsForCamerasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        streams: ListStreamsForCamerasResponseBodyStreams = None,
    ):
        self.request_id = request_id
        self.streams = streams

    def validate(self):
        if self.streams:
            self.streams.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.streams is not None:
            result['Streams'] = self.streams.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Streams') is not None:
            temp_model = ListStreamsForCamerasResponseBodyStreams()
            self.streams = temp_model.from_map(m['Streams'])
        return self


class ListStreamsForCamerasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStreamsForCamerasResponseBody = None,
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
            temp_model = ListStreamsForCamerasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVehicleEntryResultsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        camera_ids: str = None,
        instance_id: str = None,
        region_id: str = None,
        vehicle_plate: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.camera_ids = camera_ids
        self.instance_id = instance_id
        self.region_id = region_id
        self.vehicle_plate = vehicle_plate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.camera_ids is not None:
            result['CameraIds'] = self.camera_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vehicle_plate is not None:
            result['VehiclePlate'] = self.vehicle_plate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CameraIds') is not None:
            self.camera_ids = m.get('CameraIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VehiclePlate') is not None:
            self.vehicle_plate = m.get('VehiclePlate')
        return self


class ListVehicleEntryResultsResponseBodyResults(TeaModel):
    def __init__(
        self,
        camera_id: str = None,
        obj_right: int = None,
        obj_type: str = None,
        feature: str = None,
        plate_left: int = None,
        obj_left: int = None,
        score: float = None,
        crop_image: str = None,
        obj_top: int = None,
        label: str = None,
        plate_bottom: int = None,
        leave_time: str = None,
        plate_top: int = None,
        obj_bottom: int = None,
        plate_right: int = None,
        orig_image: str = None,
        time_stamp: str = None,
        vehicle_plate: str = None,
        entry_time: str = None,
        image_id: str = None,
    ):
        self.camera_id = camera_id
        self.obj_right = obj_right
        self.obj_type = obj_type
        self.feature = feature
        self.plate_left = plate_left
        self.obj_left = obj_left
        self.score = score
        self.crop_image = crop_image
        self.obj_top = obj_top
        self.label = label
        self.plate_bottom = plate_bottom
        self.leave_time = leave_time
        self.plate_top = plate_top
        self.obj_bottom = obj_bottom
        self.plate_right = plate_right
        self.orig_image = orig_image
        self.time_stamp = time_stamp
        self.vehicle_plate = vehicle_plate
        self.entry_time = entry_time
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.obj_right is not None:
            result['ObjRight'] = self.obj_right
        if self.obj_type is not None:
            result['ObjType'] = self.obj_type
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.plate_left is not None:
            result['PlateLeft'] = self.plate_left
        if self.obj_left is not None:
            result['ObjLeft'] = self.obj_left
        if self.score is not None:
            result['Score'] = self.score
        if self.crop_image is not None:
            result['CropImage'] = self.crop_image
        if self.obj_top is not None:
            result['ObjTop'] = self.obj_top
        if self.label is not None:
            result['Label'] = self.label
        if self.plate_bottom is not None:
            result['PlateBottom'] = self.plate_bottom
        if self.leave_time is not None:
            result['LeaveTime'] = self.leave_time
        if self.plate_top is not None:
            result['PlateTop'] = self.plate_top
        if self.obj_bottom is not None:
            result['ObjBottom'] = self.obj_bottom
        if self.plate_right is not None:
            result['PlateRight'] = self.plate_right
        if self.orig_image is not None:
            result['OrigImage'] = self.orig_image
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.vehicle_plate is not None:
            result['VehiclePlate'] = self.vehicle_plate
        if self.entry_time is not None:
            result['EntryTime'] = self.entry_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('ObjRight') is not None:
            self.obj_right = m.get('ObjRight')
        if m.get('ObjType') is not None:
            self.obj_type = m.get('ObjType')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('PlateLeft') is not None:
            self.plate_left = m.get('PlateLeft')
        if m.get('ObjLeft') is not None:
            self.obj_left = m.get('ObjLeft')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('CropImage') is not None:
            self.crop_image = m.get('CropImage')
        if m.get('ObjTop') is not None:
            self.obj_top = m.get('ObjTop')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('PlateBottom') is not None:
            self.plate_bottom = m.get('PlateBottom')
        if m.get('LeaveTime') is not None:
            self.leave_time = m.get('LeaveTime')
        if m.get('PlateTop') is not None:
            self.plate_top = m.get('PlateTop')
        if m.get('ObjBottom') is not None:
            self.obj_bottom = m.get('ObjBottom')
        if m.get('PlateRight') is not None:
            self.plate_right = m.get('PlateRight')
        if m.get('OrigImage') is not None:
            self.orig_image = m.get('OrigImage')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('VehiclePlate') is not None:
            self.vehicle_plate = m.get('VehiclePlate')
        if m.get('EntryTime') is not None:
            self.entry_time = m.get('EntryTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ListVehicleEntryResultsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        total_page: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        results: List[ListVehicleEntryResultsResponseBodyResults] = None,
    ):
        self.total_count = total_count
        self.total_page = total_page
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ListVehicleEntryResultsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ListVehicleEntryResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVehicleEntryResultsResponseBody = None,
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
            temp_model = ListVehicleEntryResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAlgoLibRequest(TeaModel):
    def __init__(
        self,
        algo_lib_name: str = None,
        algo_lib_version: str = None,
        capacity: int = None,
        oss_endpoint: str = None,
        oss_access_key_id: str = None,
        oss_bucket: str = None,
        oss_path: str = None,
        json_text: str = None,
        capability_names: str = None,
        algo_lib_id: str = None,
        oss_access_key_secret: str = None,
        text: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.algo_lib_name = algo_lib_name
        self.algo_lib_version = algo_lib_version
        self.capacity = capacity
        self.oss_endpoint = oss_endpoint
        self.oss_access_key_id = oss_access_key_id
        self.oss_bucket = oss_bucket
        self.oss_path = oss_path
        self.json_text = json_text
        self.capability_names = capability_names
        self.algo_lib_id = algo_lib_id
        self.oss_access_key_secret = oss_access_key_secret
        self.text = text
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.algo_lib_name is not None:
            result['AlgoLibName'] = self.algo_lib_name
        if self.algo_lib_version is not None:
            result['AlgoLibVersion'] = self.algo_lib_version
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.json_text is not None:
            result['JsonText'] = self.json_text
        if self.capability_names is not None:
            result['CapabilityNames'] = self.capability_names
        if self.algo_lib_id is not None:
            result['AlgoLibId'] = self.algo_lib_id
        if self.oss_access_key_secret is not None:
            result['OssAccessKeySecret'] = self.oss_access_key_secret
        if self.text is not None:
            result['Text'] = self.text
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoLibName') is not None:
            self.algo_lib_name = m.get('AlgoLibName')
        if m.get('AlgoLibVersion') is not None:
            self.algo_lib_version = m.get('AlgoLibVersion')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('JsonText') is not None:
            self.json_text = m.get('JsonText')
        if m.get('CapabilityNames') is not None:
            self.capability_names = m.get('CapabilityNames')
        if m.get('AlgoLibId') is not None:
            self.algo_lib_id = m.get('AlgoLibId')
        if m.get('OssAccessKeySecret') is not None:
            self.oss_access_key_secret = m.get('OssAccessKeySecret')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyAlgoLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAlgoLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAlgoLibResponseBody = None,
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
            temp_model = ModifyAlgoLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCameraRequest(TeaModel):
    def __init__(
        self,
        camera_name: str = None,
        camera_id: str = None,
        location_info: str = None,
        invite_uri: str = None,
        region_id: str = None,
        stream_status: str = None,
    ):
        self.camera_name = camera_name
        self.camera_id = camera_id
        self.location_info = location_info
        self.invite_uri = invite_uri
        self.region_id = region_id
        self.stream_status = stream_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_name is not None:
            result['CameraName'] = self.camera_name
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.location_info is not None:
            result['LocationInfo'] = self.location_info
        if self.invite_uri is not None:
            result['InviteUri'] = self.invite_uri
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraName') is not None:
            self.camera_name = m.get('CameraName')
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')
        if m.get('InviteUri') is not None:
            self.invite_uri = m.get('InviteUri')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        return self


class ModifyCameraResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCameraResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCameraResponseBody = None,
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
            temp_model = ModifyCameraResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCapabilityRequest(TeaModel):
    def __init__(
        self,
        capability_name: str = None,
        capability_id: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.capability_name = capability_name
        self.capability_id = capability_id
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.capability_name is not None:
            result['CapabilityName'] = self.capability_name
        if self.capability_id is not None:
            result['CapabilityId'] = self.capability_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapabilityName') is not None:
            self.capability_name = m.get('CapabilityName')
        if m.get('CapabilityId') is not None:
            self.capability_id = m.get('CapabilityId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyCapabilityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCapabilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCapabilityResponseBody = None,
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
            temp_model = ModifyCapabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        description: str = None,
        status: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.description = description
        self.status = status
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.description is not None:
            result['Description'] = self.description
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceResponseBody = None,
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
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyJobGroupRequestJobGroupParams(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyJobGroupRequest(TeaModel):
    def __init__(
        self,
        job_group_name: str = None,
        resource_profile_id: str = None,
        algo_lib_id: str = None,
        planed_job_count: int = None,
        stream_per_job: int = None,
        job_count: int = None,
        job_group_id: str = None,
        status: str = None,
        region_id: str = None,
        instance_id: str = None,
        job_group_params: List[ModifyJobGroupRequestJobGroupParams] = None,
    ):
        self.job_group_name = job_group_name
        self.resource_profile_id = resource_profile_id
        self.algo_lib_id = algo_lib_id
        self.planed_job_count = planed_job_count
        self.stream_per_job = stream_per_job
        self.job_count = job_count
        self.job_group_id = job_group_id
        self.status = status
        self.region_id = region_id
        self.instance_id = instance_id
        self.job_group_params = job_group_params

    def validate(self):
        if self.job_group_params:
            for k in self.job_group_params:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.resource_profile_id is not None:
            result['ResourceProfileId'] = self.resource_profile_id
        if self.algo_lib_id is not None:
            result['AlgoLibId'] = self.algo_lib_id
        if self.planed_job_count is not None:
            result['PlanedJobCount'] = self.planed_job_count
        if self.stream_per_job is not None:
            result['StreamPerJob'] = self.stream_per_job
        if self.job_count is not None:
            result['JobCount'] = self.job_count
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['JobGroupParams'] = []
        if self.job_group_params is not None:
            for k in self.job_group_params:
                result['JobGroupParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('ResourceProfileId') is not None:
            self.resource_profile_id = m.get('ResourceProfileId')
        if m.get('AlgoLibId') is not None:
            self.algo_lib_id = m.get('AlgoLibId')
        if m.get('PlanedJobCount') is not None:
            self.planed_job_count = m.get('PlanedJobCount')
        if m.get('StreamPerJob') is not None:
            self.stream_per_job = m.get('StreamPerJob')
        if m.get('JobCount') is not None:
            self.job_count = m.get('JobCount')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.job_group_params = []
        if m.get('JobGroupParams') is not None:
            for k in m.get('JobGroupParams'):
                temp_model = ModifyJobGroupRequestJobGroupParams()
                self.job_group_params.append(temp_model.from_map(k))
        return self


class ModifyJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyJobGroupResponseBody = None,
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
            temp_model = ModifyJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyResourceProfileRequestResourceProfileParams(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyResourceProfileRequest(TeaModel):
    def __init__(
        self,
        resource_profile_name: str = None,
        resource_profile_id: str = None,
        region_id: str = None,
        instance_id: str = None,
        resource_profile_params: List[ModifyResourceProfileRequestResourceProfileParams] = None,
    ):
        self.resource_profile_name = resource_profile_name
        self.resource_profile_id = resource_profile_id
        self.region_id = region_id
        self.instance_id = instance_id
        self.resource_profile_params = resource_profile_params

    def validate(self):
        if self.resource_profile_params:
            for k in self.resource_profile_params:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_profile_name is not None:
            result['ResourceProfileName'] = self.resource_profile_name
        if self.resource_profile_id is not None:
            result['ResourceProfileId'] = self.resource_profile_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['ResourceProfileParams'] = []
        if self.resource_profile_params is not None:
            for k in self.resource_profile_params:
                result['ResourceProfileParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceProfileName') is not None:
            self.resource_profile_name = m.get('ResourceProfileName')
        if m.get('ResourceProfileId') is not None:
            self.resource_profile_id = m.get('ResourceProfileId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.resource_profile_params = []
        if m.get('ResourceProfileParams') is not None:
            for k in m.get('ResourceProfileParams'):
                temp_model = ModifyResourceProfileRequestResourceProfileParams()
                self.resource_profile_params.append(temp_model.from_map(k))
        return self


class ModifyResourceProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyResourceProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyResourceProfileResponseBody = None,
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
            temp_model = ModifyResourceProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWorkGroupRequest(TeaModel):
    def __init__(
        self,
        work_group_id: str = None,
        description: str = None,
        region_id: str = None,
    ):
        self.work_group_id = work_group_id
        self.description = description
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.work_group_id is not None:
            result['WorkGroupId'] = self.work_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkGroupId') is not None:
            self.work_group_id = m.get('WorkGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyWorkGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWorkGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWorkGroupResponseBody = None,
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
            temp_model = ModifyWorkGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutCameraConfForCameraRequest(TeaModel):
    def __init__(
        self,
        camera_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        camera_name: str = None,
        context: str = None,
    ):
        self.camera_id = camera_id
        self.instance_id = instance_id
        self.region_id = region_id
        self.camera_name = camera_name
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.camera_name is not None:
            result['CameraName'] = self.camera_name
        if self.context is not None:
            result['Context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CameraName') is not None:
            self.camera_name = m.get('CameraName')
        if m.get('Context') is not None:
            self.context = m.get('Context')
        return self


class PutCameraConfForCameraResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutCameraConfForCameraResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutCameraConfForCameraResponseBody = None,
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
            temp_model = PutCameraConfForCameraResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImagesRequestAttribute(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchImagesRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        size: int = None,
        type: str = None,
        contents: str = None,
        start_time: str = None,
        end_time: str = None,
        image_ids: str = None,
        camera_ids: str = None,
        instance_id: str = None,
        no_feature: str = None,
        region_id: str = None,
        attribute: List[SearchImagesRequestAttribute] = None,
    ):
        self.from_ = from_
        self.size = size
        self.type = type
        self.contents = contents
        self.start_time = start_time
        self.end_time = end_time
        self.image_ids = image_ids
        self.camera_ids = camera_ids
        self.instance_id = instance_id
        self.no_feature = no_feature
        self.region_id = region_id
        self.attribute = attribute

    def validate(self):
        if self.attribute:
            for k in self.attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.camera_ids is not None:
            result['CameraIds'] = self.camera_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.no_feature is not None:
            result['NoFeature'] = self.no_feature
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Attribute'] = []
        if self.attribute is not None:
            for k in self.attribute:
                result['Attribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('CameraIds') is not None:
            self.camera_ids = m.get('CameraIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NoFeature') is not None:
            self.no_feature = m.get('NoFeature')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.attribute = []
        if m.get('Attribute') is not None:
            for k in m.get('Attribute'):
                temp_model = SearchImagesRequestAttribute()
                self.attribute.append(temp_model.from_map(k))
        return self


class SearchImagesResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        camera_id: str = None,
        trouser_type_score: float = None,
        obj_type: str = None,
        trouser_color: str = None,
        cloth_type_score: float = None,
        brand: str = None,
        pose_type: str = None,
        vehicle_color: str = None,
        obj_left: int = None,
        score: float = None,
        head_wear_score: float = None,
        age_type_score: float = None,
        sex_type_score: float = None,
        non_vehicle_type: str = None,
        obj_bottom: int = None,
        plate_number: str = None,
        cloth_type: str = None,
        time_stamp: str = None,
        orig_image: str = None,
        vehicle_type_score: float = None,
        trouser_color_score: float = None,
        image_id: str = None,
        vehicle_color_score: float = None,
        hair_type_score: float = None,
        hair_type: str = None,
        non_vehicle_type_score: float = None,
        head_wear: str = None,
        vehicle_type: str = None,
        sex_type: str = None,
        pose_type_score: float = None,
        obj_right: int = None,
        feature: str = None,
        cloth_color_score: float = None,
        crop_image: str = None,
        obj_top: int = None,
        brand_score: float = None,
        cloth_color: str = None,
        age_type: str = None,
        leave_time: str = None,
        trouser_type: str = None,
        entry_time: str = None,
    ):
        self.camera_id = camera_id
        self.trouser_type_score = trouser_type_score
        self.obj_type = obj_type
        self.trouser_color = trouser_color
        self.cloth_type_score = cloth_type_score
        self.brand = brand
        self.pose_type = pose_type
        self.vehicle_color = vehicle_color
        self.obj_left = obj_left
        self.score = score
        self.head_wear_score = head_wear_score
        self.age_type_score = age_type_score
        self.sex_type_score = sex_type_score
        self.non_vehicle_type = non_vehicle_type
        self.obj_bottom = obj_bottom
        self.plate_number = plate_number
        self.cloth_type = cloth_type
        self.time_stamp = time_stamp
        self.orig_image = orig_image
        self.vehicle_type_score = vehicle_type_score
        self.trouser_color_score = trouser_color_score
        self.image_id = image_id
        self.vehicle_color_score = vehicle_color_score
        self.hair_type_score = hair_type_score
        self.hair_type = hair_type
        self.non_vehicle_type_score = non_vehicle_type_score
        self.head_wear = head_wear
        self.vehicle_type = vehicle_type
        self.sex_type = sex_type
        self.pose_type_score = pose_type_score
        self.obj_right = obj_right
        self.feature = feature
        self.cloth_color_score = cloth_color_score
        self.crop_image = crop_image
        self.obj_top = obj_top
        self.brand_score = brand_score
        self.cloth_color = cloth_color
        self.age_type = age_type
        self.leave_time = leave_time
        self.trouser_type = trouser_type
        self.entry_time = entry_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.camera_id is not None:
            result['CameraId'] = self.camera_id
        if self.trouser_type_score is not None:
            result['TrouserTypeScore'] = self.trouser_type_score
        if self.obj_type is not None:
            result['ObjType'] = self.obj_type
        if self.trouser_color is not None:
            result['TrouserColor'] = self.trouser_color
        if self.cloth_type_score is not None:
            result['ClothTypeScore'] = self.cloth_type_score
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.pose_type is not None:
            result['PoseType'] = self.pose_type
        if self.vehicle_color is not None:
            result['VehicleColor'] = self.vehicle_color
        if self.obj_left is not None:
            result['ObjLeft'] = self.obj_left
        if self.score is not None:
            result['Score'] = self.score
        if self.head_wear_score is not None:
            result['HeadWearScore'] = self.head_wear_score
        if self.age_type_score is not None:
            result['AgeTypeScore'] = self.age_type_score
        if self.sex_type_score is not None:
            result['SexTypeScore'] = self.sex_type_score
        if self.non_vehicle_type is not None:
            result['NonVehicleType'] = self.non_vehicle_type
        if self.obj_bottom is not None:
            result['ObjBottom'] = self.obj_bottom
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.cloth_type is not None:
            result['ClothType'] = self.cloth_type
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.orig_image is not None:
            result['OrigImage'] = self.orig_image
        if self.vehicle_type_score is not None:
            result['VehicleTypeScore'] = self.vehicle_type_score
        if self.trouser_color_score is not None:
            result['TrouserColorScore'] = self.trouser_color_score
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.vehicle_color_score is not None:
            result['VehicleColorScore'] = self.vehicle_color_score
        if self.hair_type_score is not None:
            result['HairTypeScore'] = self.hair_type_score
        if self.hair_type is not None:
            result['HairType'] = self.hair_type
        if self.non_vehicle_type_score is not None:
            result['NonVehicleTypeScore'] = self.non_vehicle_type_score
        if self.head_wear is not None:
            result['HeadWear'] = self.head_wear
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.sex_type is not None:
            result['SexType'] = self.sex_type
        if self.pose_type_score is not None:
            result['PoseTypeScore'] = self.pose_type_score
        if self.obj_right is not None:
            result['ObjRight'] = self.obj_right
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.cloth_color_score is not None:
            result['ClothColorScore'] = self.cloth_color_score
        if self.crop_image is not None:
            result['CropImage'] = self.crop_image
        if self.obj_top is not None:
            result['ObjTop'] = self.obj_top
        if self.brand_score is not None:
            result['BrandScore'] = self.brand_score
        if self.cloth_color is not None:
            result['ClothColor'] = self.cloth_color
        if self.age_type is not None:
            result['AgeType'] = self.age_type
        if self.leave_time is not None:
            result['LeaveTime'] = self.leave_time
        if self.trouser_type is not None:
            result['TrouserType'] = self.trouser_type
        if self.entry_time is not None:
            result['EntryTime'] = self.entry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraId') is not None:
            self.camera_id = m.get('CameraId')
        if m.get('TrouserTypeScore') is not None:
            self.trouser_type_score = m.get('TrouserTypeScore')
        if m.get('ObjType') is not None:
            self.obj_type = m.get('ObjType')
        if m.get('TrouserColor') is not None:
            self.trouser_color = m.get('TrouserColor')
        if m.get('ClothTypeScore') is not None:
            self.cloth_type_score = m.get('ClothTypeScore')
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('PoseType') is not None:
            self.pose_type = m.get('PoseType')
        if m.get('VehicleColor') is not None:
            self.vehicle_color = m.get('VehicleColor')
        if m.get('ObjLeft') is not None:
            self.obj_left = m.get('ObjLeft')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('HeadWearScore') is not None:
            self.head_wear_score = m.get('HeadWearScore')
        if m.get('AgeTypeScore') is not None:
            self.age_type_score = m.get('AgeTypeScore')
        if m.get('SexTypeScore') is not None:
            self.sex_type_score = m.get('SexTypeScore')
        if m.get('NonVehicleType') is not None:
            self.non_vehicle_type = m.get('NonVehicleType')
        if m.get('ObjBottom') is not None:
            self.obj_bottom = m.get('ObjBottom')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('ClothType') is not None:
            self.cloth_type = m.get('ClothType')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('OrigImage') is not None:
            self.orig_image = m.get('OrigImage')
        if m.get('VehicleTypeScore') is not None:
            self.vehicle_type_score = m.get('VehicleTypeScore')
        if m.get('TrouserColorScore') is not None:
            self.trouser_color_score = m.get('TrouserColorScore')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('VehicleColorScore') is not None:
            self.vehicle_color_score = m.get('VehicleColorScore')
        if m.get('HairTypeScore') is not None:
            self.hair_type_score = m.get('HairTypeScore')
        if m.get('HairType') is not None:
            self.hair_type = m.get('HairType')
        if m.get('NonVehicleTypeScore') is not None:
            self.non_vehicle_type_score = m.get('NonVehicleTypeScore')
        if m.get('HeadWear') is not None:
            self.head_wear = m.get('HeadWear')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('SexType') is not None:
            self.sex_type = m.get('SexType')
        if m.get('PoseTypeScore') is not None:
            self.pose_type_score = m.get('PoseTypeScore')
        if m.get('ObjRight') is not None:
            self.obj_right = m.get('ObjRight')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('ClothColorScore') is not None:
            self.cloth_color_score = m.get('ClothColorScore')
        if m.get('CropImage') is not None:
            self.crop_image = m.get('CropImage')
        if m.get('ObjTop') is not None:
            self.obj_top = m.get('ObjTop')
        if m.get('BrandScore') is not None:
            self.brand_score = m.get('BrandScore')
        if m.get('ClothColor') is not None:
            self.cloth_color = m.get('ClothColor')
        if m.get('AgeType') is not None:
            self.age_type = m.get('AgeType')
        if m.get('LeaveTime') is not None:
            self.leave_time = m.get('LeaveTime')
        if m.get('TrouserType') is not None:
            self.trouser_type = m.get('TrouserType')
        if m.get('EntryTime') is not None:
            self.entry_time = m.get('EntryTime')
        return self


class SearchImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[SearchImagesResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = SearchImagesResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class SearchImagesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        images: SearchImagesResponseBodyImages = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.images = images

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.images is not None:
            result['Images'] = self.images.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Images') is not None:
            temp_model = SearchImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        return self


class SearchImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchImagesResponseBody = None,
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
            temp_model = SearchImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobGroupRequest(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.job_group_id = job_group_id
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartJobGroupResponseBody = None,
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
            temp_model = StartJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobGroupRequest(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.job_group_id = job_group_id
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopJobGroupResponseBody = None,
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
            temp_model = StopJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


