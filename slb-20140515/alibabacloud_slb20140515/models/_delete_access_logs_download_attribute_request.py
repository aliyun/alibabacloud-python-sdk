# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAccessLogsDownloadAttributeRequest(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        logs_download_attributes: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: str = None,
    ):
        # The CLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The access log forwarding rule. Parameters:
        # 
        # *   **LogProject**: the name of the project of Log Service.
        # *   **LogStore**: the name of the Logstore of Log Service.
        # *   **LoadBalancerId**: the ID of the CLB instance.
        # 
        # This parameter is required.
        self.logs_download_attributes = logs_download_attributes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the CLB instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags that are added to the CLB instance. The tags must be key-value pairs that are contained in a JSON dictionary.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.logs_download_attributes is not None:
            result['LogsDownloadAttributes'] = self.logs_download_attributes

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

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LogsDownloadAttributes') is not None:
            self.logs_download_attributes = m.get('LogsDownloadAttributes')

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

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

