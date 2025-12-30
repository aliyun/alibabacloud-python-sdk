# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatBIPatternIndexDeleteRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        instance_name: str = None,
        table_name: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

