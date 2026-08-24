# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ModifyForwardStrategyBindingItemsResponseBody(DaraModel):
    def __init__(
        self,
        forward_strategy_binding_items: main_models.ModifyForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItems = None,
        request_id: str = None,
    ):
        # The binding items of the forwarding rule after this modification.
        self.forward_strategy_binding_items = forward_strategy_binding_items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.forward_strategy_binding_items:
            self.forward_strategy_binding_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_strategy_binding_items is not None:
            result['ForwardStrategyBindingItems'] = self.forward_strategy_binding_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardStrategyBindingItems') is not None:
            temp_model = main_models.ModifyForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItems()
            self.forward_strategy_binding_items = temp_model.from_map(m.get('ForwardStrategyBindingItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItems(DaraModel):
    def __init__(
        self,
        forward_id: str = None,
        items: List[main_models.ModifyForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsItems] = None,
        match_mode: str = None,
    ):
        # The forwarding rule ID.
        self.forward_id = forward_id
        # The binding content. This parameter is not returned when MatchMode is **UserGroupAll** or **ApplicationAll**.
        self.items = items
        # The policy matching target type. Valid values:
        # - **UserGroupAll**: associates with all users.
        # - **UserGroupNormal**: associates with specific user groups.
        # - **ApplicationAll**: all private network applications.
        # - **Application**: specific private network applications.
        # - **Tag**: private network application tags.
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
                temp_model = main_models.ModifyForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        return self

class ModifyForwardStrategyBindingItemsResponseBodyForwardStrategyBindingItemsItems(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        tag_id: str = None,
        tag_name: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The private network access application ID.
        self.application_id = application_id
        # The private network access application name.
        self.application_name = application_name
        # The private network access tag ID.
        self.tag_id = tag_id
        # The tag name.
        self.tag_name = tag_name
        # The user group ID.
        self.user_group_id = user_group_id
        # The user group name.
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

