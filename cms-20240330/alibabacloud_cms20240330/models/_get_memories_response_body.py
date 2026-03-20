# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetMemoriesResponseBody(DaraModel):
    def __init__(
        self,
        relations: List[main_models.GetMemoriesResponseBodyRelations] = None,
        request_id: str = None,
        results: List[main_models.GetMemoriesResponseBodyResults] = None,
    ):
        self.relations = relations
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.relations:
            for v1 in self.relations:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['relations'] = []
        if self.relations is not None:
            for k1 in self.relations:
                result['relations'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.relations = []
        if m.get('relations') is not None:
            for k1 in m.get('relations'):
                temp_model = main_models.GetMemoriesResponseBodyRelations()
                self.relations.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.GetMemoriesResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class GetMemoriesResponseBodyResults(DaraModel):
    def __init__(
        self,
        actor_id: str = None,
        agent_id: str = None,
        app_id: str = None,
        created_at: str = None,
        hash: str = None,
        id: str = None,
        memory: str = None,
        metadata: Dict[str, Any] = None,
        role: str = None,
        run_id: str = None,
        score: float = None,
        updated_at: str = None,
        user_id: str = None,
    ):
        self.actor_id = actor_id
        self.agent_id = agent_id
        self.app_id = app_id
        self.created_at = created_at
        self.hash = hash
        self.id = id
        self.memory = memory
        self.metadata = metadata
        self.role = role
        self.run_id = run_id
        self.score = score
        self.updated_at = updated_at
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actor_id is not None:
            result['actorId'] = self.actor_id

        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.hash is not None:
            result['hash'] = self.hash

        if self.id is not None:
            result['id'] = self.id

        if self.memory is not None:
            result['memory'] = self.memory

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.role is not None:
            result['role'] = self.role

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.score is not None:
            result['score'] = self.score

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actorId') is not None:
            self.actor_id = m.get('actorId')

        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('hash') is not None:
            self.hash = m.get('hash')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class GetMemoriesResponseBodyRelations(DaraModel):
    def __init__(
        self,
        destination: str = None,
        relationship: str = None,
        source: str = None,
    ):
        self.destination = destination
        self.relationship = relationship
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination is not None:
            result['destination'] = self.destination

        if self.relationship is not None:
            result['relationship'] = self.relationship

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')

        if m.get('relationship') is not None:
            self.relationship = m.get('relationship')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

