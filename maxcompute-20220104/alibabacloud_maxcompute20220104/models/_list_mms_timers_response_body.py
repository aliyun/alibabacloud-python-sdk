# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsTimersResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMmsTimersResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListMmsTimersResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMmsTimersResponseBodyData(DaraModel):
    def __init__(
        self,
        object_list: List[main_models.ListMmsTimersResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.object_list = object_list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.object_list:
            for v1 in self.object_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['objectList'] = []
        if self.object_list is not None:
            for k1 in self.object_list:
                result['objectList'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k1 in m.get('objectList'):
                temp_model = main_models.ListMmsTimersResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k1))

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListMmsTimersResponseBodyDataObjectList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        db_id: int = None,
        id: int = None,
        name: str = None,
        schedule_type: str = None,
        source_id: int = None,
        src_db_name: str = None,
        stopped: bool = None,
        type: str = None,
        value: str = None,
    ):
        self.create_time = create_time
        self.db_id = db_id
        self.id = id
        self.name = name
        self.schedule_type = schedule_type
        self.source_id = source_id
        self.src_db_name = src_db_name
        self.stopped = stopped
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.db_id is not None:
            result['dbId'] = self.db_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name

        if self.stopped is not None:
            result['stopped'] = self.stopped

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')

        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

