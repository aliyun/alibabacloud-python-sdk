# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNamespaceRequest(DaraModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_id: str = None,
    ):
        # The short-format ID of the namespace. You do not need to specify the region. We recommend that you use this parameter.
        self.name_space_short_id = name_space_short_id
        # The long-format ID of the namespace. If you specify this parameter, NameSpaceShortId is ignored. This parameter is for backward compatibility. We recommend that you use the short-format namespace ID.
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

