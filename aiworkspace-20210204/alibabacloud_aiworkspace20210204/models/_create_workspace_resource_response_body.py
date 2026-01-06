# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateWorkspaceResourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[main_models.CreateWorkspaceResourceResponseBodyResources] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resources = resources
        # The total number of resources.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.CreateWorkspaceResourceResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class CreateWorkspaceResourceResponseBodyResources(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The resource ID.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

