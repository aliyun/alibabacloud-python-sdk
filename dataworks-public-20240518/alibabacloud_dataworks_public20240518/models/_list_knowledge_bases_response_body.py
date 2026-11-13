# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeBasesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListKnowledgeBasesResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code. This field is omitted when the request is successful. If the request fails, the common error response protocol is followed.
        self.code = code
        # The list of knowledge bases on the current page and the cursor for the next page.
        self.data = data
        # The maximum number of knowledge bases to return per page. Valid values: 1 to 100.
        self.max_results = max_results
        # The readable description of the business error. This field is omitted when the request is successful. Provide the RequestId along with this message when troubleshooting failures.
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
            temp_model = main_models.ListKnowledgeBasesResponseBodyData()
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

class ListKnowledgeBasesResponseBodyData(DaraModel):
    def __init__(
        self,
        knowledge_bases: List[main_models.ListKnowledgeBasesResponseBodyDataKnowledgeBases] = None,
        next_token: str = None,
    ):
        # The list of knowledge bases that the current caller has permission to view in the current region.
        self.knowledge_bases = knowledge_bases
        # The pagination cursor. Do not specify this parameter when you request the first page. For subsequent pages, use the NextToken value returned in the previous response as is. An empty response indicates that no more pages are available. If the current page is empty but the cursor is not empty, continue pagination. Keep the same MaxResults value during pagination.
        self.next_token = next_token

    def validate(self):
        if self.knowledge_bases:
            for v1 in self.knowledge_bases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeBases'] = []
        if self.knowledge_bases is not None:
            for k1 in self.knowledge_bases:
                result['KnowledgeBases'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_bases = []
        if m.get('KnowledgeBases') is not None:
            for k1 in m.get('KnowledgeBases'):
                temp_model = main_models.ListKnowledgeBasesResponseBodyDataKnowledgeBases()
                self.knowledge_bases.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListKnowledgeBasesResponseBodyDataKnowledgeBases(DaraModel):
    def __init__(
        self,
        access_role: str = None,
        create_time: int = None,
        description: str = None,
        knowledge_base_id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        status: str = None,
        type: str = None,
    ):
        # The read-only access role of the current caller for the knowledge base. Valid values:
        # - OWNER: owner
        # - ADMIN: administrator
        # - VIEWER: viewer
        self.access_role = access_role
        # The creation time of the knowledge base. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The description of the knowledge base. This field can be empty if no description is set.
        self.description = description
        # The stable ID of the knowledge base, which can be used to limit the search scope.
        self.knowledge_base_id = knowledge_base_id
        # The last modification time of the knowledge base. The value is a UNIX timestamp in milliseconds.
        self.modify_time = modify_time
        # The name of the knowledge base.
        self.name = name
        # The DataWorks user ID of the knowledge base owner.
        self.owner = owner
        # The public status of the knowledge base. This list returns only normally visible knowledge bases, and the value is ACTIVE.
        self.status = status
        # The type of the knowledge base. Valid values:
        # - PERSONAL: personal knowledge base
        # - ENTERPRISE: enterprise knowledge base
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_role is not None:
            result['AccessRole'] = self.access_role

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRole') is not None:
            self.access_role = m.get('AccessRole')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

