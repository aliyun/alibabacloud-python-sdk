# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDeploymentSetsRequest(DaraModel):
    def __init__(
        self,
        deployment_set_ids: str = None,
        deployment_set_name: str = None,
        domain: str = None,
        granularity: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        strategy: str = None,
        type: str = None,
    ):
        # The IDs of the deployment sets. The value can be a JSON array that consists of up to 100 deployment set IDs. Sample format: `["ds-xxxxxxxxx", "ds-yyyyyyyyy", … "ds-zzzzzzzzz"]`.
        self.deployment_set_ids = deployment_set_ids
        # The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.deployment_set_name = deployment_set_name
        # > This parameter is deprecated.
        self.domain = domain
        # > This parameter is deprecated.
        self.granularity = granularity
        # > This parameter is deprecated.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number.
        # 
        # Starts at 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The ID of the region where the deployment set is located. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The deployment strategy. Valid values:
        # 
        # - Availability: high availability strategy.
        # 
        # - AvailabilityGroup: high availability group strategy.
        # 
        # - LowLatency: low-latency strategy.
        self.strategy = strategy
        # The deployment type. Valid values:
        # 
        # - host: Ensures that the instances in the deployment set are deployed on different hosts.
        # 
        # - sw: Ensures that the instances in the deployment set are deployed on different switches.
        # 
        # - rack: Ensures that the instances in the deployment set are deployed on different racks.
        # 
        # Default value: host.
        self.type = type

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

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetIds') is not None:
            self.deployment_set_ids = m.get('DeploymentSetIds')

        if m.get('DeploymentSetName') is not None:
            self.deployment_set_name = m.get('DeploymentSetName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

