# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRdMemberListRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        resource_directory_id: str = None,
    ):
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        return self

