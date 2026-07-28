# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStackRequest(DaraModel):
    def __init__(
        self,
        clean_resources: bool = None,
    ):
        # Specifies whether to synchronously clean up resources managed by the stack. By default, resources are not cleaned up.
        self.clean_resources = clean_resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clean_resources is not None:
            result['cleanResources'] = self.clean_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cleanResources') is not None:
            self.clean_resources = m.get('cleanResources')

        return self

