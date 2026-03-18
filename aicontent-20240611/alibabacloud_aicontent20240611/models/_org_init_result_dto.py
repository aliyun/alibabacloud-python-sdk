# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OrgInitResultDTO(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        client_id: int = None,
        client_uuid: str = None,
        is_new: bool = None,
        org_id: int = None,
        user_id: int = None,
    ):
        self.api_key = api_key
        self.client_id = client_id
        self.client_uuid = client_uuid
        self.is_new = is_new
        self.org_id = org_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_uuid is not None:
            result['clientUuid'] = self.client_uuid

        if self.is_new is not None:
            result['isNew'] = self.is_new

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientUuid') is not None:
            self.client_uuid = m.get('clientUuid')

        if m.get('isNew') is not None:
            self.is_new = m.get('isNew')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

