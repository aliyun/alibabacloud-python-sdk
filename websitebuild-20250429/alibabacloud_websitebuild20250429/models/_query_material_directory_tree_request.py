# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMaterialDirectoryTreeRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        hidden_public: bool = None,
        root: bool = None,
    ):
        self.biz_id = biz_id
        self.hidden_public = hidden_public
        # This parameter is required.
        self.root = root

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.hidden_public is not None:
            result['HiddenPublic'] = self.hidden_public

        if self.root is not None:
            result['Root'] = self.root

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('HiddenPublic') is not None:
            self.hidden_public = m.get('HiddenPublic')

        if m.get('Root') is not None:
            self.root = m.get('Root')

        return self

