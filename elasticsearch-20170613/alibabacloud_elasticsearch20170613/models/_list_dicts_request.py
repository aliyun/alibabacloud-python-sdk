# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDictsRequest(DaraModel):
    def __init__(
        self,
        analyzer_type: str = None,
        name: str = None,
    ):
        # The type of the dictionary. Valid values:
        # 
        # *   IK: IK dictionary after a standard update
        # *   IK_HOT: IK dictionary after a rolling update
        # *   SYNONYMS: synonym dictionary
        # *   ALIWS: Alibaba Cloud dictionary
        # 
        # This parameter is required.
        self.analyzer_type = analyzer_type
        # The name of the dictionary file.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

