# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgePointResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetKnowledgePointResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code. This parameter is omitted when the request is successful. For failures, the common error response protocol is followed.
        self.code = code
        # The typed details of a single knowledge point. Only the item corresponding to the Type value is returned among Graph, Wiki, and KnowledgeContent.
        self.data = data
        # The readable description of the business error. This parameter is omitted when the request is successful. Provide the RequestId when troubleshooting failures.
        self.message = message
        # The unique identifier of the request, which can be used to troubleshoot issues.
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
            temp_model = main_models.GetKnowledgePointResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKnowledgePointResponseBodyData(DaraModel):
    def __init__(
        self,
        graph: main_models.GetKnowledgePointResponseBodyDataGraph = None,
        id: str = None,
        knowledge_base_id: str = None,
        knowledge_content: main_models.GetKnowledgePointResponseBodyDataKnowledgeContent = None,
        next_token: str = None,
        type: str = None,
        warnings: List[main_models.GetKnowledgePointResponseBodyDataWarnings] = None,
        wiki: main_models.GetKnowledgePointResponseBodyDataWiki = None,
    ):
        # The one-hop local graph with the requested Id as the entry point. This parameter is returned only when Type is set to GRAPH. It includes the entry point, the relationships on the current page, and their visible endpoints.
        self.graph = graph
        # The location ID of the knowledge point. Copy this value exactly as it appears in the search results and use it together with the corresponding KnowledgeBaseId and Type. Do not parse or convert this value.
        self.id = id
        # The ID of the knowledge base to which the knowledge point belongs. This parameter is used together with Type and Id to locate the knowledge point.
        self.knowledge_base_id = knowledge_base_id
        # The title, Markdown body, and optional sources of the knowledge content. This parameter is returned only when Type is set to KNOWLEDGE_CONTENT.
        self.knowledge_content = knowledge_content
        # The pagination cursor. Do not specify this parameter when you request the first page. For subsequent pages, use the NextToken value returned in the previous response. An empty response indicates that no more pages are available. If the current page is empty but the cursor is not empty, continue pagination. This parameter is used only when Type is set to GRAPH. You must keep the same knowledge base, entry point, and MaxResults values.
        self.next_token = next_token
        # The read category of the knowledge point. Valid values: GRAPH for local graphs, WIKI for topic pages, and KNOWLEDGE_CONTENT for knowledge content.
        self.type = type
        # The truncation, scope limitation, or degradation prompts for the current call. Use Code for programmatic judgment. Message is for reading purposes only.
        self.warnings = warnings
        # The title, Markdown body, and optional sources of the topic page. This parameter is returned only when Type is set to WIKI.
        self.wiki = wiki

    def validate(self):
        if self.graph:
            self.graph.validate()
        if self.knowledge_content:
            self.knowledge_content.validate()
        if self.warnings:
            for v1 in self.warnings:
                 if v1:
                    v1.validate()
        if self.wiki:
            self.wiki.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph is not None:
            result['Graph'] = self.graph.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_content is not None:
            result['KnowledgeContent'] = self.knowledge_content.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.type is not None:
            result['Type'] = self.type

        result['Warnings'] = []
        if self.warnings is not None:
            for k1 in self.warnings:
                result['Warnings'].append(k1.to_map() if k1 else None)

        if self.wiki is not None:
            result['Wiki'] = self.wiki.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Graph') is not None:
            temp_model = main_models.GetKnowledgePointResponseBodyDataGraph()
            self.graph = temp_model.from_map(m.get('Graph'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeContent') is not None:
            temp_model = main_models.GetKnowledgePointResponseBodyDataKnowledgeContent()
            self.knowledge_content = temp_model.from_map(m.get('KnowledgeContent'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.warnings = []
        if m.get('Warnings') is not None:
            for k1 in m.get('Warnings'):
                temp_model = main_models.GetKnowledgePointResponseBodyDataWarnings()
                self.warnings.append(temp_model.from_map(k1))

        if m.get('Wiki') is not None:
            temp_model = main_models.GetKnowledgePointResponseBodyDataWiki()
            self.wiki = temp_model.from_map(m.get('Wiki'))

        return self

class GetKnowledgePointResponseBodyDataWiki(DaraModel):
    def __init__(
        self,
        content: str = None,
        sources: List[main_models.GetKnowledgePointResponseBodyDataWikiSources] = None,
        title: str = None,
    ):
        # The currently public Markdown body. The knowledge content may be a document fragment or a readable projection of structured knowledge, and is not guaranteed to be the full text of the original file.
        self.content = content
        # The download information of the uploaded original document explicitly associated with the current content. This parameter is omitted when no reliable source is available or when you do not have read permissions for the original file. The ability to retrieve a knowledge point does not imply the ability to download the complete original file.
        self.sources = sources
        # The display title of the current knowledge point.
        self.title = title

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
        if self.content is not None:
            result['Content'] = self.content

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.GetKnowledgePointResponseBodyDataWikiSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetKnowledgePointResponseBodyDataWikiSources(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expiration_time: int = None,
        file_name: str = None,
    ):
        # The temporary HTTPS download URL of the original file, which is valid for 2 hours. This parameter is returned only when the source can be reliably located and the caller has read permissions for the original file. Do not forward this URL publicly or store it for a long time.
        self.download_url = download_url
        # The expiration time of the download URL, in UNIX milliseconds.
        self.expiration_time = expiration_time
        # The full file name of the original document used for building. This is not the name of the current knowledge point fragment.
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

class GetKnowledgePointResponseBodyDataWarnings(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The truncation or degradation prompt code. For example, CONTENT_TRUNCATED indicates that the content is truncated, and SOURCE_UNAVAILABLE indicates that the original file download is temporarily unavailable.
        self.code = code
        # The sanitized and readable description of the current prompt. Use Code for programmatic judgment instead of relying on the text.
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

class GetKnowledgePointResponseBodyDataKnowledgeContent(DaraModel):
    def __init__(
        self,
        content: str = None,
        sources: List[main_models.GetKnowledgePointResponseBodyDataKnowledgeContentSources] = None,
        title: str = None,
    ):
        # The currently public Markdown body. The knowledge content may be a document fragment or a readable projection of structured knowledge, and is not guaranteed to be the full text of the original file.
        self.content = content
        # The download information of the uploaded original document explicitly associated with the current content. This parameter is omitted when no reliable source is available or when you do not have read permissions for the original file. The ability to retrieve a knowledge point does not imply the ability to download the complete original file.
        self.sources = sources
        # The display title of the current knowledge point.
        self.title = title

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
        if self.content is not None:
            result['Content'] = self.content

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.GetKnowledgePointResponseBodyDataKnowledgeContentSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetKnowledgePointResponseBodyDataKnowledgeContentSources(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expiration_time: int = None,
        file_name: str = None,
    ):
        # The temporary HTTPS download URL of the original file, which is valid for 2 hours. This parameter is returned only when the source can be reliably located and the caller has read permissions for the original file. Do not forward this URL publicly or store it for a long time.
        self.download_url = download_url
        # The expiration time of the download URL, in UNIX milliseconds.
        self.expiration_time = expiration_time
        # The full file name of the original document used for building. This is not the name of the current knowledge point fragment.
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

class GetKnowledgePointResponseBodyDataGraph(DaraModel):
    def __init__(
        self,
        edges: List[main_models.GetKnowledgePointResponseBodyDataGraphEdges] = None,
        knowledge_base_id: str = None,
        nodes: List[main_models.GetKnowledgePointResponseBodyDataGraphNodes] = None,
        root_node_id: str = None,
        update_time: int = None,
    ):
        # The visible one-hop adjacency relationships on the current page. At least one end of each edge is the RootNodeId, and both ends are in the Nodes of the current page.
        self.edges = edges
        # The ID of the knowledge base to which the knowledge point belongs. This parameter is used together with Type and Id to locate the knowledge point.
        self.knowledge_base_id = knowledge_base_id
        # All visible endpoints involved by the entry node and the relationships on the current page, deduplicated by NodeId. Subsequent pages still include the entry node.
        self.nodes = nodes
        # The ID of the entry node for the current local graph, which is the same as the requested Id.
        self.root_node_id = root_node_id
        # The time when the current graph was last published. This parameter is returned when the time is reliable.
        self.update_time = update_time

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

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.root_node_id is not None:
            result['RootNodeId'] = self.root_node_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k1 in m.get('Edges'):
                temp_model = main_models.GetKnowledgePointResponseBodyDataGraphEdges()
                self.edges.append(temp_model.from_map(k1))

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetKnowledgePointResponseBodyDataGraphNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('RootNodeId') is not None:
            self.root_node_id = m.get('RootNodeId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetKnowledgePointResponseBodyDataGraphNodes(DaraModel):
    def __init__(
        self,
        aliases: List[str] = None,
        definition: str = None,
        description: str = None,
        entity_id: str = None,
        knowledge_base_id: str = None,
        name: str = None,
        node_id: str = None,
        type: str = None,
    ):
        # The list of reliable aliases for the node. This parameter is omitted when no aliases are available.
        self.aliases = aliases
        # The reliable business definition of the graph node. This parameter is omitted when no public definition is available.
        self.definition = definition
        # The readable supplementary description of the current node or relationship. This parameter is omitted when no reliable content is available.
        self.description = description
        # The asset ID in DataWorks Data Map that can be reliably located. This is not the NodeId of the graph node. This parameter is omitted when no unique and reliable asset mapping is available.
        self.entity_id = entity_id
        # The ID of the knowledge base to which the knowledge point belongs. This parameter is used together with Type and Id to locate the knowledge point.
        self.knowledge_base_id = knowledge_base_id
        # The display name of the graph node.
        self.name = name
        # The ID of the node in the current knowledge base graph. You can use this value as the Id parameter when Type is set to GRAPH to read the local graph of this node.
        self.node_id = node_id
        # The business category of the graph node, such as TABLE for a data table. This is not the read category of the knowledge point.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliases is not None:
            result['Aliases'] = self.aliases

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.description is not None:
            result['Description'] = self.description

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliases') is not None:
            self.aliases = m.get('Aliases')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetKnowledgePointResponseBodyDataGraphEdges(DaraModel):
    def __init__(
        self,
        description: str = None,
        edge_id: str = None,
        from_node_id: str = None,
        join: main_models.GetKnowledgePointResponseBodyDataGraphEdgesJoin = None,
        knowledge_base_id: str = None,
        relation_type: str = None,
        to_node_id: str = None,
    ):
        # The readable supplementary description of the current node or relationship. This parameter is omitted when no reliable content is available.
        self.description = description
        # The ID of the relationship in the current knowledge base graph.
        self.edge_id = edge_id
        # The NodeId of the start node of the relationship. The start node must exist in the Graph.Nodes of the same page.
        self.from_node_id = from_node_id
        # The typed field association information for verified relationships. This parameter is omitted when no reliable and complete field pairing is available.
        self.join = join
        # The ID of the knowledge base to which the knowledge point belongs. This parameter is used together with Type and Id to locate the knowledge point.
        self.knowledge_base_id = knowledge_base_id
        # The public relationship type from the start node to the end node. For example, CALCULATED_FROM indicates that the start node is calculated based on the end node. You cannot infer the complete formula based solely on the type.
        self.relation_type = relation_type
        # The NodeId of the end node of the relationship. The end node must exist in the Graph.Nodes of the same page.
        self.to_node_id = to_node_id

    def validate(self):
        if self.join:
            self.join.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.edge_id is not None:
            result['EdgeId'] = self.edge_id

        if self.from_node_id is not None:
            result['FromNodeId'] = self.from_node_id

        if self.join is not None:
            result['Join'] = self.join.to_map()

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.to_node_id is not None:
            result['ToNodeId'] = self.to_node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EdgeId') is not None:
            self.edge_id = m.get('EdgeId')

        if m.get('FromNodeId') is not None:
            self.from_node_id = m.get('FromNodeId')

        if m.get('Join') is not None:
            temp_model = main_models.GetKnowledgePointResponseBodyDataGraphEdgesJoin()
            self.join = temp_model.from_map(m.get('Join'))

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('ToNodeId') is not None:
            self.to_node_id = m.get('ToNodeId')

        return self

class GetKnowledgePointResponseBodyDataGraphEdgesJoin(DaraModel):
    def __init__(
        self,
        cardinality: str = None,
        join_keys: List[main_models.GetKnowledgePointResponseBodyDataGraphEdgesJoinJoinKeys] = None,
    ):
        # The association cardinality from the start node to the end node. Valid values: ONE_TO_ONE, ONE_TO_MANY, MANY_TO_ONE, and MANY_TO_MANY. This parameter is returned when the cardinality is reliable.
        self.cardinality = cardinality
        # The equivalent association field pairing for the nodes at both ends. Composite keys are returned in full.
        self.join_keys = join_keys

    def validate(self):
        if self.join_keys:
            for v1 in self.join_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cardinality is not None:
            result['Cardinality'] = self.cardinality

        result['JoinKeys'] = []
        if self.join_keys is not None:
            for k1 in self.join_keys:
                result['JoinKeys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cardinality') is not None:
            self.cardinality = m.get('Cardinality')

        self.join_keys = []
        if m.get('JoinKeys') is not None:
            for k1 in m.get('JoinKeys'):
                temp_model = main_models.GetKnowledgePointResponseBodyDataGraphEdgesJoinJoinKeys()
                self.join_keys.append(temp_model.from_map(k1))

        return self

class GetKnowledgePointResponseBodyDataGraphEdgesJoinJoinKeys(DaraModel):
    def __init__(
        self,
        from_field: str = None,
        to_field: str = None,
    ):
        # The name of the association field for the node corresponding to FromNodeId.
        self.from_field = from_field
        # The name of the association field for the node corresponding to ToNodeId.
        self.to_field = to_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_field is not None:
            result['FromField'] = self.from_field

        if self.to_field is not None:
            result['ToField'] = self.to_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromField') is not None:
            self.from_field = m.get('FromField')

        if m.get('ToField') is not None:
            self.to_field = m.get('ToField')

        return self

