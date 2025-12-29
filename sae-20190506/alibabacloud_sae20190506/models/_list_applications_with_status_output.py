# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsWithStatusOutput(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ApplicationWithStatus] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.applications = applications
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['applications'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('applications') is not None:
            for k1 in m.get('applications'):
                temp_model = main_models.ApplicationWithStatus()
                self.applications.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

