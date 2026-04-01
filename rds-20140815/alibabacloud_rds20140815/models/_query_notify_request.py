# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryNotifyRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        page_number: int = None,
        page_size: int = None,
        to: str = None,
        with_confirmed: bool = None,
    ):
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The page number. Pages start from page 1. Default value: 1.****
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30**
        # *   **50**
        # *   **100**
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.to = to
        # Specifies whether the query results contain confirmed notifications. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  A confirmed notification is a notification that has been marked as confirmed by calling the ConfirmNotify operation.
        # 
        # This parameter is required.
        self.with_confirmed = with_confirmed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.to is not None:
            result['To'] = self.to

        if self.with_confirmed is not None:
            result['WithConfirmed'] = self.with_confirmed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('WithConfirmed') is not None:
            self.with_confirmed = m.get('WithConfirmed')

        return self

