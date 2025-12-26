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
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The IDs of the application instances. Up to 100 IDs can be specified.
        self.app_instance_id_list = app_instance_id_list
        # Specifies whether to query the information about deleted app instances. If you set this parameter to true, you must configure AppInstanceIdList. Otherwise, a parameter error is reported.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.include_deleted = include_deleted
        # The page number. Default value: `1`. We recommend that you specify this parameter.
        self.page_number = page_number
        # The number of entries per page. The value cannot be greater than `100`. Default value: `20`. We recommend that you specify this parameter.
        self.page_size = page_size
        # The status of the application instances.
        self.status = status
        # The user IDs. You can specify up to 100 IDs.
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

