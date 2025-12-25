# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GenerateSqlFromNLResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GenerateSqlFromNLResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GenerateSqlFromNLResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GenerateSqlFromNLResponseBodyData(DaraModel):
    def __init__(
        self,
        knowledge_references: List[main_models.GenerateSqlFromNLResponseBodyDataKnowledgeReferences] = None,
        question: str = None,
        similar_sql: List[main_models.GenerateSqlFromNLResponseBodyDataSimilarSql] = None,
        sql: str = None,
        tables: List[main_models.GenerateSqlFromNLResponseBodyDataTables] = None,
        thought: str = None,
    ):
        self.knowledge_references = knowledge_references
        self.question = question
        self.similar_sql = similar_sql
        self.sql = sql
        self.tables = tables
        self.thought = thought

    def validate(self):
        if self.knowledge_references:
            for v1 in self.knowledge_references:
                 if v1:
                    v1.validate()
        if self.similar_sql:
            for v1 in self.similar_sql:
                 if v1:
                    v1.validate()
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeReferences'] = []
        if self.knowledge_references is not None:
            for k1 in self.knowledge_references:
                result['KnowledgeReferences'].append(k1.to_map() if k1 else None)

        if self.question is not None:
            result['Question'] = self.question

        result['SimilarSql'] = []
        if self.similar_sql is not None:
            for k1 in self.similar_sql:
                result['SimilarSql'].append(k1.to_map() if k1 else None)

        if self.sql is not None:
            result['Sql'] = self.sql

        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        if self.thought is not None:
            result['Thought'] = self.thought

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_references = []
        if m.get('KnowledgeReferences') is not None:
            for k1 in m.get('KnowledgeReferences'):
                temp_model = main_models.GenerateSqlFromNLResponseBodyDataKnowledgeReferences()
                self.knowledge_references.append(temp_model.from_map(k1))

        if m.get('Question') is not None:
            self.question = m.get('Question')

        self.similar_sql = []
        if m.get('SimilarSql') is not None:
            for k1 in m.get('SimilarSql'):
                temp_model = main_models.GenerateSqlFromNLResponseBodyDataSimilarSql()
                self.similar_sql.append(temp_model.from_map(k1))

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.GenerateSqlFromNLResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k1))

        if m.get('Thought') is not None:
            self.thought = m.get('Thought')

        return self

class GenerateSqlFromNLResponseBodyDataTables(DaraModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GenerateSqlFromNLResponseBodyDataSimilarSql(DaraModel):
    def __init__(
        self,
        question: str = None,
        score: str = None,
        sql: str = None,
        thought: str = None,
    ):
        self.question = question
        self.score = score
        self.sql = sql
        self.thought = thought

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.question is not None:
            result['Question'] = self.question

        if self.score is not None:
            result['Score'] = self.score

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.thought is not None:
            result['Thought'] = self.thought

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('Thought') is not None:
            self.thought = m.get('Thought')

        return self

class GenerateSqlFromNLResponseBodyDataKnowledgeReferences(DaraModel):
    def __init__(
        self,
        content: str = None,
        level: str = None,
        name: str = None,
    ):
        self.content = content
        self.level = level
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

