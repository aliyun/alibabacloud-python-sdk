# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataAgentThemeResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataAgentThemeResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
        total_pages: int = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned when the request failed.
        self.error_code = error_code
        # The error message returned when the request failed.
        self.error_message = error_message
        # The page size.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The current page number.
        self.page_number = page_number
        # The current page size.
        self.page_size = page_size
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success
        # The total number of records.
        self.total = total
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDataAgentThemeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListDataAgentThemeResponseBodyData(DaraModel):
    def __init__(
        self,
        category: str = None,
        created_at: str = None,
        description: str = None,
        modified_at: str = None,
        refer_to: str = None,
        theme_from: str = None,
        theme_id: str = None,
        theme_name: str = None,
        theme_type: str = None,
    ):
        # The common scenarios. Valid values: report, infographic, and others.
        self.category = category
        # The creation time in ISO 8601 format.
        self.created_at = created_at
        # The description.
        self.description = description
        # The modification time in ISO 8601 format.
        self.modified_at = modified_at
        # The tracing reference that points to the UUID of the source theme.
        self.refer_to = refer_to
        # The source of the theme. Valid values:
        # 
        # - system
        # - custom
        # - derived
        self.theme_from = theme_from
        # The business identifier of the theme.
        self.theme_id = theme_id
        # The display name of the theme.
        self.theme_name = theme_name
        # The theme stage. Valid values:
        # 
        # - design: contains only design.md.
        # - template: complete and renderable.
        self.theme_type = theme_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at

        if self.refer_to is not None:
            result['ReferTo'] = self.refer_to

        if self.theme_from is not None:
            result['ThemeFrom'] = self.theme_from

        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        if self.theme_name is not None:
            result['ThemeName'] = self.theme_name

        if self.theme_type is not None:
            result['ThemeType'] = self.theme_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')

        if m.get('ReferTo') is not None:
            self.refer_to = m.get('ReferTo')

        if m.get('ThemeFrom') is not None:
            self.theme_from = m.get('ThemeFrom')

        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        if m.get('ThemeName') is not None:
            self.theme_name = m.get('ThemeName')

        if m.get('ThemeType') is not None:
            self.theme_type = m.get('ThemeType')

        return self

