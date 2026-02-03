# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetInternetTupleRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        begin_time: int = None,
        cloud_ip: str = None,
        cloud_ip_list: List[str] = None,
        cloud_isp: str = None,
        cloud_port: str = None,
        direction: str = None,
        end_time: int = None,
        instance_id: str = None,
        instance_list: List[str] = None,
        order_by: str = None,
        other_city: str = None,
        other_country: str = None,
        other_ip: str = None,
        other_isp: str = None,
        other_port: str = None,
        protocol: str = None,
        region_id: str = None,
        sort: str = None,
        top_n: int = None,
        tuple_type: int = None,
        use_multi_account: bool = None,
    ):
        # The IDs of member accounts.
        self.account_ids = account_ids
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local IP addresses for filtering.
        self.cloud_ip_list = cloud_ip_list
        # The local Internet service provider (ISP).
        # 
        # >  In most cases, the value is Alibaba or Alibaba Cloud.
        self.cloud_isp = cloud_isp
        # The local port.
        # 
        # >  This parameter is required only if you set GroupBy to CloudPort.
        self.cloud_port = cloud_port
        # The direction of the Internet traffic that you want to query. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the Alibaba Cloud instance.
        self.instance_id = instance_id
        # The instance IDs for filtering.
        self.instance_list = instance_list
        # The metric for data ranking. Default value: **ByteCount**. This value indicates that Internet traffic data is ranked by traffic volume.
        # 
        # Valid values:
        # 
        # *   Rtt
        # *   ByteCount
        # *   PacketCount
        # *   RetransmitRate
        self.order_by = order_by
        # The remote city.
        # 
        # >  This parameter is required only if you set **TupleType** to **2** or **5**.
        self.other_city = other_city
        # The remote country.
        # 
        # >  This parameter is required only if you set **TupleType** to **2** or **5**.
        self.other_country = other_country
        # The remote IP address.
        # 
        # > This parameter is required only when you set **TupleType** to **2** or **5**.
        self.other_ip = other_ip
        # The remote ISP.
        # 
        # > This parameter is required if you want to view the information about the remote ISP.
        self.other_isp = other_isp
        # The remote port.
        # 
        # > This parameter is required only when you set **TupleType** to **5**.
        self.other_port = other_port
        # The protocol number.
        # 
        # > All protocols are supported. This parameter is required only when you set **TupleType** to **5**.
        self.protocol = protocol
        # The ID of the region for which you want to query the Internet traffic.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The order in which instances are ranked by Internet traffic. Valid values:
        # 
        # *   **desc**: the descending order
        # *   **asc**: the ascending order
        self.sort = sort
        # Specifies top-N traffic data to display. Default value: **10**. This value specifies to display top-10 traffic data by default. Max value: **100**.
        self.top_n = top_n
        # The type of the tuple. Valid values:
        # 
        # *   **1**: 1-tuple
        # *   **2**: 2-tuple
        # *   **5**: 5-tuple
        # 
        # This parameter is required.
        self.tuple_type = tuple_type
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
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip

        if self.cloud_ip_list is not None:
            result['CloudIpList'] = self.cloud_ip_list

        if self.cloud_isp is not None:
            result['CloudIsp'] = self.cloud_isp

        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.other_city is not None:
            result['OtherCity'] = self.other_city

        if self.other_country is not None:
            result['OtherCountry'] = self.other_country

        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip

        if self.other_isp is not None:
            result['OtherIsp'] = self.other_isp

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

        if self.tuple_type is not None:
            result['TupleType'] = self.tuple_type

        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')

        if m.get('CloudIpList') is not None:
            self.cloud_ip_list = m.get('CloudIpList')

        if m.get('CloudIsp') is not None:
            self.cloud_isp = m.get('CloudIsp')

        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OtherCity') is not None:
            self.other_city = m.get('OtherCity')

        if m.get('OtherCountry') is not None:
            self.other_country = m.get('OtherCountry')

        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')

        if m.get('OtherIsp') is not None:
            self.other_isp = m.get('OtherIsp')

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

        if m.get('TupleType') is not None:
            self.tuple_type = m.get('TupleType')

        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')

        return self

