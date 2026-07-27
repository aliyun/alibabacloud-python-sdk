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
        # The list of objects for which permissions are requested.
        # 
        # This parameter is required.
        self.apply_object = apply_object
        # The reason for the request. This is used by the administrator for evaluation and approval.
        # 
        # This parameter is required.
        self.apply_reason = apply_reason
        # The type of the request order. Valid values:
        # 
        # - MaxComputeTable: MaxCompute table permission request order.
        # - MaxComputeFunction: MaxCompute function permission request order.
        # - MaxComputeResource: MaxCompute resource permission request order.
        # - DLFSchema: Data Lake Formation (DLF) 1.0 schema permission request order.
        # - DLFTable: DLF 1.0 table permission request order.
        # - DLFColumn: DLF 1.0 column permission request order.
        # - DsApiDeploy: Data service publication permission request order.
        self.apply_type = apply_type
        # The UIDs of the Alibaba Cloud accounts for which permissions are requested. Separate multiple account UIDs with commas (,).
        # 
        # This parameter is required.
        self.apply_user_ids = apply_user_ids
        # The name of the data catalog to query. Go to the [Data Lake Formation console](https://dlf.console.aliyun.com/ap-southeast-1/metadata/catalog?spm=a2c4g.11186623.0.0.5a225658pT4Dkr) to view the data catalog name.
        self.catalog_name = catalog_name
        # The expiration time of the requested permissions. Specify a UNIX timestamp. If you do not specify this parameter, the default expiration time is January 1, 2065.
        # If LabelSecurity is not enabled for the MaxCompute project, or the security level of the requested table field is 0 or less than or equal to the security level of the requesting account, you can request only permanent permissions.
        # Go to the management page of the DataWorks workspace and check the advanced configuration page of the MaxCompute engine to verify whether column-level access control is enabled.
        # Go to the DataWorks workspace to view the security level of fields in Data Map and the security level of accounts on the Member Management page.
        self.deadline = deadline
        # This field is deprecated. Set it to empty.
        self.engine_type = engine_type
        # The name of the MaxCompute project for which permissions are requested.
        self.max_compute_project_name = max_compute_project_name
        # This field is deprecated. Set it to empty.
        self.order_type = order_type
        # The ID of the DataWorks workspace to which the MaxCompute project belongs. Go to the DataWorks workspace configuration page to obtain the workspace ID.
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
        # The permission types to request. Separate multiple permission types with commas (,). Only Select, Describe, Drop, Alter, Update, and Download types are supported.
        self.actions = actions
        # The list of column objects.
        self.column_meta_list = column_meta_list
        # The object for which permissions are requested. Only MaxCompute table permissions are supported. Enter the name of the target table.
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
        # The permission types to request. Separate multiple permission types with commas (,). Only Select, Describe, and Download types are supported.
        self.actions = actions
        # The name of the column for which permissions are requested. To request permissions on the entire table, enter all column names of the table.
        # You can request permissions on specific columns only if LabelSecurity is enabled for the MaxCompute project. If LabelSecurity is not enabled, you can request permissions only on the entire table.
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

