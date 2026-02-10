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
        # Application query condition.
        self.app_criteria = app_criteria
        # Instance type. Values:
        # - **SERVERLESS**: Serverless asset
        self.auth_item = auth_item
        # Enable auto-binding. Values:
        # 
        # - **0**: Off
        # - **1**: On
        self.auto_bind = auto_bind
        # Whether to bind all. Default is **false**. Values:
        # 
        # - **true**: Yes
        # - **false**: No
        self.bind_all = bind_all
        # List of application IDs to be bound.
        # 
        # > Obtained through the [ListMachineApps](~~ListMachineApps~~) interface.
        self.bind_app_list = bind_app_list
        # Type of asset to operate on. Values:
        # - **INSTANCE**: Instance
        # - **APP**: Application
        self.bind_asset_type = bind_asset_type
        # List of asset UUIDs to be bound.
        self.bind_uuid_list = bind_uuid_list
        # Set the conditions for searching assets. This parameter is in JSON format, and case sensitivity should be noted when entering parameters.
        # > Supports searching assets using instance ID, instance name, VPC ID, region, public IP address, etc. You can call the [DescribeCriteria](~~DescribeCriteria~~) interface to query supported search conditions.
        self.criteria = criteria
        # Set the logical relationship between multiple search conditions. Values:
        # - **OR**: Indicates an **or** relationship between multiple conditions.
        # - **AND**: Indicates an **and** relationship between multiple conditions.
        self.logical_exp = logical_exp
        # NTM version code, used for pre-binding.
        self.ntm_version = ntm_version
        # Whether it is a pre-bind operation. Values:
        # 
        # - **0**: No
        # - **1**: Yes
        # 
        # 
        # > After enabling pre-binding, the specified server will automatically bind the corresponding version\\"s authorization count after the purchase is completed.
        self.pre_bind = pre_bind
        # Pre-bind order ID.
        self.pre_bind_order_id = pre_bind_order_id
        # UID of the associated resource directory.
        self.resource_directory_uid = resource_directory_uid
        # List of application IDs to be unbound.
        # 
        # > Obtained through the [ListMachineApps](~~ListMachineApps~~) interface.
        self.un_bind_app_list = un_bind_app_list
        # List of asset UUIDs to be unbound.
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

