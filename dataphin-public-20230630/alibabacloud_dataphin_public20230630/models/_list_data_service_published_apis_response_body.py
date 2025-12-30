# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataServicePublishedApisResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListDataServicePublishedApisResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
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
            temp_model = main_models.ListDataServicePublishedApisResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataServicePublishedApisResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        api_list: List[main_models.ListDataServicePublishedApisResponseBodyPageResultApiList] = None,
        total_count: int = None,
    ):
        self.api_list = api_list
        self.total_count = total_count

    def validate(self):
        if self.api_list:
            for v1 in self.api_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiList'] = []
        if self.api_list is not None:
            for k1 in self.api_list:
                result['ApiList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_list = []
        if m.get('ApiList') is not None:
            for k1 in m.get('ApiList'):
                temp_model = main_models.ListDataServicePublishedApisResponseBodyPageResultApiList()
                self.api_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServicePublishedApisResponseBodyPageResultApiList(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        app_count: int = None,
        app_info_list: List[main_models.ListDataServicePublishedApisResponseBodyPageResultApiListAppInfoList] = None,
        apply_status: int = None,
        call_count: int = None,
        create_type: int = None,
        custom_update_rate: str = None,
        deploy_time: str = None,
        description: str = None,
        execute_mode: int = None,
        group_id: int = None,
        group_name: str = None,
        logic_unit_no: int = None,
        mode: int = None,
        owner: str = None,
        owner_user_name: str = None,
        project_id: int = None,
        project_name: str = None,
        update_rate: int = None,
        update_time: str = None,
        version: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.app_count = app_count
        self.app_info_list = app_info_list
        self.apply_status = apply_status
        self.call_count = call_count
        self.create_type = create_type
        self.custom_update_rate = custom_update_rate
        self.deploy_time = deploy_time
        self.description = description
        self.execute_mode = execute_mode
        self.group_id = group_id
        self.group_name = group_name
        self.logic_unit_no = logic_unit_no
        self.mode = mode
        self.owner = owner
        self.owner_user_name = owner_user_name
        self.project_id = project_id
        self.project_name = project_name
        self.update_rate = update_rate
        self.update_time = update_time
        self.version = version

    def validate(self):
        if self.app_info_list:
            for v1 in self.app_info_list:
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

        if self.app_count is not None:
            result['AppCount'] = self.app_count

        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k1 in self.app_info_list:
                result['AppInfoList'].append(k1.to_map() if k1 else None)

        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status

        if self.call_count is not None:
            result['CallCount'] = self.call_count

        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.custom_update_rate is not None:
            result['CustomUpdateRate'] = self.custom_update_rate

        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time

        if self.description is not None:
            result['Description'] = self.description

        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.logic_unit_no is not None:
            result['LogicUnitNo'] = self.logic_unit_no

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_user_name is not None:
            result['OwnerUserName'] = self.owner_user_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.update_rate is not None:
            result['UpdateRate'] = self.update_rate

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')

        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k1 in m.get('AppInfoList'):
                temp_model = main_models.ListDataServicePublishedApisResponseBodyPageResultApiListAppInfoList()
                self.app_info_list.append(temp_model.from_map(k1))

        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')

        if m.get('CallCount') is not None:
            self.call_count = m.get('CallCount')

        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('CustomUpdateRate') is not None:
            self.custom_update_rate = m.get('CustomUpdateRate')

        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LogicUnitNo') is not None:
            self.logic_unit_no = m.get('LogicUnitNo')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerUserName') is not None:
            self.owner_user_name = m.get('OwnerUserName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UpdateRate') is not None:
            self.update_rate = m.get('UpdateRate')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListDataServicePublishedApisResponseBodyPageResultApiListAppInfoList(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_key: int = None,
        app_name: str = None,
    ):
        self.app_id = app_id
        # appKey
        self.app_key = app_key
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

