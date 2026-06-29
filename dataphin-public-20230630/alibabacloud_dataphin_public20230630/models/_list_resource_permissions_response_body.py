# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListResourcePermissionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListResourcePermissionsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code. OK indicates a normal request.
        self.code = code
        # HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Paginated query result.
        self.page_result = page_result
        # Request ID.
        self.request_id = request_id
        # Whether the request is successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListResourcePermissionsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListResourcePermissionsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListResourcePermissionsResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        # Paginated list.
        self.data = data
        # Total number of records.
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListResourcePermissionsResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourcePermissionsResponseBodyPageResultData(DaraModel):
    def __init__(
        self,
        auth_scope: str = None,
        period: main_models.ListResourcePermissionsResponseBodyPageResultDataPeriod = None,
        permission_period_list: List[main_models.ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodList] = None,
        record_id: str = None,
        resource_info: main_models.ListResourcePermissionsResponseBodyPageResultDataResourceInfo = None,
        target_account: main_models.ListResourcePermissionsResponseBodyPageResultDataTargetAccount = None,
    ):
        # Authorization scope of the table. Specified table: selectTable. All tables in the project: projectAllTable. All logical tables in the business unit: bizUnitAllLogicTable.
        self.auth_scope = auth_scope
        # Validity period settings.
        self.period = period
        # List of validity periods for different permission types.
        self.permission_period_list = permission_period_list
        # Record ID.
        self.record_id = record_id
        # Permission resource.
        self.resource_info = resource_info
        # Authorized object.
        self.target_account = target_account

    def validate(self):
        if self.period:
            self.period.validate()
        if self.permission_period_list:
            for v1 in self.permission_period_list:
                 if v1:
                    v1.validate()
        if self.resource_info:
            self.resource_info.validate()
        if self.target_account:
            self.target_account.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_scope is not None:
            result['AuthScope'] = self.auth_scope

        if self.period is not None:
            result['Period'] = self.period.to_map()

        result['PermissionPeriodList'] = []
        if self.permission_period_list is not None:
            for k1 in self.permission_period_list:
                result['PermissionPeriodList'].append(k1.to_map() if k1 else None)

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info.to_map()

        if self.target_account is not None:
            result['TargetAccount'] = self.target_account.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthScope') is not None:
            self.auth_scope = m.get('AuthScope')

        if m.get('Period') is not None:
            temp_model = main_models.ListResourcePermissionsResponseBodyPageResultDataPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        self.permission_period_list = []
        if m.get('PermissionPeriodList') is not None:
            for k1 in m.get('PermissionPeriodList'):
                temp_model = main_models.ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodList()
                self.permission_period_list.append(temp_model.from_map(k1))

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('ResourceInfo') is not None:
            temp_model = main_models.ListResourcePermissionsResponseBodyPageResultDataResourceInfo()
            self.resource_info = temp_model.from_map(m.get('ResourceInfo'))

        if m.get('TargetAccount') is not None:
            temp_model = main_models.ListResourcePermissionsResponseBodyPageResultDataTargetAccount()
            self.target_account = temp_model.from_map(m.get('TargetAccount'))

        return self

class ListResourcePermissionsResponseBodyPageResultDataTargetAccount(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        # Personal account: the userId on the Dataphin side. Production account: the UserId obtained by calling the GetProjectProduceUser operation. User group: the user group ID obtained by calling the ListUserGroup operation.
        self.id = id
        # Personal account: the userId on the Dataphin side. Production account: the UserId obtained by calling the GetProjectProduceUser operation. User group: the user group ID obtained by calling the ListUserGroup operation.
        self.name = name
        # Authorization account type. Valid values: PERSONAL (personal account), PRODUCE (production account), and USER_GROUP (user group).
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListResourcePermissionsResponseBodyPageResultDataResourceInfo(DaraModel):
    def __init__(
        self,
        biz_unit_info: main_models.ListResourcePermissionsResponseBodyPageResultDataResourceInfoBizUnitInfo = None,
        display_name: str = None,
        env: str = None,
        id: str = None,
        name: str = None,
        project_info: main_models.ListResourcePermissionsResponseBodyPageResultDataResourceInfoProjectInfo = None,
        type: str = None,
    ):
        # Business unit.
        self.biz_unit_info = biz_unit_info
        # Resource display name.
        self.display_name = display_name
        # Resource environment type. Development: DEV. Production: PROD.
        self.env = env
        # Permission resource ID.
        self.id = id
        # Permission resource name.
        self.name = name
        # Project.
        self.project_info = project_info
        # Resource type. Valid values: PHYSICAL_TABLE, PHYSICAL_VIEW, LOGICAL_TABLE, LOGICAL_VIEW, REALTIME_LOGICAL_TABLE, REALTIME_MIRROR_TABLE, and DATASOURCE.
        self.type = type

    def validate(self):
        if self.biz_unit_info:
            self.biz_unit_info.validate()
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_info is not None:
            result['BizUnitInfo'] = self.biz_unit_info.to_map()

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitInfo') is not None:
            temp_model = main_models.ListResourcePermissionsResponseBodyPageResultDataResourceInfoBizUnitInfo()
            self.biz_unit_info = temp_model.from_map(m.get('BizUnitInfo'))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectInfo') is not None:
            temp_model = main_models.ListResourcePermissionsResponseBodyPageResultDataResourceInfoProjectInfo()
            self.project_info = temp_model.from_map(m.get('ProjectInfo'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListResourcePermissionsResponseBodyPageResultDataResourceInfoProjectInfo(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        env: str = None,
        id: int = None,
        name: str = None,
    ):
        # Display name.
        self.display_name = display_name
        # Environment identifier. Development: DEV. Production: PROD.
        self.env = env
        # Project ID.
        self.id = id
        # Name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListResourcePermissionsResponseBodyPageResultDataResourceInfoBizUnitInfo(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        env: str = None,
        id: str = None,
        name: str = None,
    ):
        # Display name.
        self.display_name = display_name
        # Environment identifier. Development: DEV. Production: PROD.
        self.env = env
        # ID.
        self.id = id
        # Name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodList(DaraModel):
    def __init__(
        self,
        period: main_models.ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodListPeriod = None,
        permission_type: str = None,
    ):
        # Validity period settings.
        self.period = period
        # Permission type.
        self.permission_type = permission_type

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period is not None:
            result['Period'] = self.period.to_map()

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            temp_model = main_models.ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodListPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        return self

class ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodListPeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        type: str = None,
    ):
        # Expiration time.
        self.end_time = end_time
        # Validity period type. Custom: CUSTOM. Long-term: LONG_TERM.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListResourcePermissionsResponseBodyPageResultDataPeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        type: str = None,
    ):
        # Expiration time.
        self.end_time = end_time
        # Validity period type. Custom: CUSTOM. Long-term: LONG_TERM.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

