# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetSubscribedCalendarResponseBody(DaraModel):
    def __init__(
        self,
        author: str = None,
        calendar_id: str = None,
        description: str = None,
        managers: List[str] = None,
        name: str = None,
        request_id: str = None,
        subscribe_scope: main_models.GetSubscribedCalendarResponseBodySubscribeScope = None,
    ):
        self.author = author
        self.calendar_id = calendar_id
        self.description = description
        self.managers = managers
        self.name = name
        # requestId
        self.request_id = request_id
        self.subscribe_scope = subscribe_scope

    def validate(self):
        if self.subscribe_scope:
            self.subscribe_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['author'] = self.author

        if self.calendar_id is not None:
            result['calendarId'] = self.calendar_id

        if self.description is not None:
            result['description'] = self.description

        if self.managers is not None:
            result['managers'] = self.managers

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.subscribe_scope is not None:
            result['subscribeScope'] = self.subscribe_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('author') is not None:
            self.author = m.get('author')

        if m.get('calendarId') is not None:
            self.calendar_id = m.get('calendarId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('managers') is not None:
            self.managers = m.get('managers')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('subscribeScope') is not None:
            temp_model = main_models.GetSubscribedCalendarResponseBodySubscribeScope()
            self.subscribe_scope = temp_model.from_map(m.get('subscribeScope'))

        return self

class GetSubscribedCalendarResponseBodySubscribeScope(DaraModel):
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

