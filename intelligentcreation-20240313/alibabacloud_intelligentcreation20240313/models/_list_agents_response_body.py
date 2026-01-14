# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class ListAgentsResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListAgentsResponseBodyList] = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.list = list
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListAgentsResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAgentsResponseBodyList(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        agent_scene: str = None,
        characters_description: str = None,
        enable_interaction: int = None,
        industry: str = None,
        online_search: bool = None,
        owner: str = None,
        reference_url: str = None,
        status: int = None,
        text_style: str = None,
        viewer: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent_scene = agent_scene
        self.characters_description = characters_description
        self.enable_interaction = enable_interaction
        self.industry = industry
        self.online_search = online_search
        self.owner = owner
        self.reference_url = reference_url
        self.status = status
        self.text_style = text_style
        self.viewer = viewer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.agent_scene is not None:
            result['agentScene'] = self.agent_scene

        if self.characters_description is not None:
            result['charactersDescription'] = self.characters_description

        if self.enable_interaction is not None:
            result['enableInteraction'] = self.enable_interaction

        if self.industry is not None:
            result['industry'] = self.industry

        if self.online_search is not None:
            result['onlineSearch'] = self.online_search

        if self.owner is not None:
            result['owner'] = self.owner

        if self.reference_url is not None:
            result['referenceUrl'] = self.reference_url

        if self.status is not None:
            result['status'] = self.status

        if self.text_style is not None:
            result['textStyle'] = self.text_style

        if self.viewer is not None:
            result['viewer'] = self.viewer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('agentScene') is not None:
            self.agent_scene = m.get('agentScene')

        if m.get('charactersDescription') is not None:
            self.characters_description = m.get('charactersDescription')

        if m.get('enableInteraction') is not None:
            self.enable_interaction = m.get('enableInteraction')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('onlineSearch') is not None:
            self.online_search = m.get('onlineSearch')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('referenceUrl') is not None:
            self.reference_url = m.get('referenceUrl')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('textStyle') is not None:
            self.text_style = m.get('textStyle')

        if m.get('viewer') is not None:
            self.viewer = m.get('viewer')

        return self

