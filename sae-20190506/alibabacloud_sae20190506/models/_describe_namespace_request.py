# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNamespaceRequest(DaraModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_id: str = None,
    ):
        # The short ID of the namespace. You do not need to specify a region ID. The value of this parameter can be up to 20 characters in length and can contain only lowercase letters and digits.
        self.name_space_short_id = name_space_short_id
        # The ID of the namespace. The information about the default namespace cannot be queried or modified. The default namespace cannot be deleted.
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

