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
        # Indicates whether auto-renewal is enabled for the extra internal bandwidth that you purchased. Valid values:
        # 
        # *   **true**: Auto-renewal is enabled.
        # *   **false**: Auto-renewal is disabled.
        # 
        # > If no extra internal bandwidth is purchased, this parameter is not returned.
        self.auto_renewal = auto_renewal
        # The expiration time of the purchased bandwidth. The time follows the ISO 8601 standard in the *yyyy-MM-dd* T *HH:mm:ss* Z format.
        # 
        # > If no extra internal bandwidth is purchased, this parameter is not returned.
        self.bandwidth_expire_time = bandwidth_expire_time
        # The billing method of the bandwidth plan. Valid values:
        # 
        # *   **0**: pay-as-you-go
        # *   **1**: subscription
        self.bandwidth_pre_paid = bandwidth_pre_paid
        # The time when the extra internal bandwidth that you purchased for temporary use expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > If no extra internal bandwidth for temporary use is purchased or the extra internal bandwidth that you purchased for temporary use has expired, **0** is returned for this parameter.
        self.expire_time = expire_time
        # Specifies whether the instance has unexpired bandwidth plans. Valid values:
        # 
        # *   **true**: The instance has unexpired bandwidth plans.
        # *   **false**: The instance does not have unexpired bandwidth plans.
        # 
        # > If no extra internal bandwidth is purchased, this parameter is not returned.
        self.has_pre_paid_band_width_order_running = has_pre_paid_band_width_order_running
        self.intranet_band_width_burst = intranet_band_width_burst
        # The internal bandwidth of the instance. This parameter indicates the combined bandwidth of all shards in the instance. Unit: Mbit/s.
        self.intranet_bandwidth = intranet_bandwidth
        # The ID of the request.
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

