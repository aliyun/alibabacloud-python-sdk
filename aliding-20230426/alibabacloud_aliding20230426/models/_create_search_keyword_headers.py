# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateSearchKeywordHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: main_models.CreateSearchKeywordHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('AccountContext') is not None:
            temp_model = main_models.CreateSearchKeywordHeadersAccountContext()
            self.account_context = temp_model.from_map(m.get('AccountContext'))

        return self

class CreateSearchKeywordHeadersAccountContext(DaraModel):
    def __init__(
        self,
        user_token: str = None,
    ):
        self.user_token = user_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_token is not None:
            result['userToken'] = self.user_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userToken') is not None:
            self.user_token = m.get('userToken')

        return self

