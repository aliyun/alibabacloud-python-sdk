# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteTextbookAssistantStartConversationRequest(DaraModel):
    def __init__(
        self,
        article_id: str = None,
        auth_token: str = None,
        scenario: str = None,
    ):
        # How you obtain this ID depends on the value of `scenario`.
        # 
        # **When the `scenario` input parameter is `SYNC`:**
        # 
        # 1. From the `Get Article List` response, use the top-level `articleId` field.
        # 
        # 2. From the `Get Article Details` response, use the top-level `articleId` field.
        # 
        # **When the `scenario` input parameter is `EXPAND`:**
        # 
        # 1. From the `Get Article Details` response, use the `sceneid` field from an element in the `sceneList` array.
        # 
        # This parameter is required.
        self.article_id = article_id
        # The authorization token for the API call. Obtain this token by calling the operation that provides the authorization token for the textbook-style AI teacher feature.
        # 
        # This parameter is required.
        self.auth_token = auth_token
        # The practice scenario. Valid values:
        # 
        # `SYNC`: synchronous practice
        # 
        # `EXPAND`: expansion practice
        # 
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article_id is not None:
            result['articleId'] = self.article_id

        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.scenario is not None:
            result['scenario'] = self.scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('articleId') is not None:
            self.article_id = m.get('articleId')

        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')

        return self

