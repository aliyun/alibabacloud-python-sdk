# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePlaybookRequest(DaraModel):
    def __init__(
        self,
        debug_flag: int = None,
        lang: str = None,
        playbook_uuid: str = None,
        taskflow_md_5: str = None,
    ):
        # The flag that indicates whether the playbook is of the debugging or published version. Valid values:
        # 
        # *   **1**: playbook of the debugging version
        # *   **0**: playbook of the published version
        self.debug_flag = debug_flag
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The MD5 hash value of the playbook.
        self.taskflow_md_5 = taskflow_md_5

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug_flag is not None:
            result['DebugFlag'] = self.debug_flag

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugFlag') is not None:
            self.debug_flag = m.get('DebugFlag')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')

        return self

