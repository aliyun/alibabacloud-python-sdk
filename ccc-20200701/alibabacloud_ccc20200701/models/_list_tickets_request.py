# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTicketsRequest(DaraModel):
    def __init__(
        self,
        assignee: str = None,
        assignee_type: str = None,
        category_id: str = None,
        creator: str = None,
        customer_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        job_id_list: str = None,
        page_number: int = None,
        page_size: int = None,
        participant: str = None,
        start_time: int = None,
        state: str = None,
        ticket_id: str = None,
        title: str = None,
    ):
        self.assignee = assignee
        self.assignee_type = assignee_type
        self.category_id = category_id
        self.creator = creator
        self.customer_id = customer_id
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.job_id_list = job_id_list
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.participant = participant
        self.start_time = start_time
        self.state = state
        self.ticket_id = ticket_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assignee is not None:
            result['Assignee'] = self.assignee

        if self.assignee_type is not None:
            result['AssigneeType'] = self.assignee_type

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.participant is not None:
            result['Participant'] = self.participant

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Assignee') is not None:
            self.assignee = m.get('Assignee')

        if m.get('AssigneeType') is not None:
            self.assignee_type = m.get('AssigneeType')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Participant') is not None:
            self.participant = m.get('Participant')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

