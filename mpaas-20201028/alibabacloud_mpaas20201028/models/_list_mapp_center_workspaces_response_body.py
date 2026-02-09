# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMappCenterWorkspacesResponseBody(DaraModel):
    def __init__(
        self,
        list_mapp_center_workspace_result: main_models.ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mapp_center_workspace_result = list_mapp_center_workspace_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mapp_center_workspace_result:
            self.list_mapp_center_workspace_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_mapp_center_workspace_result is not None:
            result['ListMappCenterWorkspaceResult'] = self.list_mapp_center_workspace_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMappCenterWorkspaceResult') is not None:
            temp_model = main_models.ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResult()
            self.list_mapp_center_workspace_result = temp_model.from_map(m.get('ListMappCenterWorkspaceResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResult(DaraModel):
    def __init__(
        self,
        mapp_center_workspace_list: List[main_models.ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResultMappCenterWorkspaceList] = None,
        result_msg: str = None,
        success: bool = None,
        user_id: str = None,
    ):
        self.mapp_center_workspace_list = mapp_center_workspace_list
        self.result_msg = result_msg
        self.success = success
        self.user_id = user_id

    def validate(self):
        if self.mapp_center_workspace_list:
            for v1 in self.mapp_center_workspace_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MappCenterWorkspaceList'] = []
        if self.mapp_center_workspace_list is not None:
            for k1 in self.mapp_center_workspace_list:
                result['MappCenterWorkspaceList'].append(k1.to_map() if k1 else None)

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mapp_center_workspace_list = []
        if m.get('MappCenterWorkspaceList') is not None:
            for k1 in m.get('MappCenterWorkspaceList'):
                temp_model = main_models.ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResultMappCenterWorkspaceList()
                self.mapp_center_workspace_list.append(temp_model.from_map(k1))

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResultMappCenterWorkspaceList(DaraModel):
    def __init__(
        self,
        compatible_id: str = None,
        create_time: str = None,
        display_name: str = None,
        id: str = None,
        region: str = None,
        status: str = None,
        tenant_id: str = None,
        type: str = None,
        uid: int = None,
        update_time: str = None,
        workspace_id: str = None,
        zones: str = None,
    ):
        self.compatible_id = compatible_id
        self.create_time = create_time
        self.display_name = display_name
        self.id = id
        self.region = region
        self.status = status
        self.tenant_id = tenant_id
        self.type = type
        self.uid = uid
        self.update_time = update_time
        self.workspace_id = workspace_id
        self.zones = zones

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compatible_id is not None:
            result['CompatibleId'] = self.compatible_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.region is not None:
            result['Region'] = self.region

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.zones is not None:
            result['Zones'] = self.zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompatibleId') is not None:
            self.compatible_id = m.get('CompatibleId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('Zones') is not None:
            self.zones = m.get('Zones')

        return self

