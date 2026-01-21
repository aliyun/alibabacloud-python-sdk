# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManageTerraformStateRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        client_token: str = None,
        identifier: str = None,
        import_resource_id: str = None,
        resource_identifier: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.identifier = identifier
        self.import_resource_id = import_resource_id
        # This parameter is required.
        self.resource_identifier = resource_identifier
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.import_resource_id is not None:
            result['importResourceId'] = self.import_resource_id

        if self.resource_identifier is not None:
            result['resourceIdentifier'] = self.resource_identifier

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('importResourceId') is not None:
            self.import_resource_id = m.get('importResourceId')

        if m.get('resourceIdentifier') is not None:
            self.resource_identifier = m.get('resourceIdentifier')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

