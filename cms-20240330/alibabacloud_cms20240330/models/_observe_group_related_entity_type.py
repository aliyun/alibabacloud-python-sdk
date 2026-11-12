# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObserveGroupRelatedEntityType(DaraModel):
    def __init__(
        self,
        cn_name: str = None,
        direction: str = None,
        domain: str = None,
        en_name: str = None,
        entity_group: str = None,
        relation: str = None,
        type: str = None,
        version: str = None,
    ):
        # The Chinese name of the entity.
        self.cn_name = cn_name
        # The association direction, which is currently fixed as outgoing, indicating that associated entities are searched along the direct outgoing edges of the primary entity.
        self.direction = direction
        # The entity domain.
        self.domain = domain
        # The English name of the entity.
        self.en_name = en_name
        # The CommonSchema group to which the entity belongs.
        self.entity_group = entity_group
        # The direct outgoing edge relationship, such as use, run_on, calls, or contains.
        self.relation = relation
        # The associated entity type.
        self.type = type
        # The effective CommonSchema version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_name is not None:
            result['cnName'] = self.cn_name

        if self.direction is not None:
            result['direction'] = self.direction

        if self.domain is not None:
            result['domain'] = self.domain

        if self.en_name is not None:
            result['enName'] = self.en_name

        if self.entity_group is not None:
            result['entityGroup'] = self.entity_group

        if self.relation is not None:
            result['relation'] = self.relation

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cnName') is not None:
            self.cn_name = m.get('cnName')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('enName') is not None:
            self.en_name = m.get('enName')

        if m.get('entityGroup') is not None:
            self.entity_group = m.get('entityGroup')

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

