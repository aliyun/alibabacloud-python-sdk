# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetWorkspacesHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: main_models.GetWorkspacesHeadersAccountContext = None,
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
            temp_model = main_models.GetWorkspacesHeadersAccountContext()
            self.account_context = temp_model.from_map(m.get('AccountContext'))

        return self

class GetWorkspacesHeadersAccountContext(DaraModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        return self

