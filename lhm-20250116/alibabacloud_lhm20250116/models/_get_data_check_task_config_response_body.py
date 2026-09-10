# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetDataCheckTaskConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataCheckTaskConfigResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data body returned by the operation. For the field structure, see the descriptions of child fields.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success. A value of false indicates failure. If the call fails, check errCode and errMessage for troubleshooting.
        self.success = success

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

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetDataCheckTaskConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetDataCheckTaskConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        check_global_params: str = None,
        check_template_id: str = None,
        check_type: int = None,
        concurrency: int = None,
        cron_exp: str = None,
        data_check_config: List[main_models.GetDataCheckTaskConfigResponseBodyDataDataCheckConfig] = None,
        dst_ds_id: str = None,
        dst_ds_name: str = None,
        dst_ds_type: str = None,
        dst_engine_id: str = None,
        dst_engine_name: str = None,
        dst_engine_type: str = None,
        execute_type: int = None,
        full_table_count: int = None,
        group_count_threshold: float = None,
        is_builtin: int = None,
        is_scheduled: int = None,
        is_white_list: int = None,
        request_id: str = None,
        schedule_id: int = None,
        scope_filter: main_models.GetDataCheckTaskConfigResponseBodyDataScopeFilter = None,
        source_global_params: str = None,
        src_ds_id: str = None,
        src_ds_name: str = None,
        src_ds_type: str = None,
        src_engine_id: str = None,
        src_engine_name: str = None,
        src_engine_type: str = None,
        start_immediately: int = None,
        target_global_params: str = None,
        task_config_info: str = None,
        task_description: str = None,
        task_id: int = None,
        task_mode: int = None,
        task_name: str = None,
        template_name: str = None,
        tenant_id: str = None,
        total_count_threshold: float = None,
        uid: str = None,
    ):
        # The batch ID that uniquely identifies a data validation batch.
        self.batch_id = batch_id
        # The global node parameter settings (built-in configuration of the data validation service).
        self.check_global_params = check_global_params
        # The validation template ID.
        self.check_template_id = check_template_id
        # The validation rule type. Valid values:
        # - 0: data volume comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        # - 3: custom comparison.
        # - 4: full-text comparison.
        # - 5: null value ratio comparison.
        self.check_type = check_type
        # The batch concurrency.
        self.concurrency = concurrency
        # The scheduling cycle expression (cron expression).
        self.cron_exp = cron_exp
        # The task configuration table.
        self.data_check_config = data_check_config
        # The destination data source ID.
        self.dst_ds_id = dst_ds_id
        # The destination data source name.
        self.dst_ds_name = dst_ds_name
        # The destination data source type.
        self.dst_ds_type = dst_ds_type
        # The ID of the destination verification engine.
        self.dst_engine_id = dst_engine_id
        # The name of the destination verification engine.
        self.dst_engine_name = dst_engine_name
        # The type of the destination verification engine.
        self.dst_engine_type = dst_engine_type
        # The execution type. Valid values:
        # - 0: immediate execution
        # - 1: scheduled execution
        self.execute_type = execute_type
        # The count mode. Valid values:
        # - 0: count by partition
        # - 1: count the entire table
        self.full_table_count = full_table_count
        # The group data volume comparison threshold.
        self.group_count_threshold = group_count_threshold
        # Indicates whether the template is a built-in template. Valid values:
        # - 0: No.
        # - 1: Yes.
        self.is_builtin = is_builtin
        # Indicates whether scheduling is enabled. Valid values:
        # - 0: No.
        # - 1: Yes.
        self.is_scheduled = is_scheduled
        # Indicates whether the task is on the whitelist. Valid values:
        # - 0: No.
        # - 1: Yes.
        self.is_white_list = is_white_list
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the scheduled task (scheduling ID).
        self.schedule_id = schedule_id
        # The scope filter JSON data.
        self.scope_filter = scope_filter
        # The source node parameter settings (source execute parameters).
        self.source_global_params = source_global_params
        # The ID of the source data source.
        self.src_ds_id = src_ds_id
        # The name of the source data source.
        self.src_ds_name = src_ds_name
        # The type of the source data source.
        self.src_ds_type = src_ds_type
        # The ID of the source verification engine.
        self.src_engine_id = src_engine_id
        # The name of the source verification engine.
        self.src_engine_name = src_engine_name
        # The type of the source verification engine.
        self.src_engine_type = src_engine_type
        # Indicates whether to start the task immediately. Valid values:
        # - 0: No.
        # - 1: Yes.
        self.start_immediately = start_immediately
        # The destination node parameter settings (destination execute parameters).
        self.target_global_params = target_global_params
        # The regular expression information of the verification task.
        self.task_config_info = task_config_info
        # The task description.
        self.task_description = task_description
        # The task ID, which uniquely identifies a task.
        self.task_id = task_id
        # The parameter creation mode. Valid values:
        # - 0: fine-grained creation on a per-table basis
        # - 1: batch creation with the same pattern
        self.task_mode = task_mode
        # The task name. When used as a query condition, fuzzy matching with % is supported (SQL syntax).
        self.task_name = task_name
        # The name of the verification template.
        self.template_name = template_name
        # The tenant ID.
        self.tenant_id = tenant_id
        # The total data volume comparison threshold.
        self.total_count_threshold = total_count_threshold
        # The user ID.
        self.uid = uid

    def validate(self):
        if self.data_check_config:
            for v1 in self.data_check_config:
                 if v1:
                    v1.validate()
        if self.scope_filter:
            self.scope_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.check_global_params is not None:
            result['checkGlobalParams'] = self.check_global_params

        if self.check_template_id is not None:
            result['checkTemplateId'] = self.check_template_id

        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.concurrency is not None:
            result['concurrency'] = self.concurrency

        if self.cron_exp is not None:
            result['cronExp'] = self.cron_exp

        result['dataCheckConfig'] = []
        if self.data_check_config is not None:
            for k1 in self.data_check_config:
                result['dataCheckConfig'].append(k1.to_map() if k1 else None)

        if self.dst_ds_id is not None:
            result['dstDsId'] = self.dst_ds_id

        if self.dst_ds_name is not None:
            result['dstDsName'] = self.dst_ds_name

        if self.dst_ds_type is not None:
            result['dstDsType'] = self.dst_ds_type

        if self.dst_engine_id is not None:
            result['dstEngineId'] = self.dst_engine_id

        if self.dst_engine_name is not None:
            result['dstEngineName'] = self.dst_engine_name

        if self.dst_engine_type is not None:
            result['dstEngineType'] = self.dst_engine_type

        if self.execute_type is not None:
            result['executeType'] = self.execute_type

        if self.full_table_count is not None:
            result['fullTableCount'] = self.full_table_count

        if self.group_count_threshold is not None:
            result['groupCountThreshold'] = self.group_count_threshold

        if self.is_builtin is not None:
            result['isBuiltin'] = self.is_builtin

        if self.is_scheduled is not None:
            result['isScheduled'] = self.is_scheduled

        if self.is_white_list is not None:
            result['isWhiteList'] = self.is_white_list

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schedule_id is not None:
            result['scheduleId'] = self.schedule_id

        if self.scope_filter is not None:
            result['scopeFilter'] = self.scope_filter.to_map()

        if self.source_global_params is not None:
            result['sourceGlobalParams'] = self.source_global_params

        if self.src_ds_id is not None:
            result['srcDsId'] = self.src_ds_id

        if self.src_ds_name is not None:
            result['srcDsName'] = self.src_ds_name

        if self.src_ds_type is not None:
            result['srcDsType'] = self.src_ds_type

        if self.src_engine_id is not None:
            result['srcEngineId'] = self.src_engine_id

        if self.src_engine_name is not None:
            result['srcEngineName'] = self.src_engine_name

        if self.src_engine_type is not None:
            result['srcEngineType'] = self.src_engine_type

        if self.start_immediately is not None:
            result['startImmediately'] = self.start_immediately

        if self.target_global_params is not None:
            result['targetGlobalParams'] = self.target_global_params

        if self.task_config_info is not None:
            result['taskConfigInfo'] = self.task_config_info

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_mode is not None:
            result['taskMode'] = self.task_mode

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.total_count_threshold is not None:
            result['totalCountThreshold'] = self.total_count_threshold

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('checkGlobalParams') is not None:
            self.check_global_params = m.get('checkGlobalParams')

        if m.get('checkTemplateId') is not None:
            self.check_template_id = m.get('checkTemplateId')

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')

        if m.get('cronExp') is not None:
            self.cron_exp = m.get('cronExp')

        self.data_check_config = []
        if m.get('dataCheckConfig') is not None:
            for k1 in m.get('dataCheckConfig'):
                temp_model = main_models.GetDataCheckTaskConfigResponseBodyDataDataCheckConfig()
                self.data_check_config.append(temp_model.from_map(k1))

        if m.get('dstDsId') is not None:
            self.dst_ds_id = m.get('dstDsId')

        if m.get('dstDsName') is not None:
            self.dst_ds_name = m.get('dstDsName')

        if m.get('dstDsType') is not None:
            self.dst_ds_type = m.get('dstDsType')

        if m.get('dstEngineId') is not None:
            self.dst_engine_id = m.get('dstEngineId')

        if m.get('dstEngineName') is not None:
            self.dst_engine_name = m.get('dstEngineName')

        if m.get('dstEngineType') is not None:
            self.dst_engine_type = m.get('dstEngineType')

        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')

        if m.get('fullTableCount') is not None:
            self.full_table_count = m.get('fullTableCount')

        if m.get('groupCountThreshold') is not None:
            self.group_count_threshold = m.get('groupCountThreshold')

        if m.get('isBuiltin') is not None:
            self.is_builtin = m.get('isBuiltin')

        if m.get('isScheduled') is not None:
            self.is_scheduled = m.get('isScheduled')

        if m.get('isWhiteList') is not None:
            self.is_white_list = m.get('isWhiteList')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scheduleId') is not None:
            self.schedule_id = m.get('scheduleId')

        if m.get('scopeFilter') is not None:
            temp_model = main_models.GetDataCheckTaskConfigResponseBodyDataScopeFilter()
            self.scope_filter = temp_model.from_map(m.get('scopeFilter'))

        if m.get('sourceGlobalParams') is not None:
            self.source_global_params = m.get('sourceGlobalParams')

        if m.get('srcDsId') is not None:
            self.src_ds_id = m.get('srcDsId')

        if m.get('srcDsName') is not None:
            self.src_ds_name = m.get('srcDsName')

        if m.get('srcDsType') is not None:
            self.src_ds_type = m.get('srcDsType')

        if m.get('srcEngineId') is not None:
            self.src_engine_id = m.get('srcEngineId')

        if m.get('srcEngineName') is not None:
            self.src_engine_name = m.get('srcEngineName')

        if m.get('srcEngineType') is not None:
            self.src_engine_type = m.get('srcEngineType')

        if m.get('startImmediately') is not None:
            self.start_immediately = m.get('startImmediately')

        if m.get('targetGlobalParams') is not None:
            self.target_global_params = m.get('targetGlobalParams')

        if m.get('taskConfigInfo') is not None:
            self.task_config_info = m.get('taskConfigInfo')

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskMode') is not None:
            self.task_mode = m.get('taskMode')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('totalCountThreshold') is not None:
            self.total_count_threshold = m.get('totalCountThreshold')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

class GetDataCheckTaskConfigResponseBodyDataScopeFilter(DaraModel):
    def __init__(
        self,
        end: str = None,
        last_n: int = None,
        scope_filter_type: int = None,
        start: str = None,
    ):
        # The end time.
        self.end = end
        # The last N parameter.
        self.last_n = last_n
        # The filter type.
        self.scope_filter_type = scope_filter_type
        # The start time.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['end'] = self.end

        if self.last_n is not None:
            result['lastN'] = self.last_n

        if self.scope_filter_type is not None:
            result['scopeFilterType'] = self.scope_filter_type

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('lastN') is not None:
            self.last_n = m.get('lastN')

        if m.get('scopeFilterType') is not None:
            self.scope_filter_type = m.get('scopeFilterType')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

class GetDataCheckTaskConfigResponseBodyDataDataCheckConfig(DaraModel):
    def __init__(
        self,
        algorithm: int = None,
        batch_id: int = None,
        batch_size: int = None,
        check_type: int = None,
        comparator: str = None,
        extra: Any = None,
        group_count_threshold: float = None,
        id: int = None,
        is_full_table_count: int = None,
        is_skipped: int = None,
        metric_type: str = None,
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
        task_config_id: int = None,
        task_config_info: str = None,
        token: str = None,
        total_count_threshold: float = None,
    ):
        # The validation algorithm.
        self.algorithm = algorithm
        # The batch ID.
        self.batch_id = batch_id
        # The batch size.
        self.batch_size = batch_size
        # The validation rule type. Valid values:
        # - 0: data volume comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        # - 3: custom comparison.
        # - 4: full-text comparison.
        # - 5: null value ratio comparison.
        self.check_type = check_type
        # The comparison type. Valid values: =, !=, >, <, >=, <=, contains, does not contain, and ==.
        self.comparator = comparator
        # The reserved field.
        self.extra = extra
        # The group data volume comparison threshold.
        self.group_count_threshold = group_count_threshold
        # The primary key ID.
        self.id = id
        # Specifies whether to perform a full table count.
        self.is_full_table_count = is_full_table_count
        # Specifies whether to skip the task. Valid values:
        # - 0: No.
        # - 1: Yes.
        self.is_skipped = is_skipped
        # The metric type. Valid values:
        # - CUSTOM_METRIC_NUM: built-in NUM mode.
        # - CUSTOM_METRIC_LEN: built-in LEN mode.
        # - CUSTOM_METRIC_MIX: built-in MIX mode.
        self.metric_type = metric_type
        # The source table columns. You can specify multiple columns separated by commas (,).
        self.source_columns = source_columns
        # The source comparison key (the key field used for data comparison between the source and destination).
        self.source_compare_key = source_compare_key
        # The source data source name.
        self.source_data_source = source_data_source
        # The GROUP BY clause for the source table.
        self.source_group_clause = source_group_clause
        self.source_hint = source_hint
        # The source data source ID.
        self.source_id = source_id
        # The source partition.
        self.source_partition = source_partition
        # The source SQL statement.
        self.source_sql = source_sql
        # The source table.
        self.source_table = source_table
        # The source data source type.
        self.source_type = source_type
        # The WHERE clause for the source table.
        self.source_where_clause = source_where_clause
        # The destination table columns. You can specify multiple columns separated by commas (,).
        self.target_columns = target_columns
        # The destination comparison key (the key field used for data comparison between the source and destination).
        self.target_compare_key = target_compare_key
        # The destination data source.
        self.target_data_source = target_data_source
        # The GROUP BY clause for the destination table.
        self.target_group_clause = target_group_clause
        self.target_hint = target_hint
        # The destination ID.
        self.target_id = target_id
        # The destination partition.
        self.target_partition = target_partition
        # The destination SQL statement.
        self.target_sql = target_sql
        # The destination table.
        self.target_table = target_table
        # The destination data source type.
        self.target_type = target_type
        # The WHERE clause for the destination table.
        self.target_where_clause = target_where_clause
        # The validation task configuration ID.
        self.task_config_id = task_config_id
        # The validation task configuration information (regular expression matching rules). This parameter takes effect only when taskMode is set to 1.
        self.task_config_info = task_config_info
        # The validation batch token. Together with batchId, it identifies the result records generated by a validation batch.
        self.token = token
        # The total data volume comparison threshold.
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

        if self.batch_id is not None:
            result['batchId'] = self.batch_id

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

        if self.task_config_id is not None:
            result['taskConfigId'] = self.task_config_id

        if self.task_config_info is not None:
            result['taskConfigInfo'] = self.task_config_info

        if self.token is not None:
            result['token'] = self.token

        if self.total_count_threshold is not None:
            result['totalCountThreshold'] = self.total_count_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')

        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

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

        if m.get('taskConfigId') is not None:
            self.task_config_id = m.get('taskConfigId')

        if m.get('taskConfigInfo') is not None:
            self.task_config_info = m.get('taskConfigInfo')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('totalCountThreshold') is not None:
            self.total_count_threshold = m.get('totalCountThreshold')

        return self

