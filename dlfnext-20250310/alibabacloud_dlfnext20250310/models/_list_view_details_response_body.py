# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class ListViewDetailsResponseBody(DaraModel):
    def __init__(
        self,
        next_page_token: str = None,
        view_details: List[main_models.View] = None,
    ):
        self.next_page_token = next_page_token
        self.view_details = view_details

    def validate(self):
        if self.view_details:
            for v1 in self.view_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        result['viewDetails'] = []
        if self.view_details is not None:
            for k1 in self.view_details:
                result['viewDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        self.view_details = []
        if m.get('viewDetails') is not None:
            for k1 in m.get('viewDetails'):
                temp_model = main_models.View()
                self.view_details.append(temp_model.from_map(k1))

        return self

