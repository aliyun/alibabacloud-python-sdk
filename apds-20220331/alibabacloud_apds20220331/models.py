# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Any, Dict, List


class CreateFileJobRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        survey_job_id: int = None,
        region_id: str = None,
    ):
        self.resource_type = resource_type
        self.survey_job_id = survey_job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.survey_job_id is not None:
            result['surveyJobId'] = self.survey_job_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('surveyJobId') is not None:
            self.survey_job_id = m.get('surveyJobId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateFileJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class CreateFileJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFileJobResponseBody = None,
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
            temp_model = CreateFileJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMigrationGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        extra: str = None,
        id: int = None,
        name: str = None,
        region_id: str = None,
    ):
        # 详细描述
        self.description = description
        # 扩充字段（json结构）
        self.extra = extra
        self.id = id
        # 名称
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.extra is not None:
            result['extra'] = self.extra
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateMigrationGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error = error
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error is not None:
            result['Error'] = self.error
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMigrationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMigrationGroupResponseBody = None,
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
            temp_model = CreateMigrationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMigrationJobRequestMigrationJobList(TeaModel):
    def __init__(
        self,
        destination: str = None,
        destination_ip: str = None,
        destination_region: str = None,
        job_gmt_create: str = None,
        job_gmt_modified: str = None,
        name: str = None,
        original_percent: str = None,
        original_progress: str = None,
        original_status: str = None,
        out_side_id: str = None,
        properties: str = None,
        source: str = None,
        source_ip: str = None,
    ):
        # 目的
        self.destination = destination
        # 目的IP
        self.destination_ip = destination_ip
        # region
        self.destination_region = destination_region
        # 任务创建时间
        self.job_gmt_create = job_gmt_create
        # 任务最后修改时间
        self.job_gmt_modified = job_gmt_modified
        # 任务名称
        self.name = name
        # 来源系统的速度
        self.original_percent = original_percent
        # 来源系统的进度
        self.original_progress = original_progress
        # 来源系统状态
        self.original_status = original_status
        # 来源系统的jobID；
        self.out_side_id = out_side_id
        # 扩展字段
        self.properties = properties
        # 源
        self.source = source
        # 源IP
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['destination'] = self.destination
        if self.destination_ip is not None:
            result['destinationIp'] = self.destination_ip
        if self.destination_region is not None:
            result['destinationRegion'] = self.destination_region
        if self.job_gmt_create is not None:
            result['jobGmtCreate'] = self.job_gmt_create
        if self.job_gmt_modified is not None:
            result['jobGmtModified'] = self.job_gmt_modified
        if self.name is not None:
            result['name'] = self.name
        if self.original_percent is not None:
            result['originalPercent'] = self.original_percent
        if self.original_progress is not None:
            result['originalProgress'] = self.original_progress
        if self.original_status is not None:
            result['originalStatus'] = self.original_status
        if self.out_side_id is not None:
            result['outSideId'] = self.out_side_id
        if self.properties is not None:
            result['properties'] = self.properties
        if self.source is not None:
            result['source'] = self.source
        if self.source_ip is not None:
            result['sourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        if m.get('destinationIp') is not None:
            self.destination_ip = m.get('destinationIp')
        if m.get('destinationRegion') is not None:
            self.destination_region = m.get('destinationRegion')
        if m.get('jobGmtCreate') is not None:
            self.job_gmt_create = m.get('jobGmtCreate')
        if m.get('jobGmtModified') is not None:
            self.job_gmt_modified = m.get('jobGmtModified')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('originalPercent') is not None:
            self.original_percent = m.get('originalPercent')
        if m.get('originalProgress') is not None:
            self.original_progress = m.get('originalProgress')
        if m.get('originalStatus') is not None:
            self.original_status = m.get('originalStatus')
        if m.get('outSideId') is not None:
            self.out_side_id = m.get('outSideId')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourceIp') is not None:
            self.source_ip = m.get('sourceIp')
        return self


class CreateMigrationJobRequest(TeaModel):
    def __init__(
        self,
        migration_job_list: List[CreateMigrationJobRequestMigrationJobList] = None,
        type: str = None,
    ):
        self.migration_job_list = migration_job_list
        self.type = type

    def validate(self):
        if self.migration_job_list:
            for k in self.migration_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['migrationJobList'] = []
        if self.migration_job_list is not None:
            for k in self.migration_job_list:
                result['migrationJobList'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.migration_job_list = []
        if m.get('migrationJobList') is not None:
            for k in m.get('migrationJobList'):
                temp_model = CreateMigrationJobRequestMigrationJobList()
                self.migration_job_list.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error = error
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error is not None:
            result['Error'] = self.error
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMigrationJobResponseBody = None,
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
            temp_model = CreateMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSurveyJobRequest(TeaModel):
    def __init__(
        self,
        region: List[str] = None,
        resource_type_list: List[str] = None,
        ak: str = None,
        channel: str = None,
        cloud_type: str = None,
        name: str = None,
        sk: str = None,
        tenant_id: str = None,
        region_id: str = None,
    ):
        self.region = region
        self.resource_type_list = resource_type_list
        self.ak = ak
        # 调研渠道
        self.channel = channel
        self.cloud_type = cloud_type
        self.name = name
        self.sk = sk
        self.tenant_id = tenant_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        if self.ak is not None:
            result['ak'] = self.ak
        if self.channel is not None:
            result['channel'] = self.channel
        if self.cloud_type is not None:
            result['cloudType'] = self.cloud_type
        if self.name is not None:
            result['name'] = self.name
        if self.sk is not None:
            result['sk'] = self.sk
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        if m.get('ak') is not None:
            self.ak = m.get('ak')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('cloudType') is not None:
            self.cloud_type = m.get('cloudType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sk') is not None:
            self.sk = m.get('sk')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateSurveyJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class CreateSurveyJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSurveyJobResponseBody = None,
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
            temp_model = CreateSurveyJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSurveyJobOfflineRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        cloud_type: str = None,
        file_name: str = None,
        name: str = None,
        object_name: str = None,
        region_id: str = None,
    ):
        # 调研渠道
        self.channel = channel
        self.cloud_type = cloud_type
        self.file_name = file_name
        self.name = name
        self.object_name = object_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.cloud_type is not None:
            result['cloudType'] = self.cloud_type
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.name is not None:
            result['name'] = self.name
        if self.object_name is not None:
            result['objectName'] = self.object_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('cloudType') is not None:
            self.cloud_type = m.get('cloudType')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateSurveyJobOfflineResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class CreateSurveyJobOfflineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSurveyJobOfflineResponseBody = None,
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
            temp_model = CreateSurveyJobOfflineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMigrationGroupRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DeleteMigrationGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DeleteMigrationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMigrationGroupResponseBody = None,
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
            temp_model = DeleteMigrationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMigrationJobRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DeleteMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DeleteMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMigrationJobResponseBody = None,
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
            temp_model = DeleteMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOssFileRequest(TeaModel):
    def __init__(
        self,
        object_name: str = None,
        region_id: str = None,
    ):
        self.object_name = object_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_name is not None:
            result['objectName'] = self.object_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DeleteOssFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DeleteOssFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteOssFileResponseBody = None,
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
            temp_model = DeleteOssFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSurveyJobRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DeleteSurveyJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DeleteSurveyJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSurveyJobResponseBody = None,
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
            temp_model = DeleteSurveyJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSurveyResourcesRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
    ):
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self


class DeleteSurveyResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error = error
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error is not None:
            result['Error'] = self.error
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSurveyResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSurveyResourcesResponseBody = None,
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
            temp_model = DeleteSurveyResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DescribeMigrationJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMigrationJobConfigResponseBody = None,
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
            temp_model = DescribeMigrationJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobCountRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        source: str = None,
        type: str = None,
    ):
        # 任务名称
        self.name = name
        # 源
        self.source = source
        # 来源系统,MigrationJobTypeEnum[DTS,SMC,OSS,value,desc]
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeMigrationJobCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DescribeMigrationJobCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMigrationJobCountResponseBody = None,
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
            temp_model = DescribeMigrationJobCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssStsRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        cloud_type: str = None,
        region: str = None,
        region_id: str = None,
        sk: str = None,
        tenant_id: str = None,
    ):
        self.ak = ak
        self.cloud_type = cloud_type
        self.region = region
        self.region_id = region_id
        self.sk = sk
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['ak'] = self.ak
        if self.cloud_type is not None:
            result['cloudType'] = self.cloud_type
        if self.region is not None:
            result['region'] = self.region
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sk is not None:
            result['sk'] = self.sk
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ak') is not None:
            self.ak = m.get('ak')
        if m.get('cloudType') is not None:
            self.cloud_type = m.get('cloudType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sk') is not None:
            self.sk = m.get('sk')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DescribeOssStsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DescribeOssStsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssStsResponseBody = None,
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
            temp_model = DescribeOssStsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSummaryByStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeSummaryByStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error = error
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error is not None:
            result['Error'] = self.error
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSummaryByStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSummaryByStatusResponseBody = None,
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
            temp_model = DescribeSummaryByStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSummaryByStatusAndGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeSummaryByStatusAndGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error = error
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error is not None:
            result['Error'] = self.error
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSummaryByStatusAndGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSummaryByStatusAndGroupResponseBody = None,
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
            temp_model = DescribeSummaryByStatusAndGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSurveyJobRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
    ):
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeSurveyJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DescribeSurveyJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSurveyJobResponseBody = None,
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
            temp_model = DescribeSurveyJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSurveyJobCountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeSurveyJobCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DescribeSurveyJobCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSurveyJobCountResponseBody = None,
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
            temp_model = DescribeSurveyJobCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSurveyResourceTagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error = error
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error is not None:
            result['Error'] = self.error
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSurveyResourceTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSurveyResourceTagResponseBody = None,
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
            temp_model = DescribeSurveyResourceTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSurveyTemplateRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class DescribeSurveyTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class DescribeSurveyTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSurveyTemplateResponseBody = None,
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
            temp_model = DescribeSurveyTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMigrationJobsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        sort_col: str = None,
        sort_type: str = None,
        source: str = None,
        type: str = None,
    ):
        # 任务名称
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.sort_col = sort_col
        self.sort_type = sort_type
        # 源
        self.source = source
        # 来源系统,MigrationJobTypeEnum[DTS,SMC,OSS,value,desc]
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort_col is not None:
            result['sortCol'] = self.sort_col
        if self.sort_type is not None:
            result['sortType'] = self.sort_type
        if self.source is not None:
            result['source'] = self.source
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sortCol') is not None:
            self.sort_col = m.get('sortCol')
        if m.get('sortType') is not None:
            self.sort_type = m.get('sortType')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMigrationJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class ListMigrationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMigrationJobsResponseBody = None,
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
            temp_model = ListMigrationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        cloud_type: str = None,
        region: str = None,
        region_id: str = None,
        sk: str = None,
        tenant_id: str = None,
    ):
        self.ak = ak
        self.cloud_type = cloud_type
        self.region = region
        self.region_id = region_id
        self.sk = sk
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['ak'] = self.ak
        if self.cloud_type is not None:
            result['cloudType'] = self.cloud_type
        if self.region is not None:
            result['region'] = self.region
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sk is not None:
            result['sk'] = self.sk
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ak') is not None:
            self.ak = m.get('ak')
        if m.get('cloudType') is not None:
            self.cloud_type = m.get('cloudType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sk') is not None:
            self.sk = m.get('sk')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSurveyJobDownLoadJobsRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        sort_col: str = None,
        sort_type: str = None,
        region_id: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.sort_col = sort_col
        self.sort_type = sort_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort_col is not None:
            result['sortCol'] = self.sort_col
        if self.sort_type is not None:
            result['sortType'] = self.sort_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sortCol') is not None:
            self.sort_col = m.get('sortCol')
        if m.get('sortType') is not None:
            self.sort_type = m.get('sortType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListSurveyJobDownLoadJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class ListSurveyJobDownLoadJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSurveyJobDownLoadJobsResponseBody = None,
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
            temp_model = ListSurveyJobDownLoadJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSurveyJobsRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        cloud_type: str = None,
        file_name: str = None,
        name: str = None,
        object_name: str = None,
        region_id: str = None,
    ):
        # 调研渠道
        self.channel = channel
        self.cloud_type = cloud_type
        self.file_name = file_name
        self.name = name
        self.object_name = object_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.cloud_type is not None:
            result['cloudType'] = self.cloud_type
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.name is not None:
            result['name'] = self.name
        if self.object_name is not None:
            result['objectName'] = self.object_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('cloudType') is not None:
            self.cloud_type = m.get('cloudType')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListSurveyJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class ListSurveyJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSurveyJobsResponseBody = None,
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
            temp_model = ListSurveyJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSurveyResourceByMigrationGroupsRequestBody(TeaModel):
    def __init__(
        self,
        ids: List[int] = None,
    ):
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self


class ListSurveyResourceByMigrationGroupsRequest(TeaModel):
    def __init__(
        self,
        body: ListSurveyResourceByMigrationGroupsRequestBody = None,
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
            temp_model = ListSurveyResourceByMigrationGroupsRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSurveyResourceByMigrationGroupsShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class ListSurveyResourceByMigrationGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error = error
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error is not None:
            result['Error'] = self.error
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSurveyResourceByMigrationGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSurveyResourceByMigrationGroupsResponseBody = None,
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
            temp_model = ListSurveyResourceByMigrationGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSurveyResourceConnectionsRequest(TeaModel):
    def __init__(
        self,
        ids: List[int] = None,
        region_id: str = None,
    ):
        self.ids = ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListSurveyResourceConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error = error
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error is not None:
            result['Error'] = self.error
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSurveyResourceConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSurveyResourceConnectionsResponseBody = None,
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
            temp_model = ListSurveyResourceConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSurveyResourceTypesRequest(TeaModel):
    def __init__(
        self,
        ak: str = None,
        cloud_type: str = None,
        region: str = None,
        region_id: str = None,
        sk: str = None,
    ):
        self.ak = ak
        self.cloud_type = cloud_type
        self.region = region
        self.region_id = region_id
        self.sk = sk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['ak'] = self.ak
        if self.cloud_type is not None:
            result['cloudType'] = self.cloud_type
        if self.region is not None:
            result['region'] = self.region
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sk is not None:
            result['sk'] = self.sk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ak') is not None:
            self.ak = m.get('ak')
        if m.get('cloudType') is not None:
            self.cloud_type = m.get('cloudType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sk') is not None:
            self.sk = m.get('sk')
        return self


class ListSurveyResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class ListSurveyResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSurveyResourceTypesResponseBody = None,
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
            temp_model = ListSurveyResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSurveyResourcesDetailRequest(TeaModel):
    def __init__(
        self,
        ip: str = None,
        job_id: int = None,
        project_id: int = None,
        resource_type: str = None,
        sub_project_id: int = None,
        region_id: str = None,
    ):
        # ip
        self.ip = ip
        # 调研任务Id
        self.job_id = job_id
        self.project_id = project_id
        # 类型
        self.resource_type = resource_type
        self.sub_project_id = sub_project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_project_id is not None:
            result['subProjectId'] = self.sub_project_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subProjectId') is not None:
            self.sub_project_id = m.get('subProjectId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListSurveyResourcesDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class ListSurveyResourcesDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSurveyResourcesDetailResponseBody = None,
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
            temp_model = ListSurveyResourcesDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverMigrationJobRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class RecoverMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class RecoverMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoverMigrationJobResponseBody = None,
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
            temp_model = RecoverMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSyncMigrationJobRequest(TeaModel):
    def __init__(
        self,
        job_type: str = None,
        region_id: str = None,
    ):
        self.job_type = job_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_type is not None:
            result['jobType'] = self.job_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class StopSyncMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class StopSyncMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopSyncMigrationJobResponseBody = None,
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
            temp_model = StopSyncMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncMigrationJobRequest(TeaModel):
    def __init__(
        self,
        job_type: str = None,
        region_id: str = None,
        regions: str = None,
    ):
        self.job_type = job_type
        self.region_id = region_id
        self.regions = regions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_type is not None:
            result['jobType'] = self.job_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.regions is not None:
            result['regions'] = self.regions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        return self


class SyncMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        success: bool = None,
        error: str = None,
    ):
        self.code = code
        self.data = data
        self.success = success
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class SyncMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncMigrationJobResponseBody = None,
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
            temp_model = SyncMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


