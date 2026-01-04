# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListVSwitchCidrReservationsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        v_switch_cidr_reservations: List[main_models.ListVSwitchCidrReservationsResponseBodyVSwitchCidrReservations] = None,
    ):
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
        # A list of reserved CIDR blocks.
        self.v_switch_cidr_reservations = v_switch_cidr_reservations

    def validate(self):
        if self.v_switch_cidr_reservations:
            for v1 in self.v_switch_cidr_reservations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VSwitchCidrReservations'] = []
        if self.v_switch_cidr_reservations is not None:
            for k1 in self.v_switch_cidr_reservations:
                result['VSwitchCidrReservations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.v_switch_cidr_reservations = []
        if m.get('VSwitchCidrReservations') is not None:
            for k1 in m.get('VSwitchCidrReservations'):
                temp_model = main_models.ListVSwitchCidrReservationsResponseBodyVSwitchCidrReservations()
                self.v_switch_cidr_reservations.append(temp_model.from_map(k1))

        return self

class ListVSwitchCidrReservationsResponseBodyVSwitchCidrReservations(DaraModel):
    def __init__(
        self,
        assigned_cidr_count: int = None,
        available_cidr_count: int = None,
        creation_time: str = None,
        ip_version: str = None,
        status: str = None,
        tags: List[main_models.ListVSwitchCidrReservationsResponseBodyVSwitchCidrReservationsTags] = None,
        type: str = None,
        v_switch_cidr_reservation_cidr: str = None,
        v_switch_cidr_reservation_description: str = None,
        v_switch_cidr_reservation_id: str = None,
        v_switch_cidr_reservation_name: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The number of used prefixes in the reserved CIDR block.
        self.assigned_cidr_count = assigned_cidr_count
        # The number of available prefixes in the reserved CIDR block.
        self.available_cidr_count = available_cidr_count
        # The time when the reserved CIDR block was created.
        self.creation_time = creation_time
        # The IP version of the reserved CIDR block. Valid values:
        # 
        # *   **IPv4** (default)
        # *   **IPv6**
        self.ip_version = ip_version
        # The status of the reserved CIDR block. Valid values:
        # 
        # *   **Assigning**
        # *   **Assigned**
        # *   **Releasing**
        # *   **Released**
        self.status = status
        # The tags.
        self.tags = tags
        # The type of the reserved CIDR block. Valid value: **prefix**. CIDR blocks are allocated from the reserved CIDR block.
        self.type = type
        # The reserved CIDR block.
        self.v_switch_cidr_reservation_cidr = v_switch_cidr_reservation_cidr
        # The description of the reserved CIDR block.
        self.v_switch_cidr_reservation_description = v_switch_cidr_reservation_description
        # The ID of the reserved CIDR block.
        self.v_switch_cidr_reservation_id = v_switch_cidr_reservation_id
        # The name of the reserved CIDR block.
        self.v_switch_cidr_reservation_name = v_switch_cidr_reservation_name
        # The ID of the vSwitch to which the reserved CIDR block belongs.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) to which the reserved CIDR block belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_cidr_count is not None:
            result['AssignedCidrCount'] = self.assigned_cidr_count

        if self.available_cidr_count is not None:
            result['AvailableCidrCount'] = self.available_cidr_count

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_cidr_reservation_cidr is not None:
            result['VSwitchCidrReservationCidr'] = self.v_switch_cidr_reservation_cidr

        if self.v_switch_cidr_reservation_description is not None:
            result['VSwitchCidrReservationDescription'] = self.v_switch_cidr_reservation_description

        if self.v_switch_cidr_reservation_id is not None:
            result['VSwitchCidrReservationId'] = self.v_switch_cidr_reservation_id

        if self.v_switch_cidr_reservation_name is not None:
            result['VSwitchCidrReservationName'] = self.v_switch_cidr_reservation_name

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedCidrCount') is not None:
            self.assigned_cidr_count = m.get('AssignedCidrCount')

        if m.get('AvailableCidrCount') is not None:
            self.available_cidr_count = m.get('AvailableCidrCount')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListVSwitchCidrReservationsResponseBodyVSwitchCidrReservationsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchCidrReservationCidr') is not None:
            self.v_switch_cidr_reservation_cidr = m.get('VSwitchCidrReservationCidr')

        if m.get('VSwitchCidrReservationDescription') is not None:
            self.v_switch_cidr_reservation_description = m.get('VSwitchCidrReservationDescription')

        if m.get('VSwitchCidrReservationId') is not None:
            self.v_switch_cidr_reservation_id = m.get('VSwitchCidrReservationId')

        if m.get('VSwitchCidrReservationName') is not None:
            self.v_switch_cidr_reservation_name = m.get('VSwitchCidrReservationName')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListVSwitchCidrReservationsResponseBodyVSwitchCidrReservationsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

