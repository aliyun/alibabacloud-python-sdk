# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccountRelationRequest(DaraModel):
    def __init__(
        self,
        relation_id: int = None,
        request_id: str = None,
    ):
        # The ID of the financial relationship. Value returned by calling the AddAccountRelation operation.
        self.relation_id = relation_id
        # The unique ID of the request. The ID is used to mark a request and troubleshoot a problem.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

