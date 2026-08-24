# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOneMetaSqlTemplateRequest(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        database_uuid: str = None,
        description: str = None,
        expr: str = None,
        knowledge_uuid: str = None,
        sql_params: str = None,
        tag: str = None,
        title: str = None,
    ):
        self.catalog_uuid = catalog_uuid
        self.database_uuid = database_uuid
        self.description = description
        self.expr = expr
        # This parameter is required.
        self.knowledge_uuid = knowledge_uuid
        self.sql_params = sql_params
        self.tag = tag
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.description is not None:
            result['Description'] = self.description

        if self.expr is not None:
            result['Expr'] = self.expr

        if self.knowledge_uuid is not None:
            result['KnowledgeUuid'] = self.knowledge_uuid

        if self.sql_params is not None:
            result['SqlParams'] = self.sql_params

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Expr') is not None:
            self.expr = m.get('Expr')

        if m.get('KnowledgeUuid') is not None:
            self.knowledge_uuid = m.get('KnowledgeUuid')

        if m.get('SqlParams') is not None:
            self.sql_params = m.get('SqlParams')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

