# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlterSearchLibRequest(DaraModel):
    def __init__(
        self,
        search_lib_config: str = None,
        search_lib_name: str = None,
    ):
        self.search_lib_config = search_lib_config
        # This parameter is required.
        self.search_lib_name = search_lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.search_lib_config is not None:
            result['SearchLibConfig'] = self.search_lib_config

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchLibConfig') is not None:
            self.search_lib_config = m.get('SearchLibConfig')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        return self

