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
        # The application ID. Fuzzy match is supported. Delivery groups in which the IDs of deployed applications contain this string are returned. You can obtain the application ID from the Apps list returned by this operation.
        # 
        # If this parameter is not specified, delivery groups are not filtered by application ID.
        self.app_id = app_id
        # The delivery group ID. Fuzzy match is supported. Delivery groups whose IDs contain this string are returned. You can call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the ID.
        # 
        # If this parameter is not specified, delivery groups are not filtered by delivery group ID.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name. Fuzzy match is supported. For example, if you specify Office applications, delivery groups whose names contain Office applications (such as My office applications and Office applications A) are returned.
        # 
        # If this parameter is not specified, delivery groups are not filtered by delivery group name.
        self.app_instance_group_name = app_instance_group_name
        # The application name. Fuzzy match is supported. Delivery groups in which the names of deployed applications contain this string are returned.
        # 
        # If this parameter is not specified, delivery groups are not filtered by application name.
        self.app_name = app_name
        # The username. Exact match is used to query the delivery groups for which the user has been granted delivery group-level authorization.
        # 
        # > This parameter is required. If this parameter is not specified, the InvalidParameter.UserId error code is returned.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The office network ID.
        self.office_site_id = office_site_id
        # The page number. Pages start from 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of delivery groups to return per page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. The value must be the same as the product type of the delivery groups to be queried. Only delivery groups of this product type are returned.
        # 
        # Valid values:
        # 
        # - CloudApp: Wuying Cloud App.
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

