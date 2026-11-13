# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgePointsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListKnowledgePointsResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code. This parameter is omitted when the request is successful. If the request fails, the common error response protocol is followed.
        self.code = code
        # The summaries of the knowledge points on the current page and the cursor for the next page.
        self.data = data
        # The maximum number of knowledge bases to return per page. Valid values: 1 to 100.
        self.max_results = max_results
        # The readable description of the business error. This parameter is omitted when the request is successful. When troubleshooting a failure, provide the RequestId at the same time.
        self.message = message
        # The unique identifier of the request. You can use the ID to troubleshoot issues.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

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
            temp_model = main_models.ListKnowledgePointsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListKnowledgePointsResponseBodyData(DaraModel):
    def __init__(
        self,
        knowledge_points: List[main_models.ListKnowledgePointsResponseBodyDataKnowledgePoints] = None,
        next_token: str = None,
    ):
        # The summaries of the knowledge points that the current caller has permission to read on the current page. The KnowledgeBaseId, Type, and Id of each item can be directly used in the GetKnowledgePoint operation.
        self.knowledge_points = knowledge_points
        # The pagination cursor. Do not specify this parameter for the first page. For subsequent pages, pass the NextToken value returned in the previous response as is, and keep the knowledge base, type, and page size unchanged. An empty cursor indicates that no more data is available. If the current page is empty but the cursor is not empty, continue querying.
        self.next_token = next_token

    def validate(self):
        if self.knowledge_points:
            for v1 in self.knowledge_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgePoints'] = []
        if self.knowledge_points is not None:
            for k1 in self.knowledge_points:
                result['KnowledgePoints'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_points = []
        if m.get('KnowledgePoints') is not None:
            for k1 in m.get('KnowledgePoints'):
                temp_model = main_models.ListKnowledgePointsResponseBodyDataKnowledgePoints()
                self.knowledge_points.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListKnowledgePointsResponseBodyDataKnowledgePoints(DaraModel):
    def __init__(
        self,
        id: str = None,
        knowledge_base_id: str = None,
        summary: str = None,
        title: str = None,
        type: str = None,
    ):
        # The read identifier of the current knowledge point. For GRAPH, it is the ID of the local graph entry node. For WIKI, it is the page ID. For KNOWLEDGE_CONTENT, it is the content ID. Use this value as is in the GetKnowledgePoint operation without parsing or concatenation.
        self.id = id
        # The ID of the knowledge base to which the knowledge point belongs. This ID is used together with Type and Id to locate the knowledge point.
        self.knowledge_base_id = knowledge_base_id
        # The readable summary of the knowledge point. The summary is not guaranteed to contain the complete content. To obtain the details, call the GetKnowledgePoint operation.
        self.summary = summary
        # The readable title of the knowledge point. For GRAPH, the name of the entry node is used.
        self.title = title
        # The read category of the knowledge point. Valid values:
        # - GRAPH: local graph.
        # - WIKI: topic page.
        # - KNOWLEDGE_CONTENT: knowledge content.
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

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

