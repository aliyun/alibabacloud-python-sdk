# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplicationConfigParam(DaraModel):
    def __init__(
        self,
        config_action: str = None,
        config_file_name: str = None,
        config_item_description: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
        config_scope: str = None,
        effective_actions: str = None,
        effective_type: str = None,
        node_group_id: str = None,
        node_id: str = None,
    ):
        self.config_action = config_action
        self.config_file_name = config_file_name
        self.config_item_description = config_item_description
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value
        self.config_scope = config_scope
        self.effective_actions = effective_actions
        self.effective_type = effective_type
        self.node_group_id = node_group_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_action is not None:
            result['ConfigAction'] = self.config_action

        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name

        if self.config_item_description is not None:
            result['ConfigItemDescription'] = self.config_item_description

        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value

        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope

        if self.effective_actions is not None:
            result['EffectiveActions'] = self.effective_actions

        if self.effective_type is not None:
            result['EffectiveType'] = self.effective_type

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigAction') is not None:
            self.config_action = m.get('ConfigAction')

        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')

        if m.get('ConfigItemDescription') is not None:
            self.config_item_description = m.get('ConfigItemDescription')

        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')

        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')

        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')

        if m.get('EffectiveActions') is not None:
            self.effective_actions = m.get('EffectiveActions')

        if m.get('EffectiveType') is not None:
            self.effective_type = m.get('EffectiveType')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

