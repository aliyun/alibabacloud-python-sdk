# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAppInstancesRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_id_list: List[str] = None,
        include_deleted: bool = None,
        page_number: int = None,
        page_size: int = None,
        status: List[str] = None,
        user_id_list: List[str] = None,
    ):
        # The delivery group ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The application instance ID.
        self.app_instance_id = app_instance_id
        # The list of application instance IDs. A maximum of 100 IDs can be specified.
        self.app_instance_id_list = app_instance_id_list
        # Specifies whether to query information about deleted instances. If this parameter is set to true, the AppInstanceIdList parameter is required. Otherwise, a parameter error is returned.
        self.include_deleted = include_deleted
        # The page number of the query results to display. Default value: `1`. Specify this parameter.
        self.page_number = page_number
        # The number of query results per page. Maximum value: `100`. Default value: `20`. Specify this parameter.
        self.page_size = page_size
        # The list of application instance statuses.
        self.status = status
        # The list of user IDs. A maximum of 100 IDs can be specified.
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_instance_id_list is not None:
            result['AppInstanceIdList'] = self.app_instance_id_list

        if self.include_deleted is not None:
            result['IncludeDeleted'] = self.include_deleted

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppInstanceIdList') is not None:
            self.app_instance_id_list = m.get('AppInstanceIdList')

        if m.get('IncludeDeleted') is not None:
            self.include_deleted = m.get('IncludeDeleted')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        return self

