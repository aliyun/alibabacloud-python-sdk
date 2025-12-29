# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CustomHostAlias(DaraModel):
    def __init__(
        self,
        host_aliases: List[main_models.HostAlias] = None,
    ):
        self.host_aliases = host_aliases

    def validate(self):
        if self.host_aliases:
            for v1 in self.host_aliases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hostAliases'] = []
        if self.host_aliases is not None:
            for k1 in self.host_aliases:
                result['hostAliases'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_aliases = []
        if m.get('hostAliases') is not None:
            for k1 in m.get('hostAliases'):
                temp_model = main_models.HostAlias()
                self.host_aliases.append(temp_model.from_map(k1))

        return self

