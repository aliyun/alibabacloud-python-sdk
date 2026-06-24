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
        # The dictionary type. Valid values:
        # 
        # - IK: IK cold update dictionary.
        # 
        # - IK_HOT: IK hot update dictionary.
        # 
        # - SYNONYMS: Synonym dictionary.
        # 
        # - ALIWS: Alibaba dictionary.
        # 
        # This parameter is required.
        self.analyzer_type = analyzer_type
        # The name of the file to filter.
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

