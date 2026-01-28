# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteComponentRequest(DaraModel):
    def __init__(
        self,
        component_action_name: str = None,
        component_asset_uuid: str = None,
        component_input: str = None,
        component_name: str = None,
        lang: str = None,
        play_book_node_name: str = None,
        playbook_uuid: str = None,
    ):
        self.component_action_name = component_action_name
        self.component_asset_uuid = component_asset_uuid
        self.component_input = component_input
        self.component_name = component_name
        self.lang = lang
        self.play_book_node_name = play_book_node_name
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_action_name is not None:
            result['ComponentActionName'] = self.component_action_name

        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid

        if self.component_input is not None:
            result['ComponentInput'] = self.component_input

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.play_book_node_name is not None:
            result['PlayBookNodeName'] = self.play_book_node_name

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentActionName') is not None:
            self.component_action_name = m.get('ComponentActionName')

        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')

        if m.get('ComponentInput') is not None:
            self.component_input = m.get('ComponentInput')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PlayBookNodeName') is not None:
            self.play_book_node_name = m.get('PlayBookNodeName')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        return self

