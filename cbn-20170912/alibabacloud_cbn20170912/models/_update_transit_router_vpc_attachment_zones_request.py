# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class UpdateTransitRouterVpcAttachmentZonesRequest(DaraModel):
    def __init__(
        self,
        add_zone_mappings: List[main_models.UpdateTransitRouterVpcAttachmentZonesRequestAddZoneMappings] = None,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        remove_zone_mappings: List[main_models.UpdateTransitRouterVpcAttachmentZonesRequestRemoveZoneMappings] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_attachment_id: str = None,
    ):
        # The zones and vSwitches that you want to add to the VPC connection.
        self.add_zone_mappings = add_zone_mappings
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, ClientToken is set to the value of RequestId. The value of RequestId for each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The zones and vSwitches that you want to remove from the VPC connection.
        self.remove_zone_mappings = remove_zone_mappings
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the VPC connection.
        # 
        # This parameter is required.
        self.transit_router_attachment_id = transit_router_attachment_id

    def validate(self):
        if self.add_zone_mappings:
            for v1 in self.add_zone_mappings:
                 if v1:
                    v1.validate()
        if self.remove_zone_mappings:
            for v1 in self.remove_zone_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddZoneMappings'] = []
        if self.add_zone_mappings is not None:
            for k1 in self.add_zone_mappings:
                result['AddZoneMappings'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['RemoveZoneMappings'] = []
        if self.remove_zone_mappings is not None:
            for k1 in self.remove_zone_mappings:
                result['RemoveZoneMappings'].append(k1.to_map() if k1 else None)

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_zone_mappings = []
        if m.get('AddZoneMappings') is not None:
            for k1 in m.get('AddZoneMappings'):
                temp_model = main_models.UpdateTransitRouterVpcAttachmentZonesRequestAddZoneMappings()
                self.add_zone_mappings.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.remove_zone_mappings = []
        if m.get('RemoveZoneMappings') is not None:
            for k1 in m.get('RemoveZoneMappings'):
                temp_model = main_models.UpdateTransitRouterVpcAttachmentZonesRequestRemoveZoneMappings()
                self.remove_zone_mappings.append(temp_model.from_map(k1))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        return self

class UpdateTransitRouterVpcAttachmentZonesRequestRemoveZoneMappings(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the vSwitch that you want to remove from the VPC connection.
        # 
        # You can remove at most 10 vSwitches from a VPC in each call.
        self.v_switch_id = v_switch_id
        # The ID of the zone where the vSwitch that you want to remove from the VPC connection is deployed.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class UpdateTransitRouterVpcAttachmentZonesRequestAddZoneMappings(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the vSwitch that you want to add to the VPC connection.
        # 
        # You can specify at most 10 vSwitches in each call.
        # 
        # *   If the VPC connection belongs to the current Alibaba Cloud account, you can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation to query the IDs of the vSwitches and zones of the VPC.
        # *   If the VPC connection belongs to another Alibaba Cloud account, you can call the [ListGrantVSwitchesToCen](https://help.aliyun.com/document_detail/427599.html) operation to query the IDs of the vSwitches and zones of the VPC.
        self.v_switch_id = v_switch_id
        # The ID of the zone where the vSwitch that you want to add to the VPC connection is deployed.
        # 
        # You can specify at most 10 vSwitches in each call.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

