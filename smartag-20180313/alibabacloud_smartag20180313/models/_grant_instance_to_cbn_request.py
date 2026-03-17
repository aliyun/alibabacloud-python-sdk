# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantInstanceToCbnRequest(DaraModel):
    def __init__(
        self,
        ccn_instance_id: str = None,
        cen_instance_id: str = None,
        cen_uid: int = None,
        grant_traffic_service: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the CCN instance.
        # 
        # This parameter is required.
        self.ccn_instance_id = ccn_instance_id
        # The ID of the CEN instance.
        # 
        # This parameter is required.
        self.cen_instance_id = cen_instance_id
        # The ID of the Alibaba Cloud account to which the CEN instance belongs.
        # 
        # This parameter is required.
        self.cen_uid = cen_uid
        # Specifies whether to grant the CEN instance permissions to manage network traffic from the CCN instance. Valid values:
        # 
        # *   **true**: grants permissions.
        # *   **false**: does not grant permissions. This is the default value.
        # 
        # >  If you set the value to true and the SAG instance connected to the CCN instance has the secure rerouting feature enabled, you cannot revoke the permissions.
        self.grant_traffic_service = grant_traffic_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the CCN instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.htmll) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ccn_instance_id is not None:
            result['CcnInstanceId'] = self.ccn_instance_id

        if self.cen_instance_id is not None:
            result['CenInstanceId'] = self.cen_instance_id

        if self.cen_uid is not None:
            result['CenUid'] = self.cen_uid

        if self.grant_traffic_service is not None:
            result['GrantTrafficService'] = self.grant_traffic_service

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcnInstanceId') is not None:
            self.ccn_instance_id = m.get('CcnInstanceId')

        if m.get('CenInstanceId') is not None:
            self.cen_instance_id = m.get('CenInstanceId')

        if m.get('CenUid') is not None:
            self.cen_uid = m.get('CenUid')

        if m.get('GrantTrafficService') is not None:
            self.grant_traffic_service = m.get('GrantTrafficService')

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

        return self

