# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KnowledgeBaseVO(DaraModel):
    def __init__(
        self,
        category: str = None,
        confidence: float = None,
        db_id: int = None,
        db_name: str = None,
        description: str = None,
        entity_id: int = None,
        env: str = None,
        expr: str = None,
        gmt_create: str = None,
        instance_name: str = None,
        is_delete: bool = None,
        knowledge_id: str = None,
        knowledge_type: str = None,
        level_type: str = None,
        name: str = None,
        old_description: str = None,
        old_summary: str = None,
        parse_desc: str = None,
        reasoning_logic: str = None,
        relation_type: str = None,
        show_type: str = None,
        summary: str = None,
        table_name: str = None,
    ):
        self.category = category
        self.confidence = confidence
        self.db_id = db_id
        self.db_name = db_name
        self.description = description
        self.entity_id = entity_id
        self.env = env
        self.expr = expr
        self.gmt_create = gmt_create
        self.instance_name = instance_name
        self.is_delete = is_delete
        self.knowledge_id = knowledge_id
        self.knowledge_type = knowledge_type
        self.level_type = level_type
        self.name = name
        self.old_description = old_description
        self.old_summary = old_summary
        self.parse_desc = parse_desc
        self.reasoning_logic = reasoning_logic
        self.relation_type = relation_type
        self.show_type = show_type
        self.summary = summary
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.description is not None:
            result['Description'] = self.description

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.env is not None:
            result['Env'] = self.env

        if self.expr is not None:
            result['Expr'] = self.expr

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type

        if self.level_type is not None:
            result['LevelType'] = self.level_type

        if self.name is not None:
            result['Name'] = self.name

        if self.old_description is not None:
            result['OldDescription'] = self.old_description

        if self.old_summary is not None:
            result['OldSummary'] = self.old_summary

        if self.parse_desc is not None:
            result['ParseDesc'] = self.parse_desc

        if self.reasoning_logic is not None:
            result['ReasoningLogic'] = self.reasoning_logic

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.show_type is not None:
            result['ShowType'] = self.show_type

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Expr') is not None:
            self.expr = m.get('Expr')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')

        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OldDescription') is not None:
            self.old_description = m.get('OldDescription')

        if m.get('OldSummary') is not None:
            self.old_summary = m.get('OldSummary')

        if m.get('ParseDesc') is not None:
            self.parse_desc = m.get('ParseDesc')

        if m.get('ReasoningLogic') is not None:
            self.reasoning_logic = m.get('ReasoningLogic')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

