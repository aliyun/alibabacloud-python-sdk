# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPublishedAppInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_name: str = None,
        exclude_user_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The application ID used for filtering delivery groups. Substring matching is supported. The delivery group must contain a deployed application that matches the condition. If this parameter is not specified or is set to an empty string, no filtering by application ID is applied. When specified together with `AppName`, the same application must satisfy both conditions.
        # 
        # This condition does not trim the returned `Apps` list.
        self.app_id = app_id
        # The delivery group ID used for filtering. Substring matching is supported. You can pass in a full ID or a consecutive segment of the ID. If this parameter is not specified or is set to an empty string, no filtering by ID is applied. This parameter can be used together with other filter conditions. Results must satisfy all conditions simultaneously.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name used for filtering. Substring matching is supported. For example, if you pass in `OfficeApps`, delivery groups whose names contain this text are matched. If this parameter is not specified or is set to an empty string, no filtering by name is applied. When specified together with the delivery group ID, both the ID and name must match.
        self.app_instance_group_name = app_instance_group_name
        # The application name used for filtering delivery groups. Substring matching is supported. The delivery group must contain a deployed application whose name includes the specified text. If this parameter is not specified or is set to an empty string, no filtering by application name is applied. When specified together with `AppId`, the same application must satisfy both conditions.
        # 
        # This condition does not trim the returned `Apps` list.
        self.app_name = app_name
        # The username to exclude based on existing authorization. Exact username matching is used, for example, `alice`. When specified, delivery groups in which all applications have been directly authorized to this user are excluded. If this parameter is not specified or is set to an empty string, no exclusion based on user authorization is applied.
        # 
        # **Authorization granted for individual applications only, or access permissions obtained through user groups, is not fully evaluated by this condition.** Do not treat the returned results as a complete list of delivery groups that the user has no access permissions to.
        self.exclude_user_id = exclude_user_id
        # The page number. This parameter is required. Start from page `1` and use this parameter together with `PageSize`. Keep other filter conditions unchanged when querying subsequent pages.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The maximum number of delivery groups to return per page. This parameter is required. Valid values: `1` to `100`. Unit: delivery groups. Specify this value explicitly and do not rely on default values from other query operations.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. This parameter is required. The value must match the product type of the delivery groups you want to query. Only published delivery groups of the specified product type are returned. A parameter error is returned if an unrecognized value is passed in.
        # 
        # Valid values:
        # 
        # - `CloudApp`: WUYING Cloud Application.
        # - `CloudBrowser`: Cloud Browser.
        # - `WuyingServer`: Enterprise Workstation.
        # - `WuyingWorkstation`: Personal Edition Lingjou Container Workstation.
        # - `WuyingWorkstationTeam`: Team Edition Lingjou Container Workstation.
        # - `WuyingWorkstationBusiness`: Dedicated Edition Lingjou Container Workstation.
        # - `AndroidCloud`: Cloud Phone.
        # - `AIAgent`: AgentBay (AI agent).
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.exclude_user_id is not None:
            result['ExcludeUserId'] = self.exclude_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ExcludeUserId') is not None:
            self.exclude_user_id = m.get('ExcludeUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

