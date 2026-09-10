# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecDataCheckSaveTaskRequest(DaraModel):
    def __init__(
        self,
        check_global_params: str = None,
        full_table_count: int = None,
        source_global_params: str = None,
        start_immediately: int = None,
        target_global_params: str = None,
        task_id: int = None,
        total_count_threshold: float = None,
    ):
        # The global parameters for the validation phase. Separate multiple parameters with a line feed (`
        # `).
        self.check_global_params = check_global_params
        # Specifies whether to perform full-table validation. Valid values:
        # 
        # - 0: Partition-level validation. This is the default value.
        # - 1: Full-table validation.
        self.full_table_count = full_table_count
        # The global parameters for the source. Separate multiple parameters with a line feed (`
        # `).
        self.source_global_params = source_global_params
        # Specifies whether to execute immediately after saving. Valid values:
        # 
        # - 0: No. This is the default value.
        # - 1: Yes.
        self.start_immediately = start_immediately
        # The global parameters for the target. Separate multiple parameters with a line feed (`
        # `).
        self.target_global_params = target_global_params
        # The ID of the validation task.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The total data volume comparison threshold, used to determine whether the data volume difference between the source and target is within an acceptable range.
        self.total_count_threshold = total_count_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_global_params is not None:
            result['checkGlobalParams'] = self.check_global_params

        if self.full_table_count is not None:
            result['fullTableCount'] = self.full_table_count

        if self.source_global_params is not None:
            result['sourceGlobalParams'] = self.source_global_params

        if self.start_immediately is not None:
            result['startImmediately'] = self.start_immediately

        if self.target_global_params is not None:
            result['targetGlobalParams'] = self.target_global_params

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.total_count_threshold is not None:
            result['totalCountThreshold'] = self.total_count_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkGlobalParams') is not None:
            self.check_global_params = m.get('checkGlobalParams')

        if m.get('fullTableCount') is not None:
            self.full_table_count = m.get('fullTableCount')

        if m.get('sourceGlobalParams') is not None:
            self.source_global_params = m.get('sourceGlobalParams')

        if m.get('startImmediately') is not None:
            self.start_immediately = m.get('startImmediately')

        if m.get('targetGlobalParams') is not None:
            self.target_global_params = m.get('targetGlobalParams')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('totalCountThreshold') is not None:
            self.total_count_threshold = m.get('totalCountThreshold')

        return self

