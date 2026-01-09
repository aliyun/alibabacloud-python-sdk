# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ESIngestionConfigurationSource(DaraModel):
    def __init__(
        self,
        bootstrap_servers: str = None,
        connector_mode: str = None,
        end_time: int = None,
        index: str = None,
        max_data_delay_sec: int = None,
        min_frag_range_sec: int = None,
        password: str = None,
        query: str = None,
        start_time: int = None,
        time_field_name: str = None,
        time_format: str = None,
        time_zone: str = None,
        username: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.bootstrap_servers = bootstrap_servers
        # This parameter is required.
        self.connector_mode = connector_mode
        self.end_time = end_time
        # This parameter is required.
        self.index = index
        # This parameter is required.
        self.max_data_delay_sec = max_data_delay_sec
        # This parameter is required.
        self.min_frag_range_sec = min_frag_range_sec
        self.password = password
        # This parameter is required.
        self.query = query
        self.start_time = start_time
        self.time_field_name = time_field_name
        self.time_format = time_format
        self.time_zone = time_zone
        self.username = username
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bootstrap_servers is not None:
            result['BootstrapServers'] = self.bootstrap_servers

        if self.connector_mode is not None:
            result['ConnectorMode'] = self.connector_mode

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.index is not None:
            result['Index'] = self.index

        if self.max_data_delay_sec is not None:
            result['MaxDataDelaySec'] = self.max_data_delay_sec

        if self.min_frag_range_sec is not None:
            result['MinFragRangeSec'] = self.min_frag_range_sec

        if self.password is not None:
            result['Password'] = self.password

        if self.query is not None:
            result['Query'] = self.query

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_field_name is not None:
            result['TimeFieldName'] = self.time_field_name

        if self.time_format is not None:
            result['TimeFormat'] = self.time_format

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.username is not None:
            result['Username'] = self.username

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootstrapServers') is not None:
            self.bootstrap_servers = m.get('BootstrapServers')

        if m.get('ConnectorMode') is not None:
            self.connector_mode = m.get('ConnectorMode')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('MaxDataDelaySec') is not None:
            self.max_data_delay_sec = m.get('MaxDataDelaySec')

        if m.get('MinFragRangeSec') is not None:
            self.min_frag_range_sec = m.get('MinFragRangeSec')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeFieldName') is not None:
            self.time_field_name = m.get('TimeFieldName')

        if m.get('TimeFormat') is not None:
            self.time_format = m.get('TimeFormat')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

