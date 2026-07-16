# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceInstanceWorkerRequest(DaraModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        ready: bool = None,
        service_name: str = None,
        sort: str = None,
        status: str = None,
        worker_name: str = None,
    ):
        # The sort order.
        # 
        # - Asc: ascending order.
        # 
        # - Desc: descending order.
        self.order = order
        # The page number. The value starts from 1. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page. The default value is 100.
        self.page_size = page_size
        # Indicates whether the health check passed.
        self.ready = ready
        # The service name.
        self.service_name = service_name
        # The field to sort by.
        self.sort = sort
        # The status of the worker instance.
        self.status = status
        # The name of the worker instance.
        self.worker_name = worker_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.status is not None:
            result['Status'] = self.status

        if self.worker_name is not None:
            result['WorkerName'] = self.worker_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkerName') is not None:
            self.worker_name = m.get('WorkerName')

        return self

