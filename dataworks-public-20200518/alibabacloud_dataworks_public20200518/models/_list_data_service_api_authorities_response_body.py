# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceApiAuthoritiesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataServiceApiAuthoritiesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The APIs on which other users are granted the access permissions.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDataServiceApiAuthoritiesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataServiceApiAuthoritiesResponseBodyData(DaraModel):
    def __init__(
        self,
        api_authorization_list: List[main_models.ListDataServiceApiAuthoritiesResponseBodyDataApiAuthorizationList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The APIs on which other users are granted the access permissions.
        self.api_authorization_list = api_authorization_list
        # The page number. The value of this parameter is the same as that of the PageNumber parameter in the request.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.api_authorization_list:
            for v1 in self.api_authorization_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiAuthorizationList'] = []
        if self.api_authorization_list is not None:
            for k1 in self.api_authorization_list:
                result['ApiAuthorizationList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_authorization_list = []
        if m.get('ApiAuthorizationList') is not None:
            for k1 in m.get('ApiAuthorizationList'):
                temp_model = main_models.ListDataServiceApiAuthoritiesResponseBodyDataApiAuthorizationList()
                self.api_authorization_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServiceApiAuthoritiesResponseBodyDataApiAuthorizationList(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        api_path: str = None,
        api_status: int = None,
        authorization_records: List[main_models.ListDataServiceApiAuthoritiesResponseBodyDataApiAuthorizationListAuthorizationRecords] = None,
        created_time: str = None,
        creator_id: str = None,
        group_id: str = None,
        modified_time: str = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The API ID.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # The path of the API.
        self.api_path = api_path
        # The status of the API. Valid values: 0 and 1. The value 0 indicates that the API is not published. The value 1 indicates that the API is published.
        self.api_status = api_status
        # The authorization records.
        self.authorization_records = authorization_records
        # The time when the API was created.
        self.created_time = created_time
        # The ID of the Alibaba Cloud account used by the API owner.
        self.creator_id = creator_id
        # The group ID.
        self.group_id = group_id
        # The time when the API was last modified.
        self.modified_time = modified_time
        # The workspace ID.
        self.project_id = project_id
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        if self.authorization_records:
            for v1 in self.authorization_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_path is not None:
            result['ApiPath'] = self.api_path

        if self.api_status is not None:
            result['ApiStatus'] = self.api_status

        result['AuthorizationRecords'] = []
        if self.authorization_records is not None:
            for k1 in self.authorization_records:
                result['AuthorizationRecords'].append(k1.to_map() if k1 else None)

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiPath') is not None:
            self.api_path = m.get('ApiPath')

        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')

        self.authorization_records = []
        if m.get('AuthorizationRecords') is not None:
            for k1 in m.get('AuthorizationRecords'):
                temp_model = main_models.ListDataServiceApiAuthoritiesResponseBodyDataApiAuthorizationListAuthorizationRecords()
                self.authorization_records.append(temp_model.from_map(k1))

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class ListDataServiceApiAuthoritiesResponseBodyDataApiAuthorizationListAuthorizationRecords(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        creator_id: str = None,
        end_time: str = None,
        project_id: int = None,
    ):
        # The time when the access permissions on the API were granted to other users.
        self.created_time = created_time
        # The ID of the Alibaba Cloud account used by the API owner.
        self.creator_id = creator_id
        # The end time of the validity period of the authorization.
        self.end_time = end_time
        # The ID of the workspace to which the access permissions on the API are granted.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

