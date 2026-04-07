# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaTableIntroWikiRequest(DaraModel):
    def __init__(
        self,
        table_guid: str = None,
        wiki_version: int = None,
    ):
        # The GUID of the metatable.
        # 
        # This parameter is required.
        self.table_guid = table_guid
        # The version of the instructions.
        self.wiki_version = wiki_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.wiki_version is not None:
            result['WikiVersion'] = self.wiki_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('WikiVersion') is not None:
            self.wiki_version = m.get('WikiVersion')

        return self

