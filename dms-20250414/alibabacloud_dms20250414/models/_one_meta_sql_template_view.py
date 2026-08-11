# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OneMetaSqlTemplateView(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        database_uuid: str = None,
        description: str = None,
        expr: str = None,
        gmt_created: int = None,
        gmt_modified: int = None,
        knowledge_uuid: str = None,
        source: str = None,
        sql_params: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        version: str = None,
    ):
        self.catalog_uuid = catalog_uuid
        self.database_uuid = database_uuid
        self.description = description
        self.expr = expr
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.knowledge_uuid = knowledge_uuid
        self.source = source
        self.sql_params = sql_params
        self.summary = summary
        self.tag = tag
        self.title = title
        self.version = version

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

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.knowledge_uuid is not None:
            result['KnowledgeUuid'] = self.knowledge_uuid

        if self.source is not None:
            result['Source'] = self.source

        if self.sql_params is not None:
            result['SqlParams'] = self.sql_params

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.title is not None:
            result['Title'] = self.title

        if self.version is not None:
            result['Version'] = self.version

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

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('KnowledgeUuid') is not None:
            self.knowledge_uuid = m.get('KnowledgeUuid')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SqlParams') is not None:
            self.sql_params = m.get('SqlParams')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

