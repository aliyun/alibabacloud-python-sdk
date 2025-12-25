# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTicketsRequest(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: int = None,
        status_list: List[str] = None,
        ticket_id: str = None,
        ticket_id_list: List[str] = None,
        uid: str = None,
    ):
        # The deadline for ticket creation. This parameter is used in conjunction with StartDate to query tickets submitted within the specified start and end time ranges.
        self.end_date = end_date
        # The ticket keyword, which is used for fuzzy search to match the content of the Description field when a ticket is created.
        self.keyword = keyword
        # Paging query page number parameters
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries queried by page parameter
        # 
        # This parameter is required.
        self.page_size = page_size
        # The time when the ticket was created. This parameter is used with EndDate to query tickets that are created within the specified start and end time ranges.
        self.start_date = start_date
        # Multiple ticket statuses
        self.status_list = status_list
        # Work Order Number
        self.ticket_id = ticket_id
        # Multiple job numbers
        self.ticket_id_list = ticket_id_list
        # UID
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.ticket_id_list is not None:
            result['TicketIdList'] = self.ticket_id_list

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('TicketIdList') is not None:
            self.ticket_id_list = m.get('TicketIdList')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

