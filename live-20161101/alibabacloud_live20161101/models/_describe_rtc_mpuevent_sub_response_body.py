# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeRtcMPUEventSubResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sub_info: main_models.DescribeRtcMPUEventSubResponseBodySubInfo = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the subscription.
        self.sub_info = sub_info

    def validate(self):
        if self.sub_info:
            self.sub_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sub_info is not None:
            result['SubInfo'] = self.sub_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubInfo') is not None:
            temp_model = main_models.DescribeRtcMPUEventSubResponseBodySubInfo()
            self.sub_info = temp_model.from_map(m.get('SubInfo'))

        return self

class DescribeRtcMPUEventSubResponseBodySubInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback_url: str = None,
        channel_ids: str = None,
        create_time: str = None,
        sub_id: str = None,
    ):
        # The application ID. You can specify only one application ID.
        self.app_id = app_id
        # The callback URL.
        self.callback_url = callback_url
        # The ID of the channel to which mixed-stream relay event callbacks are sent. Multiple channel IDs are separated by commas (,). If this parameter is not returned, mixed-stream relay event callbacks are sent to all channels.
        self.channel_ids = channel_ids
        # The time when the event callback was fired. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the subscription.
        self.sub_id = sub_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.sub_id is not None:
            result['SubId'] = self.sub_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')

        return self

