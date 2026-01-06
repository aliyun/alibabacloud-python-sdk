# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructMvBaseTableDetailModel(DaraModel):
    def __init__(
        self,
        data_volumn: str = None,
        enable_binlog: bool = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        self.data_volumn = data_volumn
        self.enable_binlog = enable_binlog
        self.schema_name = schema_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_volumn is not None:
            result['DataVolumn'] = self.data_volumn

        if self.enable_binlog is not None:
            result['EnableBinlog'] = self.enable_binlog

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataVolumn') is not None:
            self.data_volumn = m.get('DataVolumn')

        if m.get('EnableBinlog') is not None:
            self.enable_binlog = m.get('EnableBinlog')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

