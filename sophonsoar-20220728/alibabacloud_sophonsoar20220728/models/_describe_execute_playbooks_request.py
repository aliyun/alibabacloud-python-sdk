# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExecutePlaybooksRequest(DaraModel):
    def __init__(
        self,
        input_mode: str = None,
        lang: str = None,
        param_type: str = None,
        playbook_name: str = None,
        uuid: str = None,
    ):
        # The entity type of the script input parameter. When you want to query multiple entity types, separate them with commas.
        # - **ip**: IP entity.
        # - **file**: file entity.
        # - **process**: process entity.
        # - **incident**: incident entity.
        self.input_mode = input_mode
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The input parameter type of the playbook.
        # 
        # *   **template-ip**
        # *   **template-file**
        # *   **template-process**
        # *   **custom**
        self.param_type = param_type
        # The playbook name. Fuzzy search is supported.
        self.playbook_name = playbook_name
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the playbook UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_mode is not None:
            result['InputMode'] = self.input_mode

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputMode') is not None:
            self.input_mode = m.get('InputMode')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

