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
        # The region code. Valid values:
        # - **CN**: the Chinese mainland.
        # - **OverSeas**: outside the Chinese mainland.
        # - **AP1**: Asia-Pacific 1.
        # - **AP2**: Asia-Pacific 2.
        # - **AP3**: Asia-Pacific 3.
        # - **NA**: North America.
        # - **SA**: South America.
        # - **EU**: Europe.
        # - **MEAA**: Middle East and Africa.
        # - **all**: all regions.
        # 
        # > If this parameter is not specified, the default value is the Chinese mainland. Regions outside the Chinese mainland: - Asia-Pacific 1: Hong Kong (China), Macao (China), Taiwan (China), Japan, and Southeast Asian countries except Vietnam and Indonesia. - Asia-Pacific 2: Indonesia, South Korea, and Vietnam. - Asia-Pacific 3: Australia and New Zealand. North America: the United States and Canada. - South America: Brazil. - Europe: Ukraine, the United Kingdom, France, the Netherlands, Spain, Italy, Sweden, and Germany. - Middle East and Africa: South Africa, Oman, the United Arab Emirates, and Kuwait.
        self.area = area
        # The protocol of the data to retrieve. Valid values:
        # 
        # - **http**: HTTP.
        # 
        # - **https**: HTTPS.
        # 
        # - **quic**: QUIC.
        # 
        # - **all** (default): all of the preceding protocols.
        self.data_protocol = data_protocol
        # The streaming domain.
        # - You can specify a single domain name or multiple domain names. Separate multiple domain names with commas (,).
        # 
        # - If this parameter is empty, the merged data of all streaming domains is returned by default.
        self.domain_name = domain_name
        # The end time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # The end time must be later than the start time, and the difference between the end time and the start time cannot exceed **31** days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The data type of the usage data to query. Valid values:
        # - **bps**: playback bandwidth.
        # 
        # - **traf**: traffic.
        # 
        # - **req_traf**: when Type is set to push, this indicates stream ingest traffic. When Type is set to push_proxy, this indicates relay traffic.
        # 
        # - **req_bps**: when Type is set to push, this indicates stream ingest bandwidth. When Type is set to push_proxy, this indicates relay bandwidth.
        # 
        # This parameter is required.
        self.field = field
        # Forces retrieval of data at the specified time granularity, in seconds. Valid values: **300** (5 minutes), **3600** (1 hour), and **86400** (1 day).
        self.interval = interval
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of usage data to retrieve.
        # 
        # When **Field** is set to **bps** or **traf**, valid values:
        # - **rts**: RTS bandwidth or traffic.
        # - **quic**: QUIC bandwidth or traffic.
        # 
        # When **Field** is set to **req_traf** or **req_bps**, valid values:
        # - **push**: stream ingest bandwidth or traffic.
        # - **push_proxy**: relay bandwidth or traffic.
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

