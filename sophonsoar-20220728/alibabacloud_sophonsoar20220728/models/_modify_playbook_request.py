# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPlaybookRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        lang: str = None,
        playbook_uuid: str = None,
        taskflow: str = None,
    ):
        # The description of the playbook.
        self.description = description
        # The display name of the playbook.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The XML configuration of the playbook.
        self.taskflow = taskflow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')

        return self

