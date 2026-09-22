# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MarkOssV2ResultRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        freeze_type: str = None,
        operation: str = None,
        request_ids: str = None,
        start_date: str = None,
        task_name: str = None,
    ):
        # The end time. The time format is YYYY-MM-DD HH:mm:ss.
        self.end_date = end_date
        # The freeze type. This parameter is required when Operation is set to freeze. Valid values:
        # - ACL: Modify file permissions.
        # - COPY: Move the file directory. Description of the destination directory: 1. The file directory selected when the task was created takes priority. 2. If automatic freezing was not enabled during creation, or ACL freezing was configured, the directory selected during freezing in the console is used. 3. The default directory is alicip_riskfile_backup/.
        self.freeze_type = freeze_type
        # The processing operation. Valid values:
        # 
        # - freeze: Freeze.
        # - unfreeze: Unfreeze.
        # - misreport: Non-violation false positive.
        # - missOut: Violation missed.
        self.operation = operation
        # The request ID.
        self.request_ids = request_ids
        # The start time. The time format is YYYY-MM-DD HH:mm:ss.
        self.start_date = start_date
        # The task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.freeze_type is not None:
            result['FreezeType'] = self.freeze_type

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.request_ids is not None:
            result['RequestIds'] = self.request_ids

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('FreezeType') is not None:
            self.freeze_type = m.get('FreezeType')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('RequestIds') is not None:
            self.request_ids = m.get('RequestIds')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

