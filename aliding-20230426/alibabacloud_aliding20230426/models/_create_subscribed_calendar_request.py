# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateSubscribedCalendarRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        managers: List[str] = None,
        name: str = None,
        subscribe_scope: main_models.CreateSubscribedCalendarRequestSubscribeScope = None,
    ):
        self.description = description
        self.managers = managers
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.subscribe_scope = subscribe_scope

    def validate(self):
        if self.subscribe_scope:
            self.subscribe_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.managers is not None:
            result['Managers'] = self.managers

        if self.name is not None:
            result['Name'] = self.name

        if self.subscribe_scope is not None:
            result['SubscribeScope'] = self.subscribe_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Managers') is not None:
            self.managers = m.get('Managers')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SubscribeScope') is not None:
            temp_model = main_models.CreateSubscribedCalendarRequestSubscribeScope()
            self.subscribe_scope = temp_model.from_map(m.get('SubscribeScope'))

        return self

class CreateSubscribedCalendarRequestSubscribeScope(DaraModel):
    def __init__(
        self,
        corp_ids: List[str] = None,
        open_conversation_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.corp_ids = corp_ids
        self.open_conversation_ids = open_conversation_ids
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_ids is not None:
            result['CorpIds'] = self.corp_ids

        if self.open_conversation_ids is not None:
            result['OpenConversationIds'] = self.open_conversation_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIds') is not None:
            self.corp_ids = m.get('CorpIds')

        if m.get('OpenConversationIds') is not None:
            self.open_conversation_ids = m.get('OpenConversationIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

