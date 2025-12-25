# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_workorder20210610 import models as main_models
from darabonba.model import DaraModel

class GetTicketResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        data: main_models.GetTicketResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The return code of the request result.
        self.code = code
        # The data returned after the call succeeds.
        self.data = data
        # The error message. If success is set to false, the message is returned.
        self.message = message
        # Page number of the paging query parameter
        self.page_number = page_number
        # The number of entries per page in a pagination query parameter.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates that the call is normal.
        self.success = success
        # The total number of query results, that is, the total number of my ticket records.
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTicketResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetTicketResponseBodyData(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        create_time: int = None,
        creator_id: str = None,
        description: str = None,
        severity: main_models.GetTicketResponseBodyDataSeverity = None,
        status: main_models.GetTicketResponseBodyDataStatus = None,
        ticket_id: str = None,
        title: str = None,
    ):
        # The ID of the ticket issue category.
        self.category_id = category_id
        # The timestamp when the ticket was created.
        self.create_time = create_time
        # The uid of the ticket creator.
        self.creator_id = creator_id
        # The description of the ticket. Only pure text format is supported.
        self.description = description
        # Urgency enumeration value, 1 for general problem, 2 for urgent problem
        self.severity = severity
        # The status of the ticket. The reference values are as follows 1, "assigned", "Pending Response", 2, "handling", "handling", 3, "wait_feedback", "Pending feedback", 4: "feedback", "Feedback", 5, "wait_confirm", "To be confirmed", 6, "confirmed", "Completed"
        self.status = status
        # Work Order Number
        self.ticket_id = ticket_id
        # The title of the ticket.
        self.title = title

    def validate(self):
        if self.severity:
            self.severity.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.severity is not None:
            result['Severity'] = self.severity.to_map()

        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Severity') is not None:
            temp_model = main_models.GetTicketResponseBodyDataSeverity()
            self.severity = temp_model.from_map(m.get('Severity'))

        if m.get('Status') is not None:
            temp_model = main_models.GetTicketResponseBodyDataStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetTicketResponseBodyDataStatus(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        # Status Enumeration Text
        self.label = label
        # State enumeration value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetTicketResponseBodyDataSeverity(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        # Enumeration Text
        self.label = label
        # Enumeration
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

