# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserGroupsForUserRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        paging_off: str = None,
        project_id: int = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the bastion host instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the user group to query. Fuzzy match is supported.
        self.keyword = keyword
        # The page number for a paged query. Default value: **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The maximum number of entries per page for a paged query.  
        # The maximum value of PageSize is 100. The default number of entries per page is 20. If PageSize is left empty, 20 entries are returned by default.
        # > Do not leave PageSize empty.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Specifies whether to disable paging. Valid values:
        # 
        # - **true**: Disables paging and returns all data.
        # 
        # - **false**: Enables paging and returns the number of user groups specified by PageSize.
        self.paging_off = paging_off
        # The project ID.
        self.project_id = project_id
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The user ID.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.paging_off is not None:
            result['PagingOff'] = self.paging_off

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PagingOff') is not None:
            self.paging_off = m.get('PagingOff')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

