# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlowJobInfo(DaraModel):
    def __init__(
        self,
        display: bool = None,
        job_id: str = None,
        job_type: str = None,
        message_id: str = None,
        process_type: str = None,
        task_id: str = None,
    ):
        # Whether to display. Possible values are:
        # - true: Display.
        # - false: Do not display.
        self.display = display
        # Job ID.
        self.job_id = job_id
        # Task Type. Currently, only DOWNLOWD_MARKRESULT_FLOW is supported.
        self.job_type = job_type
        # Message ID.
        self.message_id = message_id
        # Processing information.
        self.process_type = process_type
        # Job ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.process_type is not None:
            result['ProcessType'] = self.process_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('ProcessType') is not None:
            self.process_type = m.get('ProcessType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

