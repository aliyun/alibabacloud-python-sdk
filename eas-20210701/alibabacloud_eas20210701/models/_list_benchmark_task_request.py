# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBenchmarkTaskRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        model_id: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        request_method: str = None,
        service_name: str = None,
        sort: str = None,
        status: str = None,
    ):
        # The filter parameter. If specified, the system searches for records that match the specified value in the EAS service name and stress testing task name.
        self.filter = filter
        # The model ID.
        self.model_id = model_id
        # The sort order. Valid values:
        # - desc: Descending order. This is the default value.
        # - asc: Ascending order.
        self.order = order
        # The page number of the stress testing task list. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of stress testing tasks to return on each page. Default value: 100.
        self.page_size = page_size
        # The request method for stress testing. Valid values:
        # - concurrency: Fixed concurrency mode.
        # - requestRate: Fixed request rate mode.
        # - peakThroughput: Peak throughput mode.
        self.request_method = request_method
        # The name of the EAS service that corresponds to the stress testing task. For more information about how to query the service name, see [ListServices](https://help.aliyun.com/document_detail/412109.html).
        self.service_name = service_name
        # The sort field.
        self.sort = sort
        # The execution status used to filter stress testing tasks.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_method is not None:
            result['RequestMethod'] = self.request_method

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestMethod') is not None:
            self.request_method = m.get('RequestMethod')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

