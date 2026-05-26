# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecognizeOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        candidate_items_shrink: str = None,
        device_id: str = None,
        order_unique_id: str = None,
        video_urls_shrink: str = None,
    ):
        self.callback_url = callback_url
        self.candidate_items_shrink = candidate_items_shrink
        self.device_id = device_id
        self.order_unique_id = order_unique_id
        self.video_urls_shrink = video_urls_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.candidate_items_shrink is not None:
            result['CandidateItems'] = self.candidate_items_shrink

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.order_unique_id is not None:
            result['OrderUniqueId'] = self.order_unique_id

        if self.video_urls_shrink is not None:
            result['VideoUrls'] = self.video_urls_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('CandidateItems') is not None:
            self.candidate_items_shrink = m.get('CandidateItems')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('OrderUniqueId') is not None:
            self.order_unique_id = m.get('OrderUniqueId')

        if m.get('VideoUrls') is not None:
            self.video_urls_shrink = m.get('VideoUrls')

        return self

