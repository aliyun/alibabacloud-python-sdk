# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSqlFlashbackTaskRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        end_time: str = None,
        polardbx_instance_id: str = None,
        recall_restore_type: str = None,
        recall_type: str = None,
        region_id: str = None,
        sql_pk: str = None,
        sql_type: str = None,
        start_time: str = None,
        table_name: str = None,
        trace_id: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.polardbx_instance_id = polardbx_instance_id
        # This parameter is required.
        self.recall_restore_type = recall_restore_type
        self.recall_type = recall_type
        # This parameter is required.
        self.region_id = region_id
        self.sql_pk = sql_pk
        self.sql_type = sql_type
        # This parameter is required.
        self.start_time = start_time
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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.polardbx_instance_id is not None:
            result['PolardbxInstanceId'] = self.polardbx_instance_id

        if self.recall_restore_type is not None:
            result['RecallRestoreType'] = self.recall_restore_type

        if self.recall_type is not None:
            result['RecallType'] = self.recall_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sql_pk is not None:
            result['SqlPk'] = self.sql_pk

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PolardbxInstanceId') is not None:
            self.polardbx_instance_id = m.get('PolardbxInstanceId')

        if m.get('RecallRestoreType') is not None:
            self.recall_restore_type = m.get('RecallRestoreType')

        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SqlPk') is not None:
            self.sql_pk = m.get('SqlPk')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

