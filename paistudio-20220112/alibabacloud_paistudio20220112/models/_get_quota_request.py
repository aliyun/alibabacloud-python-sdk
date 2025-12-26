# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQuotaRequest(DaraModel):
    def __init__(
        self,
        verbose: bool = None,
        with_node_meta: bool = None,
    ):
        self.verbose = verbose
        self.with_node_meta = with_node_meta

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.with_node_meta is not None:
            result['WithNodeMeta'] = self.with_node_meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('WithNodeMeta') is not None:
            self.with_node_meta = m.get('WithNodeMeta')

        return self

