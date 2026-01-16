# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ListTaggedResourcesOutput(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        resources: List[main_models.Resource] = None,
    ):
        self.next_token = next_token
        self.resources = resources

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
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.resources = []
        if m.get('resources') is not None:
            for k1 in m.get('resources'):
                temp_model = main_models.Resource()
                self.resources.append(temp_model.from_map(k1))

        return self

