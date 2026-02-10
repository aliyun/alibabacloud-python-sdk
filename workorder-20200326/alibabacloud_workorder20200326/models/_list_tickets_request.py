# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTicketsRequest(DaraModel):
    def __init__(
        self,
        created_after_time: int = None,
        created_before_time: int = None,
        ids: str = None,
        language: str = None,
        page_size: int = None,
        page_start: int = None,
        product_code: str = None,
        sub_user_id: str = None,
        ticket_status: str = None,
    ):
        self.created_after_time = created_after_time
        self.created_before_time = created_before_time
        self.ids = ids
        self.language = language
        self.page_size = page_size
        self.page_start = page_start
        self.product_code = product_code
        self.sub_user_id = sub_user_id
        self.ticket_status = ticket_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_after_time is not None:
            result['CreatedAfterTime'] = self.created_after_time

        if self.created_before_time is not None:
            result['CreatedBeforeTime'] = self.created_before_time

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.language is not None:
            result['Language'] = self.language

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.page_start is not None:
            result['PageStart'] = self.page_start

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.ticket_status is not None:
            result['TicketStatus'] = self.ticket_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAfterTime') is not None:
            self.created_after_time = m.get('CreatedAfterTime')

        if m.get('CreatedBeforeTime') is not None:
            self.created_before_time = m.get('CreatedBeforeTime')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('TicketStatus') is not None:
            self.ticket_status = m.get('TicketStatus')

        return self

