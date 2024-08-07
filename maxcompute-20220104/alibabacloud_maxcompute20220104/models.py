# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreatePackageRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        is_install: bool = None,
    ):
        # The request body parameters.
        self.body = body
        # Specifies whether to install the package.
        self.is_install = is_install

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.is_install is not None:
            result['isInstall'] = self.is_install
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('isInstall') is not None:
            self.is_install = m.get('isInstall')
        return self


class CreatePackageResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreatePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePackageResponseBody = None,
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
            temp_model = CreatePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
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


class CreateQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQuotaPlanResponseBody = None,
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
            temp_model = CreateQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaScheduleRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateQuotaScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateQuotaScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQuotaScheduleResponseBody = None,
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
            temp_model = CreateQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body parameters. For valid values, see [MaxCompute permissions](https://help.aliyun.com/document_detail/27935.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoleResponseBody = None,
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
            temp_model = CreateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        tenant_id: str = None,
    ):
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DeleteQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQuotaPlanResponseBody = None,
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
            temp_model = DeleteQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobResourceUsageRequest(TeaModel):
    def __init__(
        self,
        date: str = None,
        job_owner_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list: List[str] = None,
    ):
        # The date that is accurate to the day part for the query. The date must be in the yyyy-MM-dd format.
        # 
        # This parameter is required.
        self.date = date
        # The list of job executors.
        self.job_owner_list = job_owner_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list = quota_nickname_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.job_owner_list is not None:
            result['jobOwnerList'] = self.job_owner_list
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.quota_nickname_list is not None:
            result['quotaNicknameList'] = self.quota_nickname_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list = m.get('jobOwnerList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list = m.get('quotaNicknameList')
        return self


class GetJobResourceUsageShrinkRequest(TeaModel):
    def __init__(
        self,
        date: str = None,
        job_owner_list_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list_shrink: str = None,
    ):
        # The date that is accurate to the day part for the query. The date must be in the yyyy-MM-dd format.
        # 
        # This parameter is required.
        self.date = date
        # The list of job executors.
        self.job_owner_list_shrink = job_owner_list_shrink
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list_shrink = quota_nickname_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.job_owner_list_shrink is not None:
            result['jobOwnerList'] = self.job_owner_list_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.quota_nickname_list_shrink is not None:
            result['quotaNicknameList'] = self.quota_nickname_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list_shrink = m.get('jobOwnerList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list_shrink = m.get('quotaNicknameList')
        return self


class GetJobResourceUsageResponseBodyDataJobResourceUsageList(TeaModel):
    def __init__(
        self,
        cu_usage: int = None,
        date: str = None,
        job_owner: str = None,
        memory_usage: int = None,
        quota_nickname: str = None,
    ):
        # The total number of used compute units (CUs).
        self.cu_usage = cu_usage
        # The start date of the query in the format of yyyy-MM-dd.
        self.date = date
        # The job executor.
        self.job_owner = job_owner
        # The total memory usage.
        self.memory_usage = memory_usage
        # The quota nickname.
        self.quota_nickname = quota_nickname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage
        if self.date is not None:
            result['date'] = self.date
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        return self


class GetJobResourceUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        job_resource_usage_list: List[GetJobResourceUsageResponseBodyDataJobResourceUsageList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The data list returned.
        self.job_resource_usage_list = job_resource_usage_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.job_resource_usage_list:
            for k in self.job_resource_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobResourceUsageList'] = []
        if self.job_resource_usage_list is not None:
            for k in self.job_resource_usage_list:
                result['jobResourceUsageList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_resource_usage_list = []
        if m.get('jobResourceUsageList') is not None:
            for k in m.get('jobResourceUsageList'):
                temp_model = GetJobResourceUsageResponseBodyDataJobResourceUsageList()
                self.job_resource_usage_list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetJobResourceUsageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetJobResourceUsageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

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
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetJobResourceUsageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetJobResourceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResourceUsageResponseBody = None,
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
            temp_model = GetJobResourceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPackageRequest(TeaModel):
    def __init__(
        self,
        source_project: str = None,
    ):
        # The project to which the package belongs. This parameter is required if the package is installed in the MaxCompute project.
        self.source_project = source_project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_project is not None:
            result['sourceProject'] = self.source_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceProject') is not None:
            self.source_project = m.get('sourceProject')
        return self


class GetPackageResponseBodyDataAllowedProjectList(TeaModel):
    def __init__(
        self,
        label: str = None,
        project: str = None,
    ):
        # The security level for sensitive data.
        self.label = label
        # The name of the MaxCompute project.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class GetPackageResponseBodyDataResourceListFunction(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the function.
        self.actions = actions
        # The name of the function.
        self.name = name
        # The name of schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetPackageResponseBodyDataResourceListResource(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the resource.
        self.actions = actions
        # The name of the resource.
        self.name = name
        # The name of schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetPackageResponseBodyDataResourceListTable(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the table.
        self.actions = actions
        # The name of the table.
        self.name = name
        # The name of schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetPackageResponseBodyDataResourceList(TeaModel):
    def __init__(
        self,
        function: List[GetPackageResponseBodyDataResourceListFunction] = None,
        resource: List[GetPackageResponseBodyDataResourceListResource] = None,
        table: List[GetPackageResponseBodyDataResourceListTable] = None,
    ):
        # The functions.
        self.function = function
        # The resources.
        self.resource = resource
        # The tables.
        self.table = table

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = GetPackageResponseBodyDataResourceListFunction()
                self.function.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = GetPackageResponseBodyDataResourceListResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = GetPackageResponseBodyDataResourceListTable()
                self.table.append(temp_model.from_map(k))
        return self


class GetPackageResponseBodyData(TeaModel):
    def __init__(
        self,
        allowed_project_list: List[GetPackageResponseBodyDataAllowedProjectList] = None,
        resource_list: GetPackageResponseBodyDataResourceList = None,
    ):
        # The projects in which the package is installed.
        self.allowed_project_list = allowed_project_list
        # The details of the resources that are included in the package.
        self.resource_list = resource_list

    def validate(self):
        if self.allowed_project_list:
            for k in self.allowed_project_list:
                if k:
                    k.validate()
        if self.resource_list:
            self.resource_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['allowedProjectList'] = []
        if self.allowed_project_list is not None:
            for k in self.allowed_project_list:
                result['allowedProjectList'].append(k.to_map() if k else None)
        if self.resource_list is not None:
            result['resourceList'] = self.resource_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.allowed_project_list = []
        if m.get('allowedProjectList') is not None:
            for k in m.get('allowedProjectList'):
                temp_model = GetPackageResponseBodyDataAllowedProjectList()
                self.allowed_project_list.append(temp_model.from_map(k))
        if m.get('resourceList') is not None:
            temp_model = GetPackageResponseBodyDataResourceList()
            self.resource_list = temp_model.from_map(m['resourceList'])
        return self


class GetPackageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetPackageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

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
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPackageResponseBody = None,
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
            temp_model = GetPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to use additional information.
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('verbose') is not None:
            self.verbose = m.get('verbose')
        return self


class GetProjectResponseBodyDataIpWhiteList(TeaModel):
    def __init__(
        self,
        ip_list: str = None,
        vpc_ip_list: str = None,
    ):
        # The list of IP addresses.
        self.ip_list = ip_list
        # The list of virtual private cloud (VPC) IP addresses.
        self.vpc_ip_list = vpc_ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.vpc_ip_list is not None:
            result['vpcIpList'] = self.vpc_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('vpcIpList') is not None:
            self.vpc_ip_list = m.get('vpcIpList')
        return self


class GetProjectResponseBodyDataPropertiesEncryption(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        enable: bool = None,
        key: str = None,
    ):
        # The name of the encryption algorithm.
        self.algorithm = algorithm
        # Indicates whether data encryption is enabled. Valid values: true and false.
        self.enable = enable
        # The key of the encryption algorithm.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.enable is not None:
            result['enable'] = self.enable
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize(TeaModel):
    def __init__(
        self,
        long_term_size: int = None,
        low_frequency_size: int = None,
        standard_size: int = None,
    ):
        # The long-term storage.
        self.long_term_size = long_term_size
        # The IA storage.
        self.low_frequency_size = low_frequency_size
        # The standard storage.
        self.standard_size = standard_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.long_term_size is not None:
            result['longTermSize'] = self.long_term_size
        if self.low_frequency_size is not None:
            result['lowFrequencySize'] = self.low_frequency_size
        if self.standard_size is not None:
            result['standardSize'] = self.standard_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('longTermSize') is not None:
            self.long_term_size = m.get('longTermSize')
        if m.get('lowFrequencySize') is not None:
            self.low_frequency_size = m.get('lowFrequencySize')
        if m.get('standardSize') is not None:
            self.standard_size = m.get('standardSize')
        return self


class GetProjectResponseBodyDataPropertiesStorageTierInfo(TeaModel):
    def __init__(
        self,
        project_backup_size: int = None,
        project_total_size: int = None,
        storage_tier_size: GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize = None,
    ):
        # The backup storage.
        self.project_backup_size = project_backup_size
        # The total storage.
        self.project_total_size = project_total_size
        # The tiered storage.
        self.storage_tier_size = storage_tier_size

    def validate(self):
        if self.storage_tier_size:
            self.storage_tier_size.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_backup_size is not None:
            result['projectBackupSize'] = self.project_backup_size
        if self.project_total_size is not None:
            result['projectTotalSize'] = self.project_total_size
        if self.storage_tier_size is not None:
            result['storageTierSize'] = self.storage_tier_size.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectBackupSize') is not None:
            self.project_backup_size = m.get('projectBackupSize')
        if m.get('projectTotalSize') is not None:
            self.project_total_size = m.get('projectTotalSize')
        if m.get('storageTierSize') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize()
            self.storage_tier_size = temp_model.from_map(m['storageTierSize'])
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycle(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the lifecycle. Valid values: -**mandatory**: The lifecycle clause is required. You must configure a lifecycle for a table. -**optional**: The lifecycle clause is optional in a table creation statement. If you do not configure a lifecycle for a table, the table does not expire. -**inherit**: If you do not configure a lifecycle for a table when you create the table, the value of the odps.table.lifecycle.value parameter is used by default.
        self.type = type
        # The retention period of a table. Unit: days.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastAccessGreaterThan(TeaModel):
    def __init__(
        self,
        condition_code: str = None,
        value: int = None,
    ):
        self.condition_code = condition_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_code is not None:
            result['conditionCode'] = self.condition_code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conditionCode') is not None:
            self.condition_code = m.get('conditionCode')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastModificationGreaterThan(TeaModel):
    def __init__(
        self,
        condition_code: str = None,
        value: int = None,
    ):
        self.condition_code = condition_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_code is not None:
            result['conditionCode'] = self.condition_code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conditionCode') is not None:
            self.condition_code = m.get('conditionCode')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastTierModificationGreaterThan(TeaModel):
    def __init__(
        self,
        condition_code: str = None,
        value: int = None,
    ):
        self.condition_code = condition_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_code is not None:
            result['conditionCode'] = self.condition_code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conditionCode') is not None:
            self.condition_code = m.get('conditionCode')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm(TeaModel):
    def __init__(
        self,
        days_after_last_access_greater_than: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastAccessGreaterThan = None,
        days_after_last_modification_greater_than: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastModificationGreaterThan = None,
        days_after_last_tier_modification_greater_than: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastTierModificationGreaterThan = None,
    ):
        self.days_after_last_access_greater_than = days_after_last_access_greater_than
        self.days_after_last_modification_greater_than = days_after_last_modification_greater_than
        self.days_after_last_tier_modification_greater_than = days_after_last_tier_modification_greater_than

    def validate(self):
        if self.days_after_last_access_greater_than:
            self.days_after_last_access_greater_than.validate()
        if self.days_after_last_modification_greater_than:
            self.days_after_last_modification_greater_than.validate()
        if self.days_after_last_tier_modification_greater_than:
            self.days_after_last_tier_modification_greater_than.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_after_last_access_greater_than is not None:
            result['daysAfterLastAccessGreaterThan'] = self.days_after_last_access_greater_than.to_map()
        if self.days_after_last_modification_greater_than is not None:
            result['daysAfterLastModificationGreaterThan'] = self.days_after_last_modification_greater_than.to_map()
        if self.days_after_last_tier_modification_greater_than is not None:
            result['daysAfterLastTierModificationGreaterThan'] = self.days_after_last_tier_modification_greater_than.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('daysAfterLastAccessGreaterThan') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastAccessGreaterThan()
            self.days_after_last_access_greater_than = temp_model.from_map(m['daysAfterLastAccessGreaterThan'])
        if m.get('daysAfterLastModificationGreaterThan') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastModificationGreaterThan()
            self.days_after_last_modification_greater_than = temp_model.from_map(m['daysAfterLastModificationGreaterThan'])
        if m.get('daysAfterLastTierModificationGreaterThan') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongtermDaysAfterLastTierModificationGreaterThan()
            self.days_after_last_tier_modification_greater_than = temp_model.from_map(m['daysAfterLastTierModificationGreaterThan'])
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastAccessGreaterThan(TeaModel):
    def __init__(
        self,
        condition_code: str = None,
        value: int = None,
    ):
        self.condition_code = condition_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_code is not None:
            result['conditionCode'] = self.condition_code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conditionCode') is not None:
            self.condition_code = m.get('conditionCode')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastModificationGreaterThan(TeaModel):
    def __init__(
        self,
        condition_code: str = None,
        value: int = None,
    ):
        self.condition_code = condition_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_code is not None:
            result['conditionCode'] = self.condition_code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conditionCode') is not None:
            self.condition_code = m.get('conditionCode')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastTierModificationGreaterThan(TeaModel):
    def __init__(
        self,
        condition_code: str = None,
        value: int = None,
    ):
        self.condition_code = condition_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_code is not None:
            result['conditionCode'] = self.condition_code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conditionCode') is not None:
            self.condition_code = m.get('conditionCode')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency(TeaModel):
    def __init__(
        self,
        days_after_last_access_greater_than: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastAccessGreaterThan = None,
        days_after_last_modification_greater_than: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastModificationGreaterThan = None,
        days_after_last_tier_modification_greater_than: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastTierModificationGreaterThan = None,
    ):
        self.days_after_last_access_greater_than = days_after_last_access_greater_than
        self.days_after_last_modification_greater_than = days_after_last_modification_greater_than
        self.days_after_last_tier_modification_greater_than = days_after_last_tier_modification_greater_than

    def validate(self):
        if self.days_after_last_access_greater_than:
            self.days_after_last_access_greater_than.validate()
        if self.days_after_last_modification_greater_than:
            self.days_after_last_modification_greater_than.validate()
        if self.days_after_last_tier_modification_greater_than:
            self.days_after_last_tier_modification_greater_than.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_after_last_access_greater_than is not None:
            result['daysAfterLastAccessGreaterThan'] = self.days_after_last_access_greater_than.to_map()
        if self.days_after_last_modification_greater_than is not None:
            result['daysAfterLastModificationGreaterThan'] = self.days_after_last_modification_greater_than.to_map()
        if self.days_after_last_tier_modification_greater_than is not None:
            result['daysAfterLastTierModificationGreaterThan'] = self.days_after_last_tier_modification_greater_than.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('daysAfterLastAccessGreaterThan') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastAccessGreaterThan()
            self.days_after_last_access_greater_than = temp_model.from_map(m['daysAfterLastAccessGreaterThan'])
        if m.get('daysAfterLastModificationGreaterThan') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastModificationGreaterThan()
            self.days_after_last_modification_greater_than = temp_model.from_map(m['daysAfterLastModificationGreaterThan'])
        if m.get('daysAfterLastTierModificationGreaterThan') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequencyDaysAfterLastTierModificationGreaterThan()
            self.days_after_last_tier_modification_greater_than = temp_model.from_map(m['daysAfterLastTierModificationGreaterThan'])
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfig(TeaModel):
    def __init__(
        self,
        tier_to_longterm: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm = None,
        tier_to_low_frequency: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency = None,
    ):
        self.tier_to_longterm = tier_to_longterm
        self.tier_to_low_frequency = tier_to_low_frequency

    def validate(self):
        if self.tier_to_longterm:
            self.tier_to_longterm.validate()
        if self.tier_to_low_frequency:
            self.tier_to_low_frequency.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tier_to_longterm is not None:
            result['TierToLongterm'] = self.tier_to_longterm.to_map()
        if self.tier_to_low_frequency is not None:
            result['TierToLowFrequency'] = self.tier_to_low_frequency.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TierToLongterm') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm()
            self.tier_to_longterm = temp_model.from_map(m['TierToLongterm'])
        if m.get('TierToLowFrequency') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency()
            self.tier_to_low_frequency = temp_model.from_map(m['TierToLowFrequency'])
        return self


class GetProjectResponseBodyDataProperties(TeaModel):
    def __init__(
        self,
        allow_full_scan: bool = None,
        elder_tunnel_quota: str = None,
        enable_decimal_2: bool = None,
        enable_fdc_cache_force: bool = None,
        enable_tiered_storage: bool = None,
        enable_tunnel_quota_route: bool = None,
        encryption: GetProjectResponseBodyDataPropertiesEncryption = None,
        fdc_quota: str = None,
        retention_days: int = None,
        sql_metering_max: str = None,
        storage_tier_info: GetProjectResponseBodyDataPropertiesStorageTierInfo = None,
        table_lifecycle: GetProjectResponseBodyDataPropertiesTableLifecycle = None,
        table_lifecycle_config: GetProjectResponseBodyDataPropertiesTableLifecycleConfig = None,
        timezone: str = None,
        tunnel_quota: str = None,
        type_system: str = None,
    ):
        # Indicates whether a full table scan on the project is enabled.
        self.allow_full_scan = allow_full_scan
        # This operation does not return a value for this parameter.
        self.elder_tunnel_quota = elder_tunnel_quota
        # Indicates whether the DECIMAL data type in MaxCompute V2.0 is enabled.
        self.enable_decimal_2 = enable_decimal_2
        self.enable_fdc_cache_force = enable_fdc_cache_force
        self.enable_tiered_storage = enable_tiered_storage
        # Indicates whether tunnel quota routing is enabled.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The encryption information.
        self.encryption = encryption
        self.fdc_quota = fdc_quota
        # The number of days for which backup data can be retained.
        self.retention_days = retention_days
        # The upper limit for the resources that are consumed by an SQL statement.
        self.sql_metering_max = sql_metering_max
        # The information about the tiered storage.
        self.storage_tier_info = storage_tier_info
        # The lifecycle of the table in the project.
        self.table_lifecycle = table_lifecycle
        self.table_lifecycle_config = table_lifecycle_config
        # The time zone of the project.
        self.timezone = timezone
        # The name of the tunnel quota.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values: -**1**: MaxCompute V1.0 data type edition. -**2**: MaxCompute V2.0 data type edition. -**hive**: Hive-compatible data type edition.
        self.type_system = type_system

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.storage_tier_info:
            self.storage_tier_info.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()
        if self.table_lifecycle_config:
            self.table_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan
        if self.elder_tunnel_quota is not None:
            result['elderTunnelQuota'] = self.elder_tunnel_quota
        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2
        if self.enable_fdc_cache_force is not None:
            result['enableFdcCacheForce'] = self.enable_fdc_cache_force
        if self.enable_tiered_storage is not None:
            result['enableTieredStorage'] = self.enable_tiered_storage
        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route
        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()
        if self.fdc_quota is not None:
            result['fdcQuota'] = self.fdc_quota
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max
        if self.storage_tier_info is not None:
            result['storageTierInfo'] = self.storage_tier_info.to_map()
        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()
        if self.table_lifecycle_config is not None:
            result['tableLifecycleConfig'] = self.table_lifecycle_config.to_map()
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        if self.type_system is not None:
            result['typeSystem'] = self.type_system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')
        if m.get('elderTunnelQuota') is not None:
            self.elder_tunnel_quota = m.get('elderTunnelQuota')
        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')
        if m.get('enableFdcCacheForce') is not None:
            self.enable_fdc_cache_force = m.get('enableFdcCacheForce')
        if m.get('enableTieredStorage') is not None:
            self.enable_tiered_storage = m.get('enableTieredStorage')
        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')
        if m.get('encryption') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesEncryption()
            self.encryption = temp_model.from_map(m['encryption'])
        if m.get('fdcQuota') is not None:
            self.fdc_quota = m.get('fdcQuota')
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')
        if m.get('storageTierInfo') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesStorageTierInfo()
            self.storage_tier_info = temp_model.from_map(m['storageTierInfo'])
        if m.get('tableLifecycle') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m['tableLifecycle'])
        if m.get('tableLifecycleConfig') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfig()
            self.table_lifecycle_config = temp_model.from_map(m['tableLifecycleConfig'])
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')
        return self


class GetProjectResponseBodyDataSaleTag(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetProjectResponseBodyDataSecurityPropertiesProjectProtection(TeaModel):
    def __init__(
        self,
        exception_policy: str = None,
        protected: bool = None,
    ):
        # The exception policy. If cross-project data access operations are required, the project owner must configure an exception policy in advance to allow the specified user to transfer data of a specified object from the current project to a specified project. After the exception policy is configured, data of the object can be transferred to the specified project even if the project data protection feature is enabled.
        self.exception_policy = exception_policy
        # Indicates whether project data protection is enabled.
        self.protected = protected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_policy is not None:
            result['exceptionPolicy'] = self.exception_policy
        if self.protected is not None:
            result['protected'] = self.protected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exceptionPolicy') is not None:
            self.exception_policy = m.get('exceptionPolicy')
        if m.get('protected') is not None:
            self.protected = m.get('protected')
        return self


class GetProjectResponseBodyDataSecurityProperties(TeaModel):
    def __init__(
        self,
        enable_download_privilege: bool = None,
        label_security: bool = None,
        object_creator_has_access_permission: bool = None,
        object_creator_has_grant_permission: bool = None,
        project_protection: GetProjectResponseBodyDataSecurityPropertiesProjectProtection = None,
        using_acl: bool = None,
        using_policy: bool = None,
    ):
        # Indicates whether Download control is enabled.
        self.enable_download_privilege = enable_download_privilege
        # Indicates whether label-based access control is enabled.
        self.label_security = label_security
        # Indicates whether the object creator is allowed to perform operations on objects.
        self.object_creator_has_access_permission = object_creator_has_access_permission
        # Indicates whether the object creator is allowed to authorize other users to perform operations on objects.
        self.object_creator_has_grant_permission = object_creator_has_grant_permission
        # Indicates whether project data protection is enabled.
        self.project_protection = project_protection
        # Indicates whether ACL-based access control is enabled.
        self.using_acl = using_acl
        # Indicates whether policy-based access control is enabled.
        self.using_policy = using_policy

    def validate(self):
        if self.project_protection:
            self.project_protection.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_download_privilege is not None:
            result['enableDownloadPrivilege'] = self.enable_download_privilege
        if self.label_security is not None:
            result['labelSecurity'] = self.label_security
        if self.object_creator_has_access_permission is not None:
            result['objectCreatorHasAccessPermission'] = self.object_creator_has_access_permission
        if self.object_creator_has_grant_permission is not None:
            result['objectCreatorHasGrantPermission'] = self.object_creator_has_grant_permission
        if self.project_protection is not None:
            result['projectProtection'] = self.project_protection.to_map()
        if self.using_acl is not None:
            result['usingAcl'] = self.using_acl
        if self.using_policy is not None:
            result['usingPolicy'] = self.using_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableDownloadPrivilege') is not None:
            self.enable_download_privilege = m.get('enableDownloadPrivilege')
        if m.get('labelSecurity') is not None:
            self.label_security = m.get('labelSecurity')
        if m.get('objectCreatorHasAccessPermission') is not None:
            self.object_creator_has_access_permission = m.get('objectCreatorHasAccessPermission')
        if m.get('objectCreatorHasGrantPermission') is not None:
            self.object_creator_has_grant_permission = m.get('objectCreatorHasGrantPermission')
        if m.get('projectProtection') is not None:
            temp_model = GetProjectResponseBodyDataSecurityPropertiesProjectProtection()
            self.project_protection = temp_model.from_map(m['projectProtection'])
        if m.get('usingAcl') is not None:
            self.using_acl = m.get('usingAcl')
        if m.get('usingPolicy') is not None:
            self.using_policy = m.get('usingPolicy')
        return self


class GetProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        comment: str = None,
        cost_storage: str = None,
        created_time: int = None,
        default_quota: str = None,
        ip_white_list: GetProjectResponseBodyDataIpWhiteList = None,
        name: str = None,
        owner: str = None,
        product_type: str = None,
        properties: GetProjectResponseBodyDataProperties = None,
        region_id: str = None,
        sale_tag: GetProjectResponseBodyDataSaleTag = None,
        security_properties: GetProjectResponseBodyDataSecurityProperties = None,
        status: str = None,
        super_admins: List[str] = None,
        three_tier_model: bool = None,
        type: str = None,
    ):
        # The comment of the project.
        self.comment = comment
        # The storage usage.
        self.cost_storage = cost_storage
        # Create time
        self.created_time = created_time
        # The default computing quota.
        self.default_quota = default_quota
        # The IP address whitelist.
        self.ip_white_list = ip_white_list
        # The name of the MaxCompute project.
        self.name = name
        # The owner of the project.
        self.owner = owner
        # The billing method of the project.
        self.product_type = product_type
        # The properties of the project.
        self.properties = properties
        # RegionID
        self.region_id = region_id
        # The tag.
        self.sale_tag = sale_tag
        # The permission properties.
        self.security_properties = security_properties
        # The status of the project. Valid values: -**AVAILABLE**: The project was available. -**READONLY**: The project was read only. -**FROZEN**: The project was frozen. -**DELETING**: The project was being deleted.
        self.status = status
        # The Super_Administrator role.
        self.super_admins = super_admins
        # Indicates whether the current project supports the three-layer model of MaxCompute.
        self.three_tier_model = three_tier_model
        # The type of the project. Valid values: -**managed**: The project is an internal project. -**external**: The project is an external project.
        self.type = type

    def validate(self):
        if self.ip_white_list:
            self.ip_white_list.validate()
        if self.properties:
            self.properties.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.security_properties:
            self.security_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.cost_storage is not None:
            result['costStorage'] = self.cost_storage
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.default_quota is not None:
            result['defaultQuota'] = self.default_quota
        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.properties is not None:
            result['properties'] = self.properties.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.security_properties is not None:
            result['securityProperties'] = self.security_properties.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.super_admins is not None:
            result['superAdmins'] = self.super_admins
        if self.three_tier_model is not None:
            result['threeTierModel'] = self.three_tier_model
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('costStorage') is not None:
            self.cost_storage = m.get('costStorage')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('defaultQuota') is not None:
            self.default_quota = m.get('defaultQuota')
        if m.get('ipWhiteList') is not None:
            temp_model = GetProjectResponseBodyDataIpWhiteList()
            self.ip_white_list = temp_model.from_map(m['ipWhiteList'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('properties') is not None:
            temp_model = GetProjectResponseBodyDataProperties()
            self.properties = temp_model.from_map(m['properties'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetProjectResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('securityProperties') is not None:
            temp_model = GetProjectResponseBodyDataSecurityProperties()
            self.security_properties = temp_model.from_map(m['securityProperties'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('superAdmins') is not None:
            self.super_admins = m.get('superAdmins')
        if m.get('threeTierModel') is not None:
            self.three_tier_model = m.get('threeTierModel')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: GetProjectResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

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
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProjectResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaRequest(TeaModel):
    def __init__(
        self,
        ak_proven: str = None,
        mock: bool = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The trusted AccessKey pairs.
        self.ak_proven = ak_proven
        # Specifies whether to include submodules. Valid values: -true: The request includes submodules. -false: The request does not include submodules. This is the default value.
        self.mock = mock
        # The region ID.
        self.region = region
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak_proven is not None:
            result['AkProven'] = self.ak_proven
        if self.mock is not None:
            result['mock'] = self.mock
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProven') is not None:
            self.ak_proven = m.get('AkProven')
        if m.get('mock') is not None:
            self.mock = m.get('mock')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaResponseBodyBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyDataScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: GetQuotaResponseBodyDataSubQuotaInfoListSaleTag = None,
        schedule_info: GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information about the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaResponseBodyDataBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: GetQuotaResponseBodyDataSaleTag = None,
        schedule_info: GetQuotaResponseBodyDataScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[GetQuotaResponseBodyDataSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information about the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The quota ID.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information about the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyDataBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyDataScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaResponseBodyDataSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBodySaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class GetQuotaResponseBodySubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodySubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodySubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class GetQuotaResponseBodySubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaResponseBodySubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: GetQuotaResponseBodySubQuotaInfoListSaleTag = None,
        schedule_info: GetQuotaResponseBodySubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information about the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The alias of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBody(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaResponseBodyBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        data: GetQuotaResponseBodyData = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        request_id: str = None,
        sale_tag: GetQuotaResponseBodySaleTag = None,
        schedule_info: GetQuotaResponseBodyScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[GetQuotaResponseBodySubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information about the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The returned data.
        self.data = data
        # The quota ID.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information about the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.data:
            self.data.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('data') is not None:
            temp_model = GetQuotaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodySaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaResponseBodySubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaResponseBody = None,
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
            temp_model = GetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        tenant_id: str = None,
    ):
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaPlanResponseBodyDataQuotaBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaPlanResponseBodyDataQuotaScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the user who created the quota plan.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The alias of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaPlanResponseBodyDataQuota(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaPlanResponseBodyDataQuotaBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: GetQuotaPlanResponseBodyDataQuotaScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota plan was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the quota.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        quota: GetQuotaPlanResponseBodyDataQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class GetQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: GetQuotaPlanResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetQuotaPlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaPlanResponseBody = None,
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
            temp_model = GetQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaScheduleRequest(TeaModel):
    def __init__(
        self,
        display_timezone: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The time zone.
        self.display_timezone = display_timezone
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_timezone is not None:
            result['displayTimezone'] = self.display_timezone
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayTimezone') is not None:
            self.display_timezone = m.get('displayTimezone')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaScheduleResponseBodyDataCondition(TeaModel):
    def __init__(
        self,
        after: str = None,
        at: str = None,
    ):
        # The start time when the quota plan takes effect.
        self.after = after
        # The time when the quota plan takes effect.
        self.at = at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['after'] = self.after
        if self.at is not None:
            result['at'] = self.at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('after') is not None:
            self.after = m.get('after')
        if m.get('at') is not None:
            self.at = m.get('at')
        return self


class GetQuotaScheduleResponseBodyData(TeaModel):
    def __init__(
        self,
        condition: GetQuotaScheduleResponseBodyDataCondition = None,
        id: str = None,
        operator: str = None,
        plan: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The condition value.
        self.condition = condition
        # The ID of the quota plan.
        self.id = id
        # The name of the operator.
        self.operator = operator
        # The name of the quota plan.
        self.plan = plan
        # The time zone.
        self.timezone = timezone
        # The type of the quota plan.
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.operator is not None:
            result['operator'] = self.operator
        if self.plan is not None:
            result['plan'] = self.plan
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            temp_model = GetQuotaScheduleResponseBodyDataCondition()
            self.condition = temp_model.from_map(m['condition'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('plan') is not None:
            self.plan = m.get('plan')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetQuotaScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetQuotaScheduleResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetQuotaScheduleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetQuotaScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaScheduleResponseBody = None,
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
            temp_model = GetQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleAclResponseBodyDataFunction(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the function.
        self.actions = actions
        # The name of the function.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataInstance(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the instance.
        self.actions = actions
        # The name of the instance.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataPackage(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the package.
        self.actions = actions
        # The name of the package.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataProject(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the project.
        self.actions = actions
        # The name of the MaxCompute project.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataResource(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the resource.
        self.actions = actions
        # The name of the resource.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataTable(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the table.
        self.actions = actions
        # The name of the table.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyData(TeaModel):
    def __init__(
        self,
        function: List[GetRoleAclResponseBodyDataFunction] = None,
        instance: List[GetRoleAclResponseBodyDataInstance] = None,
        package: List[GetRoleAclResponseBodyDataPackage] = None,
        project: List[GetRoleAclResponseBodyDataProject] = None,
        resource: List[GetRoleAclResponseBodyDataResource] = None,
        table: List[GetRoleAclResponseBodyDataTable] = None,
    ):
        # The function.
        self.function = function
        # The instance.
        self.instance = instance
        # The package.
        self.package = package
        # The project.
        self.project = project
        # The resource.
        self.resource = resource
        # The table.
        self.table = table

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()
        if self.package:
            for k in self.package:
                if k:
                    k.validate()
        if self.project:
            for k in self.project:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['instance'].append(k.to_map() if k else None)
        result['package'] = []
        if self.package is not None:
            for k in self.package:
                result['package'].append(k.to_map() if k else None)
        result['project'] = []
        if self.project is not None:
            for k in self.project:
                result['project'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = GetRoleAclResponseBodyDataFunction()
                self.function.append(temp_model.from_map(k))
        self.instance = []
        if m.get('instance') is not None:
            for k in m.get('instance'):
                temp_model = GetRoleAclResponseBodyDataInstance()
                self.instance.append(temp_model.from_map(k))
        self.package = []
        if m.get('package') is not None:
            for k in m.get('package'):
                temp_model = GetRoleAclResponseBodyDataPackage()
                self.package.append(temp_model.from_map(k))
        self.project = []
        if m.get('project') is not None:
            for k in m.get('project'):
                temp_model = GetRoleAclResponseBodyDataProject()
                self.project.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = GetRoleAclResponseBodyDataResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = GetRoleAclResponseBodyDataTable()
                self.table.append(temp_model.from_map(k))
        return self


class GetRoleAclResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRoleAclResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

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
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRoleAclResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRoleAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoleAclResponseBody = None,
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
            temp_model = GetRoleAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleAclOnObjectRequest(TeaModel):
    def __init__(
        self,
        object_name: str = None,
        object_type: str = None,
    ):
        # The name of the object.
        # 
        # This parameter is required.
        self.object_name = object_name
        # The type of the object.
        # 
        # This parameter is required.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_name is not None:
            result['objectName'] = self.object_name
        if self.object_type is not None:
            result['objectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        return self


class GetRoleAclOnObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the object.
        self.actions = actions
        # The name of the object.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRoleAclOnObjectResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRoleAclOnObjectResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRoleAclOnObjectResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRoleAclOnObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoleAclOnObjectResponseBody = None,
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
            temp_model = GetRoleAclOnObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRolePolicyResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRolePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRolePolicyResponseBody = None,
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
            temp_model = GetRolePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunningJobsRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        job_owner_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list: List[str] = None,
        to: int = None,
    ):
        # The time when the query starts. This parameter specifies the time when a job is submitted.
        # 
        # *   The time range that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the range. If the value of **from** is the same as the value of **to**, the time range is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The list of job executors.
        self.job_owner_list = job_owner_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 20.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list = quota_nickname_list
        # The time when the query ends. This parameter specifies the time when a job is submitted.
        # 
        # *   The time interval that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the interval. If the value of **from** is the same as the value of **to**, the interval is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.job_owner_list is not None:
            result['jobOwnerList'] = self.job_owner_list
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.quota_nickname_list is not None:
            result['quotaNicknameList'] = self.quota_nickname_list
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list = m.get('jobOwnerList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list = m.get('quotaNicknameList')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class GetRunningJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        job_owner_list_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list_shrink: str = None,
        to: int = None,
    ):
        # The time when the query starts. This parameter specifies the time when a job is submitted.
        # 
        # *   The time range that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the range. If the value of **from** is the same as the value of **to**, the time range is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The list of job executors.
        self.job_owner_list_shrink = job_owner_list_shrink
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 20.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list_shrink = quota_nickname_list_shrink
        # The time when the query ends. This parameter specifies the time when a job is submitted.
        # 
        # *   The time interval that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the interval. If the value of **from** is the same as the value of **to**, the interval is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.job_owner_list_shrink is not None:
            result['jobOwnerList'] = self.job_owner_list_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.quota_nickname_list_shrink is not None:
            result['quotaNicknameList'] = self.quota_nickname_list_shrink
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list_shrink = m.get('jobOwnerList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list_shrink = m.get('quotaNicknameList')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class GetRunningJobsResponseBodyDataRunningJobInfoList(TeaModel):
    def __init__(
        self,
        cu_snapshot: float = None,
        instance_id: str = None,
        job_owner: str = None,
        memory_snapshot: float = None,
        progress: float = None,
        project: str = None,
        quota_nickname: str = None,
        running_at_time: int = None,
        submitted_at_time: int = None,
    ):
        # The compute unit (CU) snapshot proportion of the job.
        self.cu_snapshot = cu_snapshot
        # The instance ID.
        self.instance_id = instance_id
        # The account that submits the job.
        self.job_owner = job_owner
        # The memory snapshot proportion of the job.
        self.memory_snapshot = memory_snapshot
        # The progress of the job.
        self.progress = progress
        # The name of the MaxCompute project.
        self.project = project
        # The nickname of the quota that is used by the job.
        self.quota_nickname = quota_nickname
        # The time when the job starts to run.
        self.running_at_time = running_at_time
        # The time when the job is submitted.
        self.submitted_at_time = submitted_at_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_snapshot is not None:
            result['cuSnapshot'] = self.cu_snapshot
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.memory_snapshot is not None:
            result['memorySnapshot'] = self.memory_snapshot
        if self.progress is not None:
            result['progress'] = self.progress
        if self.project is not None:
            result['project'] = self.project
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.running_at_time is not None:
            result['runningAtTime'] = self.running_at_time
        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuSnapshot') is not None:
            self.cu_snapshot = m.get('cuSnapshot')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('memorySnapshot') is not None:
            self.memory_snapshot = m.get('memorySnapshot')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('runningAtTime') is not None:
            self.running_at_time = m.get('runningAtTime')
        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')
        return self


class GetRunningJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        running_job_info_list: List[GetRunningJobsResponseBodyDataRunningJobInfoList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of jobs in the running state.
        self.running_job_info_list = running_job_info_list
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.running_job_info_list:
            for k in self.running_job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['runningJobInfoList'] = []
        if self.running_job_info_list is not None:
            for k in self.running_job_info_list:
                result['runningJobInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.running_job_info_list = []
        if m.get('runningJobInfoList') is not None:
            for k in m.get('runningJobInfoList'):
                temp_model = GetRunningJobsResponseBodyDataRunningJobInfoList()
                self.running_job_info_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetRunningJobsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRunningJobsResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

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
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRunningJobsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRunningJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRunningJobsResponseBody = None,
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
            temp_model = GetRunningJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableInfoRequest(TeaModel):
    def __init__(
        self,
        schema_name: str = None,
        type: str = None,
    ):
        self.schema_name = schema_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTableInfoResponseBodyDataNativeColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.label = label
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTableInfoResponseBodyDataPartitionColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.label = label
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTableInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_refresh_enabled: bool = None,
        comment: str = None,
        create_table_ddl: str = None,
        creation_time: int = None,
        display_name: str = None,
        file_num: int = None,
        is_external_table: bool = None,
        is_outdated: bool = None,
        last_access_time: int = None,
        last_ddltime: int = None,
        last_modified_time: int = None,
        lifecycle: str = None,
        location: str = None,
        materialized_view: bool = None,
        name: str = None,
        native_columns: List[GetTableInfoResponseBodyDataNativeColumns] = None,
        odps_properties_rolearn: str = None,
        odps_sql_text_option_flush_header: bool = None,
        odps_text_option_header_lines_count: int = None,
        owner: str = None,
        partition_columns: List[GetTableInfoResponseBodyDataPartitionColumns] = None,
        physical_size: int = None,
        project_name: str = None,
        rewrite_enabled: bool = None,
        schema: str = None,
        size: int = None,
        storage_handler: str = None,
        table_label: str = None,
        tablesotre_table_name: str = None,
        tablestore_columns_mapping: str = None,
        type: str = None,
        view_text: str = None,
    ):
        self.auto_refresh_enabled = auto_refresh_enabled
        self.comment = comment
        self.create_table_ddl = create_table_ddl
        self.creation_time = creation_time
        self.display_name = display_name
        self.file_num = file_num
        self.is_external_table = is_external_table
        self.is_outdated = is_outdated
        self.last_access_time = last_access_time
        self.last_ddltime = last_ddltime
        self.last_modified_time = last_modified_time
        self.lifecycle = lifecycle
        self.location = location
        self.materialized_view = materialized_view
        self.name = name
        self.native_columns = native_columns
        self.odps_properties_rolearn = odps_properties_rolearn
        self.odps_sql_text_option_flush_header = odps_sql_text_option_flush_header
        self.odps_text_option_header_lines_count = odps_text_option_header_lines_count
        self.owner = owner
        self.partition_columns = partition_columns
        self.physical_size = physical_size
        self.project_name = project_name
        self.rewrite_enabled = rewrite_enabled
        self.schema = schema
        self.size = size
        self.storage_handler = storage_handler
        self.table_label = table_label
        self.tablesotre_table_name = tablesotre_table_name
        self.tablestore_columns_mapping = tablestore_columns_mapping
        self.type = type
        self.view_text = view_text

    def validate(self):
        if self.native_columns:
            for k in self.native_columns:
                if k:
                    k.validate()
        if self.partition_columns:
            for k in self.partition_columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_enabled is not None:
            result['autoRefreshEnabled'] = self.auto_refresh_enabled
        if self.comment is not None:
            result['comment'] = self.comment
        if self.create_table_ddl is not None:
            result['createTableDDL'] = self.create_table_ddl
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.file_num is not None:
            result['fileNum'] = self.file_num
        if self.is_external_table is not None:
            result['isExternalTable'] = self.is_external_table
        if self.is_outdated is not None:
            result['isOutdated'] = self.is_outdated
        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time
        if self.last_ddltime is not None:
            result['lastDDLTime'] = self.last_ddltime
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.lifecycle is not None:
            result['lifecycle'] = self.lifecycle
        if self.location is not None:
            result['location'] = self.location
        if self.materialized_view is not None:
            result['materializedView'] = self.materialized_view
        if self.name is not None:
            result['name'] = self.name
        result['nativeColumns'] = []
        if self.native_columns is not None:
            for k in self.native_columns:
                result['nativeColumns'].append(k.to_map() if k else None)
        if self.odps_properties_rolearn is not None:
            result['odpsPropertiesRolearn'] = self.odps_properties_rolearn
        if self.odps_sql_text_option_flush_header is not None:
            result['odpsSqlTextOptionFlushHeader'] = self.odps_sql_text_option_flush_header
        if self.odps_text_option_header_lines_count is not None:
            result['odpsTextOptionHeaderLinesCount'] = self.odps_text_option_header_lines_count
        if self.owner is not None:
            result['owner'] = self.owner
        result['partitionColumns'] = []
        if self.partition_columns is not None:
            for k in self.partition_columns:
                result['partitionColumns'].append(k.to_map() if k else None)
        if self.physical_size is not None:
            result['physicalSize'] = self.physical_size
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.rewrite_enabled is not None:
            result['rewriteEnabled'] = self.rewrite_enabled
        if self.schema is not None:
            result['schema'] = self.schema
        if self.size is not None:
            result['size'] = self.size
        if self.storage_handler is not None:
            result['storageHandler'] = self.storage_handler
        if self.table_label is not None:
            result['tableLabel'] = self.table_label
        if self.tablesotre_table_name is not None:
            result['tablesotreTableName'] = self.tablesotre_table_name
        if self.tablestore_columns_mapping is not None:
            result['tablestoreColumnsMapping'] = self.tablestore_columns_mapping
        if self.type is not None:
            result['type'] = self.type
        if self.view_text is not None:
            result['viewText'] = self.view_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRefreshEnabled') is not None:
            self.auto_refresh_enabled = m.get('autoRefreshEnabled')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('createTableDDL') is not None:
            self.create_table_ddl = m.get('createTableDDL')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')
        if m.get('isExternalTable') is not None:
            self.is_external_table = m.get('isExternalTable')
        if m.get('isOutdated') is not None:
            self.is_outdated = m.get('isOutdated')
        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')
        if m.get('lastDDLTime') is not None:
            self.last_ddltime = m.get('lastDDLTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('lifecycle') is not None:
            self.lifecycle = m.get('lifecycle')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('materializedView') is not None:
            self.materialized_view = m.get('materializedView')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.native_columns = []
        if m.get('nativeColumns') is not None:
            for k in m.get('nativeColumns'):
                temp_model = GetTableInfoResponseBodyDataNativeColumns()
                self.native_columns.append(temp_model.from_map(k))
        if m.get('odpsPropertiesRolearn') is not None:
            self.odps_properties_rolearn = m.get('odpsPropertiesRolearn')
        if m.get('odpsSqlTextOptionFlushHeader') is not None:
            self.odps_sql_text_option_flush_header = m.get('odpsSqlTextOptionFlushHeader')
        if m.get('odpsTextOptionHeaderLinesCount') is not None:
            self.odps_text_option_header_lines_count = m.get('odpsTextOptionHeaderLinesCount')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        self.partition_columns = []
        if m.get('partitionColumns') is not None:
            for k in m.get('partitionColumns'):
                temp_model = GetTableInfoResponseBodyDataPartitionColumns()
                self.partition_columns.append(temp_model.from_map(k))
        if m.get('physicalSize') is not None:
            self.physical_size = m.get('physicalSize')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('rewriteEnabled') is not None:
            self.rewrite_enabled = m.get('rewriteEnabled')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('storageHandler') is not None:
            self.storage_handler = m.get('storageHandler')
        if m.get('tableLabel') is not None:
            self.table_label = m.get('tableLabel')
        if m.get('tablesotreTableName') is not None:
            self.tablesotre_table_name = m.get('tablesotreTableName')
        if m.get('tablestoreColumnsMapping') is not None:
            self.tablestore_columns_mapping = m.get('tablestoreColumnsMapping')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('viewText') is not None:
            self.view_text = m.get('viewText')
        return self


class GetTableInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTableInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetTableInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetTableInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableInfoResponseBody = None,
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
            temp_model = GetTableInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrustedProjectsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetTrustedProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrustedProjectsResponseBody = None,
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
            temp_model = GetTrustedProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillJobsRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region in which the instance resides.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class KillJobsResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class KillJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillJobsResponseBody = None,
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
            temp_model = KillJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        prefix: str = None,
        schema_name: str = None,
    ):
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The names of the returned resources. The names must start with the value specified by the prefix parameter. If the prefix parameter is set to a, the names of the returned resources must start with a.
        self.prefix = prefix
        # the name of schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class ListFunctionsResponseBodyDataFunctions(TeaModel):
    def __init__(
        self,
        class_: str = None,
        creation_time: int = None,
        display_name: str = None,
        name: str = None,
        owner: str = None,
        resources: str = None,
        schema: str = None,
    ):
        # The class in which the function was defined.
        self.class_ = class_
        # The time when the function was created. Unit: milliseconds.
        self.creation_time = creation_time
        # The display name of the function.
        self.display_name = display_name
        # The name of the function.
        self.name = name
        # The owner of the function.
        self.owner = owner
        # The name of the resource that was associated with the function.
        self.resources = resources
        # The schema of the function.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['class'] = self.class_
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.resources is not None:
            result['resources'] = self.resources
        if self.schema is not None:
            result['schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        return self


class ListFunctionsResponseBodyData(TeaModel):
    def __init__(
        self,
        functions: List[ListFunctionsResponseBodyDataFunctions] = None,
        marker: str = None,
        max_item: int = None,
    ):
        # The information about each function.
        self.functions = functions
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['functions'].append(k.to_map() if k else None)
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k in m.get('functions'):
                temp_model = ListFunctionsResponseBodyDataFunctions()
                self.functions.append(temp_model.from_map(k))
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        return self


class ListFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListFunctionsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListFunctionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionsResponseBody = None,
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
            temp_model = ListFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobInfosRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        body: str = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to sort query results in ascending or descending order.
        self.asc_order = asc_order
        # The request body parameters.
        self.body = body
        # The column based on which you want to sort query results.
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region = region
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.body is not None:
            result['body'] = self.body
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListJobInfosResponseBodyDataJobInfoList(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        cu_snapshot: float = None,
        cu_usage: int = None,
        end_at_time: int = None,
        ext_node_id: str = None,
        ext_node_on_duty: str = None,
        ext_plant_from: str = None,
        instance_id: str = None,
        job_owner: str = None,
        job_type: str = None,
        memory_snapshot: float = None,
        memory_usage: int = None,
        priority: int = None,
        project: str = None,
        quota_nickname: str = None,
        quota_type: str = None,
        region: str = None,
        running_at_time: int = None,
        running_time: int = None,
        signature: str = None,
        status: str = None,
        status_snapshot: str = None,
        submitted_at_time: int = None,
        tags: str = None,
        tenant_id: str = None,
        total_time: int = None,
        waiting_time: int = None,
    ):
        # The cluster ID.
        self.cluster = cluster
        # The CU snapshot proportion of the job.
        self.cu_snapshot = cu_snapshot
        # The total number of used compute units (CUs).
        self.cu_usage = cu_usage
        # The time when the job stops running.
        self.end_at_time = end_at_time
        # The node ID of DataWorks.
        self.ext_node_id = ext_node_id
        # The account of the node owner.
        self.ext_node_on_duty = ext_node_on_duty
        # The upstream platform.
        self.ext_plant_from = ext_plant_from
        # The instance ID.
        self.instance_id = instance_id
        # The account that commits the job.
        self.job_owner = job_owner
        # The type of the job.
        self.job_type = job_type
        # The memory snapshot proportion of the job.
        self.memory_snapshot = memory_snapshot
        # The total memory usage.
        self.memory_usage = memory_usage
        # The priority of the job.
        self.priority = priority
        # The name of the MaxCompute project.
        self.project = project
        # The nickname of the quota that is used by the job.
        self.quota_nickname = quota_nickname
        # The type of the quota.
        self.quota_type = quota_type
        # The region ID.
        self.region = region
        # The time when the job starts to run.
        self.running_at_time = running_at_time
        # The period for which the job runs.
        self.running_time = running_time
        # The signature of the SQL job.
        self.signature = signature
        # The status of the job.
        self.status = status
        # The status of the snapshot.
        self.status_snapshot = status_snapshot
        # The time when the job was committed.
        self.submitted_at_time = submitted_at_time
        # The tags.
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # The total period for which the job runs.
        self.total_time = total_time
        # The duration for which the job waits to start.
        self.waiting_time = waiting_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.cu_snapshot is not None:
            result['cuSnapshot'] = self.cu_snapshot
        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage
        if self.end_at_time is not None:
            result['endAtTime'] = self.end_at_time
        if self.ext_node_id is not None:
            result['extNodeId'] = self.ext_node_id
        if self.ext_node_on_duty is not None:
            result['extNodeOnDuty'] = self.ext_node_on_duty
        if self.ext_plant_from is not None:
            result['extPlantFrom'] = self.ext_plant_from
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.job_type is not None:
            result['jobType'] = self.job_type
        if self.memory_snapshot is not None:
            result['memorySnapshot'] = self.memory_snapshot
        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage
        if self.priority is not None:
            result['priority'] = self.priority
        if self.project is not None:
            result['project'] = self.project
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.quota_type is not None:
            result['quotaType'] = self.quota_type
        if self.region is not None:
            result['region'] = self.region
        if self.running_at_time is not None:
            result['runningAtTime'] = self.running_at_time
        if self.running_time is not None:
            result['runningTime'] = self.running_time
        if self.signature is not None:
            result['signature'] = self.signature
        if self.status is not None:
            result['status'] = self.status
        if self.status_snapshot is not None:
            result['statusSnapshot'] = self.status_snapshot
        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time
        if self.tags is not None:
            result['tags'] = self.tags
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.total_time is not None:
            result['totalTime'] = self.total_time
        if self.waiting_time is not None:
            result['waitingTime'] = self.waiting_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('cuSnapshot') is not None:
            self.cu_snapshot = m.get('cuSnapshot')
        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')
        if m.get('endAtTime') is not None:
            self.end_at_time = m.get('endAtTime')
        if m.get('extNodeId') is not None:
            self.ext_node_id = m.get('extNodeId')
        if m.get('extNodeOnDuty') is not None:
            self.ext_node_on_duty = m.get('extNodeOnDuty')
        if m.get('extPlantFrom') is not None:
            self.ext_plant_from = m.get('extPlantFrom')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')
        if m.get('memorySnapshot') is not None:
            self.memory_snapshot = m.get('memorySnapshot')
        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('quotaType') is not None:
            self.quota_type = m.get('quotaType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('runningAtTime') is not None:
            self.running_at_time = m.get('runningAtTime')
        if m.get('runningTime') is not None:
            self.running_time = m.get('runningTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusSnapshot') is not None:
            self.status_snapshot = m.get('statusSnapshot')
        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('totalTime') is not None:
            self.total_time = m.get('totalTime')
        if m.get('waitingTime') is not None:
            self.waiting_time = m.get('waitingTime')
        return self


class ListJobInfosResponseBodyData(TeaModel):
    def __init__(
        self,
        job_info_list: List[ListJobInfosResponseBodyDataJobInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of the information about the jobs.
        self.job_info_list = job_info_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.job_info_list:
            for k in self.job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobInfoList'] = []
        if self.job_info_list is not None:
            for k in self.job_info_list:
                result['jobInfoList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('jobInfoList') is not None:
            for k in m.get('jobInfoList'):
                temp_model = ListJobInfosResponseBodyDataJobInfoList()
                self.job_info_list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListJobInfosResponseBody(TeaModel):
    def __init__(
        self,
        data: ListJobInfosResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

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
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListJobInfosResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListJobInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobInfosResponseBody = None,
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
            temp_model = ListJobInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPackagesResponseBodyDataCreatedPackages(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        name: str = None,
    ):
        # The time when the package was created.
        self.create_time = create_time
        # The name of the package.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListPackagesResponseBodyDataInstalledPackages(TeaModel):
    def __init__(
        self,
        install_time: int = None,
        name: str = None,
        source_project: str = None,
        status: str = None,
    ):
        # The time when the package was installed.
        self.install_time = install_time
        # The name of the package.
        self.name = name
        # The project to which the package belongs. This parameter is required if the package is installed in the MaxCompute project.
        self.source_project = source_project
        # The status of the package.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.install_time is not None:
            result['installTime'] = self.install_time
        if self.name is not None:
            result['name'] = self.name
        if self.source_project is not None:
            result['sourceProject'] = self.source_project
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('installTime') is not None:
            self.install_time = m.get('installTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceProject') is not None:
            self.source_project = m.get('sourceProject')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListPackagesResponseBodyData(TeaModel):
    def __init__(
        self,
        created_packages: List[ListPackagesResponseBodyDataCreatedPackages] = None,
        installed_packages: List[ListPackagesResponseBodyDataInstalledPackages] = None,
    ):
        # The packages that were created.
        self.created_packages = created_packages
        # The packages that were installed.
        self.installed_packages = installed_packages

    def validate(self):
        if self.created_packages:
            for k in self.created_packages:
                if k:
                    k.validate()
        if self.installed_packages:
            for k in self.installed_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['createdPackages'] = []
        if self.created_packages is not None:
            for k in self.created_packages:
                result['createdPackages'].append(k.to_map() if k else None)
        result['installedPackages'] = []
        if self.installed_packages is not None:
            for k in self.installed_packages:
                result['installedPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.created_packages = []
        if m.get('createdPackages') is not None:
            for k in m.get('createdPackages'):
                temp_model = ListPackagesResponseBodyDataCreatedPackages()
                self.created_packages.append(temp_model.from_map(k))
        self.installed_packages = []
        if m.get('installedPackages') is not None:
            for k in m.get('installedPackages'):
                temp_model = ListPackagesResponseBodyDataInstalledPackages()
                self.installed_packages.append(temp_model.from_map(k))
        return self


class ListPackagesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListPackagesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListPackagesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPackagesResponseBody = None,
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
            temp_model = ListPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectUsersResponseBodyDataUsers(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the user.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListProjectUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        users: List[ListProjectUsersResponseBodyDataUsers] = None,
    ):
        # An array that contains users.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListProjectUsersResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListProjectUsersResponseBody(TeaModel):
    def __init__(
        self,
        data: ListProjectUsersResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProjectUsersResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectUsersResponseBody = None,
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
            temp_model = ListProjectUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        list_system_catalog: bool = None,
        marker: str = None,
        max_item: int = None,
        prefix: str = None,
        quota_name: str = None,
        quota_nick_name: str = None,
        region: str = None,
        sale_tags: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        # Specifies whether to list a project named SystemCatalog.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.list_system_catalog = list_system_catalog
        # The maximum number of entries to return on each page.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # Specifies the marker after which the returned list begins.
        self.prefix = prefix
        # The name of the quota. The value of this parameter is the identifier of the quota in MaxCompute, which differs from the quotaNickname parameter. You can configure the quotaNickname parameter. The system automatically generates a value for the quotaName parameter. This parameter is only used to describe the tunnel quota.
        self.quota_name = quota_name
        # The name of the quota.
        self.quota_nick_name = quota_nick_name
        # The ID of the region.
        self.region = region
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tags = sale_tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # The project type. Valid values: external and managed. The value external indicates an external project, which is used in the data lakehouse solution. The value managed indicates an internal project.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_system_catalog is not None:
            result['listSystemCatalog'] = self.list_system_catalog
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.quota_name is not None:
            result['quotaName'] = self.quota_name
        if self.quota_nick_name is not None:
            result['quotaNickName'] = self.quota_nick_name
        if self.region is not None:
            result['region'] = self.region
        if self.sale_tags is not None:
            result['saleTags'] = self.sale_tags
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('listSystemCatalog') is not None:
            self.list_system_catalog = m.get('listSystemCatalog')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('quotaName') is not None:
            self.quota_name = m.get('quotaName')
        if m.get('quotaNickName') is not None:
            self.quota_nick_name = m.get('quotaNickName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('saleTags') is not None:
            self.sale_tags = m.get('saleTags')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListProjectsResponseBodyDataProjectsTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListProjectsResponseBodyDataProjectsIpWhiteList(TeaModel):
    def __init__(
        self,
        ip_list: str = None,
        vpc_ip_list: str = None,
    ):
        # The list of IP addresses.
        self.ip_list = ip_list
        # The list of virtual private cloud (VPC) IP addresses.
        self.vpc_ip_list = vpc_ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.vpc_ip_list is not None:
            result['vpcIpList'] = self.vpc_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('vpcIpList') is not None:
            self.vpc_ip_list = m.get('vpcIpList')
        return self


class ListProjectsResponseBodyDataProjectsPropertiesEncryption(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        enable: bool = None,
        key: str = None,
    ):
        # The name of the encryption algorithm.
        self.algorithm = algorithm
        # Indicates whether data encryption is enabled. Valid values: true and false.
        self.enable = enable
        # The key of the encryption algorithm.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.enable is not None:
            result['enable'] = self.enable
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the lifecycle. Valid values: -mandatory: The lifecycle clause is required. You must configure a lifecycle for a table. -optional: The lifecycle clause is optional in a table creation statement. If you do not configure a lifecycle for a table, the table does not expire. -inherit: If you do not configure a lifecycle for a table when you create the table, the value of odps.table.lifecycle.value is used by default.
        self.type = type
        # The retention period of a table. Unit: days.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListProjectsResponseBodyDataProjectsProperties(TeaModel):
    def __init__(
        self,
        allow_full_scan: bool = None,
        enable_decimal_2: bool = None,
        enable_tunnel_quota_route: bool = None,
        encryption: ListProjectsResponseBodyDataProjectsPropertiesEncryption = None,
        retention_days: int = None,
        sql_metering_max: str = None,
        table_lifecycle: ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle = None,
        timezone: str = None,
        tunnel_quota: str = None,
        type_system: str = None,
    ):
        # Indicates whether a full table scan on the project is enabled.
        self.allow_full_scan = allow_full_scan
        # Indicates whether the DECIMAL data type in the MaxCompute V2.0 data type edition is enabled.
        self.enable_decimal_2 = enable_decimal_2
        # Indicates whether tunnel quota routing is enabled.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The encryption information.
        self.encryption = encryption
        # The maximum number of days for which backup data can be retained.
        self.retention_days = retention_days
        # The upper limit for the resources that are consumed by an SQL statement.
        self.sql_metering_max = sql_metering_max
        # The lifecycle of a table in the project.
        self.table_lifecycle = table_lifecycle
        # The time zone of the instance.
        self.timezone = timezone
        # The name of the tunnel quota.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values: -1: MaxCompute V1.0 data type edition. -2: MaxCompute V2.0 data type edition. -hive: Hive-compatible data type edition.
        self.type_system = type_system

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan
        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2
        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route
        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max
        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        if self.type_system is not None:
            result['typeSystem'] = self.type_system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')
        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')
        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')
        if m.get('encryption') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsPropertiesEncryption()
            self.encryption = temp_model.from_map(m['encryption'])
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')
        if m.get('tableLifecycle') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m['tableLifecycle'])
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')
        return self


class ListProjectsResponseBodyDataProjectsSaleTag(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.resource_id = resource_id
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection(TeaModel):
    def __init__(
        self,
        exception_policy: str = None,
        protected: bool = None,
    ):
        # The exception policy. If cross-project data access operations are required, the project owner must configure an exception policy in advance to allow the specified user to transfer data of a specified object from the current project to a specified project. After the exception policy is configured, data of the object can be transferred to the specified project even if the project data protection feature is enabled.
        self.exception_policy = exception_policy
        # Indicates whether project data protection is enabled.
        self.protected = protected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_policy is not None:
            result['exceptionPolicy'] = self.exception_policy
        if self.protected is not None:
            result['protected'] = self.protected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exceptionPolicy') is not None:
            self.exception_policy = m.get('exceptionPolicy')
        if m.get('protected') is not None:
            self.protected = m.get('protected')
        return self


class ListProjectsResponseBodyDataProjectsSecurityProperties(TeaModel):
    def __init__(
        self,
        enable_download_privilege: bool = None,
        label_security: bool = None,
        object_creator_has_access_permission: bool = None,
        object_creator_has_grant_permission: bool = None,
        project_protection: ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection = None,
        using_acl: bool = None,
        using_policy: bool = None,
    ):
        # Indicates whether Download control is enabled.
        self.enable_download_privilege = enable_download_privilege
        # Indicates whether label-based access control is enabled.
        self.label_security = label_security
        # Indicates whether the object creator is allowed to perform operations on objects.
        self.object_creator_has_access_permission = object_creator_has_access_permission
        # Indicates whether the object creator is allowed to authorize other users to perform operations on objects.
        self.object_creator_has_grant_permission = object_creator_has_grant_permission
        # Indicates whether project data protection is enabled.
        self.project_protection = project_protection
        # Indicates whether ACL-based access control is enabled.
        self.using_acl = using_acl
        # Indicates whether policy-based access control is enabled.
        self.using_policy = using_policy

    def validate(self):
        if self.project_protection:
            self.project_protection.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_download_privilege is not None:
            result['enableDownloadPrivilege'] = self.enable_download_privilege
        if self.label_security is not None:
            result['labelSecurity'] = self.label_security
        if self.object_creator_has_access_permission is not None:
            result['objectCreatorHasAccessPermission'] = self.object_creator_has_access_permission
        if self.object_creator_has_grant_permission is not None:
            result['objectCreatorHasGrantPermission'] = self.object_creator_has_grant_permission
        if self.project_protection is not None:
            result['projectProtection'] = self.project_protection.to_map()
        if self.using_acl is not None:
            result['usingAcl'] = self.using_acl
        if self.using_policy is not None:
            result['usingPolicy'] = self.using_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableDownloadPrivilege') is not None:
            self.enable_download_privilege = m.get('enableDownloadPrivilege')
        if m.get('labelSecurity') is not None:
            self.label_security = m.get('labelSecurity')
        if m.get('objectCreatorHasAccessPermission') is not None:
            self.object_creator_has_access_permission = m.get('objectCreatorHasAccessPermission')
        if m.get('objectCreatorHasGrantPermission') is not None:
            self.object_creator_has_grant_permission = m.get('objectCreatorHasGrantPermission')
        if m.get('projectProtection') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection()
            self.project_protection = temp_model.from_map(m['projectProtection'])
        if m.get('usingAcl') is not None:
            self.using_acl = m.get('usingAcl')
        if m.get('usingPolicy') is not None:
            self.using_policy = m.get('usingPolicy')
        return self


class ListProjectsResponseBodyDataProjects(TeaModel):
    def __init__(
        self,
        tags: List[ListProjectsResponseBodyDataProjectsTags] = None,
        comment: str = None,
        cost_storage: str = None,
        created_time: int = None,
        default_quota: str = None,
        ip_white_list: ListProjectsResponseBodyDataProjectsIpWhiteList = None,
        name: str = None,
        owner: str = None,
        properties: ListProjectsResponseBodyDataProjectsProperties = None,
        region_id: str = None,
        sale_tag: ListProjectsResponseBodyDataProjectsSaleTag = None,
        security_properties: ListProjectsResponseBodyDataProjectsSecurityProperties = None,
        status: str = None,
        three_tier_model: bool = None,
        type: str = None,
    ):
        # The tags.
        self.tags = tags
        # The remarks.
        self.comment = comment
        # The storage usage.
        self.cost_storage = cost_storage
        # Create time
        self.created_time = created_time
        # The default computing quota.
        self.default_quota = default_quota
        # The IP address whitelist.
        self.ip_white_list = ip_white_list
        # The name of the project.
        self.name = name
        # The owner of the project.
        self.owner = owner
        # The properties of the project.
        self.properties = properties
        # Region Id
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The permission properties.
        self.security_properties = security_properties
        # The status of the project. Valid values: -AVAILABLE: The project is available. -READONLY: The project is read-only. -FROZEN: The project is frozen. -DELETING: The project is being deleted.
        self.status = status
        # Indicates whether the current project supports the MaxCompute three-layer model.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.three_tier_model = three_tier_model
        # The project type. Valid values: -managed: The project is an internal project. -external: The project is an external project.
        self.type = type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ip_white_list:
            self.ip_white_list.validate()
        if self.properties:
            self.properties.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.security_properties:
            self.security_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.comment is not None:
            result['comment'] = self.comment
        if self.cost_storage is not None:
            result['costStorage'] = self.cost_storage
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.default_quota is not None:
            result['defaultQuota'] = self.default_quota
        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.properties is not None:
            result['properties'] = self.properties.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.security_properties is not None:
            result['securityProperties'] = self.security_properties.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.three_tier_model is not None:
            result['threeTierModel'] = self.three_tier_model
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListProjectsResponseBodyDataProjectsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('costStorage') is not None:
            self.cost_storage = m.get('costStorage')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('defaultQuota') is not None:
            self.default_quota = m.get('defaultQuota')
        if m.get('ipWhiteList') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsIpWhiteList()
            self.ip_white_list = temp_model.from_map(m['ipWhiteList'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('properties') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsProperties()
            self.properties = temp_model.from_map(m['properties'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('securityProperties') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSecurityProperties()
            self.security_properties = temp_model.from_map(m['securityProperties'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('threeTierModel') is not None:
            self.three_tier_model = m.get('threeTierModel')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListProjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        marker: str = None,
        max_item: int = None,
        projects: List[ListProjectsResponseBodyDataProjects] = None,
    ):
        # A pagination token. Only continuous page turning is supported. If NextToken is not empty, the next page exists. The value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The description of the project.
        self.projects = projects

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = ListProjectsResponseBodyDataProjects()
                self.projects.append(temp_model.from_map(k))
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListProjectsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProjectsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsResponseBody = None,
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasRequest(TeaModel):
    def __init__(
        self,
        billing_type: str = None,
        marker: str = None,
        max_item: int = None,
        product_id: str = None,
        region: str = None,
        sale_tags: str = None,
        tenant_id: str = None,
    ):
        # The billing method of the quota.
        self.billing_type = billing_type
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The service ID.
        self.product_id = product_id
        # The ID of the region.
        self.region = region
        # The cost tag. You can filter out quota objects based on the cost tag. The cost tag is created when you tag a service.
        self.sale_tags = sale_tags
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_type is not None:
            result['billingType'] = self.billing_type
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.region is not None:
            result['region'] = self.region
        if self.sale_tags is not None:
            result['saleTags'] = self.sale_tags
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingType') is not None:
            self.billing_type = m.get('billingType')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('saleTags') is not None:
            self.sale_tags = m.get('saleTags')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListQuotasResponseBodyDataQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyDataQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag = None,
        schedule_info: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the endpoint group.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version of the algorithm image.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyDataQuotaInfoList(TeaModel):
    def __init__(
        self,
        tags: List[ListQuotasResponseBodyDataQuotaInfoListTags] = None,
        billing_policy: ListQuotasResponseBodyDataQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: ListQuotasResponseBodyDataQuotaInfoListSaleTag = None,
        schedule_info: ListQuotasResponseBodyDataQuotaInfoListScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The tags.
        self.tags = tags
        # The information of the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The quota ID.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the endpoint group.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        marker: str = None,
        max_item: int = None,
        quota_info_list: List[ListQuotasResponseBodyDataQuotaInfoList] = None,
    ):
        # A pagination token. Only continuous page turning is supported. If NextToken is not empty, the next page exists. The value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The list of quotas.
        self.quota_info_list = quota_info_list

    def validate(self):
        if self.quota_info_list:
            for k in self.quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['quotaInfoList'] = []
        if self.quota_info_list is not None:
            for k in self.quota_info_list:
                result['quotaInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.quota_info_list = []
        if m.get('quotaInfoList') is not None:
            for k in m.get('quotaInfoList'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoList()
                self.quota_info_list.append(temp_model.from_map(k))
        return self


class ListQuotasResponseBodyQuotaInfoListTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListQuotasResponseBodyQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag = None,
        schedule_info: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The alias of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the endpoint group.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyQuotaInfoList(TeaModel):
    def __init__(
        self,
        tags: List[ListQuotasResponseBodyQuotaInfoListTags] = None,
        billing_policy: ListQuotasResponseBodyQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: ListQuotasResponseBodyQuotaInfoListSaleTag = None,
        schedule_info: ListQuotasResponseBodyQuotaInfoListScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The tags.
        self.tags = tags
        # The information of the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The quota ID.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the endpoint group.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version.
        self.version = version

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListQuotasResponseBodyQuotaInfoListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        data: ListQuotasResponseBodyData = None,
        marker: str = None,
        max_item: int = None,
        quota_info_list: List[ListQuotasResponseBodyQuotaInfoList] = None,
        request_id: str = None,
    ):
        # A pagination token. Only continuous page turning is supported. If NextToken is not empty, the next page exists. The value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The returned data.
        self.data = data
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The list of quotas.
        self.quota_info_list = quota_info_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()
        if self.quota_info_list:
            for k in self.quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['quotaInfoList'] = []
        if self.quota_info_list is not None:
            for k in self.quota_info_list:
                result['quotaInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('data') is not None:
            temp_model = ListQuotasResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.quota_info_list = []
        if m.get('quotaInfoList') is not None:
            for k in m.get('quotaInfoList'):
                temp_model = ListQuotasResponseBodyQuotaInfoList()
                self.quota_info_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotasResponseBody = None,
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
            temp_model = ListQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasPlansRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        tenant_id: str = None,
    ):
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota plan was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuota(TeaModel):
    def __init__(
        self,
        billing_policy: ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota plan was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the quota.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasPlansResponseBodyDataPlanList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        quota: ListQuotasPlansResponseBodyDataPlanListQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class ListQuotasPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        plan_list: List[ListQuotasPlansResponseBodyDataPlanList] = None,
    ):
        # The list of quota plans.
        self.plan_list = plan_list

    def validate(self):
        if self.plan_list:
            for k in self.plan_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['planList'] = []
        if self.plan_list is not None:
            for k in self.plan_list:
                result['planList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plan_list = []
        if m.get('planList') is not None:
            for k in m.get('planList'):
                temp_model = ListQuotasPlansResponseBodyDataPlanList()
                self.plan_list.append(temp_model.from_map(k))
        return self


class ListQuotasPlansResponseBody(TeaModel):
    def __init__(
        self,
        data: ListQuotasPlansResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListQuotasPlansResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQuotasPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotasPlansResponseBody = None,
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
            temp_model = ListQuotasPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        name: str = None,
        schema_name: str = None,
    ):
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The name of the resource.
        self.name = name
        # The name of the schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class ListResourcesResponseBodyDataResources(TeaModel):
    def __init__(
        self,
        comment: str = None,
        content_md5: str = None,
        creation_time: int = None,
        display_name: str = None,
        last_modified_time: int = None,
        last_updator: str = None,
        name: str = None,
        owner: str = None,
        schema: str = None,
        size: int = None,
        type: str = None,
    ):
        # The remarks.
        self.comment = comment
        # The Base64-encoded 128-bit MD5 hash value of the HTTP request body.
        self.content_md5 = content_md5
        # The time when the resource was created.
        self.creation_time = creation_time
        # The display name.
        self.display_name = display_name
        # The time when the resource was modified.
        self.last_modified_time = last_modified_time
        # The user who updated the resource.
        self.last_updator = last_updator
        # The name of the resource.
        self.name = name
        # The owner of the resource.
        self.owner = owner
        # The schema to which the resource belongs.
        self.schema = schema
        # The size of the resource.
        self.size = size
        # The resource type.
        # 
        # Valid values:
        # 
        # *   file
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   py
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   jar
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   volumefile
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   table
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.content_md5 is not None:
            result['contentMD5'] = self.content_md5
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.last_updator is not None:
            result['lastUpdator'] = self.last_updator
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.schema is not None:
            result['schema'] = self.schema
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('contentMD5') is not None:
            self.content_md5 = m.get('contentMD5')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('lastUpdator') is not None:
            self.last_updator = m.get('lastUpdator')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        resources: List[ListResourcesResponseBodyDataResources] = None,
    ):
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The list of resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ListResourcesResponseBodyDataResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListResourcesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesResponseBody = None,
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
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesResponseBodyDataRolesAclFunction(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the function.
        self.actions = actions
        # The name of the function.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclInstance(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the instance.
        self.actions = actions
        # The name of the instance.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclPackage(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the package.
        self.actions = actions
        # The name of the package.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclProject(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the project.
        self.actions = actions
        # The name of the MaxCompute project.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclResource(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the resource.
        self.actions = actions
        # The name of the resource.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclTable(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the table.
        self.actions = actions
        # The name of the table.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAcl(TeaModel):
    def __init__(
        self,
        function: List[ListRolesResponseBodyDataRolesAclFunction] = None,
        instance: List[ListRolesResponseBodyDataRolesAclInstance] = None,
        package: List[ListRolesResponseBodyDataRolesAclPackage] = None,
        project: List[ListRolesResponseBodyDataRolesAclProject] = None,
        resource: List[ListRolesResponseBodyDataRolesAclResource] = None,
        table: List[ListRolesResponseBodyDataRolesAclTable] = None,
    ):
        # The function.
        self.function = function
        # The instance.
        self.instance = instance
        # The package.
        self.package = package
        # The project.
        self.project = project
        # The resource.
        self.resource = resource
        # The table.
        self.table = table

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()
        if self.package:
            for k in self.package:
                if k:
                    k.validate()
        if self.project:
            for k in self.project:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['instance'].append(k.to_map() if k else None)
        result['package'] = []
        if self.package is not None:
            for k in self.package:
                result['package'].append(k.to_map() if k else None)
        result['project'] = []
        if self.project is not None:
            for k in self.project:
                result['project'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = ListRolesResponseBodyDataRolesAclFunction()
                self.function.append(temp_model.from_map(k))
        self.instance = []
        if m.get('instance') is not None:
            for k in m.get('instance'):
                temp_model = ListRolesResponseBodyDataRolesAclInstance()
                self.instance.append(temp_model.from_map(k))
        self.package = []
        if m.get('package') is not None:
            for k in m.get('package'):
                temp_model = ListRolesResponseBodyDataRolesAclPackage()
                self.package.append(temp_model.from_map(k))
        self.project = []
        if m.get('project') is not None:
            for k in m.get('project'):
                temp_model = ListRolesResponseBodyDataRolesAclProject()
                self.project.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = ListRolesResponseBodyDataRolesAclResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = ListRolesResponseBodyDataRolesAclTable()
                self.table.append(temp_model.from_map(k))
        return self


class ListRolesResponseBodyDataRoles(TeaModel):
    def __init__(
        self,
        acl: ListRolesResponseBodyDataRolesAcl = None,
        name: str = None,
        policy: str = None,
        type: str = None,
    ):
        # The ACL-based permissions that are granted to the role.
        self.acl = acl
        # The name of the role.
        self.name = name
        # The policy that is attached to the role.
        self.policy = policy
        # The type of the role.
        self.type = type

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.policy is not None:
            result['policy'] = self.policy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            temp_model = ListRolesResponseBodyDataRolesAcl()
            self.acl = temp_model.from_map(m['acl'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListRolesResponseBodyData(TeaModel):
    def __init__(
        self,
        roles: List[ListRolesResponseBodyDataRoles] = None,
    ):
        # The MaxCompute project-level roles.
        self.roles = roles

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = ListRolesResponseBodyDataRoles()
                self.roles.append(temp_model.from_map(k))
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListRolesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListRolesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRolesResponseBody = None,
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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        prefix: str = None,
        schema_name: str = None,
        type: str = None,
    ):
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The names of the returned resources. The names must start with the value specified by the prefix parameter. If the prefix parameter is set to a, the names of the returned resources must start with a.
        self.prefix = prefix
        # The name of the schema.
        self.schema_name = schema_name
        # The type of the table.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTablesResponseBodyDataTablesNativeColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
    ):
        # The remarks.
        self.comment = comment
        # The security level of the column.
        self.label = label
        # The name of the column.
        self.name = name
        # The type of the column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTablesResponseBodyDataTablesPartitionColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
    ):
        # The remarks.
        self.comment = comment
        # The security level of the partition column.
        self.label = label
        # The name of the partition column.
        self.name = name
        # The type of the partition column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTablesResponseBodyDataTables(TeaModel):
    def __init__(
        self,
        auto_refresh_enabled: bool = None,
        create_table_ddl: str = None,
        creation_time: int = None,
        display_name: str = None,
        file_num: int = None,
        is_external_table: bool = None,
        is_outdated: bool = None,
        last_access_time: int = None,
        last_ddltime: int = None,
        last_modified_time: int = None,
        lifecycle: str = None,
        location: str = None,
        materialized_view: bool = None,
        name: str = None,
        native_columns: List[ListTablesResponseBodyDataTablesNativeColumns] = None,
        odps_properties_rolearn: str = None,
        odps_sql_text_option_flush_header: bool = None,
        odps_text_option_header_lines_count: int = None,
        owner: str = None,
        partition_columns: List[ListTablesResponseBodyDataTablesPartitionColumns] = None,
        physical_size: int = None,
        project_name: str = None,
        rewrite_enabled: bool = None,
        schema: str = None,
        size: int = None,
        storage_handler: str = None,
        table_comment: str = None,
        table_label: str = None,
        tablesotre_table_name: str = None,
        tablestore_columns_mapping: str = None,
        type: str = None,
        view_text: str = None,
    ):
        # Indicates whether to enable the scheduled update feature for the materialized view.
        self.auto_refresh_enabled = auto_refresh_enabled
        # The DDL statement that is used to create the table.
        self.create_table_ddl = create_table_ddl
        # The time when the table was created.
        self.creation_time = creation_time
        # The display name of the table.
        self.display_name = display_name
        # The number of files.
        self.file_num = file_num
        # Indicates whether the table is an external table.
        self.is_external_table = is_external_table
        # Indicates whether the data in the materialized view is invalid due to data changes in the source table.
        self.is_outdated = is_outdated
        # The time when the data was last accessed.
        self.last_access_time = last_access_time
        # The last time when the DDL statement of the table was updated.
        self.last_ddltime = last_ddltime
        # The time when the data was last updated.
        self.last_modified_time = last_modified_time
        # The lifecycle of the table.
        self.lifecycle = lifecycle
        # The storage location of the external table.
        self.location = location
        # Indicates whether a materialized view is created.
        self.materialized_view = materialized_view
        # The name of the table.
        self.name = name
        # The information about columns.
        self.native_columns = native_columns
        # The Alibaba Cloud Resource Name (ARN) of AliyunODPSDefaultRole in Resource Access Management (RAM).
        self.odps_properties_rolearn = odps_properties_rolearn
        # Indicates whether to ignore the table header.
        self.odps_sql_text_option_flush_header = odps_sql_text_option_flush_header
        # Indicates whether to ignore the first N rows of the table header.
        self.odps_text_option_header_lines_count = odps_text_option_header_lines_count
        # The owner of the table.
        self.owner = owner
        # The information about the partition column.
        self.partition_columns = partition_columns
        # The physical size of the table.
        self.physical_size = physical_size
        # The name of the project.
        self.project_name = project_name
        # Indicates whether to enable the query rewrite operation that is performed based on the materialized view.
        self.rewrite_enabled = rewrite_enabled
        # The schema to which the table belongs.
        self.schema = schema
        # The size of the table.
        self.size = size
        # The extractor of the external table.
        self.storage_handler = storage_handler
        # The description of the table.
        self.table_comment = table_comment
        # The security level of the table.
        self.table_label = table_label
        # The name of the Tablestore table that you want MaxCompute to access.
        self.tablesotre_table_name = tablesotre_table_name
        # The columns of the Tablestore table that you want MaxCompute to access. The columns include primary key columns and attribute columns.
        self.tablestore_columns_mapping = tablestore_columns_mapping
        # The type of the table.
        self.type = type
        # The statement that is used to generate the view.
        self.view_text = view_text

    def validate(self):
        if self.native_columns:
            for k in self.native_columns:
                if k:
                    k.validate()
        if self.partition_columns:
            for k in self.partition_columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_enabled is not None:
            result['autoRefreshEnabled'] = self.auto_refresh_enabled
        if self.create_table_ddl is not None:
            result['createTableDDL'] = self.create_table_ddl
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.file_num is not None:
            result['fileNum'] = self.file_num
        if self.is_external_table is not None:
            result['isExternalTable'] = self.is_external_table
        if self.is_outdated is not None:
            result['isOutdated'] = self.is_outdated
        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time
        if self.last_ddltime is not None:
            result['lastDDLTime'] = self.last_ddltime
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.lifecycle is not None:
            result['lifecycle'] = self.lifecycle
        if self.location is not None:
            result['location'] = self.location
        if self.materialized_view is not None:
            result['materializedView'] = self.materialized_view
        if self.name is not None:
            result['name'] = self.name
        result['nativeColumns'] = []
        if self.native_columns is not None:
            for k in self.native_columns:
                result['nativeColumns'].append(k.to_map() if k else None)
        if self.odps_properties_rolearn is not None:
            result['odpsPropertiesRolearn'] = self.odps_properties_rolearn
        if self.odps_sql_text_option_flush_header is not None:
            result['odpsSqlTextOptionFlushHeader'] = self.odps_sql_text_option_flush_header
        if self.odps_text_option_header_lines_count is not None:
            result['odpsTextOptionHeaderLinesCount'] = self.odps_text_option_header_lines_count
        if self.owner is not None:
            result['owner'] = self.owner
        result['partitionColumns'] = []
        if self.partition_columns is not None:
            for k in self.partition_columns:
                result['partitionColumns'].append(k.to_map() if k else None)
        if self.physical_size is not None:
            result['physicalSize'] = self.physical_size
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.rewrite_enabled is not None:
            result['rewriteEnabled'] = self.rewrite_enabled
        if self.schema is not None:
            result['schema'] = self.schema
        if self.size is not None:
            result['size'] = self.size
        if self.storage_handler is not None:
            result['storageHandler'] = self.storage_handler
        if self.table_comment is not None:
            result['tableComment'] = self.table_comment
        if self.table_label is not None:
            result['tableLabel'] = self.table_label
        if self.tablesotre_table_name is not None:
            result['tablesotreTableName'] = self.tablesotre_table_name
        if self.tablestore_columns_mapping is not None:
            result['tablestoreColumnsMapping'] = self.tablestore_columns_mapping
        if self.type is not None:
            result['type'] = self.type
        if self.view_text is not None:
            result['viewText'] = self.view_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRefreshEnabled') is not None:
            self.auto_refresh_enabled = m.get('autoRefreshEnabled')
        if m.get('createTableDDL') is not None:
            self.create_table_ddl = m.get('createTableDDL')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')
        if m.get('isExternalTable') is not None:
            self.is_external_table = m.get('isExternalTable')
        if m.get('isOutdated') is not None:
            self.is_outdated = m.get('isOutdated')
        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')
        if m.get('lastDDLTime') is not None:
            self.last_ddltime = m.get('lastDDLTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('lifecycle') is not None:
            self.lifecycle = m.get('lifecycle')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('materializedView') is not None:
            self.materialized_view = m.get('materializedView')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.native_columns = []
        if m.get('nativeColumns') is not None:
            for k in m.get('nativeColumns'):
                temp_model = ListTablesResponseBodyDataTablesNativeColumns()
                self.native_columns.append(temp_model.from_map(k))
        if m.get('odpsPropertiesRolearn') is not None:
            self.odps_properties_rolearn = m.get('odpsPropertiesRolearn')
        if m.get('odpsSqlTextOptionFlushHeader') is not None:
            self.odps_sql_text_option_flush_header = m.get('odpsSqlTextOptionFlushHeader')
        if m.get('odpsTextOptionHeaderLinesCount') is not None:
            self.odps_text_option_header_lines_count = m.get('odpsTextOptionHeaderLinesCount')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        self.partition_columns = []
        if m.get('partitionColumns') is not None:
            for k in m.get('partitionColumns'):
                temp_model = ListTablesResponseBodyDataTablesPartitionColumns()
                self.partition_columns.append(temp_model.from_map(k))
        if m.get('physicalSize') is not None:
            self.physical_size = m.get('physicalSize')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('rewriteEnabled') is not None:
            self.rewrite_enabled = m.get('rewriteEnabled')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('storageHandler') is not None:
            self.storage_handler = m.get('storageHandler')
        if m.get('tableComment') is not None:
            self.table_comment = m.get('tableComment')
        if m.get('tableLabel') is not None:
            self.table_label = m.get('tableLabel')
        if m.get('tablesotreTableName') is not None:
            self.tablesotre_table_name = m.get('tablesotreTableName')
        if m.get('tablestoreColumnsMapping') is not None:
            self.tablestore_columns_mapping = m.get('tablestoreColumnsMapping')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('viewText') is not None:
            self.view_text = m.get('viewText')
        return self


class ListTablesResponseBodyData(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        tables: List[ListTablesResponseBodyDataTables] = None,
    ):
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The information about tables.
        self.tables = tables

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.tables = []
        if m.get('tables') is not None:
            for k in m.get('tables'):
                temp_model = ListTablesResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        return self


class ListTablesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTablesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListTablesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTablesResponseBody = None,
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
            temp_model = ListTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListUsersResponseBodyDataUsers(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        account_type: str = None,
        display_name: str = None,
        tenant_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The username of the account.
        self.account_name = account_name
        # The type of the account.
        self.account_type = account_type
        # The display name.
        self.display_name = display_name
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        users: List[ListUsersResponseBodyDataUsers] = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count
        # The users.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListUsersResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        data: ListUsersResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersByRoleResponseBodyDataUsers(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the user.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListUsersByRoleResponseBodyData(TeaModel):
    def __init__(
        self,
        users: List[ListUsersByRoleResponseBodyDataUsers] = None,
    ):
        # The users.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListUsersByRoleResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersByRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: ListUsersByRoleResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListUsersByRoleResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUsersByRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersByRoleResponseBody = None,
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
            temp_model = ListUsersByRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePackageRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdatePackageResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePackageResponseBody = None,
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
            temp_model = UpdatePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateProjectIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProjectIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectIpWhiteListResponseBody = None,
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
            temp_model = UpdateProjectIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        ak_proven: str = None,
    ):
        self.common_headers = common_headers
        # The trusted AccessKey pairs.
        self.ak_proven = ak_proven

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.ak_proven is not None:
            result['AkProven'] = self.ak_proven
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AkProven') is not None:
            self.ak_proven = m.get('AkProven')
        return self


class UpdateQuotaRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameter.
        self.body = body
        # The region ID.
        self.region = region
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateQuotaResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQuotaResponseBody = None,
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
            temp_model = UpdateQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQuotaPlanResponseBody = None,
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
            temp_model = UpdateQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaScheduleRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateQuotaScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQuotaScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQuotaScheduleResponseBody = None,
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
            temp_model = UpdateQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


