# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyExpressCloudConnectionAttributeRequest(DaraModel):
    def __init__(
        self,
        bgp_as: str = None,
        ce_ip: str = None,
        description: str = None,
        ecc_id: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pe_ip: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The BGP autonomous system number (ASN) to be configured for the Smart Access Gateway (SAG) device.
        self.bgp_as = bgp_as
        # The peer IP address when the SAG device is connected to the cloud.
        self.ce_ip = ce_ip
        # Descriptions of ECC.
        self.description = description
        # The ID of the ECC instance.
        # 
        # This parameter is required.
        self.ecc_id = ecc_id
        # The name of the ECC instance.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The on-premises IP address when the SAG device is connected to the cloud.
        self.pe_ip = pe_ip
        # The region ID of the ECC instance.
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
        if self.bgp_as is not None:
            result['BgpAs'] = self.bgp_as

        if self.ce_ip is not None:
            result['CeIp'] = self.ce_ip

        if self.description is not None:
            result['Description'] = self.description

        if self.ecc_id is not None:
            result['EccId'] = self.ecc_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pe_ip is not None:
            result['PeIp'] = self.pe_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpAs') is not None:
            self.bgp_as = m.get('BgpAs')

        if m.get('CeIp') is not None:
            self.ce_ip = m.get('CeIp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EccId') is not None:
            self.ecc_id = m.get('EccId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeIp') is not None:
            self.pe_ip = m.get('PeIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

