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
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The ID of the application used to filter delivery groups. Partial matching is supported. The delivery group must contain a deployed application that meets the condition. If this parameter is not specified or is set to an empty string, the results are not filtered by application ID. If this parameter is specified together with `AppName`, both conditions must be met by the same application.
        # 
        # This condition does not restrict the returned `Apps` list to the matched applications.
        self.app_id = app_id
        # The ID of the delivery group used for filtering. Partial matching is supported. You can pass the complete ID or a continuous segment of it. If this parameter is not specified or is set to an empty string, the results are not filtered by ID. This parameter can be used together with other filter conditions, and the results must meet all conditions.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery group used for filtering. Partial matching is supported. For example, if you pass `Office applications`, delivery groups whose names contain this text are matched. If this parameter is not specified or is set to an empty string, the results are not filtered by name. If this parameter is specified together with the delivery group ID, both the ID and the name must be matched.
        self.app_instance_group_name = app_instance_group_name
        # The name of the application used to filter delivery groups. Partial matching is supported. The delivery group must contain a deployed application whose name contains the specified text. If this parameter is not specified or is set to an empty string, the results are not filtered by application name. If this parameter is specified together with `AppId`, both conditions must be met by the same application.
        # 
        # This condition does not restrict the returned `Apps` list to the matched applications.
        self.app_name = app_name
        # The username to be excluded based on existing authorizations. Exact match by full username is supported, such as `alice`. If this parameter is specified, delivery groups for which all applications have been directly authorized to the user are excluded. If this parameter is not specified or is set to an empty string, the results are not filtered by user authorization status.
        # 
        # **Authorizations for a single application or access permissions obtained through user groups are not fully evaluated by this condition.** Do not equate the returned results with a list of delivery groups to which the user has no access at all.
        self.exclude_user_id = exclude_user_id
        # The ID of the office network.
        self.office_site_id = office_site_id
        # The page number. This parameter is required. Start the query from page `1` and use it in conjunction with `PageSize`. Keep other filter conditions unchanged when querying subsequent pages.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The maximum number of delivery groups to return per page. This parameter is required. Valid values: `1` to `100`. Explicitly specify this parameter and do not use the default values of other query operations.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. This parameter is required. The value must be the same as the product type of the delivery groups to be queried. Only published delivery groups of this product type are returned. If an unrecognized value is passed, a parameter error is returned.
        # 
        # Valid values:
        # 
        # - `CloudApp`: Wuying Cloud App.
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

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

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

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

