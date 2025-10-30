# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class QueryContentResponseBody(DaraModel):
    def __init__(
        self,
        embedding_tokens: str = None,
        entities: main_models.QueryContentResponseBodyEntities = None,
        matches: main_models.QueryContentResponseBodyMatches = None,
        message: str = None,
        relations: main_models.QueryContentResponseBodyRelations = None,
        request_id: str = None,
        status: str = None,
        usage: main_models.QueryContentResponseBodyUsage = None,
        window_matches: main_models.QueryContentResponseBodyWindowMatches = None,
    ):
        # Number of tokens used for vectorization.
        # 
        # > A token refers to the smallest unit into which the input text is divided; a token can be a word, a phrase, a punctuation mark, or a character, etc.
        self.embedding_tokens = embedding_tokens
        self.entities = entities
        # The retrieved data.
        self.matches = matches
        # Return message.
        self.message = message
        self.relations = relations
        # The request ID.
        self.request_id = request_id
        # The execution state of the operation. Valid values:
        # 
        # *   **false**: The operation fails.
        # *   **true**: The operation is successful.
        self.status = status
        # Resource usage for this query.
        self.usage = usage
        # List of windowed matches.
        self.window_matches = window_matches

    def validate(self):
        if self.entities:
            self.entities.validate()
        if self.matches:
            self.matches.validate()
        if self.relations:
            self.relations.validate()
        if self.usage:
            self.usage.validate()
        if self.window_matches:
            self.window_matches.validate()

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

        if self.window_matches is not None:
            result['WindowMatches'] = self.window_matches.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')

        if m.get('Entities') is not None:
            temp_model = main_models.QueryContentResponseBodyEntities()
            self.entities = temp_model.from_map(m.get('Entities'))

        if m.get('Matches') is not None:
            temp_model = main_models.QueryContentResponseBodyMatches()
            self.matches = temp_model.from_map(m.get('Matches'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Relations') is not None:
            temp_model = main_models.QueryContentResponseBodyRelations()
            self.relations = temp_model.from_map(m.get('Relations'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Usage') is not None:
            temp_model = main_models.QueryContentResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        if m.get('WindowMatches') is not None:
            temp_model = main_models.QueryContentResponseBodyWindowMatches()
            self.window_matches = temp_model.from_map(m.get('WindowMatches'))

        return self

class QueryContentResponseBodyWindowMatches(DaraModel):
    def __init__(
        self,
        window_matches: List[main_models.QueryContentResponseBodyWindowMatchesWindowMatches] = None,
    ):
        self.window_matches = window_matches

    def validate(self):
        if self.window_matches:
            for v1 in self.window_matches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['windowMatches'] = []
        if self.window_matches is not None:
            for k1 in self.window_matches:
                result['windowMatches'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.window_matches = []
        if m.get('windowMatches') is not None:
            for k1 in m.get('windowMatches'):
                temp_model = main_models.QueryContentResponseBodyWindowMatchesWindowMatches()
                self.window_matches.append(temp_model.from_map(k1))

        return self

class QueryContentResponseBodyWindowMatchesWindowMatches(DaraModel):
    def __init__(
        self,
        window_match: main_models.QueryContentResponseBodyWindowMatchesWindowMatchesWindowMatch = None,
    ):
        # List of individual top windowed matches.
        self.window_match = window_match

    def validate(self):
        if self.window_match:
            self.window_match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.window_match is not None:
            result['WindowMatch'] = self.window_match.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WindowMatch') is not None:
            temp_model = main_models.QueryContentResponseBodyWindowMatchesWindowMatchesWindowMatch()
            self.window_match = temp_model.from_map(m.get('WindowMatch'))

        return self

class QueryContentResponseBodyWindowMatchesWindowMatchesWindowMatch(DaraModel):
    def __init__(
        self,
        window_match: List[main_models.QueryContentResponseBodyWindowMatchesWindowMatchesWindowMatchWindowMatch] = None,
    ):
        self.window_match = window_match

    def validate(self):
        if self.window_match:
            for v1 in self.window_match:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['windowMatch'] = []
        if self.window_match is not None:
            for k1 in self.window_match:
                result['windowMatch'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.window_match = []
        if m.get('windowMatch') is not None:
            for k1 in m.get('windowMatch'):
                temp_model = main_models.QueryContentResponseBodyWindowMatchesWindowMatchesWindowMatchWindowMatch()
                self.window_match.append(temp_model.from_map(k1))

        return self

class QueryContentResponseBodyWindowMatchesWindowMatchesWindowMatchWindowMatch(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        id: str = None,
        loader_metadata: str = None,
        metadata: Dict[str, str] = None,
    ):
        # Text content.
        self.content = content
        # File name.
        self.file_name = file_name
        # Unique ID of the vector data.
        self.id = id
        # Metadata information when the document loader was loaded.
        self.loader_metadata = loader_metadata
        # Metadata map.
        self.metadata = metadata

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

        if self.id is not None:
            result['Id'] = self.id

        if self.loader_metadata is not None:
            result['LoaderMetadata'] = self.loader_metadata

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LoaderMetadata') is not None:
            self.loader_metadata = m.get('LoaderMetadata')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        return self

class QueryContentResponseBodyUsage(DaraModel):
    def __init__(
        self,
        embedding_entries: str = None,
        embedding_tokens: str = None,
    ):
        # The number of entries used for vectorization.
        # > An entry refers to the number of processing items when performing vectorization on text or images. For example, processing one piece of text counts as 1 entry, while processing one image counts as 2 entries.
        self.embedding_entries = embedding_entries
        # Number of tokens used for vectorization.
        # 
        # > A token refers to the smallest unit into which the input text is divided; a token can be a word, a phrase, a punctuation mark, or a character, etc.
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

class QueryContentResponseBodyRelations(DaraModel):
    def __init__(
        self,
        relations: List[main_models.QueryContentResponseBodyRelationsRelations] = None,
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
                temp_model = main_models.QueryContentResponseBodyRelationsRelations()
                self.relations.append(temp_model.from_map(k1))

        return self

class QueryContentResponseBodyRelationsRelations(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_name: str = None,
        id: str = None,
        source_entity: str = None,
        target_entity: str = None,
    ):
        self.description = description
        self.file_name = file_name
        self.id = id
        self.source_entity = source_entity
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

class QueryContentResponseBodyMatches(DaraModel):
    def __init__(
        self,
        match_list: List[main_models.QueryContentResponseBodyMatchesMatchList] = None,
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
                temp_model = main_models.QueryContentResponseBodyMatchesMatchList()
                self.match_list.append(temp_model.from_map(k1))

        return self

class QueryContentResponseBodyMatchesMatchList(DaraModel):
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
        vector: main_models.QueryContentResponseBodyMatchesMatchListVector = None,
    ):
        # The content that is used for full-text search. If you leave this parameter empty, only vector search is used. If you do not leave this parameter empty, two-way retrieval based on vector search and full-text search is used.
        # 
        # >  You must specify at least one of the Content and Vector parameters.
        self.content = content
        # The name of the document.
        # 
        # >  You can call the [ListDocuments](https://help.aliyun.com/document_detail/2618453.html) operation to query a list of documents.
        self.file_name = file_name
        # The public URL of the query result image, valid for 2 hours
        self.file_url = file_url
        # The unique ID of the vector data.
        self.id = id
        # Metadata during document loader loading.
        self.loader_metadata = loader_metadata
        # The metadata.
        self.metadata = metadata
        # Re-ranking score.
        self.rerank_score = rerank_score
        # Source of the retrieval results:
        # 
        # - 1 indicates vector retrieval
        # - 2 indicates full-text retrieval
        # - 3 indicates dual-path recall
        self.retrieval_source = retrieval_source
        # The similarity score of the data. It is related to the `l2, ip, or cosine` algorithm that is specified when you create an index.
        self.score = score
        # The vector data. The length of the value must be the same as that of the Dimension parameter in the [CreateCollection](https://help.aliyun.com/document_detail/2401497.html) operation.
        # 
        # >  If you leave this parameter empty, only full-text search results are returned.
        self.vector = vector

    def validate(self):
        if self.vector:
            self.vector.validate()

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

        if self.vector is not None:
            result['Vector'] = self.vector.to_map()

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

        if m.get('Vector') is not None:
            temp_model = main_models.QueryContentResponseBodyMatchesMatchListVector()
            self.vector = temp_model.from_map(m.get('Vector'))

        return self

class QueryContentResponseBodyMatchesMatchListVector(DaraModel):
    def __init__(
        self,
        vector_list: List[float] = None,
    ):
        self.vector_list = vector_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vector_list is not None:
            result['VectorList'] = self.vector_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VectorList') is not None:
            self.vector_list = m.get('VectorList')

        return self

class QueryContentResponseBodyEntities(DaraModel):
    def __init__(
        self,
        entities: List[main_models.QueryContentResponseBodyEntitiesEntities] = None,
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
                temp_model = main_models.QueryContentResponseBodyEntitiesEntities()
                self.entities.append(temp_model.from_map(k1))

        return self

class QueryContentResponseBodyEntitiesEntities(DaraModel):
    def __init__(
        self,
        description: str = None,
        entity: str = None,
        file_name: str = None,
        id: str = None,
        type: str = None,
    ):
        self.description = description
        self.entity = entity
        self.file_name = file_name
        self.id = id
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

