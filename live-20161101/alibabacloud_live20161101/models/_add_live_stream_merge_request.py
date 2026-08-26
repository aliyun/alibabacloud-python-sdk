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
        select_app_name: str = None,
        select_stream_name: str = None,
        start_time: str = None,
        stream_name: str = None,
        switch_mode: str = None,
    ):
        # The AppName of the output stream. For the configuration to take effect, this AppName must match the one in the ingest URL. Wildcards (`*`) are not supported.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end time of the stream merge.
        # 
        # The time must be in UTC and specified in the ISO 8601 standard format: `yyyy-MM-ddTHH:mm:ssZ`.
        # 
        # > The interval between `StartTime` and `EndTime` cannot exceed 7 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The AppName of the primary input stream. This value must match the AppName in the ingest URL for the primary stream.
        # 
        # This parameter is required.
        self.in_app_name_1 = in_app_name_1
        # The AppName of the backup input stream. This value must match the AppName in the ingest URL for the backup stream.
        # 
        # This parameter is required.
        self.in_app_name_2 = in_app_name_2
        # The StreamName of the primary input stream. This value must match the StreamName in the ingest URL for the primary stream.
        # 
        # This parameter is required.
        self.in_stream_name_1 = in_stream_name_1
        # The StreamName of the backup input stream. This value must match the StreamName in the ingest URL for the backup stream.
        # 
        # This parameter is required.
        self.in_stream_name_2 = in_stream_name_2
        # The engine to use for stream merging.
        # 
        # - `on`: The new liveswitch engine.
        # 
        # - `off`: A legacy engine (such as rtmpr). This is the default.
        self.live_merger = live_merger
        # Parameters that define the failover conditions. A failover is triggered when one of the following conditions is met:
        # 
        # 1. An explicit stream disconnection occurs, such as an end-of-file (EOF) or network error.
        # 
        # 2. The stutter rate exceeds 60% in the last 5 seconds.
        # 
        # 3. A stream pulling timeout occurs if no frame data is received for 2 consecutive seconds.
        # 
        # 4. The average frame rate over the period specified by `ali_max_no_frame_timeout` drops below `ali_low_frame_rate_threshold`. This condition applies even if there is no stream disconnection or stuttering. If you set `ali_max_no_frame_timeout`, the timeout for Condition 3 is also updated to this value.
        # 
        # 5. If `block_all_jitter` is set to `1`, Conditions 2, 3, and 4 do not apply.
        # 
        # - `ali_max_no_frame_timeout`: an integer from 2 to 10.<br>`ali_low_frame_rate_threshold`: an integer from 1 to 200.<br>`block_all_jitter`: `0` or `1`.<br><br>
        self.merge_parameters = merge_parameters
        self.owner_id = owner_id
        # The live stream protocol for the input streams. Valid values:
        # 
        # - **rtmp** (Default)
        # 
        # - **rtc**
        self.protocol = protocol
        # The region ID.
        self.region_id = region_id
        self.select_app_name = select_app_name
        self.select_stream_name = select_stream_name
        # The start time of the stream merge.
        # 
        # The time must be in UTC and specified in the ISO 8601 standard format: `yyyy-MM-ddTHH:mm:ssZ`.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The StreamName of the output stream. For the configuration to take effect, this StreamName must match the one in the ingest URL. Wildcards (`*`) are not supported.
        # 
        # This parameter is required.
        self.stream_name = stream_name
        self.switch_mode = switch_mode

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

        if self.select_app_name is not None:
            result['SelectAppName'] = self.select_app_name

        if self.select_stream_name is not None:
            result['SelectStreamName'] = self.select_stream_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

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

        if m.get('SelectAppName') is not None:
            self.select_app_name = m.get('SelectAppName')

        if m.get('SelectStreamName') is not None:
            self.select_stream_name = m.get('SelectStreamName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

