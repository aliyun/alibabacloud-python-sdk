# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyPlaybookRequest(DaraModel):
    def __init__(
        self,
        playbook_uuid: str = None,
        task_flow: str = None,
    ):
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the playbook UUID.
        self.playbook_uuid = playbook_uuid
        # The XML configuration of the playbook.
        self.task_flow = task_flow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.task_flow is not None:
            result['TaskFlow'] = self.task_flow

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('TaskFlow') is not None:
            self.task_flow = m.get('TaskFlow')

        return self

