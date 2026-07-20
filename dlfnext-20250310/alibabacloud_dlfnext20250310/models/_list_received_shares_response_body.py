# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class ListReceivedSharesResponseBody(DaraModel):
    def __init__(
        self,
        next_page_token: str = None,
        shares: List[main_models.ReceivedShare] = None,
    ):
        self.next_page_token = next_page_token
        self.shares = shares

    def validate(self):
        if self.shares:
            for v1 in self.shares:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        result['shares'] = []
        if self.shares is not None:
            for k1 in self.shares:
                result['shares'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        self.shares = []
        if m.get('shares') is not None:
            for k1 in m.get('shares'):
                temp_model = main_models.ReceivedShare()
                self.shares.append(temp_model.from_map(k1))

        return self

