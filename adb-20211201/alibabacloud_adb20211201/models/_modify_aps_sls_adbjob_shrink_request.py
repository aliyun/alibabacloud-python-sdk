# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApsSlsADBJobShrinkRequest(DaraModel):
    def __init__(
        self,
        columns_shrink: str = None,
        dbcluster_id: str = None,
        db_name: str = None,
        dirty_data_process_pattern: str = None,
        exactly_once: str = None,
        password: str = None,
        region_id: str = None,
        starting_offsets: str = None,
        table_name: str = None,
        unix_timestamp_convert: str = None,
        user_name: str = None,
        workload_id: str = None,
        workload_name: str = None,
    ):
        # The information about columns.
        self.columns_shrink = columns_shrink
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.db_name = db_name
        # The dirty data processing mode.
        self.dirty_data_process_pattern = dirty_data_process_pattern
        # Specifies whether to enable the consistency check.
        self.exactly_once = exactly_once
        # The password of the database account.
        self.password = password
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start offset.
        self.starting_offsets = starting_offsets
        # The name of the table.
        self.table_name = table_name
        # The timestamp conversion.
        self.unix_timestamp_convert = unix_timestamp_convert
        # The name of the database account.
        self.user_name = user_name
        # The job ID.
        # 
        # This parameter is required.
        self.workload_id = workload_id
        # The name of the workload.
        self.workload_name = workload_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns_shrink is not None:
            result['Columns'] = self.columns_shrink

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.dirty_data_process_pattern is not None:
            result['DirtyDataProcessPattern'] = self.dirty_data_process_pattern

        if self.exactly_once is not None:
            result['ExactlyOnce'] = self.exactly_once

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.starting_offsets is not None:
            result['StartingOffsets'] = self.starting_offsets

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.unix_timestamp_convert is not None:
            result['UnixTimestampConvert'] = self.unix_timestamp_convert

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns_shrink = m.get('Columns')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DirtyDataProcessPattern') is not None:
            self.dirty_data_process_pattern = m.get('DirtyDataProcessPattern')

        if m.get('ExactlyOnce') is not None:
            self.exactly_once = m.get('ExactlyOnce')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartingOffsets') is not None:
            self.starting_offsets = m.get('StartingOffsets')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UnixTimestampConvert') is not None:
            self.unix_timestamp_convert = m.get('UnixTimestampConvert')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')

        return self

