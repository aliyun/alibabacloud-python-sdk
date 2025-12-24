# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeploymentSetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deployment_set_name: str = None,
        description: str = None,
        domain: str = None,
        granularity: str = None,
        group_count: int = None,
        on_unable_to_redeploy_failed_instance: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        strategy: str = None,
    ):
        # The description of the deployment set. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.client_token = client_token
        # The name of the deployment set. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain digits, letters, colons (:), underscores (_), and hyphens (-).
        self.deployment_set_name = deployment_set_name
        # The emergency solution to use in the situation where instances in the deployment set cannot be evenly distributed to different zones due to resource insufficiency after the instances failover. Valid values:
        # 
        # *   CancelMembershipAndStart: removes the instances from the deployment set and starts the instances immediately after they are failed over.
        # *   KeepStopped: leaves the instances in the Stopped state and starts them after resources are replenished.
        # 
        # Default value: CancelMembershipAndStart.
        self.description = description
        # >  This parameter is deprecated.
        self.domain = domain
        # >  This parameter is deprecated.
        self.granularity = granularity
        # The deployment strategy. Valid values:
        # 
        # *   Availability: high availability strategy.
        # *   AvailabilityGroup: high availability group strategy.
        # 
        # Default value: Availability.
        self.group_count = group_count
        # The region ID of the deployment set. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent list of regions.
        self.on_unable_to_redeploy_failed_instance = on_unable_to_redeploy_failed_instance
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Creates a deployment set in a specific region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The deployment strategy. Valid values:
        # 
        # *   Availability: high availability strategy
        # *   AvailabilityGroup: high availability group strategy
        # *   LowLatency: low latency strategy
        # 
        # Default value: Availability.
        self.strategy = strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deployment_set_name is not None:
            result['DeploymentSetName'] = self.deployment_set_name

        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.on_unable_to_redeploy_failed_instance is not None:
            result['OnUnableToRedeployFailedInstance'] = self.on_unable_to_redeploy_failed_instance

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeploymentSetName') is not None:
            self.deployment_set_name = m.get('DeploymentSetName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('OnUnableToRedeployFailedInstance') is not None:
            self.on_unable_to_redeploy_failed_instance = m.get('OnUnableToRedeployFailedInstance')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

