# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetQueryOptimizeDataStatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQueryOptimizeDataStatsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetQueryOptimizeDataStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQueryOptimizeDataStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        extra: str = None,
        list: List[main_models.GetQueryOptimizeDataStatsResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The reserved parameter.
        self.extra = extra
        # The information about the SQL templates.
        self.list = list
        # The reserved parameter.
        self.page_no = page_no
        # The reserved parameter.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetQueryOptimizeDataStatsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetQueryOptimizeDataStatsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        avg_lock_time: float = None,
        avg_query_time: float = None,
        avg_rows_affected: float = None,
        avg_rows_examined: float = None,
        avg_rows_sent: float = None,
        count: int = None,
        dbname: str = None,
        instance_id: str = None,
        max_lock_time: float = None,
        max_query_time: float = None,
        max_rows_affected: int = None,
        max_rows_examined: int = None,
        max_rows_sent: int = None,
        psql: str = None,
        rule_list: List[main_models.GetQueryOptimizeDataStatsResponseBodyDataListRuleList] = None,
        sql_id: str = None,
        sql_sample: str = None,
        sql_type: str = None,
        user: str = None,
    ):
        # The average lock wait time. Unit: seconds.
        self.avg_lock_time = avg_lock_time
        # The average query execution time. Unit: seconds.
        self.avg_query_time = avg_query_time
        # The average number of rows affected by the SQL statement.
        # 
        # > A value of -1 indicates that this parameter is not collected.
        self.avg_rows_affected = avg_rows_affected
        # The average number of scanned rows.
        self.avg_rows_examined = avg_rows_examined
        # The average number of returned rows.
        self.avg_rows_sent = avg_rows_sent
        # The number of times that the SQL template is executed.
        self.count = count
        # The name of the database to which the SQL template belongs.
        self.dbname = dbname
        # The instance ID.
        self.instance_id = instance_id
        # The longest lock wait time. Unit: seconds.
        self.max_lock_time = max_lock_time
        # The longest query execution time. Unit: seconds.
        self.max_query_time = max_query_time
        # The largest number of rows affected by the SQL template.
        # 
        # > A value of -1 indicates that this parameter is not collected.
        self.max_rows_affected = max_rows_affected
        # The largest number of scanned rows.
        self.max_rows_examined = max_rows_examined
        # The largest number of returned rows.
        self.max_rows_sent = max_rows_sent
        # The SQL template.
        self.psql = psql
        # The information about the rules.
        self.rule_list = rule_list
        # The SQL template ID.
        self.sql_id = sql_id
        # The sample query that took the longest time to execute.
        self.sql_sample = sql_sample
        # The type of the SQL statement.
        self.sql_type = sql_type
        # The account of the database.
        self.user = user

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_lock_time is not None:
            result['AvgLockTime'] = self.avg_lock_time

        if self.avg_query_time is not None:
            result['AvgQueryTime'] = self.avg_query_time

        if self.avg_rows_affected is not None:
            result['AvgRowsAffected'] = self.avg_rows_affected

        if self.avg_rows_examined is not None:
            result['AvgRowsExamined'] = self.avg_rows_examined

        if self.avg_rows_sent is not None:
            result['AvgRowsSent'] = self.avg_rows_sent

        if self.count is not None:
            result['Count'] = self.count

        if self.dbname is not None:
            result['Dbname'] = self.dbname

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_lock_time is not None:
            result['MaxLockTime'] = self.max_lock_time

        if self.max_query_time is not None:
            result['MaxQueryTime'] = self.max_query_time

        if self.max_rows_affected is not None:
            result['MaxRowsAffected'] = self.max_rows_affected

        if self.max_rows_examined is not None:
            result['MaxRowsExamined'] = self.max_rows_examined

        if self.max_rows_sent is not None:
            result['MaxRowsSent'] = self.max_rows_sent

        if self.psql is not None:
            result['Psql'] = self.psql

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_sample is not None:
            result['SqlSample'] = self.sql_sample

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgLockTime') is not None:
            self.avg_lock_time = m.get('AvgLockTime')

        if m.get('AvgQueryTime') is not None:
            self.avg_query_time = m.get('AvgQueryTime')

        if m.get('AvgRowsAffected') is not None:
            self.avg_rows_affected = m.get('AvgRowsAffected')

        if m.get('AvgRowsExamined') is not None:
            self.avg_rows_examined = m.get('AvgRowsExamined')

        if m.get('AvgRowsSent') is not None:
            self.avg_rows_sent = m.get('AvgRowsSent')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxLockTime') is not None:
            self.max_lock_time = m.get('MaxLockTime')

        if m.get('MaxQueryTime') is not None:
            self.max_query_time = m.get('MaxQueryTime')

        if m.get('MaxRowsAffected') is not None:
            self.max_rows_affected = m.get('MaxRowsAffected')

        if m.get('MaxRowsExamined') is not None:
            self.max_rows_examined = m.get('MaxRowsExamined')

        if m.get('MaxRowsSent') is not None:
            self.max_rows_sent = m.get('MaxRowsSent')

        if m.get('Psql') is not None:
            self.psql = m.get('Psql')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.GetQueryOptimizeDataStatsResponseBodyDataListRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlSample') is not None:
            self.sql_sample = m.get('SqlSample')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class GetQueryOptimizeDataStatsResponseBodyDataListRuleList(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The rule name.
        self.name = name
        # The type of the rule. Valid values:
        # 
        # * **Predefined**
        # * **UserDefined**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

