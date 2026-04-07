# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCheckProcessesRequest(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        message_id: str = None,
        operator: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        status: str = None,
    ):
        # Extension point event encoding.
        # 
        # This parameter is required.
        self.event_code = event_code
        # The message ID in DataWorks OpenEvent. You can obtain the ID from a received message when an extension point event is triggered.
        self.message_id = message_id
        # The operator ID.
        self.operator = operator
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the workspace.
        self.project_id = project_id
        # The check status of the extension. Valid values:
        # 
        # *   CHECKING
        # *   PASSED
        # *   BLOCKED
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

