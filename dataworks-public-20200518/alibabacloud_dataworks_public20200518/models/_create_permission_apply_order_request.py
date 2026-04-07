# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class CreatePermissionApplyOrderRequest(DaraModel):
    def __init__(
        self,
        apply_object: List[main_models.CreatePermissionApplyOrderRequestApplyObject] = None,
        apply_reason: str = None,
        apply_type: str = None,
        apply_user_ids: str = None,
        catalog_name: str = None,
        deadline: int = None,
        engine_type: str = None,
        max_compute_project_name: str = None,
        order_type: int = None,
        workspace_id: int = None,
    ):
        # The list of requested objects.
        # 
        # This parameter is required.
        self.apply_object = apply_object
        # The reason for your request. The administrator determines whether to approve the request based on the reason.
        # 
        # This parameter is required.
        self.apply_reason = apply_reason
        self.apply_type = apply_type
        # The ID of the Alibaba Cloud account for which you want to request permissions. If you want to request permissions for multiple Alibaba Cloud accounts, separate the IDs of the accounts with commas (,).
        # 
        # This parameter is required.
        self.apply_user_ids = apply_user_ids
        self.catalog_name = catalog_name
        # The expiration time of the permissions that you request. This value is a UNIX timestamp. The default value is January 1, 2065. If LabelSecurity is disabled for the MaxCompute project in which you want to request permissions on the fields of a table, or the security level of the fields is 0 or is lower than or equal to the security level of the Alibaba Cloud account for which you want to request permissions, you can request only permanent permissions. You can go to the Workspace Management page in the DataWorks console, click MaxCompute Management in the left-side navigation pane, and then check whether column-level access control is enabled. You can go to your DataWorks workspace, view the security level of the fields in Data Map, and then view the security level of the Alibaba Cloud account on the User Management page.
        self.deadline = deadline
        # The type of compute engine for permission requests. Currently only supports ODPS, which means only MaxCompute compute engine permissions are supported.
        self.engine_type = engine_type
        # The name of the MaxCompute project you request access to.
        self.max_compute_project_name = max_compute_project_name
        # The request type. The only supported value is 1, which represents an object ACL permission request.
        self.order_type = order_type
        # The DataWorks workspace ID to which the MaxCompute project belongs for permission requests. You can check the workspace ID on the DataWorks workspace configuration page.
        self.workspace_id = workspace_id

    def validate(self):
        if self.apply_object:
            for v1 in self.apply_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplyObject'] = []
        if self.apply_object is not None:
            for k1 in self.apply_object:
                result['ApplyObject'].append(k1.to_map() if k1 else None)

        if self.apply_reason is not None:
            result['ApplyReason'] = self.apply_reason

        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type

        if self.apply_user_ids is not None:
            result['ApplyUserIds'] = self.apply_user_ids

        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.deadline is not None:
            result['Deadline'] = self.deadline

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.max_compute_project_name is not None:
            result['MaxComputeProjectName'] = self.max_compute_project_name

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_object = []
        if m.get('ApplyObject') is not None:
            for k1 in m.get('ApplyObject'):
                temp_model = main_models.CreatePermissionApplyOrderRequestApplyObject()
                self.apply_object.append(temp_model.from_map(k1))

        if m.get('ApplyReason') is not None:
            self.apply_reason = m.get('ApplyReason')

        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')

        if m.get('ApplyUserIds') is not None:
            self.apply_user_ids = m.get('ApplyUserIds')

        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('MaxComputeProjectName') is not None:
            self.max_compute_project_name = m.get('MaxComputeProjectName')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreatePermissionApplyOrderRequestApplyObject(DaraModel):
    def __init__(
        self,
        actions: str = None,
        column_meta_list: List[main_models.CreatePermissionApplyOrderRequestApplyObjectColumnMetaList] = None,
        name: str = None,
    ):
        # The type of permissions requested. Use commas (,) to separate multiple permission types in a single request. Currently only supports Select, Describe, Drop, Alter, Update, and Download permission types.
        self.actions = actions
        # The list of column objects.
        self.column_meta_list = column_meta_list
        # The object you request access to. Currently, only permission requests for MaxCompute tables are supported. The name of the target table needs to be entered here.
        self.name = name

    def validate(self):
        if self.column_meta_list:
            for v1 in self.column_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['Actions'] = self.actions

        result['ColumnMetaList'] = []
        if self.column_meta_list is not None:
            for k1 in self.column_meta_list:
                result['ColumnMetaList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')

        self.column_meta_list = []
        if m.get('ColumnMetaList') is not None:
            for k1 in m.get('ColumnMetaList'):
                temp_model = main_models.CreatePermissionApplyOrderRequestApplyObjectColumnMetaList()
                self.column_meta_list.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreatePermissionApplyOrderRequestApplyObjectColumnMetaList(DaraModel):
    def __init__(
        self,
        actions: str = None,
        name: str = None,
    ):
        self.actions = actions
        # Permissions for the target columns. Enter the column names here. If applying for permissions on the entire table, enter all column names of the table. Permissions for specific columns can only be requested if labelSecurity is enabled for the MaxCompute project. Otherwise, you can only apply for permissions on the entire table.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['Actions'] = self.actions

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

