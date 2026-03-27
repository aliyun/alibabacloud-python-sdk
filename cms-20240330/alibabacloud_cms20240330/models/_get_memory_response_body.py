# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMemoryResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        created_at: str = None,
        expiration_date: str = None,
        id: str = None,
        immutable: str = None,
        memory: str = None,
        metadata: str = None,
        organization: str = None,
        owner: str = None,
        request_id: str = None,
        run_id: str = None,
        updated_at: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.app_id = app_id
        self.created_at = created_at
        self.expiration_date = expiration_date
        self.id = id
        self.immutable = immutable
        self.memory = memory
        self.metadata = metadata
        self.organization = organization
        self.owner = owner
        self.request_id = request_id
        self.run_id = run_id
        self.updated_at = updated_at
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.expiration_date is not None:
            result['expirationDate'] = self.expiration_date

        if self.id is not None:
            result['id'] = self.id

        if self.immutable is not None:
            result['immutable'] = self.immutable

        if self.memory is not None:
            result['memory'] = self.memory

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.organization is not None:
            result['organization'] = self.organization

        if self.owner is not None:
            result['owner'] = self.owner

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('expirationDate') is not None:
            self.expiration_date = m.get('expirationDate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('organization') is not None:
            self.organization = m.get('organization')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

