# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPermissionListRequest(DaraModel):
    def __init__(
        self,
        relation_id: int = None,
    ):
        # The relationship ID. Obtain this ID from the RelationId parameter in the response of the QueryRelationList operation.
        # 
        # This parameter is required.
        self.relation_id = relation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        return self

