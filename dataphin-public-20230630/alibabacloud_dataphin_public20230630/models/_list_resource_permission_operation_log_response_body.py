# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListResourcePermissionOperationLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListResourcePermissionOperationLogResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
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
            temp_model = main_models.ListResourcePermissionOperationLogResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListResourcePermissionOperationLogResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListResourcePermissionOperationLogResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        self.data = data
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
                temp_model = main_models.ListResourcePermissionOperationLogResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourcePermissionOperationLogResponseBodyPageResultData(DaraModel):
    def __init__(
        self,
        account: main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataAccount = None,
        auth_scope: str = None,
        operate_id: int = None,
        operate_time: int = None,
        operate_type: str = None,
        period: main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataPeriod = None,
        reason: str = None,
        resource_info: main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfo = None,
        target_account: main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataTargetAccount = None,
    ):
        self.account = account
        self.auth_scope = auth_scope
        self.operate_id = operate_id
        self.operate_time = operate_time
        self.operate_type = operate_type
        self.period = period
        self.reason = reason
        self.resource_info = resource_info
        self.target_account = target_account

    def validate(self):
        if self.account:
            self.account.validate()
        if self.period:
            self.period.validate()
        if self.resource_info:
            self.resource_info.validate()
        if self.target_account:
            self.target_account.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account.to_map()

        if self.auth_scope is not None:
            result['AuthScope'] = self.auth_scope

        if self.operate_id is not None:
            result['OperateId'] = self.operate_id

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.period is not None:
            result['Period'] = self.period.to_map()

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info.to_map()

        if self.target_account is not None:
            result['TargetAccount'] = self.target_account.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataAccount()
            self.account = temp_model.from_map(m.get('Account'))

        if m.get('AuthScope') is not None:
            self.auth_scope = m.get('AuthScope')

        if m.get('OperateId') is not None:
            self.operate_id = m.get('OperateId')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Period') is not None:
            temp_model = main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ResourceInfo') is not None:
            temp_model = main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfo()
            self.resource_info = temp_model.from_map(m.get('ResourceInfo'))

        if m.get('TargetAccount') is not None:
            temp_model = main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataTargetAccount()
            self.target_account = temp_model.from_map(m.get('TargetAccount'))

        return self

class ListResourcePermissionOperationLogResponseBodyPageResultDataTargetAccount(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
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

class ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfo(DaraModel):
    def __init__(
        self,
        biz_unit_info: main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoBizUnitInfo = None,
        display_name: str = None,
        env: str = None,
        id: str = None,
        name: str = None,
        project_info: main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoProjectInfo = None,
        type: str = None,
    ):
        self.biz_unit_info = biz_unit_info
        self.display_name = display_name
        self.env = env
        self.id = id
        self.name = name
        self.project_info = project_info
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
            temp_model = main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoBizUnitInfo()
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
            temp_model = main_models.ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoProjectInfo()
            self.project_info = temp_model.from_map(m.get('ProjectInfo'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoProjectInfo(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        env: str = None,
        id: int = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.env = env
        self.id = id
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

class ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoBizUnitInfo(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        env: str = None,
        id: str = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.env = env
        # Id
        self.id = id
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

class ListResourcePermissionOperationLogResponseBodyPageResultDataPeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        type: str = None,
    ):
        self.end_time = end_time
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

class ListResourcePermissionOperationLogResponseBodyPageResultDataAccount(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
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

