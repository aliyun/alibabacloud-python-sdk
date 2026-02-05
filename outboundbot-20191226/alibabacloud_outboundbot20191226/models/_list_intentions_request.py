# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntentionsRequest(DaraModel):
    def __init__(
        self,
        annotation_mission_data_source_type: int = None,
        bot_id: str = None,
        environment: int = None,
        instance_id: str = None,
        intent_id: int = None,
        page_index: int = None,
        page_size: int = None,
        script_id: str = None,
        user_nick: str = None,
    ):
        self.annotation_mission_data_source_type = annotation_mission_data_source_type
        self.bot_id = bot_id
        self.environment = environment
        self.instance_id = instance_id
        self.intent_id = intent_id
        self.page_index = page_index
        self.page_size = page_size
        self.script_id = script_id
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_data_source_type is not None:
            result['AnnotationMissionDataSourceType'] = self.annotation_mission_data_source_type

        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionDataSourceType') is not None:
            self.annotation_mission_data_source_type = m.get('AnnotationMissionDataSourceType')

        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

