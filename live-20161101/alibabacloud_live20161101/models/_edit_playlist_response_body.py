# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class EditPlaylistResponseBody(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        items: main_models.EditPlaylistResponseBodyItems = None,
        program_id: str = None,
        request_id: str = None,
    ):
        # The ID of the production studio. You can use the ID as a request parameter in the API operation that is used to configure callbacks or add a virtual studio layout.
        self.caster_id = caster_id
        # The information about the episodes.
        self.items = items
        # The ID of the episode list. You can use the ID as a request parameter in the API operation that is used to delete the episode list, query the information about the episode list, start the episode list, or stop the episode list.
        self.program_id = program_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('Items') is not None:
            temp_model = main_models.EditPlaylistResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class EditPlaylistResponseBodyItems(DaraModel):
    def __init__(
        self,
        failed_items: List[main_models.EditPlaylistResponseBodyItemsFailedItems] = None,
        success_items: List[main_models.EditPlaylistResponseBodyItemsSuccessItems] = None,
    ):
        # The episodes that failed to be added.
        self.failed_items = failed_items
        # The episodes that were added.
        self.success_items = success_items

    def validate(self):
        if self.failed_items:
            for v1 in self.failed_items:
                 if v1:
                    v1.validate()
        if self.success_items:
            for v1 in self.success_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedItems'] = []
        if self.failed_items is not None:
            for k1 in self.failed_items:
                result['FailedItems'].append(k1.to_map() if k1 else None)

        result['SuccessItems'] = []
        if self.success_items is not None:
            for k1 in self.success_items:
                result['SuccessItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_items = []
        if m.get('FailedItems') is not None:
            for k1 in m.get('FailedItems'):
                temp_model = main_models.EditPlaylistResponseBodyItemsFailedItems()
                self.failed_items.append(temp_model.from_map(k1))

        self.success_items = []
        if m.get('SuccessItems') is not None:
            for k1 in m.get('SuccessItems'):
                temp_model = main_models.EditPlaylistResponseBodyItemsSuccessItems()
                self.success_items.append(temp_model.from_map(k1))

        return self

class EditPlaylistResponseBodyItemsSuccessItems(DaraModel):
    def __init__(
        self,
        item_id: str = None,
        item_name: str = None,
    ):
        # The ID of the episode.
        self.item_id = item_id
        # The name of the episode.
        self.item_name = item_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        return self

class EditPlaylistResponseBodyItemsFailedItems(DaraModel):
    def __init__(
        self,
        item_id: str = None,
        item_name: str = None,
    ):
        # The ID of the episode.
        self.item_id = item_id
        # The name of the episode.
        self.item_name = item_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        return self

