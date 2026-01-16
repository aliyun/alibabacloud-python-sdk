# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVpcBindingsOutput(DaraModel):
    def __init__(
        self,
        vpc_ids: List[str] = None,
    ):
        self.vpc_ids = vpc_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_ids is not None:
            result['vpcIds'] = self.vpc_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpcIds') is not None:
            self.vpc_ids = m.get('vpcIds')

        return self

