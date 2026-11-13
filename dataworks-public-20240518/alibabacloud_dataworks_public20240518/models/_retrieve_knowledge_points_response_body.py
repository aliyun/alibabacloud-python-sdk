# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class RetrieveKnowledgePointsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RetrieveKnowledgePointsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code. This field may be omitted if the request succeeds. If the request fails, the common error response protocol applies.
        self.code = code
        # The knowledge point summaries, relationship paths, ambiguity candidates, and warnings for the current search.
        self.data = data
        # A human-readable description of the business error. This field may be omitted if the request succeeds. Provide the RequestId when troubleshooting failures.
        self.message = message
        # The unique identifier of the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.RetrieveKnowledgePointsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RetrieveKnowledgePointsResponseBodyData(DaraModel):
    def __init__(
        self,
        ambiguities: List[main_models.RetrieveKnowledgePointsResponseBodyDataAmbiguities] = None,
        paths: List[main_models.RetrieveKnowledgePointsResponseBodyDataPaths] = None,
        results: List[main_models.RetrieveKnowledgePointsResponseBodyDataResults] = None,
        warnings: List[main_models.RetrieveKnowledgePointsResponseBodyDataWarnings] = None,
    ):
        # The ambiguity descriptions and candidate objects returned when the target is not yet confirmed.
        self.ambiguities = ambiguities
        # The relationship paths matched by the search. Path indexes do not correspond to indexes in the Results array. The paths may cover only a subset of relationships.
        self.paths = paths
        # Knowledge point summaries ranked by relevance across all knowledge bases. The total number of results does not exceed MaxResults. Results can include GRAPH, WIKI, and KNOWLEDGE_CONTENT.
        self.results = results
        # The truncation, scope limitation, or degradation warnings for the current call. Use Code for programmatic judgment. Message is for reading purposes only.
        self.warnings = warnings

    def validate(self):
        if self.ambiguities:
            for v1 in self.ambiguities:
                 if v1:
                    v1.validate()
        if self.paths:
            for v1 in self.paths:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()
        if self.warnings:
            for v1 in self.warnings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ambiguities'] = []
        if self.ambiguities is not None:
            for k1 in self.ambiguities:
                result['Ambiguities'].append(k1.to_map() if k1 else None)

        result['Paths'] = []
        if self.paths is not None:
            for k1 in self.paths:
                result['Paths'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        result['Warnings'] = []
        if self.warnings is not None:
            for k1 in self.warnings:
                result['Warnings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ambiguities = []
        if m.get('Ambiguities') is not None:
            for k1 in m.get('Ambiguities'):
                temp_model = main_models.RetrieveKnowledgePointsResponseBodyDataAmbiguities()
                self.ambiguities.append(temp_model.from_map(k1))

        self.paths = []
        if m.get('Paths') is not None:
            for k1 in m.get('Paths'):
                temp_model = main_models.RetrieveKnowledgePointsResponseBodyDataPaths()
                self.paths.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.RetrieveKnowledgePointsResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        self.warnings = []
        if m.get('Warnings') is not None:
            for k1 in m.get('Warnings'):
                temp_model = main_models.RetrieveKnowledgePointsResponseBodyDataWarnings()
                self.warnings.append(temp_model.from_map(k1))

        return self

class RetrieveKnowledgePointsResponseBodyDataWarnings(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The truncation or degradation warning code. For example, CONTENT_TRUNCATED indicates that the content is truncated, and SOURCE_UNAVAILABLE indicates that the original file download is temporarily unavailable.
        self.code = code
        # The sanitized readable description of the current warning. Use Code for programmatic judgment instead of relying on the text.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class RetrieveKnowledgePointsResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        id: str = None,
        knowledge_base_id: str = None,
        sources: List[main_models.RetrieveKnowledgePointsResponseBodyDataResultsSources] = None,
        summary: str = None,
        title: str = None,
        type: str = None,
    ):
        # The location ID of the knowledge point. Copy this value exactly as it appears in the search results and use it together with the corresponding KnowledgeBaseId and Type. Do not parse or convert this value.
        self.id = id
        # The ID of the knowledge base to which the knowledge point belongs. This parameter is used together with Type and Id to locate the knowledge point.
        self.knowledge_base_id = knowledge_base_id
        # The download information of the uploaded original documents explicitly associated with the current content. This parameter is omitted if no reliable source is available or if the caller lacks read permissions for the original files. The ability to retrieve knowledge points does not imply the permission to download the complete original files.
        self.sources = sources
        # The readable summary of the knowledge point. The summary is not guaranteed to contain the complete content. To obtain details, call GetKnowledgePoint.
        self.summary = summary
        # The display title of the current knowledge point.
        self.title = title
        # The read category of the knowledge point. GRAPH indicates a local graph, WIKI indicates a topic page, and KNOWLEDGE_CONTENT indicates knowledge content.
        self.type = type

    def validate(self):
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.RetrieveKnowledgePointsResponseBodyDataResultsSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RetrieveKnowledgePointsResponseBodyDataResultsSources(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expiration_time: int = None,
        file_name: str = None,
    ):
        # The temporary HTTPS download URL of the original file. The URL is valid for 2 hours. This parameter is returned only when the source can be reliably located and the caller has read permissions for the original file. Do not forward the URL publicly or store it for a long time.
        self.download_url = download_url
        # The expiration time of the download URL. The value is a UNIX timestamp in milliseconds.
        self.expiration_time = expiration_time
        # The full file name of the original document used for building. This is not the name of the current knowledge point segment.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

class RetrieveKnowledgePointsResponseBodyDataPaths(DaraModel):
    def __init__(
        self,
        edges: List[main_models.RetrieveKnowledgePointsResponseBodyDataPathsEdges] = None,
        nodes: List[main_models.RetrieveKnowledgePointsResponseBodyDataPathsNodes] = None,
    ):
        # The directed relationships that connect the nodes in the Nodes array of the current path.
        self.edges = edges
        # The graph nodes in the relationship path. You can read the details of each node by using its KnowledgeBaseId, Type, and Id.
        self.nodes = nodes

    def validate(self):
        if self.edges:
            for v1 in self.edges:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Edges'] = []
        if self.edges is not None:
            for k1 in self.edges:
                result['Edges'].append(k1.to_map() if k1 else None)

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k1 in m.get('Edges'):
                temp_model = main_models.RetrieveKnowledgePointsResponseBodyDataPathsEdges()
                self.edges.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.RetrieveKnowledgePointsResponseBodyDataPathsNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class RetrieveKnowledgePointsResponseBodyDataPathsNodes(DaraModel):
    def __init__(
        self,
        id: str = None,
        knowledge_base_id: str = None,
        title: str = None,
        type: str = None,
    ):
        # The location ID of the knowledge point. Copy this value exactly as it appears in the search results and use it together with the corresponding KnowledgeBaseId and Type. Do not parse or convert this value.
        self.id = id
        # The ID of the knowledge base to which the knowledge point belongs. This parameter is used together with Type and Id to locate the knowledge point.
        self.knowledge_base_id = knowledge_base_id
        # The display title of the current knowledge point.
        self.title = title
        # The read category of the knowledge point. Use GRAPH for the current focus objects and graph nodes.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RetrieveKnowledgePointsResponseBodyDataPathsEdges(DaraModel):
    def __init__(
        self,
        from_id: str = None,
        relation_type: str = None,
        to_id: str = None,
    ):
        # The Id of the start node in the Nodes array of the same path.
        self.from_id = from_id
        # The public relationship type directed from the start node to the end node. For example, CALCULATED_FROM indicates that the start node is calculated based on the end node. You cannot infer the complete formula based solely on the relationship type.
        self.relation_type = relation_type
        # The Id of the end node in the Nodes array of the same path.
        self.to_id = to_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_id is not None:
            result['FromId'] = self.from_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.to_id is not None:
            result['ToId'] = self.to_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('ToId') is not None:
            self.to_id = m.get('ToId')

        return self

class RetrieveKnowledgePointsResponseBodyDataAmbiguities(DaraModel):
    def __init__(
        self,
        candidates: List[main_models.RetrieveKnowledgePointsResponseBodyDataAmbiguitiesCandidates] = None,
        mention: str = None,
    ):
        # The candidate graph nodes when ambiguity exists. Each candidate carries the KnowledgeBaseId, Type, and Id for reading details, which does not indicate that the user has confirmed the selection.
        self.candidates = candidates
        # The name or description of the object whose referent is not yet determined in the query.
        self.mention = mention

    def validate(self):
        if self.candidates:
            for v1 in self.candidates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Candidates'] = []
        if self.candidates is not None:
            for k1 in self.candidates:
                result['Candidates'].append(k1.to_map() if k1 else None)

        if self.mention is not None:
            result['Mention'] = self.mention

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.candidates = []
        if m.get('Candidates') is not None:
            for k1 in m.get('Candidates'):
                temp_model = main_models.RetrieveKnowledgePointsResponseBodyDataAmbiguitiesCandidates()
                self.candidates.append(temp_model.from_map(k1))

        if m.get('Mention') is not None:
            self.mention = m.get('Mention')

        return self

class RetrieveKnowledgePointsResponseBodyDataAmbiguitiesCandidates(DaraModel):
    def __init__(
        self,
        id: str = None,
        knowledge_base_id: str = None,
        title: str = None,
        type: str = None,
    ):
        # The location ID of the knowledge point. Copy this value exactly as it appears in the search results and use it together with the corresponding KnowledgeBaseId and Type. Do not parse or convert this value.
        self.id = id
        # The ID of the knowledge base to which the knowledge point belongs. This parameter is used together with Type and Id to locate the knowledge point.
        self.knowledge_base_id = knowledge_base_id
        # The display title of the current knowledge point.
        self.title = title
        # The read category of the knowledge point. Use GRAPH for the current focus objects and graph nodes.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

