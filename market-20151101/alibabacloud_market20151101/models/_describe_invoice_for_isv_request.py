# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInvoiceForIsvRequest(DaraModel):
    def __init__(
        self,
        create_time_end: str = None,
        create_time_start: str = None,
        invoice_id: int = None,
        max_results: int = None,
        next_token: str = None,
        page_index: int = None,
        page_size: int = None,
        status: int = None,
        type: int = None,
        user_id: int = None,
    ):
        # The end time. By default, 23:59:59 is appended to the date.
        self.create_time_end = create_time_end
        # The start time. By default, 00:00:00 is appended to the date.
        self.create_time_start = create_time_start
        # The ID of the invoice application. This corresponds to the Result.Id field in the response of the DescribeInvoiceForIsv operation.
        self.invoice_id = invoice_id
        # The maximum number of entries per page in a paging query. Maximum value: 50. Default value: 10. (This parameter is not enabled.)
        self.max_results = max_results
        # The pagination token returned by the current call. This parameter is not enabled.
        self.next_token = next_token
        # The page number. Pages start from 1.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The current invoice status. Valid values:
        # - 0: Applying.
        # - 1: Completed.
        self.status = status
        # The invoice type. If this parameter is left empty, all types are queried by default. Valid values:
        # - 2: Digital electronic ordinary invoice.
        # - 3: Digital electronic special invoice.
        self.type = type
        # The Alibaba Cloud user ID of the customer.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.invoice_id is not None:
            result['InvoiceId'] = self.invoice_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('InvoiceId') is not None:
            self.invoice_id = m.get('InvoiceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

