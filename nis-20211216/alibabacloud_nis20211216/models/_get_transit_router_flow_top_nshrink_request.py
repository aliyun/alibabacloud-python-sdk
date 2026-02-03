# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTransitRouterFlowTopNShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        bandwith_package_id: str = None,
        begin_time: int = None,
        cen_id: str = None,
        direction: str = None,
        end_time: int = None,
        group_by: str = None,
        order_by: str = None,
        other_ip: str = None,
        other_port: str = None,
        other_region: str = None,
        protocol: str = None,
        sort: str = None,
        this_ip: str = None,
        this_port: str = None,
        this_region: str = None,
        top_n: int = None,
        use_multi_account: bool = None,
    ):
        # The IDs of the member accounts.
        self.account_ids_shrink = account_ids_shrink
        # The ID of the CEN bandwidth plan.
        self.bandwith_package_id = bandwith_package_id
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The CEN instance ID.
        self.cen_id = cen_id
        # The direction of the inter-region traffic in the local regions or for the local IP addresses. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The dimension for ranking inter-region traffic data. The value of this parameter is case-sensitive. Valid values:
        # 
        # *   **1Tuple**: queries the rankings of inter-region traffic data for the local regions, Cloud Enterprise Network (CEN) instances, and IP addresses.
        # *   **2Tuple**: queries the rankings of inter-region traffic data for the local and remote regions, and the local and remote IP addresses.
        # *   **5Tuple**: queries the rankings of inter-region traffic data for the local and remote IP addresses, local and remote ports, and protocols.
        # *   **Cen**: queries the rankings of inter-region traffic data for CEN instances.
        # *   **RegionPair**: queries the rankings of inter-region traffic data for the local and remote regions.
        # *   **Port**: queries the rankings of inter-region traffic data for the local and remote ports.
        # *   **Protocol**: queries the rankings of inter-region traffic data for the protocols.
        # 
        # This parameter is required.
        self.group_by = group_by
        # The metric for ranking inter-region traffic data. Default value: Bytes. This value specifies that inter-region traffic data is ranked by traffic volume.
        self.order_by = order_by
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        self.other_port = other_port
        # The remote region.
        self.other_region = other_region
        # The protocol number.
        # 
        # >  All protocols are supported. This parameter is required only if you set **GroupBy** to **5Tuple** or **Protocol**.
        self.protocol = protocol
        # The order for ranking inter-region traffic data. Valid values:
        # 
        # *   **desc**: descending order
        # *   **asc**: ascending order
        self.sort = sort
        # The local IP address.
        self.this_ip = this_ip
        # The local port.
        self.this_port = this_port
        # The local region where the **local IP address** resides.
        self.this_region = this_region
        # Specifies the maximum number of data entries to display. Default value: **10**. Maximum value: 100.
        self.top_n = top_n
        # Specifies whether to enable the multi-account management feature. Default value: **false**. This value specifies that the multi-account management feature is disabled.
        # 
        # >  By default, the multi-account management feature is not available. If you want to use this feature, contact your account manager to apply for permissions.
        self.use_multi_account = use_multi_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink

        if self.bandwith_package_id is not None:
            result['BandwithPackageId'] = self.bandwith_package_id

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip

        if self.other_port is not None:
            result['OtherPort'] = self.other_port

        if self.other_region is not None:
            result['OtherRegion'] = self.other_region

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.this_ip is not None:
            result['ThisIp'] = self.this_ip

        if self.this_port is not None:
            result['ThisPort'] = self.this_port

        if self.this_region is not None:
            result['ThisRegion'] = self.this_region

        if self.top_n is not None:
            result['TopN'] = self.top_n

        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')

        if m.get('BandwithPackageId') is not None:
            self.bandwith_package_id = m.get('BandwithPackageId')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')

        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')

        if m.get('OtherRegion') is not None:
            self.other_region = m.get('OtherRegion')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('ThisIp') is not None:
            self.this_ip = m.get('ThisIp')

        if m.get('ThisPort') is not None:
            self.this_port = m.get('ThisPort')

        if m.get('ThisRegion') is not None:
            self.this_region = m.get('ThisRegion')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')

        return self

