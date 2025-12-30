# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LiveManifestConfig(DaraModel):
    def __init__(
        self,
        ad_markers: str = None,
        date_time_interval: int = None,
        manifest_duration: int = None,
        max_video_bitrate: int = None,
        min_buffer_time: int = None,
        min_update_period: int = None,
        min_video_bitrate: int = None,
        presentation_delay: int = None,
        segment_count: int = None,
        segment_template_format: str = None,
        stream_order: str = None,
    ):
        self.ad_markers = ad_markers
        self.date_time_interval = date_time_interval
        self.manifest_duration = manifest_duration
        self.max_video_bitrate = max_video_bitrate
        self.min_buffer_time = min_buffer_time
        self.min_update_period = min_update_period
        self.min_video_bitrate = min_video_bitrate
        self.presentation_delay = presentation_delay
        self.segment_count = segment_count
        self.segment_template_format = segment_template_format
        self.stream_order = stream_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_markers is not None:
            result['AdMarkers'] = self.ad_markers

        if self.date_time_interval is not None:
            result['DateTimeInterval'] = self.date_time_interval

        if self.manifest_duration is not None:
            result['ManifestDuration'] = self.manifest_duration

        if self.max_video_bitrate is not None:
            result['MaxVideoBitrate'] = self.max_video_bitrate

        if self.min_buffer_time is not None:
            result['MinBufferTime'] = self.min_buffer_time

        if self.min_update_period is not None:
            result['MinUpdatePeriod'] = self.min_update_period

        if self.min_video_bitrate is not None:
            result['MinVideoBitrate'] = self.min_video_bitrate

        if self.presentation_delay is not None:
            result['PresentationDelay'] = self.presentation_delay

        if self.segment_count is not None:
            result['SegmentCount'] = self.segment_count

        if self.segment_template_format is not None:
            result['SegmentTemplateFormat'] = self.segment_template_format

        if self.stream_order is not None:
            result['StreamOrder'] = self.stream_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdMarkers') is not None:
            self.ad_markers = m.get('AdMarkers')

        if m.get('DateTimeInterval') is not None:
            self.date_time_interval = m.get('DateTimeInterval')

        if m.get('ManifestDuration') is not None:
            self.manifest_duration = m.get('ManifestDuration')

        if m.get('MaxVideoBitrate') is not None:
            self.max_video_bitrate = m.get('MaxVideoBitrate')

        if m.get('MinBufferTime') is not None:
            self.min_buffer_time = m.get('MinBufferTime')

        if m.get('MinUpdatePeriod') is not None:
            self.min_update_period = m.get('MinUpdatePeriod')

        if m.get('MinVideoBitrate') is not None:
            self.min_video_bitrate = m.get('MinVideoBitrate')

        if m.get('PresentationDelay') is not None:
            self.presentation_delay = m.get('PresentationDelay')

        if m.get('SegmentCount') is not None:
            self.segment_count = m.get('SegmentCount')

        if m.get('SegmentTemplateFormat') is not None:
            self.segment_template_format = m.get('SegmentTemplateFormat')

        if m.get('StreamOrder') is not None:
            self.stream_order = m.get('StreamOrder')

        return self

