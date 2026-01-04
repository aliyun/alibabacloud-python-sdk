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
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run, without performing the actual request. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The IP version of the reserved CIDR block. Valid values:
        # 
        # *   **IPv4** (default)
        # *   **IPv6**
        self.ip_version = ip_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the vSwitch is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Resource tags
        self.tag = tag
        # The reserved CIDR block of the vSwitch.
        # 
        # *   When **IpVersion** is set to **IPv4**, the reserved CIDR block must be a proper subset of the IPv4 CIDR block of the vSwitch and the subnet mask length of the reserved CIDR block cannot be greater than 28.
        # *   When **IpVersion** is set to **IPv6**, the reserved CIDR block must be a proper subset of the IPv6 CIDR block of the vSwitch and the subnet mask length of the reserved CIDR block cannot be greater than 80.
        # 
        # >  You must specify one of **VSwitchCidrReservationMask** and **VSwitchCidrReservationCidr**.
        self.v_switch_cidr_reservation_cidr = v_switch_cidr_reservation_cidr
        # The description of the reserved CIDR block. This parameter is empty by default.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter and cannot start with `http://` or `https://`.
        self.v_switch_cidr_reservation_description = v_switch_cidr_reservation_description
        # The subnet mask of the reserved CIDR block.
        # 
        # *   When **IpVersion** is set to **IPv4**, the subnet mask length of the CIDR block must be greater than the IPv4 subnet mask length of the vSwitch and cannot be greater than 28.
        # *   When **IpVersion** is set to **IPv6**, the subnet mask length of the CIDR block must be greater than the IPv6 subnet mask length of the vSwitch and cannot be greater than 80.
        # 
        # >  You must specify one of **VSwitchCidrReservationMask** and **VSwitchCidrReservationCidr**.
        self.v_switch_cidr_reservation_mask = v_switch_cidr_reservation_mask
        # The name of the reserved CIDR block.
        # 
        # The name must be 2 to 128 characters in length and can contain digits, underscores (_), and hyphens (-). It must start with a letter.
        self.v_switch_cidr_reservation_name = v_switch_cidr_reservation_name
        # The type of reserved CIDR block. Set the value to **prefix**.
        # 
        # >  When a user or a cloud service allocates a CIDR block to an elastic network interface (ENI), the CIDR block must be allocated from the reserved CIDR block. If the reserved CIDR block is exhausted, an error is returned.
        self.v_switch_cidr_reservation_type = v_switch_cidr_reservation_type
        # The ID of the vSwitch to which the reserved CIDR block belongs.
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
        # The key of tag N to add to the resource. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The value of tag N to add to the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain http:// or https://.
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

