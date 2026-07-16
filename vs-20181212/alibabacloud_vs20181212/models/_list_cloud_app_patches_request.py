# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudAppPatchesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        patch_id: str = None,
        patch_name: str = None,
        start_time: str = None,
    ):
        # The ID of the cloud application. This ID corresponds to a unique application package.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The time range for filtering. The time must be in UTC and in the ISO 8601 standard format yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # The page number of the list to return. The value starts from 1.
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is 100.
        # Default value: 10.
        self.page_size = page_size
        # The ID of the patch package.
        self.patch_id = patch_id
        # The name of the patch package.
        self.patch_name = patch_name
        # The start of the time range to query. The time is in UTC and follows the ISO 8601 standard. The format is yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

        if self.patch_name is not None:
            result['PatchName'] = self.patch_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        if m.get('PatchName') is not None:
            self.patch_name = m.get('PatchName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

