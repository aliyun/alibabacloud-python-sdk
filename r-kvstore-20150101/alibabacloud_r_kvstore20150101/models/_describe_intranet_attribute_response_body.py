# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIntranetAttributeResponseBody(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        bandwidth_expire_time: str = None,
        bandwidth_pre_paid: str = None,
        expire_time: str = None,
        has_pre_paid_band_width_order_running: bool = None,
        intranet_band_width_burst: int = None,
        intranet_bandwidth: int = None,
        request_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled for the bandwidth package. Valid values:
        # 
        # - **true**: Auto-renewal is enabled.
        # 
        # - **false**: Auto-renewal is disabled.
        # 
        # > This parameter is not returned if no additional bandwidth is purchased.
        self.auto_renewal = auto_renewal
        # The expiration time of the bandwidth package. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format.
        # 
        # > This parameter is not returned if no additional bandwidth is purchased.
        self.bandwidth_expire_time = bandwidth_expire_time
        # The billing method of the bandwidth package. Valid values:
        # 
        # - **0**: pay-as-you-go.
        # 
        # - **1**: subscription.
        self.bandwidth_pre_paid = bandwidth_pre_paid
        # The expiration time of the temporary bandwidth. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format.
        # 
        # > This parameter returns **0** if the instance has no temporary bandwidth or if the temporary bandwidth has expired.
        self.expire_time = expire_time
        # Indicates whether the instance has an unexpired bandwidth package. Valid values:
        # 
        # - **true**: An unexpired bandwidth package exists.
        # 
        # - **false**: No unexpired bandwidth package exists.
        # 
        # > This parameter is not returned if no additional bandwidth is purchased.
        self.has_pre_paid_band_width_order_running = has_pre_paid_band_width_order_running
        self.intranet_band_width_burst = intranet_band_width_burst
        # The total intranet bandwidth across all shards in the instance, in MB/s.
        self.intranet_bandwidth = intranet_bandwidth
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.bandwidth_expire_time is not None:
            result['BandwidthExpireTime'] = self.bandwidth_expire_time

        if self.bandwidth_pre_paid is not None:
            result['BandwidthPrePaid'] = self.bandwidth_pre_paid

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.has_pre_paid_band_width_order_running is not None:
            result['HasPrePaidBandWidthOrderRunning'] = self.has_pre_paid_band_width_order_running

        if self.intranet_band_width_burst is not None:
            result['IntranetBandWidthBurst'] = self.intranet_band_width_burst

        if self.intranet_bandwidth is not None:
            result['IntranetBandwidth'] = self.intranet_bandwidth

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('BandwidthExpireTime') is not None:
            self.bandwidth_expire_time = m.get('BandwidthExpireTime')

        if m.get('BandwidthPrePaid') is not None:
            self.bandwidth_pre_paid = m.get('BandwidthPrePaid')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HasPrePaidBandWidthOrderRunning') is not None:
            self.has_pre_paid_band_width_order_running = m.get('HasPrePaidBandWidthOrderRunning')

        if m.get('IntranetBandWidthBurst') is not None:
            self.intranet_band_width_burst = m.get('IntranetBandWidthBurst')

        if m.get('IntranetBandwidth') is not None:
            self.intranet_bandwidth = m.get('IntranetBandwidth')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

