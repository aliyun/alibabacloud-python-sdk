# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ApplyPhysicalConnectionLOARequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        company_name: str = None,
        construction_time: str = None,
        instance_id: str = None,
        line_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pminfo: List[main_models.ApplyPhysicalConnectionLOARequestPMInfo] = None,
        peer_location: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        si: str = None,
    ):
        # The bandwidth of the Express Connect circuit. Unit: Mbit/s.
        # 
        # Valid values: **2** to **10240**.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The name of the customer company that requires the Express Connect circuit.
        # 
        # This parameter is required.
        self.company_name = company_name
        # The time when construction started. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        # 
        # This parameter is required.
        self.construction_time = construction_time
        # The ID of the Express Connect circuit.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the Express Connect circuit. Valid values:
        # 
        # *   **MSTP**: MSTP line
        # *   **MPLSVPN**: MPLSVPN line
        # *   **FIBRE**: fiber line
        # *   **Other**: other types
        # 
        # This parameter is required.
        self.line_type = line_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The information about the construction engineer.
        self.pminfo = pminfo
        # The geographic location where the Express Connect circuit is deployed.
        self.peer_location = peer_location
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The construction company.
        # 
        # This parameter is required.
        self.si = si

    def validate(self):
        if self.pminfo:
            for v1 in self.pminfo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.construction_time is not None:
            result['ConstructionTime'] = self.construction_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.line_type is not None:
            result['LineType'] = self.line_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['PMInfo'] = []
        if self.pminfo is not None:
            for k1 in self.pminfo:
                result['PMInfo'].append(k1.to_map() if k1 else None)

        if self.peer_location is not None:
            result['PeerLocation'] = self.peer_location

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.si is not None:
            result['Si'] = self.si

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('ConstructionTime') is not None:
            self.construction_time = m.get('ConstructionTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LineType') is not None:
            self.line_type = m.get('LineType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.pminfo = []
        if m.get('PMInfo') is not None:
            for k1 in m.get('PMInfo'):
                temp_model = main_models.ApplyPhysicalConnectionLOARequestPMInfo()
                self.pminfo.append(temp_model.from_map(k1))

        if m.get('PeerLocation') is not None:
            self.peer_location = m.get('PeerLocation')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Si') is not None:
            self.si = m.get('Si')

        return self

class ApplyPhysicalConnectionLOARequestPMInfo(DaraModel):
    def __init__(
        self,
        pmcertificate_no: str = None,
        pmcertificate_type: str = None,
        pmcontact_info: str = None,
        pmgender: str = None,
        pmname: str = None,
    ):
        # The ID number of the construction engineer. You can specify the ID number of an ID card or an international passport.
        # 
        # You can configure information for up to 16 construction engineers.
        self.pmcertificate_no = pmcertificate_no
        # The type of the identity document of the construction engineer. Valid values:
        # 
        # *   **IDCard**
        # *   **Passport**
        self.pmcertificate_type = pmcertificate_type
        # The contact information about the construction engineer.
        self.pmcontact_info = pmcontact_info
        # The gender of the construction engineer.
        self.pmgender = pmgender
        # The name of the construction engineer.
        self.pmname = pmname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pmcertificate_no is not None:
            result['PMCertificateNo'] = self.pmcertificate_no

        if self.pmcertificate_type is not None:
            result['PMCertificateType'] = self.pmcertificate_type

        if self.pmcontact_info is not None:
            result['PMContactInfo'] = self.pmcontact_info

        if self.pmgender is not None:
            result['PMGender'] = self.pmgender

        if self.pmname is not None:
            result['PMName'] = self.pmname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PMCertificateNo') is not None:
            self.pmcertificate_no = m.get('PMCertificateNo')

        if m.get('PMCertificateType') is not None:
            self.pmcertificate_type = m.get('PMCertificateType')

        if m.get('PMContactInfo') is not None:
            self.pmcontact_info = m.get('PMContactInfo')

        if m.get('PMGender') is not None:
            self.pmgender = m.get('PMGender')

        if m.get('PMName') is not None:
            self.pmname = m.get('PMName')

        return self

