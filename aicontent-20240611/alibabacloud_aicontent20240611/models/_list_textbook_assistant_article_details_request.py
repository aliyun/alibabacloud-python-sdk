# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTextbookAssistantArticleDetailsRequest(DaraModel):
    def __init__(
        self,
        article_id_list: List[str] = None,
        auth_token: str = None,
    ):
        # The list of article IDs.
        self.article_id_list = article_id_list
        # The authorization code for API calls. You can obtain this code by calling the operation that retrieves the authorization code for the English textbook-style AI teacher feature.
        # 
        # This parameter is required.
        self.auth_token = auth_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article_id_list is not None:
            result['articleIdList'] = self.article_id_list

        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('articleIdList') is not None:
            self.article_id_list = m.get('articleIdList')

        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        return self

