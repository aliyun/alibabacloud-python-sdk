# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetVbrFlowTopNRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        attachment_id: str = None,
        begin_time: int = None,
        cen_id: str = None,
        cloud_ip: str = None,
        cloud_port: str = None,
        direction: str = None,
        end_time: int = None,
        group_by: str = None,
        order_by: str = None,
        other_ip: str = None,
        other_port: str = None,
        protocol: str = None,
        region_id: str = None,
        sort: str = None,
        top_n: int = None,
        use_multi_account: bool = None,
        virtual_border_router_id: str = None,
    ):
        # The IDs of member accounts.
        self.account_ids = account_ids
        # The CEN connection ID.
        self.attachment_id = attachment_id
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The CEN instance ID.
        self.cen_id = cen_id
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local port.
        # 
        # >  This parameter is required only if you set **GroupBy** to **CloudPort**.
        self.cloud_port = cloud_port
        # The direction of the hybrid cloud traffic in the local regions or for the local IP addresses. Valid values:
        # 
        # *   **in**: traffic from a data center to Alibaba Cloud
        # *   **out**: traffic from Alibaba Cloud to a data center
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The dimension for ranking hybrid cloud traffic data. The value of this parameter is case-sensitive. Valid values:
        # 
        # *   **1Tuple**: queries the rankings of hybrid cloud traffic data for the Cloud Enterprise Network (CEN) instances, CEN connections, virtual border routers (VBRs), and IP addresses.
        # *   **2Tuple**: queries the rankings of hybrid cloud traffic data for the local and remote IP addresses.
        # *   **5Tuple**: queries the rankings of hybrid cloud traffic data for the local and remote IP addresses, local and remote ports, and protocols.
        # *   **CloudPort**: queries the rankings of hybrid cloud traffic data for the local ports.
        # *   **OtherPort**: queries the rankings of hybrid cloud traffic data for the remote ports.
        # *   **Protocol**: queries the rankings of hybrid cloud traffic data for the protocols.
        # 
        # This parameter is required.
        self.group_by = group_by
        # The metric for ranking hybrid cloud traffic data. Default value: Bytes. This value specifies that hybrid cloud traffic data is ranked by traffic volumes.
        self.order_by = order_by
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        # 
        # >  This parameter is required only if you set **GroupBy** to **OtherPort**.
        self.other_port = other_port
        # The protocol number.
        # 
        # >  All protocols are supported. This parameter is required only if you set **GroupBy** to **5Tuple** or **Protocol**.
        self.protocol = protocol
        # The local region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The order for ranking hybrid cloud traffic data. Valid values:
        # 
        # *   **desc**: descending order
        # *   **asc**: ascending order
        self.sort = sort
        # Specifies top-N traffic data to display. Default value: **10**. This value specifies that top-10 traffic data is displayed by default. Maximum value: **100**.
        self.top_n = top_n
        # Specifies whether to enable the multi-account management feature. Default value: **false**. This value specifies that the multi-account management feature is disabled.
        # 
        # >  By default, the multi-account management feature is not available. If you want to use this feature, contact your account manager to apply for permissions.
        self.use_multi_account = use_multi_account
        # The ID of the VBR that is associated with the Express Connect circuit.
        self.virtual_border_router_id = virtual_border_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip

        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port

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

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.top_n is not None:
            result['TopN'] = self.top_n

        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account

        if self.virtual_border_router_id is not None:
            result['VirtualBorderRouterId'] = self.virtual_border_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')

        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')

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

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')

        if m.get('VirtualBorderRouterId') is not None:
            self.virtual_border_router_id = m.get('VirtualBorderRouterId')

        return self

