# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationGroupsRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        deploy_region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_product: str = None,
        resource_type: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The ID of the region in which the related resources reside.
        self.deploy_region_id = deploy_region_id
        # The number of entries to return on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The ID of the cloud resource.
        self.resource_id = resource_id
        # The code of the product to which the cloud resource belongs.
        self.resource_product = resource_product
        # The type of the cloud resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

