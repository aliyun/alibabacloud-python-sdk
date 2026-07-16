# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeploymentSetRequest(DaraModel):
    def __init__(
        self,
        affinity: int = None,
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
        type: str = None,
    ):
        # The affinity level of the deployment set. This level determines how instances are distributed within the set. The value must be an integer from 1 to 10. Default value: 1.
        self.affinity = affinity
        # A client-generated token that you can use to ensure request idempotence. The token must be unique across requests.
        # 
        # The **ClientToken** value must be an ASCII string of up to 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The name of the deployment set. The name must be 2 to 128 characters long and start with a letter. It can contain digits, colons (:), underscores (_), and hyphens (-). The name cannot start with `http://` or `https://`.
        self.deployment_set_name = deployment_set_name
        # The description of the deployment set. The description must be 2 to 256 characters long and cannot start with `http://` or `https://`.
        self.description = description
        # > This parameter is deprecated.
        self.domain = domain
        # > This parameter is deprecated.
        self.granularity = granularity
        # The number of partitions in the deployment set group. Valid values: 1 to 7.
        # 
        # Default value: 3.
        # 
        # > This parameter is valid only when `Strategy` is set to `AvailabilityGroup`.
        self.group_count = group_count
        # The policy for an instance that fails to be redeployed after a failover due to insufficient resources. Valid values:
        # 
        # - CancelMembershipAndStart: Removes the instance from the deployment set and starts the instance immediately after failover.
        # 
        # - KeepStopped: Keeps the instance in the deployment set and in the Stopped state.
        # 
        # Default value: CancelMembershipAndStart.
        self.on_unable_to_redeploy_failed_instance = on_unable_to_redeploy_failed_instance
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region for the deployment set. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The deployment strategy. Valid values:
        # 
        # - Availability: High availability strategy.
        # 
        # - AvailabilityGroup: High availability strategy for deployment set groups.
        # 
        # - LowLatency: Low-latency strategy.
        # 
        # Default value: Availability.
        self.strategy = strategy
        # The deployment granularity. Valid values:
        # 
        # - host: Spreads instances across different hosts.
        # 
        # - sw: Spreads instances across different switches.
        # 
        # - rack: Spreads instances across different racks.
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
        if self.affinity is not None:
            result['Affinity'] = self.affinity

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

