# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveStreamDelayConfigRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        flv_delay: int = None,
        flv_level: str = None,
        hls_delay: int = None,
        hls_level: str = None,
        owner_id: int = None,
        region_id: str = None,
        rtmp_delay: int = None,
        rtmp_level: str = None,
    ):
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The latency of FLV-based playback. Unit: seconds.
        # 
        # >  If this parameter is left empty, the latency is set to a value corresponding to the FlvLevel parameter.
        self.flv_delay = flv_delay
        # The latency level of FLV-based playback. Ignore this parameter if the FlvDelay parameter is configured.
        # 
        # Valid values:
        # 
        # *   **short** (default): The latency is 4 seconds.
        # *   **medium**: The latency is 8 seconds.
        # *   **long**: The latency is 16 seconds.
        # 
        # >  If both the FlvDelay and FlvLevel parameters are left empty, FlvLevel is set to **short** by default.
        self.flv_level = flv_level
        # The latency of HLS-based playback. Unit: seconds.
        # 
        # >  If this parameter is left empty, the latency is set to a value corresponding to the HlsLevel parameter.
        self.hls_delay = hls_delay
        # The latency level of HLS-based playback. Ignore this parameter if the HlsDelay parameter is configured.
        # 
        # Valid values:
        # 
        # *   **short**: The latency is 3 seconds. This is the default value.
        # *   **medium**: The latency is 6 seconds.
        # *   **long**: The latency is 15 seconds.
        # 
        # >  If both the HlsDelay and HlsLevel parameters are left empty, HlsLevel is set to **short** by default.
        self.hls_level = hls_level
        self.owner_id = owner_id
        self.region_id = region_id
        # The latency of RTMP-based playback. Unit: seconds.
        # 
        # >  If this parameter is left empty, the latency is set to a value corresponding to the RtmpLevel parameter.
        self.rtmp_delay = rtmp_delay
        # The latency level of RTMP-based playback. Ignore this parameter if the RtmpDelay parameter is configured.
        # 
        # Valid values:
        # 
        # *   **short** (default): The latency is 4 seconds.
        # *   **medium**: The latency is 8 seconds.
        # *   **long**: The latency is 16 seconds.
        # 
        # >  If both the RtmpDelay and RtmpLevel parameters are left empty, RtmpLevel is set to **short** by default.
        self.rtmp_level = rtmp_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.flv_delay is not None:
            result['FlvDelay'] = self.flv_delay

        if self.flv_level is not None:
            result['FlvLevel'] = self.flv_level

        if self.hls_delay is not None:
            result['HlsDelay'] = self.hls_delay

        if self.hls_level is not None:
            result['HlsLevel'] = self.hls_level

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rtmp_delay is not None:
            result['RtmpDelay'] = self.rtmp_delay

        if self.rtmp_level is not None:
            result['RtmpLevel'] = self.rtmp_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FlvDelay') is not None:
            self.flv_delay = m.get('FlvDelay')

        if m.get('FlvLevel') is not None:
            self.flv_level = m.get('FlvLevel')

        if m.get('HlsDelay') is not None:
            self.hls_delay = m.get('HlsDelay')

        if m.get('HlsLevel') is not None:
            self.hls_level = m.get('HlsLevel')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RtmpDelay') is not None:
            self.rtmp_delay = m.get('RtmpDelay')

        if m.get('RtmpLevel') is not None:
            self.rtmp_level = m.get('RtmpLevel')

        return self

