# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAiRtcAuthCodeListRequest(DaraModel):
    def __init__(
        self,
        license_item_id: str = None,
        need_total_count: bool = None,
        page_no: int = None,
        page_size: int = None,
        status: int = None,
        type: int = None,
    ):
        # The ID of the batch.
        self.license_item_id = license_item_id
        # Specifies whether to include the total count of records in the response. Defaults to `true`.
        self.need_total_count = need_total_count
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The status of the authorization code. Valid values:
        # 
        # *   `1`: Activated
        # *   `2`: Inactive
        self.status = status
        # The type of license. Valid values:
        # 
        # *   `1`: Audio call
        # *   `2`: Vision call
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.license_item_id is not None:
            result['LicenseItemId'] = self.license_item_id

        if self.need_total_count is not None:
            result['NeedTotalCount'] = self.need_total_count

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicenseItemId') is not None:
            self.license_item_id = m.get('LicenseItemId')

        if m.get('NeedTotalCount') is not None:
            self.need_total_count = m.get('NeedTotalCount')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

