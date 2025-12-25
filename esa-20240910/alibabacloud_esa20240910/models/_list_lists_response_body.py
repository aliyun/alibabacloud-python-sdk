# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListListsResponseBody(DaraModel):
    def __init__(
        self,
        items_usage: int = None,
        lists: List[main_models.ListListsResponseBodyLists] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        usage: int = None,
    ):
        self.items_usage = items_usage
        # The array that contains list information, including list data after paging.
        self.lists = lists
        # The page number returned.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of filtered lists.
        self.total_count = total_count
        # The number of created lists.
        self.usage = usage

    def validate(self):
        if self.lists:
            for v1 in self.lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items_usage is not None:
            result['ItemsUsage'] = self.items_usage

        result['Lists'] = []
        if self.lists is not None:
            for k1 in self.lists:
                result['Lists'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemsUsage') is not None:
            self.items_usage = m.get('ItemsUsage')

        self.lists = []
        if m.get('Lists') is not None:
            for k1 in m.get('Lists'):
                temp_model = main_models.ListListsResponseBodyLists()
                self.lists.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class ListListsResponseBodyLists(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        kind: str = None,
        length: int = None,
        name: str = None,
        update_time: str = None,
    ):
        # The list description.
        self.description = description
        # The ID of the custom list.[](~~2850217~~)
        self.id = id
        # The list type.
        self.kind = kind
        # The length of the list information array, which indicates how many items the list contains.
        self.length = length
        # The list name.
        self.name = name
        # The time when the list was last modified.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.length is not None:
            result['Length'] = self.length

        if self.name is not None:
            result['Name'] = self.name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

