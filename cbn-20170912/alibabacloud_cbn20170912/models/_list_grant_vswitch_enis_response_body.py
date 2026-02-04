# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListGrantVSwitchEnisResponseBody(DaraModel):
    def __init__(
        self,
        grant_vswitch_enis: List[main_models.ListGrantVSwitchEnisResponseBodyGrantVSwitchEnis] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The information about the ENI.
        self.grant_vswitch_enis = grant_vswitch_enis
        # The total number of entries returned.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        # 
        # > If MaxResults and NextToken are sued to query results by page, ignore this parameter.
        self.total_count = total_count

    def validate(self):
        if self.grant_vswitch_enis:
            for v1 in self.grant_vswitch_enis:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GrantVSwitchEnis'] = []
        if self.grant_vswitch_enis is not None:
            for k1 in self.grant_vswitch_enis:
                result['GrantVSwitchEnis'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grant_vswitch_enis = []
        if m.get('GrantVSwitchEnis') is not None:
            for k1 in m.get('GrantVSwitchEnis'):
                temp_model = main_models.ListGrantVSwitchEnisResponseBodyGrantVSwitchEnis()
                self.grant_vswitch_enis.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListGrantVSwitchEnisResponseBodyGrantVSwitchEnis(DaraModel):
    def __init__(
        self,
        description: str = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
        primary_ip_address: str = None,
        transit_router_flag: bool = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The ENI description.
        self.description = description
        # The ENI ID.
        self.network_interface_id = network_interface_id
        # The ENI name.
        self.network_interface_name = network_interface_name
        # The primary private IPv4 address of the ENI.
        self.primary_ip_address = primary_ip_address
        # Indicates whether the ENI is created by a transit router. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # ENIs that are created by transit routers cannot be used as multicast sources or members.
        self.transit_router_flag = transit_router_flag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.transit_router_flag is not None:
            result['TransitRouterFlag'] = self.transit_router_flag

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('TransitRouterFlag') is not None:
            self.transit_router_flag = m.get('TransitRouterFlag')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

