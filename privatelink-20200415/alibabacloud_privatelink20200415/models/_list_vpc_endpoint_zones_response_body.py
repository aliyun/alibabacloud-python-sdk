# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointZonesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        zones: List[main_models.ListVpcEndpointZonesResponseBodyZones] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
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

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

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

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.ListVpcEndpointZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class ListVpcEndpointZonesResponseBodyZones(DaraModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_ip: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        zone_domain: str = None,
        zone_id: str = None,
        zone_ipv_6address: str = None,
        zone_status: str = None,
    ):
        # The ID of the endpoint ENI.
        self.eni_id = eni_id
        # The IP address of the endpoint ENI.
        self.eni_ip = eni_ip
        # The region ID of the endpoint.
        self.region_id = region_id
        # The ID of the vSwitch in the zone. The system automatically creates an endpoint elastic network interface (ENI) in the vSwitch.
        self.v_switch_id = v_switch_id
        # The domain name of the zone.
        # 
        # After the endpoint in the zone is connected to the endpoint service, you can access the service resources of the endpoint service by using the domain name of the zone.
        self.zone_domain = zone_domain
        # The zone ID.
        self.zone_id = zone_id
        # Indicates whether the endpoint service supports IPv6. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.zone_ipv_6address = zone_ipv_6address
        # The state of the zone. Valid values:
        # 
        # *   **Creating**: The zone is being created.
        # *   **Wait**: The zone is to be connected.
        # *   **Connected**: The zone is connected.
        # *   **Deleting**: The zone is being deleted.
        # *   **Disconnecting**: The zone is being disconnected.
        # *   **Disconnected**: The zone is disconnected.
        # *   **Connecting**: The zone is being connected.
        self.zone_status = zone_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.eni_ip is not None:
            result['EniIp'] = self.eni_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_domain is not None:
            result['ZoneDomain'] = self.zone_domain

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_ipv_6address is not None:
            result['ZoneIpv6Address'] = self.zone_ipv_6address

        if self.zone_status is not None:
            result['ZoneStatus'] = self.zone_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('EniIp') is not None:
            self.eni_ip = m.get('EniIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneDomain') is not None:
            self.zone_domain = m.get('ZoneDomain')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIpv6Address') is not None:
            self.zone_ipv_6address = m.get('ZoneIpv6Address')

        if m.get('ZoneStatus') is not None:
            self.zone_status = m.get('ZoneStatus')

        return self

