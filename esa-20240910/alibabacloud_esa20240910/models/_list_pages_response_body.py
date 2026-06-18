# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListPagesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pages: List[main_models.ListPagesResponseBodyPages] = None,
        request_id: str = None,
        total_count: int = None,
        usage: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_size = page_size
        # A list of custom response pages.
        self.pages = pages
        # The request ID.
        self.request_id = request_id
        # The total number of custom response pages that match the filter criteria.
        self.total_count = total_count
        # The number of custom response pages that you have created.
        self.usage = usage

    def validate(self):
        if self.pages:
            for v1 in self.pages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Pages'] = []
        if self.pages is not None:
            for k1 in self.pages:
                result['Pages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.pages = []
        if m.get('Pages') is not None:
            for k1 in m.get('Pages'):
                temp_model = main_models.ListPagesResponseBodyPages()
                self.pages.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class ListPagesResponseBodyPages(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        id: int = None,
        kind: str = None,
        name: str = None,
        update_time: str = None,
    ):
        # The Base64-encoded content of the custom response page.
        # 
        # This parameter is required.
        self.content = content
        # The value of the Content-Type header in the HTTP response.
        # 
        # This parameter is required.
        self.content_type = content_type
        # A custom description for the response page.
        self.description = description
        # The ID of the custom response page.[](~~2850223~~)
        self.id = id
        # The type of the custom response page.
        self.kind = kind
        # The name of the custom response page.
        self.name = name
        # The time the custom response page was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.name is not None:
            result['Name'] = self.name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

