# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataAgentMcpResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataAgentMcpResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The paging query results of MCP Servers.
        self.data = data
        # The return code. The value is success if the request was successful, or an error code if the request failed.
        self.error_code = error_code
        # The error message returned when a system-level request failure occurs.
        self.error_message = error_message
        # The maximum number of records returned in this response.
        self.max_results = max_results
        # The token for the next page. This value is empty when no more results are available.
        self.next_token = next_token
        # The request ID, which is used to locate this call.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - true: Successful.
        # - false: Failed.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDataAgentMcpResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataAgentMcpResponseBodyData(DaraModel):
    def __init__(
        self,
        content: Any = None,
        page_number: float = None,
        page_size: float = None,
        total_elements: float = None,
        total_pages: float = None,
    ):
        # The list of MCP Servers on the current page. Each item contains information such as the service identifier, name, workspace, network, connection method, status, and enabled state.
        self.content = content
        # The current page number, starting from 1.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The total number of records that match the filter conditions.
        self.total_elements = total_elements
        # The total number of pages that match the filter conditions.
        self.total_pages = total_pages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

