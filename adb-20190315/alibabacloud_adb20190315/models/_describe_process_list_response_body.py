# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeProcessListResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeProcessListResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The total number of pages returned.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

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
        if m.get('Items') is not None:
            temp_model = main_models.DescribeProcessListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeProcessListResponseBodyItems(DaraModel):
    def __init__(
        self,
        process: List[main_models.DescribeProcessListResponseBodyItemsProcess] = None,
    ):
        self.process = process

    def validate(self):
        if self.process:
            for v1 in self.process:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Process'] = []
        if self.process is not None:
            for k1 in self.process:
                result['Process'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.process = []
        if m.get('Process') is not None:
            for k1 in m.get('Process'):
                temp_model = main_models.DescribeProcessListResponseBodyItemsProcess()
                self.process.append(temp_model.from_map(k1))

        return self

class DescribeProcessListResponseBodyItemsProcess(DaraModel):
    def __init__(
        self,
        command: str = None,
        db: str = None,
        host: str = None,
        id: int = None,
        info: str = None,
        process_id: str = None,
        start_time: str = None,
        time: int = None,
        user: str = None,
    ):
        self.command = command
        self.db = db
        self.host = host
        self.id = id
        self.info = info
        self.process_id = process_id
        self.start_time = start_time
        self.time = time
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.db is not None:
            result['DB'] = self.db

        if self.host is not None:
            result['Host'] = self.host

        if self.id is not None:
            result['Id'] = self.id

        if self.info is not None:
            result['Info'] = self.info

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time is not None:
            result['Time'] = self.time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('DB') is not None:
            self.db = m.get('DB')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

