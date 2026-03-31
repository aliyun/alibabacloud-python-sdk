# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeTemplateResourceCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_count: List[main_models.DescribeTemplateResourceCountResponseBodyResourceCount] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The number of protected objects or protected object groups for which the protection template takes effect.
        self.resource_count = resource_count

    def validate(self):
        if self.resource_count:
            for v1 in self.resource_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceCount'] = []
        if self.resource_count is not None:
            for k1 in self.resource_count:
                result['ResourceCount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_count = []
        if m.get('ResourceCount') is not None:
            for k1 in m.get('ResourceCount'):
                temp_model = main_models.DescribeTemplateResourceCountResponseBodyResourceCount()
                self.resource_count.append(temp_model.from_map(k1))

        return self

class DescribeTemplateResourceCountResponseBodyResourceCount(DaraModel):
    def __init__(
        self,
        asset_count: int = None,
        group_count: int = None,
        single_count: int = None,
        template_id: int = None,
    ):
        self.asset_count = asset_count
        # The number of protected object groups.
        self.group_count = group_count
        # The number of protected objects.
        self.single_count = single_count
        # The ID of the protection template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.single_count is not None:
            result['SingleCount'] = self.single_count

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('SingleCount') is not None:
            self.single_count = m.get('SingleCount')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

