# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDIJobEventsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDIJobEventsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDIJobEventsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDIJobEventsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        dijob_event: List[main_models.ListDIJobEventsResponseBodyPagingInfoDIJobEvent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The events returned. The value of this parameter is an array.
        self.dijob_event = dijob_event
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dijob_event:
            for v1 in self.dijob_event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DIJobEvent'] = []
        if self.dijob_event is not None:
            for k1 in self.dijob_event:
                result['DIJobEvent'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dijob_event = []
        if m.get('DIJobEvent') is not None:
            for k1 in m.get('DIJobEvent'):
                temp_model = main_models.ListDIJobEventsResponseBodyPagingInfoDIJobEvent()
                self.dijob_event.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDIJobEventsResponseBodyPagingInfoDIJobEvent(DaraModel):
    def __init__(
        self,
        action: str = None,
        channels: str = None,
        create_time: str = None,
        detail: str = None,
        dst_sql: str = None,
        dst_table: str = None,
        failover_message: str = None,
        id: str = None,
        severity: str = None,
        src_sql: str = None,
        src_table: str = None,
        status: str = None,
        type: str = None,
    ):
        # The processing result of the DDL event. Valid values: Critical, Ignore, Normal, and Warning.
        self.action = action
        # The alert notification method. Valid values: Phone, Mail, Sms, Ding, and Webhook.
        self.channels = channels
        # The time when the event was created.
        self.create_time = create_time
        # The alert details.
        self.detail = detail
        # The DDL statement of the destination table.
        self.dst_sql = dst_sql
        # The name of the destination table.
        self.dst_table = dst_table
        # The error logs for failovers.
        self.failover_message = failover_message
        # The event ID.
        self.id = id
        # The severity level of the alert. Valid values: Warning and Critical.
        self.severity = severity
        # The DDL statement of the source table.
        self.src_sql = src_sql
        # The name of the source table.
        self.src_table = src_table
        # The sending status of an alert notification. Valid values: Success, Fail, and Silence.
        self.status = status
        # The type of the alert event.
        # 
        # *   Heartbeat
        # *   Delay
        # *   FailoverCount
        # *   DdlReport
        # *   ResourceUtilization
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.dst_sql is not None:
            result['DstSql'] = self.dst_sql

        if self.dst_table is not None:
            result['DstTable'] = self.dst_table

        if self.failover_message is not None:
            result['FailoverMessage'] = self.failover_message

        if self.id is not None:
            result['Id'] = self.id

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.src_sql is not None:
            result['SrcSql'] = self.src_sql

        if self.src_table is not None:
            result['SrcTable'] = self.src_table

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('DstSql') is not None:
            self.dst_sql = m.get('DstSql')

        if m.get('DstTable') is not None:
            self.dst_table = m.get('DstTable')

        if m.get('FailoverMessage') is not None:
            self.failover_message = m.get('FailoverMessage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('SrcSql') is not None:
            self.src_sql = m.get('SrcSql')

        if m.get('SrcTable') is not None:
            self.src_table = m.get('SrcTable')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

