# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RecognizeOrderRequest(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        candidate_items: List[str] = None,
        device_id: str = None,
        order_unique_id: str = None,
        video_urls: List[str] = None,
    ):
        # Callback URL for this task. If not provided, the registered default address is used.
        self.callback_url = callback_url
        # List of candidate items. It is recommended to pass platform_item_id.
        self.candidate_items = candidate_items
        # Device ID
        self.device_id = device_id
        # Unique idempotent ID of the business party, unique within the same business party
        self.order_unique_id = order_unique_id
        # List of shopping video OSS addresses (currently only one is supported)
        self.video_urls = video_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.candidate_items is not None:
            result['CandidateItems'] = self.candidate_items

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.order_unique_id is not None:
            result['OrderUniqueId'] = self.order_unique_id

        if self.video_urls is not None:
            result['VideoUrls'] = self.video_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('CandidateItems') is not None:
            self.candidate_items = m.get('CandidateItems')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('OrderUniqueId') is not None:
            self.order_unique_id = m.get('OrderUniqueId')

        if m.get('VideoUrls') is not None:
            self.video_urls = m.get('VideoUrls')

        return self

