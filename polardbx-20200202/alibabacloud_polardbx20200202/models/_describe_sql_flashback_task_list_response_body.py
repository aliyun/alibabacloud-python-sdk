# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlFlashbackTaskListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSqlFlashbackTaskListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
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
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSqlFlashbackTaskListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSqlFlashbackTaskListResponseBodyData(DaraModel):
    def __init__(
        self,
        sql_flashback_tasks: List[main_models.DescribeSqlFlashbackTaskListResponseBodyDataSqlFlashbackTasks] = None,
    ):
        self.sql_flashback_tasks = sql_flashback_tasks

    def validate(self):
        if self.sql_flashback_tasks:
            for v1 in self.sql_flashback_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SqlFlashbackTasks'] = []
        if self.sql_flashback_tasks is not None:
            for k1 in self.sql_flashback_tasks:
                result['SqlFlashbackTasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sql_flashback_tasks = []
        if m.get('SqlFlashbackTasks') is not None:
            for k1 in m.get('SqlFlashbackTasks'):
                temp_model = main_models.DescribeSqlFlashbackTaskListResponseBodyDataSqlFlashbackTasks()
                self.sql_flashback_tasks.append(temp_model.from_map(k1))

        return self

class DescribeSqlFlashbackTaskListResponseBodyDataSqlFlashbackTasks(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        download_url: str = None,
        expire_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        inst_id: str = None,
        recall_progress: str = None,
        recall_restore_type: str = None,
        recall_status: str = None,
        recall_type: str = None,
        search_end_time: str = None,
        search_start_time: str = None,
        sql_counter: str = None,
        sql_pk: str = None,
        sql_type: str = None,
        table_name: str = None,
        trace_id: str = None,
    ):
        self.db_name = db_name
        self.download_url = download_url
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.inst_id = inst_id
        self.recall_progress = recall_progress
        self.recall_restore_type = recall_restore_type
        self.recall_status = recall_status
        self.recall_type = recall_type
        self.search_end_time = search_end_time
        self.search_start_time = search_start_time
        self.sql_counter = sql_counter
        self.sql_pk = sql_pk
        self.sql_type = sql_type
        self.table_name = table_name
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.inst_id is not None:
            result['InstId'] = self.inst_id

        if self.recall_progress is not None:
            result['RecallProgress'] = self.recall_progress

        if self.recall_restore_type is not None:
            result['RecallRestoreType'] = self.recall_restore_type

        if self.recall_status is not None:
            result['RecallStatus'] = self.recall_status

        if self.recall_type is not None:
            result['RecallType'] = self.recall_type

        if self.search_end_time is not None:
            result['SearchEndTime'] = self.search_end_time

        if self.search_start_time is not None:
            result['SearchStartTime'] = self.search_start_time

        if self.sql_counter is not None:
            result['SqlCounter'] = self.sql_counter

        if self.sql_pk is not None:
            result['SqlPk'] = self.sql_pk

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstId') is not None:
            self.inst_id = m.get('InstId')

        if m.get('RecallProgress') is not None:
            self.recall_progress = m.get('RecallProgress')

        if m.get('RecallRestoreType') is not None:
            self.recall_restore_type = m.get('RecallRestoreType')

        if m.get('RecallStatus') is not None:
            self.recall_status = m.get('RecallStatus')

        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')

        if m.get('SearchEndTime') is not None:
            self.search_end_time = m.get('SearchEndTime')

        if m.get('SearchStartTime') is not None:
            self.search_start_time = m.get('SearchStartTime')

        if m.get('SqlCounter') is not None:
            self.sql_counter = m.get('SqlCounter')

        if m.get('SqlPk') is not None:
            self.sql_pk = m.get('SqlPk')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

