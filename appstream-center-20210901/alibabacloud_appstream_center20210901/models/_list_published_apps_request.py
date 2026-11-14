# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPublishedAppsRequest(DaraModel):
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
        # The ID of the application used for filtering. Substring matching is supported. You can pass the complete ID or a continuous segment of it. If this parameter is not specified or an empty string is passed, filtering is not performed based on the application ID. If this parameter and `AppName` are specified at the same time, both conditions must be met by the same application.
        self.app_id = app_id
        # The ID of the delivery group used for filtering. Substring matching is supported. You can pass the complete ID or a continuous segment of it. If this parameter is not specified or an empty string is passed, filtering is not performed based on the delivery group ID. You can call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the delivery group ID. This parameter can be used together with other filter conditions, and all conditions must be met.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery group used for filtering. Substring matching is supported. For example, if you pass `Office applications`, delivery groups whose names contain this text are matched. If this parameter is not specified or an empty string is passed, filtering is not performed based on the delivery group name. If this parameter and the delivery group ID are specified at the same time, both conditions must be met.
        self.app_instance_group_name = app_instance_group_name
        # The name of the application used for filtering. Substring matching is supported. For example, if you pass `Office applications`, applications whose names contain this text are matched. If this parameter is not specified or an empty string is passed, filtering is not performed based on the application name. If this parameter and `AppId` are specified at the same time, both conditions must be met by the same application.
        self.app_name = app_name
        # The username to be excluded. Exact matching is performed based on the full username, such as `alice`. If this parameter is specified, applications that have been authorized for this user on a per-application basis through [AuthorizeUsersForApp](~~AuthorizeUsersForApp~~) are not returned. This can be used to find applications that can still be authorized for the user. If this parameter is not specified or an empty string is passed, filtering is not performed based on user authorization.
        # 
        # **Access permissions obtained through overall delivery group authorization or user groups are not evaluated by this condition.** Do not equate the returned results with a list of applications that the user has absolutely no access to.
        self.exclude_user_id = exclude_user_id
        # The page number. This parameter is required. Start the query from page `1` and use it in conjunction with `PageSize`. Keep other filter conditions unchanged when querying subsequent pages. If the value is invalid, the error code `InvalidParameter.PageNumber` is returned.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The maximum number of application records to return per page. This parameter is required. Valid values: `1` to `100`. If the value is out of range, the error code `InvalidParameter.PageSize` is returned.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. This parameter is required and is not case-sensitive. Only applications in published delivery groups of this product type are returned. If an unrecognized value is passed, the error code `InvalidParameter.ProductType` is returned. Filtering and statistics related to per-application authorization (`ExcludeUserId` and `AuthorizedUserCount`) are primarily used in WUYING Cloud App scenarios.
        # 
        # Valid values:
        # 
        # - `CloudApp`: WUYING Cloud App.
        # - `CloudBrowser`: Cloud browser.
        # - `WuyingServer`: Enterprise Edition workstation.
        # - `WuyingWorkstation`: Personal Edition Linggou container workstation.
        # - `WuyingWorkstationTeam`: Team Edition Linggou container workstation.
        # - `WuyingWorkstationBusiness`: Dedicated Edition Linggou container workstation.
        # - `AndroidCloud`: Cloud phone.
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

