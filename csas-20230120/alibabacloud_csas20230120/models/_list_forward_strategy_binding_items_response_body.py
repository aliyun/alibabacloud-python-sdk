# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListForwardStrategyBindingItemsResponseBody(DaraModel):
    def __init__(
        self,
        forward_strategy_binding_items_list: List[main_models.ListForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsList] = None,
        item_type: str = None,
        request_id: str = None,
    ):
        self.forward_strategy_binding_items_list = forward_strategy_binding_items_list
        self.item_type = item_type
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.forward_strategy_binding_items_list:
            for v1 in self.forward_strategy_binding_items_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ForwardStrategyBindingItemsList'] = []
        if self.forward_strategy_binding_items_list is not None:
            for k1 in self.forward_strategy_binding_items_list:
                result['ForwardStrategyBindingItemsList'].append(k1.to_map() if k1 else None)

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forward_strategy_binding_items_list = []
        if m.get('ForwardStrategyBindingItemsList') is not None:
            for k1 in m.get('ForwardStrategyBindingItemsList'):
                temp_model = main_models.ListForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsList()
                self.forward_strategy_binding_items_list.append(temp_model.from_map(k1))

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsList(DaraModel):
    def __init__(
        self,
        forward_id: str = None,
        items: List[main_models.ListForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsListItems] = None,
        match_mode: str = None,
    ):
        self.forward_id = forward_id
        self.items = items
        self.match_mode = match_mode

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_id is not None:
            result['ForwardId'] = self.forward_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardId') is not None:
            self.forward_id = m.get('ForwardId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsListItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        return self

class ListForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsListItems(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        tag_id: str = None,
        tag_name: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.application_id = application_id
        self.application_name = application_name
        self.tag_id = tag_id
        self.tag_name = tag_name
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

