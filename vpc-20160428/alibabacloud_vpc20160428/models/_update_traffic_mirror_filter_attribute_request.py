# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTrafficMirrorFilterAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_mirror_filter_description: str = None,
        traffic_mirror_filter_id: str = None,
        traffic_mirror_filter_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** value as the **ClientToken** value. The **RequestId** value of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without modifying the configuration of the traffic mirror filter. The system checks the required parameters, request format, and business restrictions. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): sends a normal request. If the request passes the dry run, a 2xx HTTP status code is returned and the configuration of the traffic mirror filter is modified.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the traffic mirror filter.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list. For more information about the regions that support traffic mirroring, see [Traffic mirroring overview](https://help.aliyun.com/document_detail/207513.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new description of the traffic mirror filter.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.traffic_mirror_filter_description = traffic_mirror_filter_description
        # The instance ID of the traffic mirror filter.
        # 
        # This parameter is required.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        # The new name of the traffic mirror filter.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.traffic_mirror_filter_name = traffic_mirror_filter_name

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

        if self.traffic_mirror_filter_description is not None:
            result['TrafficMirrorFilterDescription'] = self.traffic_mirror_filter_description

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        if self.traffic_mirror_filter_name is not None:
            result['TrafficMirrorFilterName'] = self.traffic_mirror_filter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        if m.get('TrafficMirrorFilterDescription') is not None:
            self.traffic_mirror_filter_description = m.get('TrafficMirrorFilterDescription')

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        if m.get('TrafficMirrorFilterName') is not None:
            self.traffic_mirror_filter_name = m.get('TrafficMirrorFilterName')

        return self

