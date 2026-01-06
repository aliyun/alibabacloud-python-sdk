# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSqlConcurrencyControlKeywordsFromSqlTextRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        sql_text: str = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The SQL statement based on which a throttling keyword string is to be generated.
        # 
        # This parameter is required.
        self.sql_text = sql_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        return self

