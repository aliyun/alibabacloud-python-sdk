# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsDbsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMmsDbsResponseBodyData = None,
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
            temp_model = main_models.ListMmsDbsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMmsDbsResponseBodyData(DaraModel):
    def __init__(
        self,
        object_list: List[main_models.ListMmsDbsResponseBodyDataObjectList] = None,
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
                temp_model = main_models.ListMmsDbsResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k1))

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListMmsDbsResponseBodyDataObjectList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        deleted: bool = None,
        description: str = None,
        dst_name: str = None,
        dst_project_name: str = None,
        extra: str = None,
        id: int = None,
        last_ddl_time: str = None,
        location: str = None,
        name: str = None,
        num_rows: int = None,
        owner: str = None,
        partitions: int = None,
        partitions_doing: int = None,
        partitions_done: int = None,
        partitions_failed: int = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        tables: int = None,
        tables_doing: int = None,
        tables_done: int = None,
        tables_failed: int = None,
        tables_part_done: int = None,
        update_time: str = None,
        updated: bool = None,
    ):
        self.create_time = create_time
        self.deleted = deleted
        self.description = description
        self.dst_name = dst_name
        self.dst_project_name = dst_project_name
        self.extra = extra
        self.id = id
        # Last DDL Time
        self.last_ddl_time = last_ddl_time
        self.location = location
        self.name = name
        self.num_rows = num_rows
        self.owner = owner
        self.partitions = partitions
        self.partitions_doing = partitions_doing
        self.partitions_done = partitions_done
        self.partitions_failed = partitions_failed
        self.size = size
        self.source_id = source_id
        self.source_name = source_name
        self.status = status
        self.tables = tables
        self.tables_doing = tables_doing
        self.tables_done = tables_done
        self.tables_failed = tables_failed
        self.tables_part_done = tables_part_done
        self.update_time = update_time
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.deleted is not None:
            result['deleted'] = self.deleted

        if self.description is not None:
            result['description'] = self.description

        if self.dst_name is not None:
            result['dstName'] = self.dst_name

        if self.dst_project_name is not None:
            result['dstProjectName'] = self.dst_project_name

        if self.extra is not None:
            result['extra'] = self.extra

        if self.id is not None:
            result['id'] = self.id

        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time

        if self.location is not None:
            result['location'] = self.location

        if self.name is not None:
            result['name'] = self.name

        if self.num_rows is not None:
            result['numRows'] = self.num_rows

        if self.owner is not None:
            result['owner'] = self.owner

        if self.partitions is not None:
            result['partitions'] = self.partitions

        if self.partitions_doing is not None:
            result['partitionsDoing'] = self.partitions_doing

        if self.partitions_done is not None:
            result['partitionsDone'] = self.partitions_done

        if self.partitions_failed is not None:
            result['partitionsFailed'] = self.partitions_failed

        if self.size is not None:
            result['size'] = self.size

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.status is not None:
            result['status'] = self.status

        if self.tables is not None:
            result['tables'] = self.tables

        if self.tables_doing is not None:
            result['tablesDoing'] = self.tables_doing

        if self.tables_done is not None:
            result['tablesDone'] = self.tables_done

        if self.tables_failed is not None:
            result['tablesFailed'] = self.tables_failed

        if self.tables_part_done is not None:
            result['tablesPartDone'] = self.tables_part_done

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('dstName') is not None:
            self.dst_name = m.get('dstName')

        if m.get('dstProjectName') is not None:
            self.dst_project_name = m.get('dstProjectName')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')

        if m.get('partitionsDoing') is not None:
            self.partitions_doing = m.get('partitionsDoing')

        if m.get('partitionsDone') is not None:
            self.partitions_done = m.get('partitionsDone')

        if m.get('partitionsFailed') is not None:
            self.partitions_failed = m.get('partitionsFailed')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tables') is not None:
            self.tables = m.get('tables')

        if m.get('tablesDoing') is not None:
            self.tables_doing = m.get('tablesDoing')

        if m.get('tablesDone') is not None:
            self.tables_done = m.get('tablesDone')

        if m.get('tablesFailed') is not None:
            self.tables_failed = m.get('tablesFailed')

        if m.get('tablesPartDone') is not None:
            self.tables_part_done = m.get('tablesPartDone')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

