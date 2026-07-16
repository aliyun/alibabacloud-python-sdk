# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateTransitRouterVpnAttachmentRequest(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        cen_id: str = None,
        charge_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateTransitRouterVpnAttachmentRequestTag] = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_name: str = None,
        transit_router_id: str = None,
        vpn_id: str = None,
        vpn_owner_id: int = None,
        zone: List[main_models.CreateTransitRouterVpnAttachmentRequestZone] = None,
    ):
        # Specifies whether to enable the transit router to automatically publish routes to the IPsec-VPN connection. Valid values:
        # 
        # - **true** (default): enabled.
        # 
        # - **false**: disabled.
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The billing method.
        # 
        # The value is set to **POSTPAY** (default), which specifies the pay-as-you-go billing method.
        self.charge_type = charge_type
        # A client token that is used to ensure the idempotence of the request.
        # 
        # Generate a unique token on your client. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run but does not create the VPN connection. The system checks the request for required parameters, format, and service limits. If the request fails the check, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): performs a dry run and creates the VPN connection if the request passes the check.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the transit router instance is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # The description of the VPN connection.
        # 
        # The description can be empty or 1 to 256 characters in length, and cannot start with \\`http\\://\\` or \\`https\\://\\`.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The name of the VPN connection.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with \\`http\\://\\` or \\`https\\://\\`.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The ID of the transit router instance.
        self.transit_router_id = transit_router_id
        # The ID of the IPsec-VPN connection.
        # 
        # This parameter is required.
        self.vpn_id = vpn_id
        # The ID of the Alibaba Cloud account to which the IPsec-VPN connection belongs.
        # 
        # - If you do not specify this parameter, the ID of the current Alibaba Cloud account is used.
        # 
        # - This parameter is required if you want to connect to a cross-account IPsec-VPN connection.
        self.vpn_owner_id = vpn_owner_id
        # The ID of the zone in the current region.
        # 
        # The system creates resources in the specified zone.
        # 
        # > Do not specify this parameter if the attached IPsec-VPN connection is in dual-tunnel mode.
        self.zone = zone

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.zone:
            for v1 in self.zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description

        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.vpn_id is not None:
            result['VpnId'] = self.vpn_id

        if self.vpn_owner_id is not None:
            result['VpnOwnerId'] = self.vpn_owner_id

        result['Zone'] = []
        if self.zone is not None:
            for k1 in self.zone:
                result['Zone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTransitRouterVpnAttachmentRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')

        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('VpnId') is not None:
            self.vpn_id = m.get('VpnId')

        if m.get('VpnOwnerId') is not None:
            self.vpn_owner_id = m.get('VpnOwnerId')

        self.zone = []
        if m.get('Zone') is not None:
            for k1 in m.get('Zone'):
                temp_model = main_models.CreateTransitRouterVpnAttachmentRequestZone()
                self.zone.append(temp_model.from_map(k1))

        return self

class CreateTransitRouterVpnAttachmentRequestZone(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        # The zone ID.
        # 
        # You can call the [ListTransitRouterAvailableResource](https://help.aliyun.com/document_detail/261356.html) operation to query available zones.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateTransitRouterVpnAttachmentRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot be an empty string. It can be up to 64 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # The tag value can be an empty string or a string of up to 128 characters. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag values.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

