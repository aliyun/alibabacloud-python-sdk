# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthorizedAppInstanceGroupByUserRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_name: str = None,
        end_user_id: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The application ID. Fuzzy match is supported. App instance groups in which the IDs of deployed applications contain this string are returned. You can obtain the application ID from the Apps list returned by this operation.
        # 
        # If this parameter is not specified, app instance groups are not filtered by application ID.
        self.app_id = app_id
        # The app instance group ID. Fuzzy match is supported. App instance groups whose IDs contain this string are returned. You can call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the ID.
        # 
        # If this parameter is not specified, app instance groups are not filtered by app instance group ID.
        self.app_instance_group_id = app_instance_group_id
        # The app instance group name. Fuzzy match is supported. For example, if you specify `Office applications`, app instance groups whose names contain `Office applications` (such as `My office applications` and `Office applications A`) are queried.
        # 
        # If this parameter is not specified, app instance groups are not filtered by app instance group name.
        self.app_instance_group_name = app_instance_group_name
        # The application name. Fuzzy match is supported. App instance groups in which the names of deployed applications contain this string are returned.
        # 
        # If this parameter is not specified, app instance groups are not filtered by application name.
        self.app_name = app_name
        # The username. Exact match is used based on the username to query the app instance groups to which the user has been granted app instance group-level authorization.
        # 
        # > This parameter is required. If this parameter is not specified, the error code InvalidParameter.UserId is returned.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The office network ID.
        self.office_site_id = office_site_id
        # The page number. Pages start from 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of app instance groups to return on each page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. The value must be consistent with the product type of the queried app instance groups. Only app instance groups of this product type are returned.
        # 
        # Valid values:
        # 
        # - CloudApp: Cloud App.
        # - CloudBrowser: Cloud Browser.
        # - WuyingServer: Enterprise Edition workstation.
        # - WuyingWorkstation: Personal Edition Linggou container workstation.
        # - WuyingWorkstationTeam: Team Edition Linggou container workstation.
        # - WuyingWorkstationBusiness: Exclusive Edition Linggou container workstation.
        # - AndroidCloud: Cloud Phone.
        # - AIAgent: AgentBay (AI agent).
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

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

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

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

