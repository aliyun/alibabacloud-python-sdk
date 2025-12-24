# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainUsageDataRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        data_protocol: str = None,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        interval: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The billable region. Valid values:
        # 
        # *   **CN**: Chinese mainland
        # *   **OverSeas**: outside the Chinese mainland
        # *   **AP1**: Asia Pacific 1
        # *   **AP2**: Asia Pacific 2
        # *   **AP3**: Asia Pacific 3
        # *   **NA**: North America
        # *   **SA**: South America
        # *   **EU**: Europe
        # *   **MEAA**: Middle East and Africa
        # *   **all**: all regions
        # 
        # >  If you do not specify this parameter, the default value CN is used. Alibaba Cloud supports the following countries and regions outside the Chinese mainland: - Asia Pacific 1: Hong Kong (China), Macao (China), Taiwan (China), Japan, and Southeast Asia excluding Vietnam and Indonesia. - Asia Pacific 2: Indonesia, South Korea, and Vietnam. - Asia Pacific 3: Australia and New Zealand. - North America: US and Canada. - South America: Brazil. Europe: Ukraine, UK, France, Netherlands, Spain, Italy, Sweden, and Germany. - Middle East and Africa: South Africa, Oman, UAE, and Kuwait.
        self.area = area
        # The protocol of the data to query. Valid values:
        # 
        # *   **http**: HTTP
        # *   **https**: HTTPS
        # *   **quic**: QUIC
        # *   **all** (default): HTTP, HTTPS, and QUIC
        self.data_protocol = data_protocol
        # The domain name.
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you leave this parameter empty, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # The end time must be later than the start time. The maximum time range that you can specify is **31** days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The category of the resource usage data to query. Valid values:
        # 
        # *   **bps**: streaming bandwidth
        # *   **traf**: streaming traffic
        # *   **req_traf**: stream ingest traffic if you set Type to push, or stream relay traffic if you set Type to push_proxy
        # *   **req_bps**: stream ingest bandwidth if you set Type to push, or stream relay bandwidth if you set Type to push_proxy
        # 
        # This parameter is required.
        self.field = field
        # The time interval between the data entries to return. Unit: seconds. Valid values: **300** (5 minutes), **3600** (1 hour), and **86400** (1 day).
        self.interval = interval
        self.owner_id = owner_id
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of the resource usage data to query.
        # 
        # Valid values if you set **Field** to **bps** or **traf**:
        # 
        # *   **rts**: bandwidth or traffic for Real-Time Streaming (RTS)
        # *   **quic**: bandwidth or traffic for QUIC
        # *   **all**: all bandwidth or traffic
        # 
        # Valid values if you set **Field** to **req_traf** or **req_bps**:
        # 
        # *   **push**: stream ingest bandwidth or traffic
        # *   **push_proxy**: stream relay bandwidth or traffic
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.data_protocol is not None:
            result['DataProtocol'] = self.data_protocol

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.field is not None:
            result['Field'] = self.field

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('DataProtocol') is not None:
            self.data_protocol = m.get('DataProtocol')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

