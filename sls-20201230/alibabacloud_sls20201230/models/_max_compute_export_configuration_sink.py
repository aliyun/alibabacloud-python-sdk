# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MaxComputeExportConfigurationSink(DaraModel):
    def __init__(
        self,
        buffer_interval: str = None,
        fields: List[str] = None,
        filter_invalid: bool = None,
        odps_access_key_id: str = None,
        odps_access_secret: str = None,
        odps_endpoint: str = None,
        odps_project: str = None,
        odps_rolearn: str = None,
        odps_table: str = None,
        odps_tunnel_endpoint: str = None,
        partition_column: List[str] = None,
        partition_time_format: str = None,
        time_format_type: str = None,
        time_zone: str = None,
    ):
        self.buffer_interval = buffer_interval
        # This parameter is required.
        self.fields = fields
        self.filter_invalid = filter_invalid
        self.odps_access_key_id = odps_access_key_id
        self.odps_access_secret = odps_access_secret
        # This parameter is required.
        self.odps_endpoint = odps_endpoint
        # This parameter is required.
        self.odps_project = odps_project
        # This parameter is required.
        self.odps_rolearn = odps_rolearn
        # This parameter is required.
        self.odps_table = odps_table
        self.odps_tunnel_endpoint = odps_tunnel_endpoint
        # This parameter is required.
        self.partition_column = partition_column
        # This parameter is required.
        self.partition_time_format = partition_time_format
        self.time_format_type = time_format_type
        # This parameter is required.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buffer_interval is not None:
            result['bufferInterval'] = self.buffer_interval

        if self.fields is not None:
            result['fields'] = self.fields

        if self.filter_invalid is not None:
            result['filterInvalid'] = self.filter_invalid

        if self.odps_access_key_id is not None:
            result['odpsAccessKeyId'] = self.odps_access_key_id

        if self.odps_access_secret is not None:
            result['odpsAccessSecret'] = self.odps_access_secret

        if self.odps_endpoint is not None:
            result['odpsEndpoint'] = self.odps_endpoint

        if self.odps_project is not None:
            result['odpsProject'] = self.odps_project

        if self.odps_rolearn is not None:
            result['odpsRolearn'] = self.odps_rolearn

        if self.odps_table is not None:
            result['odpsTable'] = self.odps_table

        if self.odps_tunnel_endpoint is not None:
            result['odpsTunnelEndpoint'] = self.odps_tunnel_endpoint

        if self.partition_column is not None:
            result['partitionColumn'] = self.partition_column

        if self.partition_time_format is not None:
            result['partitionTimeFormat'] = self.partition_time_format

        if self.time_format_type is not None:
            result['timeFormatType'] = self.time_format_type

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bufferInterval') is not None:
            self.buffer_interval = m.get('bufferInterval')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('filterInvalid') is not None:
            self.filter_invalid = m.get('filterInvalid')

        if m.get('odpsAccessKeyId') is not None:
            self.odps_access_key_id = m.get('odpsAccessKeyId')

        if m.get('odpsAccessSecret') is not None:
            self.odps_access_secret = m.get('odpsAccessSecret')

        if m.get('odpsEndpoint') is not None:
            self.odps_endpoint = m.get('odpsEndpoint')

        if m.get('odpsProject') is not None:
            self.odps_project = m.get('odpsProject')

        if m.get('odpsRolearn') is not None:
            self.odps_rolearn = m.get('odpsRolearn')

        if m.get('odpsTable') is not None:
            self.odps_table = m.get('odpsTable')

        if m.get('odpsTunnelEndpoint') is not None:
            self.odps_tunnel_endpoint = m.get('odpsTunnelEndpoint')

        if m.get('partitionColumn') is not None:
            self.partition_column = m.get('partitionColumn')

        if m.get('partitionTimeFormat') is not None:
            self.partition_time_format = m.get('partitionTimeFormat')

        if m.get('timeFormatType') is not None:
            self.time_format_type = m.get('timeFormatType')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

