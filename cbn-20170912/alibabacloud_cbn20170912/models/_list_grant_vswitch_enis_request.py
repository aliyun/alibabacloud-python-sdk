# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListGrantVSwitchEnisRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        max_results: int = None,
        network_interface_id: List[str] = None,
        network_interface_name: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        primary_ip_address: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of the CEN instance to which the VPC is attached.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The number of entries to return on each page. Valid values: 10 to 500.
        # 
        # Default value:
        # 
        # *   If you do not specify a value, the default value is 20.
        # *   If this parameter is set to a value greater than 500, the default value is 500.
        self.max_results = max_results
        # The ID of ENI N. Valid values of N: 1 to 100.
        self.network_interface_id = network_interface_id
        # The name of the ENI.
        self.network_interface_name = network_interface_name
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The primary private IPv4 address of the ENI.
        self.primary_ip_address = primary_ip_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of a vSwitch in the VPC. You can specify only one vSwitch in each call.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

