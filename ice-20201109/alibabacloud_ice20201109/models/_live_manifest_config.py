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
        # The type of ad markers to include in the manifest.
        # 
        # *   NONE: Removes all ad markers.
        # *   DATE_RANGE: Inserts EXT-X-DATERANGE tags (HLS spec). Valid for HLS/HLS-CMAF endpoints.
        # *   XML: Inserts XML-based ad markers (DASH spec). Valid for DASH endpoints.
        self.ad_markers = ad_markers
        # The interval, in seconds, at which to insert the EXT-X-PROGRAM-DATE-TIME tag into the playlist. By default, no tags are inserted. Valid values: 1 to 3600. Applies only to HLS and HLS-CMAF endpoints.
        self.date_time_interval = date_time_interval
        # The duration of the startover window, in seconds. It defines the maximum time a viewer can seek backward in the live stream. Valid values: 1 to 3600. Default value: 60. Applies only to DASH endpoints.
        self.manifest_duration = manifest_duration
        # The maximum bitrate threshold (in bits per second) that video tracks must be at or below to be available for playback from this endpoint. It must be a positive integer. If not set, no maximum bitrate is enforced.
        self.max_video_bitrate = max_video_bitrate
        # The minimum buffer time, in seconds. Valid values: 1 to 30. Default value: the duration of two segments. Applies only to DASH endpoints.
        # 
        # Note: Setting this value too low may cause playback to stutter. We recommend a value no less than two segment durations.
        self.min_buffer_time = min_buffer_time
        # The minimum update period for the manifest, in seconds. Valid values: 1 to 3600. Default value: the duration of two segments. Applies only to DASH endpoints.
        # 
        # Note: For smooth playback, set this value to be less than MinBufferTime.
        self.min_update_period = min_update_period
        # The minimum bitrate threshold (in bits per second) that video tracks must be at or above to be available for playback from this endpoint. It must be a positive integer. If not set, no minimum bitrate is enforced.
        self.min_video_bitrate = min_video_bitrate
        # The suggested presentation delay, in seconds. Valid values: 1 to 60. Default value: the duration of three segments.
        self.presentation_delay = presentation_delay
        # The number of segments to include in the playlist. Applies to HLS and HLS-CMAF protocols. If not set, the channel\\"s default configuration is used. Valid values: 2 to 100.
        self.segment_count = segment_count
        # The format of the segment template. Only NUMBER_TIMELINE is supported (default). Applies only to DASH endpoints.
        self.segment_template_format = segment_template_format
        # The order of streams in the master playlist. Valid values:
        # 
        # *   ORIGINAL: Preserves the original order of the input streams.
        # *   VIDEO_BITRATE_ASCENDING: sorts the streams in ascending order of bitrates, from lowest to highest.
        # *   VIDEO_BITRATE_DESCENDING: sorts the streams in descending order of bitrates, from highest to lowest.
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

