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
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The input parameters that you use to debug the playbook. You can define the parameters based on your business requirements.
        self.record = record
        # The XML configuration of the playbook.
        # 
        # >  You can call the [DescribePlaybook](~~DescribePlaybook~~) operation to query the XML configuration of the playbook.
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

