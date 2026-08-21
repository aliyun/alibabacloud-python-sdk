# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchEditingProjectRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        owner_account: str = None,
        owner_id: str = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        title: str = None,
    ):
        # The end of the time range to query based on CreationTime. Specify the time in the format of <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_no = page_no
        # The number of entries to return on each page. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The sorting method of the results. Valid values:
        # 
        # - **desc** (default): sorts the results in reverse chronological order based on creation time.
        # - **asc**: sorts the results in chronological order based on creation time.
        self.sort_by = sort_by
        # The start of the time range to query based on CreationTime. Specify the time in the format of <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.start_time = start_time
        # The status of the online editing project. Separate multiple statuses with commas (,). By default, all online editing projects are returned. Valid values:
        # 
        # - **Normal**: Draft.
        # - **Producing**: Being produced.
        # - **Produced**: Produced.
        # - **ProduceFailed**: Failed to be produced.
        self.status = status
        # The title of the online editing project.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

