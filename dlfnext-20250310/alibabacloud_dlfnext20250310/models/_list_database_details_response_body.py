# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class ListDatabaseDetailsResponseBody(DaraModel):
    def __init__(
        self,
        database_details: List[main_models.Database] = None,
        next_page_token: str = None,
    ):
        self.database_details = database_details
        self.next_page_token = next_page_token

    def validate(self):
        if self.database_details:
            for v1 in self.database_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['databaseDetails'] = []
        if self.database_details is not None:
            for k1 in self.database_details:
                result['databaseDetails'].append(k1.to_map() if k1 else None)

        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_details = []
        if m.get('databaseDetails') is not None:
            for k1 in m.get('databaseDetails'):
                temp_model = main_models.Database()
                self.database_details.append(temp_model.from_map(k1))

        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        return self

