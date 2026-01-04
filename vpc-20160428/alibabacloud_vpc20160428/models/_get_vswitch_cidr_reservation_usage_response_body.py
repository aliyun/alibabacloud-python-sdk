# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetVSwitchCidrReservationUsageResponseBody(DaraModel):
    def __init__(
        self,
        cidr_reservation_usages: List[main_models.GetVSwitchCidrReservationUsageResponseBodyCidrReservationUsages] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of reserved CIDR blocks that are in use.
        self.cidr_reservation_usages = cidr_reservation_usages
        # The number of entries to return per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cidr_reservation_usages:
            for v1 in self.cidr_reservation_usages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CidrReservationUsages'] = []
        if self.cidr_reservation_usages is not None:
            for k1 in self.cidr_reservation_usages:
                result['CidrReservationUsages'].append(k1.to_map() if k1 else None)

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
        self.cidr_reservation_usages = []
        if m.get('CidrReservationUsages') is not None:
            for k1 in m.get('CidrReservationUsages'):
                temp_model = main_models.GetVSwitchCidrReservationUsageResponseBodyCidrReservationUsages()
                self.cidr_reservation_usages.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetVSwitchCidrReservationUsageResponseBodyCidrReservationUsages(DaraModel):
    def __init__(
        self,
        ip_prefix_cidr: str = None,
        ip_prefix_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        v_switch_cidr_reservation_id: str = None,
        v_switch_id: str = None,
    ):
        # The CIDR block allocated to the ENI from the reserved CIDR block.
        self.ip_prefix_cidr = ip_prefix_cidr
        # The ID of the reserved CIDR block.
        self.ip_prefix_id = ip_prefix_id
        # The ID of the elastic network interface (ENI) whose CIDR block is allocated from the reserved CIDR block.
        self.resource_id = resource_id
        # The type of the resource to which a CIDR block is allocated from the reserved CIDR block. Only **NetworkInterface** may be returned, which indicates an ENI.
        self.resource_type = resource_type
        # The ID of the reserved CIDR block.
        self.v_switch_cidr_reservation_id = v_switch_cidr_reservation_id
        # The ID of the vSwitch to which the reserved CIDR block belongs.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_prefix_cidr is not None:
            result['IpPrefixCidr'] = self.ip_prefix_cidr

        if self.ip_prefix_id is not None:
            result['IpPrefixId'] = self.ip_prefix_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.v_switch_cidr_reservation_id is not None:
            result['VSwitchCidrReservationId'] = self.v_switch_cidr_reservation_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPrefixCidr') is not None:
            self.ip_prefix_cidr = m.get('IpPrefixCidr')

        if m.get('IpPrefixId') is not None:
            self.ip_prefix_id = m.get('IpPrefixId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('VSwitchCidrReservationId') is not None:
            self.v_switch_cidr_reservation_id = m.get('VSwitchCidrReservationId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

