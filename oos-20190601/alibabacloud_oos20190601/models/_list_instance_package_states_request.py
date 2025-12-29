# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancePackageStatesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        template_names: str = None,
    ):
        # ECS instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Page size.
        self.max_results = max_results
        # Pagination token.
        self.next_token = next_token
        # Region ID.
        self.region_id = region_id
        # List of extension names
        self.template_names = template_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_names is not None:
            result['TemplateNames'] = self.template_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateNames') is not None:
            self.template_names = m.get('TemplateNames')

        return self

