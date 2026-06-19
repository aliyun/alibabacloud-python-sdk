# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteInstancesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        force: bool = None,
        force_stop: bool = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        terminate_subscription: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # - true: sends a check request without querying resource status. The check items include whether your AccessKey pair is valid, whether Resource Access Management (RAM) user authorization is granted, and whether the required parameters are specified. If the check fails, the corresponding error is returned. If the check succeeds, the DRYRUN.SUCCESS error code is returned.
        # - false: sends a Normal request. After the check succeeds, a 2xx HTTP status code is returned and the resource status is queried directly.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # Specifies whether to forcefully release an instance that is in the **Running** (`Running`) state.
        # 
        # - true: forcefully releases ECS instance that is in the **Running** (`Running`) state.
        # - false: releases ECS instance only when it is in the **Stopped** (`Stopped`) state.
        # 
        # Default value: false.
        # >Warning: Forceful release is equivalent to powering off ECS instance. All in-memory data and temporary data in the storage are erased and cannot be recovered..
        self.force = force
        # Specifies whether to forcefully shut down the instance before release when the instance is in the **Running** (`Running`) state. This parameter takes effect only when `Force=true`. Valid values:
        # 
        # - true: forcefully shuts down and releases the instance. This is equivalent to a power-off operation. The instance directly enters the resource release process.
        # >Warning: Forceful release is equivalent to powering off the instance. All in-memory data and temporary data in the storage are erased and cannot be recovered.
        # - false: performs a standard shutdown before releasing the instance. This mode causes the release process to take several minutes. You can configure service draining actions during the operating system shutdown to reduce noise in your business systems.
        # 
        # Default value: true.
        self.force_stop = force_stop
        # The instance ID array. Array length: 1 to 100.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instances. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to release an expired subscription instance.
        # 
        # - true: releases the instance.
        # - false: does not release the instance.
        # 
        # Default value: false.
        self.terminate_subscription = terminate_subscription

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.force is not None:
            result['Force'] = self.force

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.terminate_subscription is not None:
            result['TerminateSubscription'] = self.terminate_subscription

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('TerminateSubscription') is not None:
            self.terminate_subscription = m.get('TerminateSubscription')

        return self

