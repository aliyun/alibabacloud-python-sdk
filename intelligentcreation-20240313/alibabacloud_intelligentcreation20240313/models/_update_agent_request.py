# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentRequest(DaraModel):
    def __init__(
        self,
        agent_icon_url: str = None,
        agent_id: str = None,
        agent_name: str = None,
        character_age_stage: str = None,
        character_gender: str = None,
        character_name: str = None,
        extra_description: str = None,
        industry: str = None,
    ):
        self.agent_icon_url = agent_icon_url
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.character_age_stage = character_age_stage
        self.character_gender = character_gender
        self.character_name = character_name
        self.extra_description = extra_description
        self.industry = industry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_icon_url is not None:
            result['agentIconUrl'] = self.agent_icon_url

        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.character_age_stage is not None:
            result['characterAgeStage'] = self.character_age_stage

        if self.character_gender is not None:
            result['characterGender'] = self.character_gender

        if self.character_name is not None:
            result['characterName'] = self.character_name

        if self.extra_description is not None:
            result['extraDescription'] = self.extra_description

        if self.industry is not None:
            result['industry'] = self.industry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentIconUrl') is not None:
            self.agent_icon_url = m.get('agentIconUrl')

        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('characterAgeStage') is not None:
            self.character_age_stage = m.get('characterAgeStage')

        if m.get('characterGender') is not None:
            self.character_gender = m.get('characterGender')

        if m.get('characterName') is not None:
            self.character_name = m.get('characterName')

        if m.get('extraDescription') is not None:
            self.extra_description = m.get('extraDescription')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        return self

