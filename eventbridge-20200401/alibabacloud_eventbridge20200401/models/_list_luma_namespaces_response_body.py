# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListLumaNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLumaNamespacesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of Success indicates a successful operation. If the operation fails, a specific error code is returned.
        self.code = code
        # The list of namespaces bound to the agent, including entries and pagination information.
        self.data = data
        # The response message. A value of Operation success is returned if the operation succeeds. A specific error description is returned if the operation fails.
        self.message = message
        # The unique ID of the request. Use this ID for troubleshooting and when submitting a ticket.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success.
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
            temp_model = main_models.ListLumaNamespacesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListLumaNamespacesResponseBodyData(DaraModel):
    def __init__(
        self,
        limit: int = None,
        namespaces: List[main_models.Namespace] = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The effective page size for this request. If the Limit parameter is not specified, the server default value is used. If the specified value exceeds the upper limit, the value is adjusted to the maximum allowed value.
        self.limit = limit
        # The list of namespaces bound to the agent.
        self.namespaces = namespaces
        # The token for the next page. Pass this value as the NextToken parameter in the next request to retrieve the next page. An empty value indicates that no more data is available.
        self.next_token = next_token
        # The total number of namespaces bound to the agent, regardless of the number of entries returned on the current page.
        self.total_count = total_count

    def validate(self):
        if self.namespaces:
            for v1 in self.namespaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        result['Namespaces'] = []
        if self.namespaces is not None:
            for k1 in self.namespaces:
                result['Namespaces'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k1 in m.get('Namespaces'):
                temp_model = main_models.Namespace()
                self.namespaces.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

