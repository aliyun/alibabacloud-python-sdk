# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApplicationsForUserRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        query_mode: str = None,
        user_id: str = None,
    ):
        # The IDs of the applications that the EIAM account can access. You can query a maximum of 100 application IDs at a time.
        self.application_ids = application_ids
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The query mode. Default value: **OnlyDirect**. Valid values:
        # 
        # *   OnlyDirect: Only the direct permissions are queried. Direct permissions are the permissions that are directly granted to the account.
        # *   IncludeInherit: Both the permissions that are directly granted to the account and the inherited permissions are queried. Inherited permissions are the permissions that an account inherits from the parent organization or the group to which the account belongs.
        self.query_mode = query_mode
        # The ID of the EIAM account.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

