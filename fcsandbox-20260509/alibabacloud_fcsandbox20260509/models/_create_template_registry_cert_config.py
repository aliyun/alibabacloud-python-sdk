# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTemplateRegistryCertConfig(DaraModel):
    def __init__(
        self,
        insecure: bool = None,
    ):
        # Specifies whether to skip certificate verification.
        self.insecure = insecure

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insecure is not None:
            result['insecure'] = self.insecure

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('insecure') is not None:
            self.insecure = m.get('insecure')

        return self

