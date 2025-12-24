# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListPlaylistItemsResponseBody(DaraModel):
    def __init__(
        self,
        program_items: List[main_models.ListPlaylistItemsResponseBodyProgramItems] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The episodes.
        self.program_items = program_items
        # The request ID.
        self.request_id = request_id
        # The total number of episodes.
        self.total = total

    def validate(self):
        if self.program_items:
            for v1 in self.program_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProgramItems'] = []
        if self.program_items is not None:
            for k1 in self.program_items:
                result['ProgramItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.program_items = []
        if m.get('ProgramItems') is not None:
            for k1 in m.get('ProgramItems'):
                temp_model = main_models.ListPlaylistItemsResponseBodyProgramItems()
                self.program_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListPlaylistItemsResponseBodyProgramItems(DaraModel):
    def __init__(
        self,
        index: int = None,
        program_id: str = None,
        program_item_id: str = None,
        program_item_name: str = None,
        resource_type: str = None,
        resource_value: str = None,
    ):
        # The sequence number of the episode in the query result.
        self.index = index
        # The ID of the episode list. You can use the ID as a request parameter in the API operation that is used to edit the episode list, delete the episode list, query the information about the episode list, start the episode list, or stop the episode list.
        self.program_id = program_id
        # The ID of the episode.
        self.program_item_id = program_item_id
        # The name of the episode.
        self.program_item_name = program_item_name
        # The resource type.
        self.resource_type = resource_type
        # The resource ID.
        self.resource_value = resource_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.program_item_id is not None:
            result['ProgramItemId'] = self.program_item_id

        if self.program_item_name is not None:
            result['ProgramItemName'] = self.program_item_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_value is not None:
            result['ResourceValue'] = self.resource_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('ProgramItemId') is not None:
            self.program_item_id = m.get('ProgramItemId')

        if m.get('ProgramItemName') is not None:
            self.program_item_name = m.get('ProgramItemName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceValue') is not None:
            self.resource_value = m.get('ResourceValue')

        return self

