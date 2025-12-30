# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListLivePackageChannelsResponseBody(DaraModel):
    def __init__(
        self,
        live_package_channels: List[main_models.ListLivePackageChannelsResponseBodyLivePackageChannels] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sort_by: str = None,
        total_count: int = None,
    ):
        # The live package channels.
        self.live_package_channels = live_package_channels
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The sort order. Valid values: asc and desc (default).
        self.sort_by = sort_by
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.live_package_channels:
            for v1 in self.live_package_channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LivePackageChannels'] = []
        if self.live_package_channels is not None:
            for k1 in self.live_package_channels:
                result['LivePackageChannels'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_package_channels = []
        if m.get('LivePackageChannels') is not None:
            for k1 in m.get('LivePackageChannels'):
                temp_model = main_models.ListLivePackageChannelsResponseBodyLivePackageChannels()
                self.live_package_channels.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLivePackageChannelsResponseBodyLivePackageChannels(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        create_time: str = None,
        description: str = None,
        group_name: str = None,
        ingest_endpoints: List[main_models.ListLivePackageChannelsResponseBodyLivePackageChannelsIngestEndpoints] = None,
        last_modified: str = None,
        protocol: str = None,
        segment_count: int = None,
        segment_duration: int = None,
    ):
        # The channel name.
        self.channel_name = channel_name
        # The time when the channel was created.
        self.create_time = create_time
        # The channel description.
        self.description = description
        # The channel group name.
        self.group_name = group_name
        # The ingest endpoints.
        self.ingest_endpoints = ingest_endpoints
        # The time when the channel was last modified.
        self.last_modified = last_modified
        # The ingest protocol. Only HLS is supported.
        self.protocol = protocol
        # The number of M3U8 segments.
        self.segment_count = segment_count
        # The segment duration.
        self.segment_duration = segment_duration

    def validate(self):
        if self.ingest_endpoints:
            for v1 in self.ingest_endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        result['IngestEndpoints'] = []
        if self.ingest_endpoints is not None:
            for k1 in self.ingest_endpoints:
                result['IngestEndpoints'].append(k1.to_map() if k1 else None)

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.segment_count is not None:
            result['SegmentCount'] = self.segment_count

        if self.segment_duration is not None:
            result['SegmentDuration'] = self.segment_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        self.ingest_endpoints = []
        if m.get('IngestEndpoints') is not None:
            for k1 in m.get('IngestEndpoints'):
                temp_model = main_models.ListLivePackageChannelsResponseBodyLivePackageChannelsIngestEndpoints()
                self.ingest_endpoints.append(temp_model.from_map(k1))

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SegmentCount') is not None:
            self.segment_count = m.get('SegmentCount')

        if m.get('SegmentDuration') is not None:
            self.segment_duration = m.get('SegmentDuration')

        return self

class ListLivePackageChannelsResponseBodyLivePackageChannelsIngestEndpoints(DaraModel):
    def __init__(
        self,
        id: str = None,
        password: str = None,
        url: str = None,
        username: str = None,
    ):
        # The ingest endpoint ID.
        self.id = id
        # The password.
        self.password = password
        # The ingest endpoint URL.
        self.url = url
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.password is not None:
            result['Password'] = self.password

        if self.url is not None:
            result['Url'] = self.url

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

