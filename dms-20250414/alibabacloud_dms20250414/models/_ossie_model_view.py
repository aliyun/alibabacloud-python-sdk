# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OssieModelView(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        database_uuid: str = None,
        description: str = None,
        doc_format: str = None,
        domain_topic: str = None,
        expr: str = None,
        gmt_created: int = None,
        gmt_modified: int = None,
        knowledge_uuid: str = None,
        raw_doc: str = None,
        semantic_type: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        version: str = None,
    ):
        self.catalog_uuid = catalog_uuid
        self.database_uuid = database_uuid
        self.description = description
        self.doc_format = doc_format
        self.domain_topic = domain_topic
        self.expr = expr
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.knowledge_uuid = knowledge_uuid
        self.raw_doc = raw_doc
        self.semantic_type = semantic_type
        self.source = source
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

        if self.doc_format is not None:
            result['DocFormat'] = self.doc_format

        if self.domain_topic is not None:
            result['DomainTopic'] = self.domain_topic

        if self.expr is not None:
            result['Expr'] = self.expr

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.knowledge_uuid is not None:
            result['KnowledgeUuid'] = self.knowledge_uuid

        if self.raw_doc is not None:
            result['RawDoc'] = self.raw_doc

        if self.semantic_type is not None:
            result['SemanticType'] = self.semantic_type

        if self.source is not None:
            result['Source'] = self.source

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

        if m.get('DocFormat') is not None:
            self.doc_format = m.get('DocFormat')

        if m.get('DomainTopic') is not None:
            self.domain_topic = m.get('DomainTopic')

        if m.get('Expr') is not None:
            self.expr = m.get('Expr')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('KnowledgeUuid') is not None:
            self.knowledge_uuid = m.get('KnowledgeUuid')

        if m.get('RawDoc') is not None:
            self.raw_doc = m.get('RawDoc')

        if m.get('SemanticType') is not None:
            self.semantic_type = m.get('SemanticType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

