# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetIdpMetadataResponseBody(DaraModel):
    def __init__(
        self,
        idp_entity_id: str = None,
        request_id: str = None,
    ):
        # The entity ID obtained after the IdP metadata file is parsed.
        self.idp_entity_id = idp_entity_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idp_entity_id is not None:
            result['IdpEntityId'] = self.idp_entity_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpEntityId') is not None:
            self.idp_entity_id = m.get('IdpEntityId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

