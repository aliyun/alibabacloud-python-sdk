# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_type: str = None,
        project_name: str = None,
    ):
        self.source_ip = source_ip
        self.project_type = project_type
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class CreateProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        gmt_create: int = None,
    ):
        self.project_id = project_id
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        data: CreateProjectResponseBodyData = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = CreateProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class CreateSlrRoleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        role_name: str = None,
        duration_seconds: int = None,
    ):
        self.source_ip = source_ip
        self.role_name = role_name
        self.duration_seconds = duration_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        return self


class CreateSlrRoleResponseBody(TeaModel):
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


class CreateSlrRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSlrRoleResponseBody = None,
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
            temp_model = CreateSlrRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMnsServeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteMnsServeResponseBody(TeaModel):
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


class DeleteMnsServeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMnsServeResponseBody = None,
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
            temp_model = DeleteMnsServeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        group_id: int = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserGroupResponseBody = None,
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
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        user_id: int = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.user_id = user_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserInfoResponseBody = None,
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
            temp_model = DeleteUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllEndPointRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeAllEndPointResponseBodyData(TeaModel):
    def __init__(
        self,
        city_name: str = None,
        end_point: str = None,
    ):
        self.city_name = city_name
        self.end_point = end_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        return self


class DescribeAllEndPointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        data: List[DescribeAllEndPointResponseBodyData] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAllEndPointResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAllEndPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAllEndPointResponseBody = None,
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
            temp_model = DescribeAllEndPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBindUserIdListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeBindUserIdListResponseBodyData(TeaModel):
    def __init__(
        self,
        certificate_type: str = None,
        user_name: str = None,
        certificate_no: str = None,
        id: int = None,
    ):
        self.certificate_type = certificate_type
        self.user_name = user_name
        self.certificate_no = certificate_no
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.certificate_no is not None:
            result['CertificateNo'] = self.certificate_no
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('CertificateNo') is not None:
            self.certificate_no = m.get('CertificateNo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeBindUserIdListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[DescribeBindUserIdListResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeBindUserIdListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class DescribeBindUserIdListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBindUserIdListResponseBody = None,
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
            temp_model = DescribeBindUserIdListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateTypeListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeCertificateTypeListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        type_list: List[str] = None,
    ):
        self.request_id = request_id
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type_list is not None:
            result['TypeList'] = self.type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')
        return self


class DescribeCertificateTypeListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCertificateTypeListResponseBody = None,
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
            temp_model = DescribeCertificateTypeListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        page_size: int = None,
        current_page: int = None,
        keyword: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.page_size = page_size
        self.current_page = current_page
        self.keyword = keyword
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeDeviceListResponseBodyDeviceList(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        device_status: str = None,
        category_name: str = None,
        memo_name: str = None,
        iot_id: str = None,
    ):
        self.device_name = device_name
        self.device_status = device_status
        self.category_name = category_name
        self.memo_name = memo_name
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.memo_name is not None:
            result['MemoName'] = self.memo_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('MemoName') is not None:
            self.memo_name = m.get('MemoName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class DescribeDeviceListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        device_list: List[DescribeDeviceListResponseBodyDeviceList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.device_list = device_list

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DeviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['DeviceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.device_list = []
        if m.get('DeviceList') is not None:
            for k in m.get('DeviceList'):
                temp_model = DescribeDeviceListResponseBodyDeviceList()
                self.device_list.append(temp_model.from_map(k))
        return self


class DescribeDeviceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceListResponseBody = None,
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
            temp_model = DescribeDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExcelAnalysisResultRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        key: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.key = key
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.key is not None:
            result['Key'] = self.key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeExcelAnalysisResultResponseBodyExcelResult(TeaModel):
    def __init__(
        self,
        insert_count: int = None,
        update_count: int = None,
        error_count: int = None,
        error_line: List[str] = None,
        total: int = None,
    ):
        self.insert_count = insert_count
        self.update_count = update_count
        self.error_count = error_count
        self.error_line = error_line
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.insert_count is not None:
            result['InsertCount'] = self.insert_count
        if self.update_count is not None:
            result['UpdateCount'] = self.update_count
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.error_line is not None:
            result['ErrorLine'] = self.error_line
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InsertCount') is not None:
            self.insert_count = m.get('InsertCount')
        if m.get('UpdateCount') is not None:
            self.update_count = m.get('UpdateCount')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('ErrorLine') is not None:
            self.error_line = m.get('ErrorLine')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeExcelAnalysisResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        excel_result: DescribeExcelAnalysisResultResponseBodyExcelResult = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.excel_result = excel_result
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        if self.excel_result:
            self.excel_result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.excel_result is not None:
            result['ExcelResult'] = self.excel_result.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExcelResult') is not None:
            temp_model = DescribeExcelAnalysisResultResponseBodyExcelResult()
            self.excel_result = temp_model.from_map(m['ExcelResult'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExcelAnalysisResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExcelAnalysisResultResponseBody = None,
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
            temp_model = DescribeExcelAnalysisResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIdentifyRecordListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        group_name: str = None,
        device_name: str = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
        current_page: int = None,
        user_name: str = None,
        certificate_no: str = None,
        phone_no: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.group_name = group_name
        self.device_name = device_name
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time
        self.current_page = current_page
        self.user_name = user_name
        self.certificate_no = certificate_no
        self.phone_no = phone_no
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.certificate_no is not None:
            result['CertificateNo'] = self.certificate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('CertificateNo') is not None:
            self.certificate_no = m.get('CertificateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeIdentifyRecordListResponseBodyRecordList(TeaModel):
    def __init__(
        self,
        captured_image: str = None,
        device_name: str = None,
        group_name: str = None,
        user_id: int = None,
        identifying_image: str = None,
        gmt_create: int = None,
        user_name: str = None,
        iot_id: str = None,
    ):
        self.captured_image = captured_image
        self.device_name = device_name
        self.group_name = group_name
        self.user_id = user_id
        self.identifying_image = identifying_image
        self.gmt_create = gmt_create
        self.user_name = user_name
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.captured_image is not None:
            result['CapturedImage'] = self.captured_image
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.identifying_image is not None:
            result['IdentifyingImage'] = self.identifying_image
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapturedImage') is not None:
            self.captured_image = m.get('CapturedImage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('IdentifyingImage') is not None:
            self.identifying_image = m.get('IdentifyingImage')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class DescribeIdentifyRecordListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        record_list: List[DescribeIdentifyRecordListResponseBodyRecordList] = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.record_list = record_list
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        if self.record_list:
            for k in self.record_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RecordList'] = []
        if self.record_list is not None:
            for k in self.record_list:
                result['RecordList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.record_list = []
        if m.get('RecordList') is not None:
            for k in m.get('RecordList'):
                temp_model = DescribeIdentifyRecordListResponseBodyRecordList()
                self.record_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeIdentifyRecordListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIdentifyRecordListResponseBody = None,
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
            temp_model = DescribeIdentifyRecordListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMnsOauthRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeMnsOauthResponseBodyData(TeaModel):
    def __init__(
        self,
        topic_list: List[str] = None,
        topic_name: str = None,
        mns_authorized: bool = None,
        end_point: str = None,
        mns_serve: bool = None,
        open_mns_service: bool = None,
    ):
        self.topic_list = topic_list
        self.topic_name = topic_name
        self.mns_authorized = mns_authorized
        self.end_point = end_point
        self.mns_serve = mns_serve
        self.open_mns_service = open_mns_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic_list is not None:
            result['TopicList'] = self.topic_list
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.mns_authorized is not None:
            result['MnsAuthorized'] = self.mns_authorized
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.mns_serve is not None:
            result['MnsServe'] = self.mns_serve
        if self.open_mns_service is not None:
            result['OpenMnsService'] = self.open_mns_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TopicList') is not None:
            self.topic_list = m.get('TopicList')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('MnsAuthorized') is not None:
            self.mns_authorized = m.get('MnsAuthorized')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('MnsServe') is not None:
            self.mns_serve = m.get('MnsServe')
        if m.get('OpenMnsService') is not None:
            self.open_mns_service = m.get('OpenMnsService')
        return self


class DescribeMnsOauthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeMnsOauthResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeMnsOauthResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeMnsOauthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMnsOauthResponseBody = None,
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
            temp_model = DescribeMnsOauthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssOauthRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeOssOauthResponseBodyData(TeaModel):
    def __init__(
        self,
        oss_serve: bool = None,
        bucket_name: str = None,
        open_oss_service: bool = None,
        oss_authorized: bool = None,
        open_oss_time: int = None,
    ):
        self.oss_serve = oss_serve
        self.bucket_name = bucket_name
        self.open_oss_service = open_oss_service
        self.oss_authorized = oss_authorized
        self.open_oss_time = open_oss_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.oss_serve is not None:
            result['OssServe'] = self.oss_serve
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.open_oss_service is not None:
            result['OpenOssService'] = self.open_oss_service
        if self.oss_authorized is not None:
            result['OssAuthorized'] = self.oss_authorized
        if self.open_oss_time is not None:
            result['OpenOssTime'] = self.open_oss_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssServe') is not None:
            self.oss_serve = m.get('OssServe')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OpenOssService') is not None:
            self.open_oss_service = m.get('OpenOssService')
        if m.get('OssAuthorized') is not None:
            self.oss_authorized = m.get('OssAuthorized')
        if m.get('OpenOssTime') is not None:
            self.open_oss_time = m.get('OpenOssTime')
        return self


class DescribeOssOauthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeOssOauthResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeOssOauthResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeOssOauthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOssOauthResponseBody = None,
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
            temp_model = DescribeOssOauthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSignedUrlRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
        key: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class DescribeSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        img_url: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.img_url = img_url
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.img_url is not None:
            result['ImgUrl'] = self.img_url
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ImgUrl') is not None:
            self.img_url = m.get('ImgUrl')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSignedUrlResponseBody = None,
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
            temp_model = DescribeSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopicRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
        end_point: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id
        self.end_point = end_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        return self


class DescribeTopicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[str] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DescribeTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTopicResponseBody = None,
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
            temp_model = DescribeTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadPreSignRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeUploadPreSignResponseBody(TeaModel):
    def __init__(
        self,
        policy: str = None,
        expire: str = None,
        request_id: str = None,
        access_id: str = None,
        signature: str = None,
        host: str = None,
        code: int = None,
        key: str = None,
        success: bool = None,
    ):
        self.policy = policy
        self.expire = expire
        self.request_id = request_id
        self.access_id = access_id
        self.signature = signature
        self.host = host
        self.code = code
        self.key = key
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.code is not None:
            result['Code'] = self.code
        if self.key is not None:
            result['Key'] = self.key
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeUploadPreSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUploadPreSignResponseBody = None,
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
            temp_model = DescribeUploadPreSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserGroupListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeUserGroupListResponseBodyData(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        group_user_count: int = None,
        id: int = None,
    ):
        self.group_name = group_name
        self.group_user_count = group_user_count
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_user_count is not None:
            result['GroupUserCount'] = self.group_user_count
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupUserCount') is not None:
            self.group_user_count = m.get('GroupUserCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeUserGroupListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[DescribeUserGroupListResponseBodyData] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeUserGroupListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeUserGroupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserGroupListResponseBody = None,
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
            temp_model = DescribeUserGroupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserInfoListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        page_size: int = None,
        user_name: str = None,
        current_page: int = None,
        certificate_no: str = None,
        phone_no: str = None,
        user_group_id: int = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.page_size = page_size
        self.user_name = user_name
        self.current_page = current_page
        self.certificate_no = certificate_no
        self.phone_no = phone_no
        self.user_group_id = user_group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.certificate_no is not None:
            result['CertificateNo'] = self.certificate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('CertificateNo') is not None:
            self.certificate_no = m.get('CertificateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeUserInfoListResponseBodyUserInfoList(TeaModel):
    def __init__(
        self,
        sex: int = None,
        certificate_type: str = None,
        birthday: int = None,
        phone_no: str = None,
        group_name: str = None,
        user_group_id: int = None,
        identifying_image: str = None,
        user_name: str = None,
        certificate_no: str = None,
        id: int = None,
    ):
        self.sex = sex
        self.certificate_type = certificate_type
        self.birthday = birthday
        self.phone_no = phone_no
        self.group_name = group_name
        self.user_group_id = user_group_id
        self.identifying_image = identifying_image
        self.user_name = user_name
        self.certificate_no = certificate_no
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.identifying_image is not None:
            result['IdentifyingImage'] = self.identifying_image
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.certificate_no is not None:
            result['CertificateNo'] = self.certificate_no
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('IdentifyingImage') is not None:
            self.identifying_image = m.get('IdentifyingImage')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('CertificateNo') is not None:
            self.certificate_no = m.get('CertificateNo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeUserInfoListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        user_info_list: List[DescribeUserInfoListResponseBodyUserInfoList] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.user_info_list = user_info_list

    def validate(self):
        if self.user_info_list:
            for k in self.user_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserInfoList'] = []
        if self.user_info_list is not None:
            for k in self.user_info_list:
                result['UserInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_info_list = []
        if m.get('UserInfoList') is not None:
            for k in m.get('UserInfoList'):
                temp_model = DescribeUserInfoListResponseBodyUserInfoList()
                self.user_info_list.append(temp_model.from_map(k))
        return self


class DescribeUserInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserInfoListResponseBody = None,
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
            temp_model = DescribeUserInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountProjectRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class GetAccountProjectResponseBodyList(TeaModel):
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
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetAccountProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        list: List[GetAccountProjectResponseBodyList] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.list = list
        self.success = success

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetAccountProjectResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAccountProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccountProjectResponseBody = None,
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
            temp_model = GetAccountProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveMnsServeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
        topic_name: str = None,
        end_point: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id
        self.topic_name = topic_name
        self.end_point = end_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        return self


class SaveMnsServeResponseBody(TeaModel):
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


class SaveMnsServeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveMnsServeResponseBody = None,
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
            temp_model = SaveMnsServeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveOssServeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class SaveOssServeResponseBody(TeaModel):
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


class SaveOssServeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveOssServeResponseBody = None,
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
            temp_model = SaveOssServeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        group_name: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.group_name = group_name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class SaveUserGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        id: int = None,
    ):
        self.gmt_create = gmt_create
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SaveUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        data: SaveUserGroupResponseBodyData = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = SaveUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveUserGroupResponseBody = None,
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
            temp_model = SaveUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveUserInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        user_group_id: int = None,
        birthday: int = None,
        image_base_64: str = None,
        group_name: str = None,
        image_url: str = None,
        sex: int = None,
        user_name: str = None,
        certificate_no: str = None,
        phone_no: str = None,
        certificate_type: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.user_group_id = user_group_id
        self.birthday = birthday
        self.image_base_64 = image_base_64
        self.group_name = group_name
        self.image_url = image_url
        self.sex = sex
        self.user_name = user_name
        self.certificate_no = certificate_no
        self.phone_no = phone_no
        self.certificate_type = certificate_type
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.image_base_64 is not None:
            result['ImageBase64'] = self.image_base_64
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.certificate_no is not None:
            result['CertificateNo'] = self.certificate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('ImageBase64') is not None:
            self.image_base_64 = m.get('ImageBase64')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('CertificateNo') is not None:
            self.certificate_no = m.get('CertificateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class SaveUserInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        id: int = None,
    ):
        self.gmt_create = gmt_create
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SaveUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        data: SaveUserInfoResponseBodyData = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = SaveUserInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveUserInfoResponseBody = None,
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
            temp_model = SaveUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDeviceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        iot_id: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.iot_id = iot_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UnbindDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindDeviceResponseBody = None,
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
            temp_model = UnbindDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceControlInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
        iot_id: int = None,
        multi_person: int = None,
        control_door_time: int = None,
        enable_measure_tempurature: int = None,
        speed_clock: int = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id
        self.iot_id = iot_id
        self.multi_person = multi_person
        self.control_door_time = control_door_time
        self.enable_measure_tempurature = enable_measure_tempurature
        self.speed_clock = speed_clock

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.multi_person is not None:
            result['MultiPerson'] = self.multi_person
        if self.control_door_time is not None:
            result['ControlDoorTime'] = self.control_door_time
        if self.enable_measure_tempurature is not None:
            result['EnableMeasureTempurature'] = self.enable_measure_tempurature
        if self.speed_clock is not None:
            result['SpeedClock'] = self.speed_clock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('MultiPerson') is not None:
            self.multi_person = m.get('MultiPerson')
        if m.get('ControlDoorTime') is not None:
            self.control_door_time = m.get('ControlDoorTime')
        if m.get('EnableMeasureTempurature') is not None:
            self.enable_measure_tempurature = m.get('EnableMeasureTempurature')
        if m.get('SpeedClock') is not None:
            self.speed_clock = m.get('SpeedClock')
        return self


class UpdateDeviceControlInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDeviceControlInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceControlInfoResponseBody = None,
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
            temp_model = UpdateDeviceControlInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceNameRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        iot_id: str = None,
        project_id: str = None,
        device_name: str = None,
    ):
        self.source_ip = source_ip
        self.iot_id = iot_id
        self.project_id = project_id
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        return self


class UpdateDeviceNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDeviceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceNameResponseBody = None,
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
            temp_model = UpdateDeviceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectNameRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.source_ip = source_ip
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateProjectNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateProjectNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectNameResponseBody = None,
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
            temp_model = UpdateProjectNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        group_id: int = None,
        group_name: str = None,
        project_id: str = None,
    ):
        self.source_ip = source_ip
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserGroupResponseBody = None,
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
            temp_model = UpdateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        user_group_id: int = None,
        birthday: int = None,
        image_base_64: str = None,
        group_name: str = None,
        image_url: str = None,
        sex: int = None,
        user_name: str = None,
        user_id: int = None,
        certificate_no: str = None,
        phone_no: str = None,
        certificate_type: str = None,
        project_id: str = None,
        overwrite_img: bool = None,
    ):
        self.source_ip = source_ip
        self.user_group_id = user_group_id
        self.birthday = birthday
        self.image_base_64 = image_base_64
        self.group_name = group_name
        self.image_url = image_url
        self.sex = sex
        self.user_name = user_name
        self.user_id = user_id
        self.certificate_no = certificate_no
        self.phone_no = phone_no
        self.certificate_type = certificate_type
        self.project_id = project_id
        self.overwrite_img = overwrite_img

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.image_base_64 is not None:
            result['ImageBase64'] = self.image_base_64
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.certificate_no is not None:
            result['CertificateNo'] = self.certificate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.overwrite_img is not None:
            result['OverwriteImg'] = self.overwrite_img
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('ImageBase64') is not None:
            self.image_base_64 = m.get('ImageBase64')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CertificateNo') is not None:
            self.certificate_no = m.get('CertificateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('OverwriteImg') is not None:
            self.overwrite_img = m.get('OverwriteImg')
        return self


class UpdateUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserInfoResponseBody = None,
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
            temp_model = UpdateUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadIdentifyRecordRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        user_id: int = None,
        user_name: str = None,
        project_id: str = None,
        iot_id: str = None,
        identifying_image_base_64: str = None,
        identifying_time: int = None,
        identifying_image_url: str = None,
        device_name: str = None,
    ):
        self.source_ip = source_ip
        self.user_id = user_id
        self.user_name = user_name
        self.project_id = project_id
        self.iot_id = iot_id
        self.identifying_image_base_64 = identifying_image_base_64
        self.identifying_time = identifying_time
        self.identifying_image_url = identifying_image_url
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.identifying_image_base_64 is not None:
            result['IdentifyingImageBase64'] = self.identifying_image_base_64
        if self.identifying_time is not None:
            result['IdentifyingTime'] = self.identifying_time
        if self.identifying_image_url is not None:
            result['IdentifyingImageUrl'] = self.identifying_image_url
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IdentifyingImageBase64') is not None:
            self.identifying_image_base_64 = m.get('IdentifyingImageBase64')
        if m.get('IdentifyingTime') is not None:
            self.identifying_time = m.get('IdentifyingTime')
        if m.get('IdentifyingImageUrl') is not None:
            self.identifying_image_url = m.get('IdentifyingImageUrl')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        return self


class UploadIdentifyRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadIdentifyRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadIdentifyRecordResponseBody = None,
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
            temp_model = UploadIdentifyRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyAccountProjectRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class VerifyAccountProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyAccountProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyAccountProjectResponseBody = None,
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
            temp_model = VerifyAccountProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


