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
        # The end time. Specify the time in the YYYY-MM-DD HH:mm:ss format.
        self.end_date = end_date
        # The freeze type. This parameter is required when Operation is set to freeze. Valid values:
        # - ACL: Modifies file permissions.
        # - COPY: Moves the file directory. Destination directory rules: 1. The file directory selected during task creation takes precedence. 2. If automatic freezing is not enabled during creation, or if ACL freezing is configured, the directory selected in the console during freezing is used. 3. The default directory is alicip_riskfile_backup/.
        self.freeze_type = freeze_type
        # The handling operation. Valid values:
        # - freeze: Freezes the object.
        # - unfreeze: Unfreezes the object.
        # - misreport: Reports a false positive.
        # - missOut: Reports a missed violation.
        self.operation = operation
        # The request IDs.
        self.request_ids = request_ids
        # The start time. Specify the time in the YYYY-MM-DD HH:mm:ss format.
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

