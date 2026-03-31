# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeApisecSlsProjectsResponseBody(DaraModel):
    def __init__(
        self,
        projects: List[str] = None,
        request_id: str = None,
    ):
        # The names of the projects in Simple Log Service.
        self.projects = projects
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.projects is not None:
            result['Projects'] = self.projects

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Projects') is not None:
            self.projects = m.get('Projects')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

