# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExpressCloudConnectionRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        contact_mail: str = None,
        contact_tel: str = None,
        description: str = None,
        idcard_no: str = None,
        idc_sp: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_city: str = None,
        peer_location: str = None,
        port_type: str = None,
        redundant_ecc_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The bandwidth for ECC, which corresponds to the bandwidth for the underlying circuit.
        # 
        # Unit: Mbit/s.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The email address of the contact who applies for ECC.
        self.contact_mail = contact_mail
        # The phone number of the contact who applies for ECC.
        self.contact_tel = contact_tel
        # The description of ECC.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # The ID card number of the contact who applies for ECC.
        self.idcard_no = idcard_no
        # The Internet service provider (ISP) for the data center.
        # 
        # This parameter is required.
        self.idc_sp = idc_sp
        # The name of the ECC instance.
        # 
        # The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter but cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The city where the data center is located.
        self.peer_city = peer_city
        # The geographical location of the data center.
        # 
        # > It must be accurate to house number-floor-room number-server rack number.
        # 
        # This parameter is required.
        self.peer_location = peer_location
        # The port of the Express Connect circuit. Valid values:
        # 
        # *   100Base-T
        # *   1000Base-T
        # *   1000Base-LX
        # *   10GBase-T
        # *   10GBase-LR
        self.port_type = port_type
        # The ID of the standby Express Connect circuit.
        self.redundant_ecc_id = redundant_ecc_id
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
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail

        if self.contact_tel is not None:
            result['ContactTel'] = self.contact_tel

        if self.description is not None:
            result['Description'] = self.description

        if self.idcard_no is not None:
            result['IDCardNo'] = self.idcard_no

        if self.idc_sp is not None:
            result['IdcSP'] = self.idc_sp

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_city is not None:
            result['PeerCity'] = self.peer_city

        if self.peer_location is not None:
            result['PeerLocation'] = self.peer_location

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.redundant_ecc_id is not None:
            result['RedundantEccId'] = self.redundant_ecc_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')

        if m.get('ContactTel') is not None:
            self.contact_tel = m.get('ContactTel')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IDCardNo') is not None:
            self.idcard_no = m.get('IDCardNo')

        if m.get('IdcSP') is not None:
            self.idc_sp = m.get('IdcSP')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerCity') is not None:
            self.peer_city = m.get('PeerCity')

        if m.get('PeerLocation') is not None:
            self.peer_location = m.get('PeerLocation')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('RedundantEccId') is not None:
            self.redundant_ecc_id = m.get('RedundantEccId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

