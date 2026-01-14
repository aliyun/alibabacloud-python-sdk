# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMailTaskStatusRequest(DaraModel):
    def __init__(
        self,
        mail_id: str = None,
        task_id: int = None,
    ):
        # Mail ID
        # 
        # This parameter is required.
        self.mail_id = mail_id
        # Task ID
        # 
        # > - If the task ID is not provided, the latest task status will be returned by default;
        # > - If the task ID is provided, the status of the specified task will be returned.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mail_id is not None:
            result['MailId'] = self.mail_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailId') is not None:
            self.mail_id = m.get('MailId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

