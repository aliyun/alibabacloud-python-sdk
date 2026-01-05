# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeCloudPhoneNodeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        display_config: str = None,
        down_bandwidth_limit: int = None,
        instance_type: str = None,
        node_id: str = None,
        phone_count: int = None,
        phone_data_volume: int = None,
        promotion_id: str = None,
        share_data_volume: int = None,
        swap_size: int = None,
        up_bandwidth_limit: int = None,
    ):
        self.auto_pay = auto_pay
        self.display_config = display_config
        self.down_bandwidth_limit = down_bandwidth_limit
        self.instance_type = instance_type
        self.node_id = node_id
        self.phone_count = phone_count
        self.phone_data_volume = phone_data_volume
        self.promotion_id = promotion_id
        self.share_data_volume = share_data_volume
        self.swap_size = swap_size
        self.up_bandwidth_limit = up_bandwidth_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.display_config is not None:
            result['DisplayConfig'] = self.display_config

        if self.down_bandwidth_limit is not None:
            result['DownBandwidthLimit'] = self.down_bandwidth_limit

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count

        if self.phone_data_volume is not None:
            result['PhoneDataVolume'] = self.phone_data_volume

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.share_data_volume is not None:
            result['ShareDataVolume'] = self.share_data_volume

        if self.swap_size is not None:
            result['SwapSize'] = self.swap_size

        if self.up_bandwidth_limit is not None:
            result['UpBandwidthLimit'] = self.up_bandwidth_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('DisplayConfig') is not None:
            self.display_config = m.get('DisplayConfig')

        if m.get('DownBandwidthLimit') is not None:
            self.down_bandwidth_limit = m.get('DownBandwidthLimit')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')

        if m.get('PhoneDataVolume') is not None:
            self.phone_data_volume = m.get('PhoneDataVolume')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('ShareDataVolume') is not None:
            self.share_data_volume = m.get('ShareDataVolume')

        if m.get('SwapSize') is not None:
            self.swap_size = m.get('SwapSize')

        if m.get('UpBandwidthLimit') is not None:
            self.up_bandwidth_limit = m.get('UpBandwidthLimit')

        return self

