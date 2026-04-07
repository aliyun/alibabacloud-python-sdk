# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetaTableIntroWikiRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        table_guid: str = None,
    ):
        # The details of the instructions on how to use the metatable.
        # 
        # This parameter is required.
        self.content = content
        # The GUID of the table. Specify the GUID in the odps.{projectName}.{tableName} format.
        # 
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

