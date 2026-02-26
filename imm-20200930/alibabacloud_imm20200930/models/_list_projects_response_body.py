# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ListProjectsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        projects: List[main_models.Project] = None,
        request_id: str = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The projects.
        self.projects = projects
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.projects:
            for v1 in self.projects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['Projects'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.projects = []
        if m.get('Projects') is not None:
            for k1 in m.get('Projects'):
                temp_model = main_models.Project()
                self.projects.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

