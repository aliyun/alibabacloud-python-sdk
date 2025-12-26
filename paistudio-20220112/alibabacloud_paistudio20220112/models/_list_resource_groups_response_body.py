# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_groups: List[main_models.ResourceGroup] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.resource_groups = resource_groups
        # This parameter is required.
        self.total_count = total_count

    def validate(self):
        if self.resource_groups:
            for v1 in self.resource_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k1 in self.resource_groups:
                result['ResourceGroups'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k1 in m.get('ResourceGroups'):
                temp_model = main_models.ResourceGroup()
                self.resource_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

