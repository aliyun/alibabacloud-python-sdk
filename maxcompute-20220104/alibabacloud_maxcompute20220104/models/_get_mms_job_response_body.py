# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetMmsJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMmsJobResponseBodyData = None,
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
            temp_model = main_models.GetMmsJobResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMmsJobResponseBodyData(DaraModel):
    def __init__(
        self,
        config: main_models.GetMmsJobResponseBodyDataConfig = None,
        create_time: str = None,
        db_id: int = None,
        dst_db_name: str = None,
        dst_schema_name: str = None,
        eta: str = None,
        id: int = None,
        name: str = None,
        source_id: int = None,
        source_name: str = None,
        src_db_name: str = None,
        src_schema_name: str = None,
        status: str = None,
        stopped: bool = None,
        task_done: int = None,
        task_num: int = None,
        type: str = None,
    ):
        self.config = config
        self.create_time = create_time
        self.db_id = db_id
        self.dst_db_name = dst_db_name
        self.dst_schema_name = dst_schema_name
        self.eta = eta
        self.id = id
        self.name = name
        self.source_id = source_id
        self.source_name = source_name
        self.src_db_name = src_db_name
        self.src_schema_name = src_schema_name
        self.status = status
        self.stopped = stopped
        self.task_done = task_done
        self.task_num = task_num
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.db_id is not None:
            result['dbId'] = self.db_id

        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name

        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name

        if self.eta is not None:
            result['eta'] = self.eta

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_name is not None:
            result['sourceName'] = self.source_name

        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name

        if self.src_schema_name is not None:
            result['srcSchemaName'] = self.src_schema_name

        if self.status is not None:
            result['status'] = self.status

        if self.stopped is not None:
            result['stopped'] = self.stopped

        if self.task_done is not None:
            result['taskDone'] = self.task_done

        if self.task_num is not None:
            result['taskNum'] = self.task_num

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.GetMmsJobResponseBodyDataConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')

        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')

        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')

        if m.get('eta') is not None:
            self.eta = m.get('eta')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')

        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')

        if m.get('srcSchemaName') is not None:
            self.src_schema_name = m.get('srcSchemaName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')

        if m.get('taskDone') is not None:
            self.task_done = m.get('taskDone')

        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetMmsJobResponseBodyDataConfig(DaraModel):
    def __init__(
        self,
        column_mapping: Dict[str, str] = None,
        enable_verification: bool = None,
        increment: bool = None,
        others: Dict[str, Any] = None,
        partition_filters: Dict[str, str] = None,
        partitions: List[int] = None,
        schema_only: bool = None,
        table_black_list: List[str] = None,
        table_mapping: Dict[str, str] = None,
        table_white_list: List[str] = None,
        tables: List[str] = None,
        task_type: str = None,
        tunnel_quota: str = None,
    ):
        self.column_mapping = column_mapping
        self.enable_verification = enable_verification
        self.increment = increment
        self.others = others
        self.partition_filters = partition_filters
        self.partitions = partitions
        self.schema_only = schema_only
        self.table_black_list = table_black_list
        self.table_mapping = table_mapping
        self.table_white_list = table_white_list
        self.tables = tables
        self.task_type = task_type
        self.tunnel_quota = tunnel_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_mapping is not None:
            result['columnMapping'] = self.column_mapping

        if self.enable_verification is not None:
            result['enableVerification'] = self.enable_verification

        if self.increment is not None:
            result['increment'] = self.increment

        if self.others is not None:
            result['others'] = self.others

        if self.partition_filters is not None:
            result['partitionFilters'] = self.partition_filters

        if self.partitions is not None:
            result['partitions'] = self.partitions

        if self.schema_only is not None:
            result['schemaOnly'] = self.schema_only

        if self.table_black_list is not None:
            result['tableBlackList'] = self.table_black_list

        if self.table_mapping is not None:
            result['tableMapping'] = self.table_mapping

        if self.table_white_list is not None:
            result['tableWhiteList'] = self.table_white_list

        if self.tables is not None:
            result['tables'] = self.tables

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnMapping') is not None:
            self.column_mapping = m.get('columnMapping')

        if m.get('enableVerification') is not None:
            self.enable_verification = m.get('enableVerification')

        if m.get('increment') is not None:
            self.increment = m.get('increment')

        if m.get('others') is not None:
            self.others = m.get('others')

        if m.get('partitionFilters') is not None:
            self.partition_filters = m.get('partitionFilters')

        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')

        if m.get('schemaOnly') is not None:
            self.schema_only = m.get('schemaOnly')

        if m.get('tableBlackList') is not None:
            self.table_black_list = m.get('tableBlackList')

        if m.get('tableMapping') is not None:
            self.table_mapping = m.get('tableMapping')

        if m.get('tableWhiteList') is not None:
            self.table_white_list = m.get('tableWhiteList')

        if m.get('tables') is not None:
            self.tables = m.get('tables')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')

        return self

