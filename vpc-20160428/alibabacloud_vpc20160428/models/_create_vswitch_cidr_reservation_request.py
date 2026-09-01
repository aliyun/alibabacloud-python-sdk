# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateVSwitchCidrReservationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ip_prefix_number: int = None,
        ip_version: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateVSwitchCidrReservationRequestTag] = None,
        v_switch_cidr_reservation_cidr: str = None,
        v_switch_cidr_reservation_description: str = None,
        v_switch_cidr_reservation_mask: str = None,
        v_switch_cidr_reservation_name: str = None,
        v_switch_cidr_reservation_type: str = None,
        v_switch_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # - **true**: sends a check request without creating the reserved CIDR block for a vSwitch. The system checks whether the required parameters are specified, the request format is valid, and the service limits are not exceeded. If the check fails, the corresponding error message is returned. If the check passes, the `DryRunOperation` error code is returned.
        # - **false** (default): sends a Normal request. After the check passes, an HTTP 2xx status code is returned and the vSwitch reserved CIDR block for a vSwitch is created.
        self.dry_run = dry_run
        # The expected number of IP prefixes to reserve. Valid values: 1 to 32.
        self.ip_prefix_number = ip_prefix_number
        # The IP version of the reserved CIDR block for a vSwitch. Valid values:
        # 
        # - **IPv4** (default)
        # - **IPv6**
        # 
        # > You do not need to specify this parameter when creating an IPv4 reserved CIDR block for a vSwitch. This parameter is required when creating an IPv6 reserved CIDR block for a vSwitch.
        self.ip_version = ip_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the vSwitch.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource tags.
        self.tag = tag
        # The reserved CIDR block for a vSwitch.
        # 
        # - If **IpVersion** is set to **IPv4**, the reserved CIDR block for a vSwitch must be a proper subset of the IPv4 CIDR block of the vSwitch, and the mask length cannot exceed 28.
        # - If **IpVersion** is set to **IPv6**, the reserved CIDR block for a vSwitch must be a proper subset of the IPv6 CIDR block of the vSwitch, and the mask length cannot exceed 80.
        # 
        # > - You must specify either the **VSwitchCidrReservationMask** parameter or the **VSwitchCidrReservationCidr** parameter.
        # > - The reserved CIDR block cannot contain the system reserved IP addresses of the vSwitch.
        self.v_switch_cidr_reservation_cidr = v_switch_cidr_reservation_cidr
        # The description of the reserved CIDR block for a vSwitch. If you leave this parameter empty, the default value is empty.
        # 
        # The description must be 1 to 256 characters in length and must start with a letter or Chinese character. It cannot start with `http://` or `https://`.
        self.v_switch_cidr_reservation_description = v_switch_cidr_reservation_description
        # The mask of the reserved CIDR block for a vSwitch.
        # 
        # - If **IpVersion** is set to **IPv4**, the mask length of the reserved CIDR block must be at least 2 bits longer than the IPv4 CIDR block mask of the vSwitch and cannot exceed 28.
        # - If **IpVersion** is set to **IPv6**, the mask length of the reserved CIDR block must be longer than the IPv6 CIDR block mask of the vSwitch and cannot exceed 80.
        # 
        # > - You must specify either the **VSwitchCidrReservationMask** parameter or the **VSwitchCidrReservationCidr** parameter.
        # > - The reserved CIDR block cannot contain the system reserved IP addresses of the vSwitch.
        self.v_switch_cidr_reservation_mask = v_switch_cidr_reservation_mask
        # The name of the reserved CIDR block for a vSwitch.
        # 
        # The name must be 1 to 128 characters in length and must start with a letter or Chinese character. It can contain digits, underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        self.v_switch_cidr_reservation_name = v_switch_cidr_reservation_name
        # The type of the reserved CIDR block for a vSwitch. Valid values: **prefix**, which indicates that IP addresses are allocated by CIDR block.
        # 
        # > When users or cloud services automatically assign CIDR blocks to elastic network interfaces (ENIs), the CIDR blocks must be allocated from the reserved CIDR block for a vSwitch. If the IP addresses in the reserved CIDR block for a vSwitch are exhausted, the system returns an error.
        self.v_switch_cidr_reservation_type = v_switch_cidr_reservation_type
        # The ID of the vSwitch for which you want to create a reserved CIDR block for a vSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ip_prefix_number is not None:
            result['IpPrefixNumber'] = self.ip_prefix_number

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

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

        if self.v_switch_cidr_reservation_cidr is not None:
            result['VSwitchCidrReservationCidr'] = self.v_switch_cidr_reservation_cidr

        if self.v_switch_cidr_reservation_description is not None:
            result['VSwitchCidrReservationDescription'] = self.v_switch_cidr_reservation_description

        if self.v_switch_cidr_reservation_mask is not None:
            result['VSwitchCidrReservationMask'] = self.v_switch_cidr_reservation_mask

        if self.v_switch_cidr_reservation_name is not None:
            result['VSwitchCidrReservationName'] = self.v_switch_cidr_reservation_name

        if self.v_switch_cidr_reservation_type is not None:
            result['VSwitchCidrReservationType'] = self.v_switch_cidr_reservation_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpPrefixNumber') is not None:
            self.ip_prefix_number = m.get('IpPrefixNumber')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

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
                temp_model = main_models.CreateVSwitchCidrReservationRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchCidrReservationCidr') is not None:
            self.v_switch_cidr_reservation_cidr = m.get('VSwitchCidrReservationCidr')

        if m.get('VSwitchCidrReservationDescription') is not None:
            self.v_switch_cidr_reservation_description = m.get('VSwitchCidrReservationDescription')

        if m.get('VSwitchCidrReservationMask') is not None:
            self.v_switch_cidr_reservation_mask = m.get('VSwitchCidrReservationMask')

        if m.get('VSwitchCidrReservationName') is not None:
            self.v_switch_cidr_reservation_name = m.get('VSwitchCidrReservationName')

        if m.get('VSwitchCidrReservationType') is not None:
            self.v_switch_cidr_reservation_type = m.get('VSwitchCidrReservationType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class CreateVSwitchCidrReservationRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. If you specify this parameter, the value cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. If you specify this parameter, the value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain `http://` or `https://`.
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

