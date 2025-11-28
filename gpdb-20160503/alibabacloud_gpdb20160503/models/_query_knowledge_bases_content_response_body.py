# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class QueryKnowledgeBasesContentResponseBody(DaraModel):
    def __init__(
        self,
        embedding_tokens: str = None,
        entities: main_models.QueryKnowledgeBasesContentResponseBodyEntities = None,
        matches: main_models.QueryKnowledgeBasesContentResponseBodyMatches = None,
        message: str = None,
        relations: main_models.QueryKnowledgeBasesContentResponseBodyRelations = None,
        request_id: str = None,
        status: str = None,
        usage: main_models.QueryKnowledgeBasesContentResponseBodyUsage = None,
    ):
        # The number of tokens that are used during vectorization.
        # 
        # >  A token is the minimum unit for segmenting text. A token can be a word, phrase, punctuation, or character.
        self.embedding_tokens = embedding_tokens
        # The details of the entity.
        self.entities = entities
        # A single data record.
        self.matches = matches
        # The returned information.
        self.message = message
        # The details of the relationship edge.
        self.relations = relations
        # The unique ID of the request.
        self.request_id = request_id
        # The status of the operation. Valid values:
        # 
        # *   **success**.
        # *   **fail**.
        self.status = status
        # The total number of tokens that are consumed by this query.
        self.usage = usage

    def validate(self):
        if self.entities:
            self.entities.validate()
        if self.matches:
            self.matches.validate()
        if self.relations:
            self.relations.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens

        if self.entities is not None:
            result['Entities'] = self.entities.to_map()

        if self.matches is not None:
            result['Matches'] = self.matches.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.relations is not None:
            result['Relations'] = self.relations.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')

        if m.get('Entities') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentResponseBodyEntities()
            self.entities = temp_model.from_map(m.get('Entities'))

        if m.get('Matches') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentResponseBodyMatches()
            self.matches = temp_model.from_map(m.get('Matches'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Relations') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentResponseBodyRelations()
            self.relations = temp_model.from_map(m.get('Relations'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Usage') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class QueryKnowledgeBasesContentResponseBodyUsage(DaraModel):
    def __init__(
        self,
        embedding_entries: str = None,
        embedding_tokens: str = None,
    ):
        # The number of entries that are used during vectorization.
        # 
        # >  An entry refers to a single unit of vectorization processing. Processing one text input counts as 1 entry, while processing one image counts as 2 entries.
        self.embedding_entries = embedding_entries
        # The number of tokens that are used for vectorization.
        # 
        # >  A token is the minimum unit for splitting text. A token can be a word, phrase, punctuation, or character.
        self.embedding_tokens = embedding_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding_entries is not None:
            result['EmbeddingEntries'] = self.embedding_entries

        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbeddingEntries') is not None:
            self.embedding_entries = m.get('EmbeddingEntries')

        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')

        return self

class QueryKnowledgeBasesContentResponseBodyRelations(DaraModel):
    def __init__(
        self,
        relations: List[main_models.QueryKnowledgeBasesContentResponseBodyRelationsRelations] = None,
    ):
        self.relations = relations

    def validate(self):
        if self.relations:
            for v1 in self.relations:
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.relations = []
        if m.get('relations') is not None:
            for k1 in m.get('relations'):
                temp_model = main_models.QueryKnowledgeBasesContentResponseBodyRelationsRelations()
                self.relations.append(temp_model.from_map(k1))

        return self

class QueryKnowledgeBasesContentResponseBodyRelationsRelations(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_name: str = None,
        id: str = None,
        source_entity: str = None,
        target_entity: str = None,
    ):
        # The description of the relationship edge.
        self.description = description
        # The name of the file.
        self.file_name = file_name
        # The ID of the link.
        self.id = id
        # The source entity.
        self.source_entity = source_entity
        # The destination entity.
        self.target_entity = target_entity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.id is not None:
            result['Id'] = self.id

        if self.source_entity is not None:
            result['SourceEntity'] = self.source_entity

        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SourceEntity') is not None:
            self.source_entity = m.get('SourceEntity')

        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')

        return self

class QueryKnowledgeBasesContentResponseBodyMatches(DaraModel):
    def __init__(
        self,
        match_list: List[main_models.QueryKnowledgeBasesContentResponseBodyMatchesMatchList] = None,
    ):
        self.match_list = match_list

    def validate(self):
        if self.match_list:
            for v1 in self.match_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MatchList'] = []
        if self.match_list is not None:
            for k1 in self.match_list:
                result['MatchList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match_list = []
        if m.get('MatchList') is not None:
            for k1 in m.get('MatchList'):
                temp_model = main_models.QueryKnowledgeBasesContentResponseBodyMatchesMatchList()
                self.match_list.append(temp_model.from_map(k1))

        return self

class QueryKnowledgeBasesContentResponseBodyMatchesMatchList(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        file_url: str = None,
        id: str = None,
        loader_metadata: str = None,
        metadata: Dict[str, str] = None,
        rerank_score: float = None,
        retrieval_source: int = None,
        score: float = None,
    ):
        # The content of the text.
        self.content = content
        # The name of the file.
        self.file_name = file_name
        # The public network URL of the image result. By default, the URL is valid for 2 hours.
        # 
        # You can use the UrlExpiration parameter to specify a validity period.
        self.file_url = file_url
        # The unique ID of the vector data.
        self.id = id
        # Document loader metadata.
        self.loader_metadata = loader_metadata
        # The metadata map.
        self.metadata = metadata
        # The rerank score.
        self.rerank_score = rerank_score
        # The source of the retrieval results. 1 indicates vector retrieval, 2 indicates full-text retrieval, and 3 indicates dual-path retrieval.
        self.retrieval_source = retrieval_source
        # The similarity score of the data. It is related to the algorithm (l2, ip, or cosine) that is specified when you create an index.
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.id is not None:
            result['Id'] = self.id

        if self.loader_metadata is not None:
            result['LoaderMetadata'] = self.loader_metadata

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.rerank_score is not None:
            result['RerankScore'] = self.rerank_score

        if self.retrieval_source is not None:
            result['RetrievalSource'] = self.retrieval_source

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LoaderMetadata') is not None:
            self.loader_metadata = m.get('LoaderMetadata')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RerankScore') is not None:
            self.rerank_score = m.get('RerankScore')

        if m.get('RetrievalSource') is not None:
            self.retrieval_source = m.get('RetrievalSource')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

class QueryKnowledgeBasesContentResponseBodyEntities(DaraModel):
    def __init__(
        self,
        entities: List[main_models.QueryKnowledgeBasesContentResponseBodyEntitiesEntities] = None,
    ):
        self.entities = entities

    def validate(self):
        if self.entities:
            for v1 in self.entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['entities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entities = []
        if m.get('entities') is not None:
            for k1 in m.get('entities'):
                temp_model = main_models.QueryKnowledgeBasesContentResponseBodyEntitiesEntities()
                self.entities.append(temp_model.from_map(k1))

        return self

class QueryKnowledgeBasesContentResponseBodyEntitiesEntities(DaraModel):
    def __init__(
        self,
        description: str = None,
        entity: str = None,
        file_name: str = None,
        id: str = None,
        type: str = None,
    ):
        # The entity description.
        self.description = description
        # The name of the entity.
        self.entity = entity
        # The name of the file.
        self.file_name = file_name
        # The entity ID.
        self.id = id
        # The entity type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.entity is not None:
            result['Entity'] = self.entity

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Entity') is not None:
            self.entity = m.get('Entity')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

