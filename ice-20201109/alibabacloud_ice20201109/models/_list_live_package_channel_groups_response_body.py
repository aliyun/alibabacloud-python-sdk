# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListLivePackageChannelGroupsResponseBody(DaraModel):
    def __init__(
        self,
        live_package_channel_groups: List[main_models.ListLivePackageChannelGroupsResponseBodyLivePackageChannelGroups] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sort_by: str = None,
        total_count: int = None,
    ):
        # The channel groups returned.
        self.live_package_channel_groups = live_package_channel_groups
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The sort order.
        self.sort_by = sort_by
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.live_package_channel_groups:
            for v1 in self.live_package_channel_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LivePackageChannelGroups'] = []
        if self.live_package_channel_groups is not None:
            for k1 in self.live_package_channel_groups:
                result['LivePackageChannelGroups'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_package_channel_groups = []
        if m.get('LivePackageChannelGroups') is not None:
            for k1 in m.get('LivePackageChannelGroups'):
                temp_model = main_models.ListLivePackageChannelGroupsResponseBodyLivePackageChannelGroups()
                self.live_package_channel_groups.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLivePackageChannelGroupsResponseBodyLivePackageChannelGroups(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_name: str = None,
        last_modified: str = None,
        origin_domain: str = None,
    ):
        # The time when the channel group was created. It is in the `yyyy-MM-ddTHH:mm:ssZ` format and displayed in UTC.
        self.create_time = create_time
        # The channel group description.
        self.description = description
        # The channel group name.
        self.group_name = group_name
        # The time when the channel group was last modified. It is in the `yyyy-MM-ddTHH:mm:ssZ` format and displayed in UTC.
        self.last_modified = last_modified
        # The origin domain.
        self.origin_domain = origin_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.origin_domain is not None:
            result['OriginDomain'] = self.origin_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('OriginDomain') is not None:
            self.origin_domain = m.get('OriginDomain')

        return self

