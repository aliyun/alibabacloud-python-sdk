# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeBaseRetrievalGrantsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListKnowledgeBaseRetrievalGrantsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code. You can use this code to determine the error type when the request fails.
        self.code = code
        # The business data returned when the request is successful.
        self.data = data
        # The error message returned when the request fails.
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
            temp_model = main_models.ListKnowledgeBaseRetrievalGrantsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListKnowledgeBaseRetrievalGrantsResponseBodyData(DaraModel):
    def __init__(
        self,
        knowledge_base_retrieval_grants: List[main_models.ListKnowledgeBaseRetrievalGrantsResponseBodyDataKnowledgeBaseRetrievalGrants] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The user grants on the current page.
        self.knowledge_base_retrieval_grants = knowledge_base_retrieval_grants
        # The maximum number of entries per page used in the current request. If you do not specify this parameter in the request, the value is 20. This value is not the actual number of entries returned on the current page.
        self.max_results = max_results
        # The cursor for the next page. If no subsequent pages exist, null is returned.
        self.next_token = next_token

    def validate(self):
        if self.knowledge_base_retrieval_grants:
            for v1 in self.knowledge_base_retrieval_grants:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeBaseRetrievalGrants'] = []
        if self.knowledge_base_retrieval_grants is not None:
            for k1 in self.knowledge_base_retrieval_grants:
                result['KnowledgeBaseRetrievalGrants'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_base_retrieval_grants = []
        if m.get('KnowledgeBaseRetrievalGrants') is not None:
            for k1 in m.get('KnowledgeBaseRetrievalGrants'):
                temp_model = main_models.ListKnowledgeBaseRetrievalGrantsResponseBodyDataKnowledgeBaseRetrievalGrants()
                self.knowledge_base_retrieval_grants.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListKnowledgeBaseRetrievalGrantsResponseBodyDataKnowledgeBaseRetrievalGrants(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # The knowledge base ID.
        self.knowledge_base_id = knowledge_base_id
        # The DataWorks user ID of the principal that receives the share. When a principal is added, the system verifies whether the user is a member of the same tenant.
        self.principal_id = principal_id
        # The type of principal that receives the share. Default value: USER. Only USER is supported in the initial release.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

