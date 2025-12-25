# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOrdersRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        order_result_type: str = None,
        order_status: str = None,
        page_number: int = None,
        page_size: int = None,
        plugin_type: str = None,
        search_content: str = None,
        search_date_type: str = None,
        start_time: str = None,
        tid: int = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The scope of the tickets that you want to query. Valid values:
        # 
        # *   **AS_ADMIN**: all tickets.
        # *   **AS_COMMITTER**: the tickets that are submitted by the current user.
        # *   **AS_HANDLER**: the tickets to be processed by the current user.
        # *   **AS_OWNER**: the tickets that are processed by the current user.
        # *   **AS_Related**: the tickets that are related to the current user.
        self.order_result_type = order_result_type
        # The status of the tickets that you want to query. Valid values:
        # 
        # *   **ALL**: queries the tickets of all statuses.
        # *   **FINISHED**: queries the tickets that are completed.
        # *   **RUNNING**: queries the tickets that are being processed.
        self.order_status = order_status
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The type of the tickets that you want to query. For more information, see [PluginType parameter](https://help.aliyun.com/document_detail/429109.html).
        self.plugin_type = plugin_type
        # The keyword that is used to query tickets.
        self.search_content = search_content
        # The time condition based on which you want to query tickets. Valid values:
        # 
        # *   **CREATE_TIME**: the time when a ticket was created.
        # *   **MODIFY_TIME**: the time when a ticket was last modified.
        self.search_date_type = search_date_type
        # The beginning of the time range to query.
        self.start_time = start_time
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.order_result_type is not None:
            result['OrderResultType'] = self.order_result_type

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.search_content is not None:
            result['SearchContent'] = self.search_content

        if self.search_date_type is not None:
            result['SearchDateType'] = self.search_date_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OrderResultType') is not None:
            self.order_result_type = m.get('OrderResultType')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('SearchContent') is not None:
            self.search_content = m.get('SearchContent')

        if m.get('SearchDateType') is not None:
            self.search_date_type = m.get('SearchDateType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

