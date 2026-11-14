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
        # The application ID. This parameter is used to filter users who are **specifically authorized for this application** (authorized through the [AuthorizeUsersForApp](~~AuthorizeUsersForApp~~) operation). This parameter applies to app instance groups whose authorization mode is `App`. You can obtain the application ID from the Apps list returned by the [GetAppInstanceGroup](~~GetAppInstanceGroup~~) operation.
        # 
        # If this parameter is not specified, all authorized users under the app instance group are returned. This parameter is not supported when querying by app instance group set.
        self.app_id = app_id
        # The app instance group ID. You can call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the ID. For cloud browser groups, specify the browser group ID returned by the [ListBrowserInstanceGroup](~~ListBrowserInstanceGroup~~) operation.
        # 
        # **You must specify either this parameter or AppInstanceGroupSetId, but not both.**
        self.app_instance_group_id = app_instance_group_id
        # The app instance group set ID.
        # 
        # **You must specify either this parameter or AppInstanceGroupId, but not both.** When querying by set, do not specify AppId or AppInstancePersistentId. Otherwise, a parameter error is returned.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The persistent session ID. This parameter is used to filter users who are granted this persistent session. This parameter applies to app instance groups whose authorization mode is `Session`. You can call the [ListPersistentAppInstances](~~ListPersistentAppInstances~~) operation to obtain the ID.
        # 
        # If this parameter is specified, only the users granted this session are returned. However, the AppInstancePersistentIds response parameter still lists all persistent sessions granted to the user. This parameter is not supported when querying by app instance group set.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The username. Performs **exact match** by username. If this parameter is not specified, filtering by full username is not applied. This parameter can be specified together with UserIdFuzzy, and both conditions must be met.
        self.end_user_id = end_user_id
        # The page number. Pages start from 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of records returned per page. Valid values: 1 to 100.
        # 
        # When the authorization mode is `App` or `AppInstanceGroup`, pagination is based on authorization records. Multiple authorization records for the same user are merged into one user in the response. Therefore, the actual number of users returned on the current page may be less than this value.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. The value must be consistent with the product type of the queried app instance group or app instance group set. If they are inconsistent, a resource not found error code is returned.
        # 
        # Valid values:
        # 
        # - CloudApp: Wuying Cloud App
        # - CloudBrowser: Cloud Browser
        # - WuyingServer: Enterprise Edition workstation
        # - WuyingWorkstation: Personal Edition Linggou container workstation
        # - WuyingWorkstationTeam: Team Edition Linggou container workstation
        # - WuyingWorkstationBusiness: Dedicated Edition Linggou container workstation
        # - AndroidCloud: Cloud Phone
        # - AIAgent: AgentBay (AI agent)
        # 
        # This parameter is required.
        self.product_type = product_type
        # The username keyword. Performs **fuzzy match** by username. A hit occurs if the username contains this keyword. For example, if you specify `ali`, both `alice` and `ali.wang` are matched. If this parameter is not specified, filtering by keyword is not applied.
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

