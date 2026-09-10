# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListDataCheckConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataCheckConfigResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListDataCheckConfigResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListDataCheckConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        algorithm: int = None,
        batch_size: int = None,
        check_type: int = None,
        comparator: str = None,
        extra: str = None,
        group_count_threshold: float = None,
        id: int = None,
        is_full_table_count: int = None,
        is_skipped: int = None,
        metric_type: str = None,
        source_check_all_column: int = None,
        source_columns: str = None,
        source_compare_key: str = None,
        source_data_source: str = None,
        source_group_clause: str = None,
        source_hint: str = None,
        source_id: str = None,
        source_partition: str = None,
        source_sql: str = None,
        source_table: str = None,
        source_type: str = None,
        source_where_clause: str = None,
        target_check_all_column: int = None,
        target_columns: str = None,
        target_compare_key: str = None,
        target_data_source: str = None,
        target_group_clause: str = None,
        target_hint: str = None,
        target_id: str = None,
        target_partition: str = None,
        target_sql: str = None,
        target_table: str = None,
        target_type: str = None,
        target_where_clause: str = None,
        task_config_info: str = None,
        task_id: int = None,
        total_count_threshold: float = None,
    ):
        self.algorithm = algorithm
        self.batch_size = batch_size
        self.check_type = check_type
        self.comparator = comparator
        self.extra = extra
        self.group_count_threshold = group_count_threshold
        self.id = id
        self.is_full_table_count = is_full_table_count
        self.is_skipped = is_skipped
        self.metric_type = metric_type
        self.source_check_all_column = source_check_all_column
        self.source_columns = source_columns
        self.source_compare_key = source_compare_key
        self.source_data_source = source_data_source
        self.source_group_clause = source_group_clause
        self.source_hint = source_hint
        self.source_id = source_id
        self.source_partition = source_partition
        self.source_sql = source_sql
        self.source_table = source_table
        self.source_type = source_type
        self.source_where_clause = source_where_clause
        self.target_check_all_column = target_check_all_column
        self.target_columns = target_columns
        self.target_compare_key = target_compare_key
        self.target_data_source = target_data_source
        self.target_group_clause = target_group_clause
        self.target_hint = target_hint
        self.target_id = target_id
        self.target_partition = target_partition
        self.target_sql = target_sql
        self.target_table = target_table
        self.target_type = target_type
        self.target_where_clause = target_where_clause
        self.task_config_info = task_config_info
        self.task_id = task_id
        self.total_count_threshold = total_count_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm

        if self.batch_size is not None:
            result['batchSize'] = self.batch_size

        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.comparator is not None:
            result['comparator'] = self.comparator

        if self.extra is not None:
            result['extra'] = self.extra

        if self.group_count_threshold is not None:
            result['groupCountThreshold'] = self.group_count_threshold

        if self.id is not None:
            result['id'] = self.id

        if self.is_full_table_count is not None:
            result['isFullTableCount'] = self.is_full_table_count

        if self.is_skipped is not None:
            result['isSkipped'] = self.is_skipped

        if self.metric_type is not None:
            result['metricType'] = self.metric_type

        if self.source_check_all_column is not None:
            result['sourceCheckAllColumn'] = self.source_check_all_column

        if self.source_columns is not None:
            result['sourceColumns'] = self.source_columns

        if self.source_compare_key is not None:
            result['sourceCompareKey'] = self.source_compare_key

        if self.source_data_source is not None:
            result['sourceDataSource'] = self.source_data_source

        if self.source_group_clause is not None:
            result['sourceGroupClause'] = self.source_group_clause

        if self.source_hint is not None:
            result['sourceHint'] = self.source_hint

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_partition is not None:
            result['sourcePartition'] = self.source_partition

        if self.source_sql is not None:
            result['sourceSql'] = self.source_sql

        if self.source_table is not None:
            result['sourceTable'] = self.source_table

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.source_where_clause is not None:
            result['sourceWhereClause'] = self.source_where_clause

        if self.target_check_all_column is not None:
            result['targetCheckAllColumn'] = self.target_check_all_column

        if self.target_columns is not None:
            result['targetColumns'] = self.target_columns

        if self.target_compare_key is not None:
            result['targetCompareKey'] = self.target_compare_key

        if self.target_data_source is not None:
            result['targetDataSource'] = self.target_data_source

        if self.target_group_clause is not None:
            result['targetGroupClause'] = self.target_group_clause

        if self.target_hint is not None:
            result['targetHint'] = self.target_hint

        if self.target_id is not None:
            result['targetId'] = self.target_id

        if self.target_partition is not None:
            result['targetPartition'] = self.target_partition

        if self.target_sql is not None:
            result['targetSql'] = self.target_sql

        if self.target_table is not None:
            result['targetTable'] = self.target_table

        if self.target_type is not None:
            result['targetType'] = self.target_type

        if self.target_where_clause is not None:
            result['targetWhereClause'] = self.target_where_clause

        if self.task_config_info is not None:
            result['taskConfigInfo'] = self.task_config_info

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.total_count_threshold is not None:
            result['totalCountThreshold'] = self.total_count_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')

        if m.get('batchSize') is not None:
            self.batch_size = m.get('batchSize')

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('comparator') is not None:
            self.comparator = m.get('comparator')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('groupCountThreshold') is not None:
            self.group_count_threshold = m.get('groupCountThreshold')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isFullTableCount') is not None:
            self.is_full_table_count = m.get('isFullTableCount')

        if m.get('isSkipped') is not None:
            self.is_skipped = m.get('isSkipped')

        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')

        if m.get('sourceCheckAllColumn') is not None:
            self.source_check_all_column = m.get('sourceCheckAllColumn')

        if m.get('sourceColumns') is not None:
            self.source_columns = m.get('sourceColumns')

        if m.get('sourceCompareKey') is not None:
            self.source_compare_key = m.get('sourceCompareKey')

        if m.get('sourceDataSource') is not None:
            self.source_data_source = m.get('sourceDataSource')

        if m.get('sourceGroupClause') is not None:
            self.source_group_clause = m.get('sourceGroupClause')

        if m.get('sourceHint') is not None:
            self.source_hint = m.get('sourceHint')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourcePartition') is not None:
            self.source_partition = m.get('sourcePartition')

        if m.get('sourceSql') is not None:
            self.source_sql = m.get('sourceSql')

        if m.get('sourceTable') is not None:
            self.source_table = m.get('sourceTable')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('sourceWhereClause') is not None:
            self.source_where_clause = m.get('sourceWhereClause')

        if m.get('targetCheckAllColumn') is not None:
            self.target_check_all_column = m.get('targetCheckAllColumn')

        if m.get('targetColumns') is not None:
            self.target_columns = m.get('targetColumns')

        if m.get('targetCompareKey') is not None:
            self.target_compare_key = m.get('targetCompareKey')

        if m.get('targetDataSource') is not None:
            self.target_data_source = m.get('targetDataSource')

        if m.get('targetGroupClause') is not None:
            self.target_group_clause = m.get('targetGroupClause')

        if m.get('targetHint') is not None:
            self.target_hint = m.get('targetHint')

        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')

        if m.get('targetPartition') is not None:
            self.target_partition = m.get('targetPartition')

        if m.get('targetSql') is not None:
            self.target_sql = m.get('targetSql')

        if m.get('targetTable') is not None:
            self.target_table = m.get('targetTable')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('targetWhereClause') is not None:
            self.target_where_clause = m.get('targetWhereClause')

        if m.get('taskConfigInfo') is not None:
            self.task_config_info = m.get('taskConfigInfo')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('totalCountThreshold') is not None:
            self.total_count_threshold = m.get('totalCountThreshold')

        return self

