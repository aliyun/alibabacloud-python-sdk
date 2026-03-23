# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCDeploymentSetsRequest(DaraModel):
    def __init__(
        self,
        deployment_set_ids: str = None,
        deployment_set_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        strategy: str = None,
        tag: str = None,
    ):
        self.deployment_set_ids = deployment_set_ids
        self.deployment_set_name = deployment_set_name
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.strategy = strategy
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_set_ids is not None:
            result['DeploymentSetIds'] = self.deployment_set_ids

        if self.deployment_set_name is not None:
            result['DeploymentSetName'] = self.deployment_set_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetIds') is not None:
            self.deployment_set_ids = m.get('DeploymentSetIds')

        if m.get('DeploymentSetName') is not None:
            self.deployment_set_name = m.get('DeploymentSetName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

