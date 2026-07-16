# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyServerlessAuthToMachineRequest(DaraModel):
    def __init__(
        self,
        app_criteria: str = None,
        auth_item: str = None,
        auto_bind: int = None,
        bind_all: bool = None,
        bind_app_list: List[str] = None,
        bind_asset_type: str = None,
        bind_uuid_list: List[str] = None,
        criteria: str = None,
        logical_exp: str = None,
        ntm_version: str = None,
        pre_bind: int = None,
        pre_bind_order_id: int = None,
        resource_directory_uid: int = None,
        un_bind_app_list: List[str] = None,
        un_bind_uuid_list: List[str] = None,
    ):
        # The application query conditions.
        self.app_criteria = app_criteria
        # The instance type. Valid values:
        # - **SERVERLESS**: Serverless asset.
        self.auth_item = auth_item
        # Specifies whether to enable automatic binding. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.auto_bind = auto_bind
        # Specifies whether to bind all assets. Default value: **false**. Valid values:
        # 
        # - **true**: Bind all assets.
        # - **false**: Do not bind all assets.
        self.bind_all = bind_all
        # The list of application IDs to bind.
        # 
        # > Retrieve the IDs by calling the [ListMachineApps](~~ListMachineApps~~) operation.
        self.bind_app_list = bind_app_list
        # The Asset Type for the operation. Valid values:
        # - **INSTANCE**: instance.
        # - **APP**: application.
        self.bind_asset_type = bind_asset_type
        # The list of asset UUIDs to bind.
        self.bind_uuid_list = bind_uuid_list
        # The search conditions for assets. This parameter is in JSON format. Pay attention to letter case when specifying this parameter.
        # > You can search for assets by instance ID, instance name, VPC ID, region, public IP address, and other conditions. Call the [DescribeCriteria](~~DescribeCriteria~~) operation to query supported search conditions.
        self.criteria = criteria
        # The logical relationship among multiple search conditions. Valid values:
        # - **OR**: The search conditions are evaluated with a logical OR.
        # - **AND**: The search conditions are evaluated with a logical AND.
        self.logical_exp = logical_exp
        # The NTM version code for pre-binding.
        self.ntm_version = ntm_version
        # Specifies whether to perform a pre-binding operation. Valid values:
        # 
        # - **0**: No.
        # - **1**: Yes.
        # 
        # 
        # > After pre-binding is enabled, the corresponding edition authorization quota is automatically bound to the specified servers after the purchase is completed.
        self.pre_bind = pre_bind
        # The pre-binding order ID.
        self.pre_bind_order_id = pre_bind_order_id
        # The UID of the resource directory.
        self.resource_directory_uid = resource_directory_uid
        # The list of application IDs to unbind.
        # 
        # > Retrieve the IDs by calling the [ListMachineApps](~~ListMachineApps~~) operation.
        self.un_bind_app_list = un_bind_app_list
        # The list of asset UUIDs to unbind.
        self.un_bind_uuid_list = un_bind_uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_criteria is not None:
            result['AppCriteria'] = self.app_criteria

        if self.auth_item is not None:
            result['AuthItem'] = self.auth_item

        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        if self.bind_all is not None:
            result['BindAll'] = self.bind_all

        if self.bind_app_list is not None:
            result['BindAppList'] = self.bind_app_list

        if self.bind_asset_type is not None:
            result['BindAssetType'] = self.bind_asset_type

        if self.bind_uuid_list is not None:
            result['BindUuidList'] = self.bind_uuid_list

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.ntm_version is not None:
            result['NtmVersion'] = self.ntm_version

        if self.pre_bind is not None:
            result['PreBind'] = self.pre_bind

        if self.pre_bind_order_id is not None:
            result['PreBindOrderId'] = self.pre_bind_order_id

        if self.resource_directory_uid is not None:
            result['ResourceDirectoryUid'] = self.resource_directory_uid

        if self.un_bind_app_list is not None:
            result['UnBindAppList'] = self.un_bind_app_list

        if self.un_bind_uuid_list is not None:
            result['UnBindUuidList'] = self.un_bind_uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCriteria') is not None:
            self.app_criteria = m.get('AppCriteria')

        if m.get('AuthItem') is not None:
            self.auth_item = m.get('AuthItem')

        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        if m.get('BindAll') is not None:
            self.bind_all = m.get('BindAll')

        if m.get('BindAppList') is not None:
            self.bind_app_list = m.get('BindAppList')

        if m.get('BindAssetType') is not None:
            self.bind_asset_type = m.get('BindAssetType')

        if m.get('BindUuidList') is not None:
            self.bind_uuid_list = m.get('BindUuidList')

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('NtmVersion') is not None:
            self.ntm_version = m.get('NtmVersion')

        if m.get('PreBind') is not None:
            self.pre_bind = m.get('PreBind')

        if m.get('PreBindOrderId') is not None:
            self.pre_bind_order_id = m.get('PreBindOrderId')

        if m.get('ResourceDirectoryUid') is not None:
            self.resource_directory_uid = m.get('ResourceDirectoryUid')

        if m.get('UnBindAppList') is not None:
            self.un_bind_app_list = m.get('UnBindAppList')

        if m.get('UnBindUuidList') is not None:
            self.un_bind_uuid_list = m.get('UnBindUuidList')

        return self

