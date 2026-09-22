# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthorizedUsersRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_set_id: str = None,
        app_instance_persistent_id: str = None,
        end_user_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        user_id_fuzzy: str = None,
    ):
        # The application ID. Specifies the application to filter users who are **authorized for that specific application** (authorized through the [AuthorizeUsersForApp](~~AuthorizeUsersForApp~~) operation). This parameter applies to delivery groups with the `App` authorization mode. Obtain the application ID from the Apps list returned by the [GetAppInstanceGroup](~~GetAppInstanceGroup~~) operation.
        # 
        # If not specified, all authorized users under the delivery group are returned. This parameter is not supported when querying by delivery group set.
        self.app_id = app_id
        # The delivery group ID. Call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain this value. For cloud browser groups, specify the browser group ID returned by the [ListBrowserInstanceGroup](~~ListBrowserInstanceGroup~~) operation.
        # 
        # **Exactly one of this parameter and AppInstanceGroupSetId must be specified.**
        self.app_instance_group_id = app_instance_group_id
        # The delivery group set ID.
        # 
        # **Exactly one of this parameter and AppInstanceGroupId must be specified.** When querying by set, do not specify AppId or AppInstancePersistentId. Otherwise, a parameter error is returned.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The persistent session ID. Specifies the persistent session to filter users who are granted that session. This parameter applies to delivery groups with the `Session` authorization mode. Call the [ListPersistentAppInstances](~~ListPersistentAppInstances~~) operation to obtain this value.
        # 
        # If specified, only users granted that session are returned. However, the response parameter AppInstancePersistentIds still lists all persistent sessions granted to each user. This parameter is not supported when querying by delivery group set.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The username for **exact matching**. If not specified, no filtering by exact username is applied. Can be specified together with UserIdFuzzy, in which case both conditions must be met.
        self.end_user_id = end_user_id
        # The page number, starting from 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of records per page. Valid values: 1 to 100.
        # 
        # When the authorization mode is `App` or `AppInstanceGroup`, pagination is based on authorization records. Multiple authorization records for the same user are merged into a single user entry. Therefore, the actual number of users returned on the current page may be less than this value.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. The value must match the product type of the queried delivery group or delivery group set. If the value does not match, a resource-not-found error code is returned.
        # 
        # Valid values:
        # 
        # - CloudApp: Wuying Cloud Application.
        # - CloudBrowser: Cloud Browser.
        # - WuyingServer: Enterprise Edition Workstation.
        # - WuyingWorkstation: Personal Edition Linggou Container Workstation.
        # - WuyingWorkstationTeam: Linggou Team Edition Container Workstation.
        # - WuyingWorkstationBusiness: Linggou Dedicated Edition Container Workstation.
        # - AndroidCloud: Cloud Phone.
        # - AIAgent: AgentBay (AI agent).
        # 
        # This parameter is required.
        self.product_type = product_type
        # The username keyword for **fuzzy matching**. A match occurs if the username contains this keyword. For example, if you specify `ali`, both `alice` and `ali.wang` are returned. If not specified, no keyword-based filtering is applied.
        self.user_id_fuzzy = user_id_fuzzy

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

        if self.app_instance_group_set_id is not None:
            result['AppInstanceGroupSetId'] = self.app_instance_group_set_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.user_id_fuzzy is not None:
            result['UserIdFuzzy'] = self.user_id_fuzzy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupSetId') is not None:
            self.app_instance_group_set_id = m.get('AppInstanceGroupSetId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('UserIdFuzzy') is not None:
            self.user_id_fuzzy = m.get('UserIdFuzzy')

        return self

