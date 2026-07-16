# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRuleMetadataRequest(DaraModel):
    def __init__(
        self,
        meta_name: str = None,
    ):
        # The name of the metadata.
        # 
        # This parameter is required.
        self.meta_name = meta_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_name is not None:
            result['MetaName'] = self.meta_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaName') is not None:
            self.meta_name = m.get('MetaName')

        return self

