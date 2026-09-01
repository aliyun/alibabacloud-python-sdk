# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DebugPlaybookRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
        record: str = None,
        taskflow: str = None,
    ):
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The UUID of the playbook.
        # 
        # > Call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The user-defined input parameters for debugging the playbook.
        self.record = record
        # The XML configuration of the playbook.
        # 
        # > Call the [DescribePlaybook](~~DescribePlaybook~~) operation to obtain this configuration.
        # 
        # This parameter is required.
        self.taskflow = taskflow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.record is not None:
            result['Record'] = self.record

        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('Record') is not None:
            self.record = m.get('Record')

        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')

        return self

