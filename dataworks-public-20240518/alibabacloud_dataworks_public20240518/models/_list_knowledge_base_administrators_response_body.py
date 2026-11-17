# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeBaseAdministratorsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListKnowledgeBaseAdministratorsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code, which is used to determine the error type when the request fails.
        self.code = code
        # The business data returned when the request is successful.
        self.data = data
        # The security error message returned when the request fails.
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
            temp_model = main_models.ListKnowledgeBaseAdministratorsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListKnowledgeBaseAdministratorsResponseBodyData(DaraModel):
    def __init__(
        self,
        knowledge_base_administrators: List[main_models.ListKnowledgeBaseAdministratorsResponseBodyDataKnowledgeBaseAdministrators] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The administrators on the current page, excluding the owner.
        self.knowledge_base_administrators = knowledge_base_administrators
        # The maximum number of entries per page used for the current request. If the input parameter is omitted, the value is 20. This is not the actual number of entries returned on the current page.
        self.max_results = max_results
        # The cursor for the next page. If no subsequent pages exist, null is returned.
        self.next_token = next_token

    def validate(self):
        if self.knowledge_base_administrators:
            for v1 in self.knowledge_base_administrators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeBaseAdministrators'] = []
        if self.knowledge_base_administrators is not None:
            for k1 in self.knowledge_base_administrators:
                result['KnowledgeBaseAdministrators'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_base_administrators = []
        if m.get('KnowledgeBaseAdministrators') is not None:
            for k1 in m.get('KnowledgeBaseAdministrators'):
                temp_model = main_models.ListKnowledgeBaseAdministratorsResponseBodyDataKnowledgeBaseAdministrators()
                self.knowledge_base_administrators.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListKnowledgeBaseAdministratorsResponseBodyDataKnowledgeBaseAdministrators(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        display_name: str = None,
        knowledge_base_id: str = None,
        user_id: str = None,
    ):
        # The creation time of the record, represented as a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The display name of the user. This field is optional and is not used to verify the user’s identity.
        self.display_name = display_name
        # The ID of the knowledge base.
        self.knowledge_base_id = knowledge_base_id
        # The DataWorks user ID of the administrator.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

