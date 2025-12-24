# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveStreamMergeRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        in_app_name_1: str = None,
        in_app_name_2: str = None,
        in_stream_name_1: str = None,
        in_stream_name_2: str = None,
        live_merger: str = None,
        merge_parameters: str = None,
        owner_id: int = None,
        protocol: str = None,
        region_id: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application that generates the output stream. The value must be the same as the application name in the ingest URL of the output stream. Otherwise, the configuration does not take effect. You cannot set the value to an asterisk (\\*).
        # 
        # This parameter is required.
        self.app_name = app_name
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end time of the stream mixing.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The interval between the start time and the end time must be within 7 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the application that generates the input primary stream. The value must be the same as the application name that is specified in the ingest URL of the primary stream. Otherwise, the configuration does not take effect.
        # 
        # This parameter is required.
        self.in_app_name_1 = in_app_name_1
        # The name of the application that generates the input secondary stream. The value must be the same as the application name that is specified in the ingest URL of the secondary stream. Otherwise, the configuration does not take effect.
        # 
        # This parameter is required.
        self.in_app_name_2 = in_app_name_2
        # The name of the input primary stream. The value must be the same as the stream name that is specified in the ingest URL of the primary stream. Otherwise, the configuration does not take effect.
        # 
        # This parameter is required.
        self.in_stream_name_1 = in_stream_name_1
        # The name of the input secondary stream. The value must be the same as the stream name that is specified in the ingest URL of the secondary stream. Otherwise, the configuration does not take effect.
        # 
        # This parameter is required.
        self.in_stream_name_2 = in_stream_name_2
        self.live_merger = live_merger
        self.merge_parameters = merge_parameters
        self.owner_id = owner_id
        # The streaming protocol. Valid values:
        # 
        # *   **rtmp**: This is the default value.
        # *   **rtc**
        self.protocol = protocol
        self.region_id = region_id
        # The start time of the stream mixing.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the output stream. The value must be the same as the stream name in the ingest URL of the output stream. Otherwise, the configuration does not take effect. You cannot set the value to an asterisk (\\*).
        # 
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.in_app_name_1 is not None:
            result['InAppName1'] = self.in_app_name_1

        if self.in_app_name_2 is not None:
            result['InAppName2'] = self.in_app_name_2

        if self.in_stream_name_1 is not None:
            result['InStreamName1'] = self.in_stream_name_1

        if self.in_stream_name_2 is not None:
            result['InStreamName2'] = self.in_stream_name_2

        if self.live_merger is not None:
            result['LiveMerger'] = self.live_merger

        if self.merge_parameters is not None:
            result['MergeParameters'] = self.merge_parameters

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InAppName1') is not None:
            self.in_app_name_1 = m.get('InAppName1')

        if m.get('InAppName2') is not None:
            self.in_app_name_2 = m.get('InAppName2')

        if m.get('InStreamName1') is not None:
            self.in_stream_name_1 = m.get('InStreamName1')

        if m.get('InStreamName2') is not None:
            self.in_stream_name_2 = m.get('InStreamName2')

        if m.get('LiveMerger') is not None:
            self.live_merger = m.get('LiveMerger')

        if m.get('MergeParameters') is not None:
            self.merge_parameters = m.get('MergeParameters')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

