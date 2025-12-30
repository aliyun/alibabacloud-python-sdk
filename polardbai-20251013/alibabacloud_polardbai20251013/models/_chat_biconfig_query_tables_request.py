# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatBIConfigQueryTablesRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        input_field: str = None,
        instance_name: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        self.input_field = input_field
        # This parameter is required.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.input_field is not None:
            result['InputField'] = self.input_field

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('InputField') is not None:
            self.input_field = m.get('InputField')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

