# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutLayerACLRequest(DaraModel):
    def __init__(
        self,
        acl: str = None,
        public: str = None,
    ):
        # Specify the access permission of the layer. A value of 1 indicates public and a value of 0 indicates private. The default value is 0.
        self.acl = acl
        # Specify whether the layer is a public layer. Valid values: true and false.
        self.public = public

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl

        if self.public is not None:
            result['public'] = self.public

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('public') is not None:
            self.public = m.get('public')

        return self

