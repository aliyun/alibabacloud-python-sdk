# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        series_codes_shrink: str = None,
        storage_secret_key: str = None,
        tags: str = None,
    ):
        # The filter condition that is used to query instances. If you do not configure this parameter, all instances are queried.
        self.filter = filter
        # The page number.
        # 
        # Valid values: 1 to 100000000.
        # 
        # If you set this parameter to a value smaller than 1, the system uses 1 as the value. If you set this parameter to a value greater than 100000000, the system uses 100000000 as the value.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Value values: 10 to 200.
        # 
        # If you set this parameter to a value smaller than 10, the system uses 10 as the value. If you set this parameter to a value greater than 200, the system uses 200 as the value.
        self.page_size = page_size
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The primary edition of the instance.
        # 
        # Valid values:
        # 
        # *   standard: Standard Edition
        # *   ultimate: Enterprise Platinum Edition
        # *   professional: Professional Edition
        self.series_codes_shrink = series_codes_shrink
        # The storage encryption key.
        self.storage_secret_key = storage_secret_key
        # The tags that are used to filter instances.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.series_codes_shrink is not None:
            result['seriesCodes'] = self.series_codes_shrink

        if self.storage_secret_key is not None:
            result['storageSecretKey'] = self.storage_secret_key

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('seriesCodes') is not None:
            self.series_codes_shrink = m.get('seriesCodes')

        if m.get('storageSecretKey') is not None:
            self.storage_secret_key = m.get('storageSecretKey')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

