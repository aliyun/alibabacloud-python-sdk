# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListInstanceStatusResponseBody(DaraModel):
    def __init__(
        self,
        instance_statuses: List[main_models.ListInstanceStatusResponseBodyInstanceStatuses] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ID of the simple application server.
        self.instance_statuses = instance_statuses
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_statuses:
            for v1 in self.instance_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k1 in self.instance_statuses:
                result['InstanceStatuses'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k1 in m.get('InstanceStatuses'):
                temp_model = main_models.ListInstanceStatusResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstanceStatusResponseBodyInstanceStatuses(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        status: str = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The status of the simple application server. Valid values:
        # 
        # - Pending
        # 
        # - Starting
        # 
        # - Running
        # 
        # - Stopping
        # 
        # - Stopped
        # 
        # - Resetting
        # 
        # - Upgrading
        # 
        # - Disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

