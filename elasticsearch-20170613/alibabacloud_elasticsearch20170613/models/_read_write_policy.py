# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadWritePolicy(DaraModel):
    def __init__(
        self,
        auto_generate_pk: bool = None,
        write_ha: bool = None,
        write_policy: str = None,
    ):
        self.auto_generate_pk = auto_generate_pk
        self.write_ha = write_ha
        self.write_policy = write_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_generate_pk is not None:
            result['autoGeneratePk'] = self.auto_generate_pk

        if self.write_ha is not None:
            result['writeHa'] = self.write_ha

        if self.write_policy is not None:
            result['writePolicy'] = self.write_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoGeneratePk') is not None:
            self.auto_generate_pk = m.get('autoGeneratePk')

        if m.get('writeHa') is not None:
            self.write_ha = m.get('writeHa')

        if m.get('writePolicy') is not None:
            self.write_policy = m.get('writePolicy')

        return self

