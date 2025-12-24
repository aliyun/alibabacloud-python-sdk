# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamDelayConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_stream_flv_delay_config: main_models.DescribeLiveStreamDelayConfigResponseBodyLiveStreamFlvDelayConfig = None,
        live_stream_hls_delay_config: main_models.DescribeLiveStreamDelayConfigResponseBodyLiveStreamHlsDelayConfig = None,
        live_stream_rtmp_delay_config: main_models.DescribeLiveStreamDelayConfigResponseBodyLiveStreamRtmpDelayConfig = None,
        request_id: str = None,
    ):
        # The latency of FLV-based playback.
        self.live_stream_flv_delay_config = live_stream_flv_delay_config
        # The latency of HLS-based playback.
        self.live_stream_hls_delay_config = live_stream_hls_delay_config
        # The latency of RTMP-based playback.
        self.live_stream_rtmp_delay_config = live_stream_rtmp_delay_config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_stream_flv_delay_config:
            self.live_stream_flv_delay_config.validate()
        if self.live_stream_hls_delay_config:
            self.live_stream_hls_delay_config.validate()
        if self.live_stream_rtmp_delay_config:
            self.live_stream_rtmp_delay_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_stream_flv_delay_config is not None:
            result['LiveStreamFlvDelayConfig'] = self.live_stream_flv_delay_config.to_map()

        if self.live_stream_hls_delay_config is not None:
            result['LiveStreamHlsDelayConfig'] = self.live_stream_hls_delay_config.to_map()

        if self.live_stream_rtmp_delay_config is not None:
            result['LiveStreamRtmpDelayConfig'] = self.live_stream_rtmp_delay_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveStreamFlvDelayConfig') is not None:
            temp_model = main_models.DescribeLiveStreamDelayConfigResponseBodyLiveStreamFlvDelayConfig()
            self.live_stream_flv_delay_config = temp_model.from_map(m.get('LiveStreamFlvDelayConfig'))

        if m.get('LiveStreamHlsDelayConfig') is not None:
            temp_model = main_models.DescribeLiveStreamDelayConfigResponseBodyLiveStreamHlsDelayConfig()
            self.live_stream_hls_delay_config = temp_model.from_map(m.get('LiveStreamHlsDelayConfig'))

        if m.get('LiveStreamRtmpDelayConfig') is not None:
            temp_model = main_models.DescribeLiveStreamDelayConfigResponseBodyLiveStreamRtmpDelayConfig()
            self.live_stream_rtmp_delay_config = temp_model.from_map(m.get('LiveStreamRtmpDelayConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamDelayConfigResponseBodyLiveStreamRtmpDelayConfig(DaraModel):
    def __init__(
        self,
        delay: int = None,
        level: str = None,
    ):
        # The playback latency. Unit: seconds.
        self.delay = delay
        # The latency level. Valid values:
        # 
        # *   **short**: The latency is less than or equal to 4 seconds.
        # *   **medium**: The latency is greater than 4 seconds, and less than or equal to 8 seconds.
        # *   **long**: The latency is greater than 8 seconds.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay is not None:
            result['Delay'] = self.delay

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

class DescribeLiveStreamDelayConfigResponseBodyLiveStreamHlsDelayConfig(DaraModel):
    def __init__(
        self,
        delay: int = None,
        level: str = None,
    ):
        # The playback latency. Unit: seconds.
        self.delay = delay
        # The latency level. Valid values:
        # 
        # *   **short**: The latency is less than or equal to 4 seconds.
        # *   **medium**: The latency is greater than 4 seconds, and less than or equal to 8 seconds.
        # *   **long**: The latency is greater than 8 seconds.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay is not None:
            result['Delay'] = self.delay

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

class DescribeLiveStreamDelayConfigResponseBodyLiveStreamFlvDelayConfig(DaraModel):
    def __init__(
        self,
        delay: int = None,
        level: str = None,
    ):
        # The playback latency. Unit: seconds.
        self.delay = delay
        # The latency level. Valid values:
        # 
        # *   **short**: The latency is less than or equal to 4 seconds.
        # *   **medium**: The latency is greater than 4 seconds, and less than or equal to 8 seconds.
        # *   **long**: The latency is greater than 8 seconds.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay is not None:
            result['Delay'] = self.delay

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

