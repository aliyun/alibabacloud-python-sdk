# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class PostInnerConvertRequest(DaraModel):
    def __init__(
        self,
        sql_convert_map: Dict[str, Any] = None,
        src_data_source_name: str = None,
        tgt_data_source_name: str = None,
    ):
        # SQL node type mapping, where the key is the source node type and the value is the target node type. If not empty, it will be assembled into `workflow.converter.sqlNodeTypeMapping` in `innerConvertConfig` and written via the task configuration update interface after creating the scheduling transformation task.
        self.sql_convert_map = sql_convert_map
        # Source data source name, i.e., the name of the scheduling data source at the source end of the transformation task.
        self.src_data_source_name = src_data_source_name
        # Target data source name, i.e., the name of the scheduling data source at the target end of the transformation task.
        self.tgt_data_source_name = tgt_data_source_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sql_convert_map is not None:
            result['sqlConvertMap'] = self.sql_convert_map

        if self.src_data_source_name is not None:
            result['srcDataSourceName'] = self.src_data_source_name

        if self.tgt_data_source_name is not None:
            result['tgtDataSourceName'] = self.tgt_data_source_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sqlConvertMap') is not None:
            self.sql_convert_map = m.get('sqlConvertMap')

        if m.get('srcDataSourceName') is not None:
            self.src_data_source_name = m.get('srcDataSourceName')

        if m.get('tgtDataSourceName') is not None:
            self.tgt_data_source_name = m.get('tgtDataSourceName')

        return self

