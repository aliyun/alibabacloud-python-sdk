# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartViewShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        bg_color: main_models.StartViewShrinkRequestBgColor = None,
        channel_id: str = None,
        crop_mode: int = None,
        region_color: main_models.StartViewShrinkRequestRegionColor = None,
        start_without_channel: bool = None,
        start_without_channel_wait_time: int = None,
        task_id: str = None,
        template_id: str = None,
        view_content: str = None,
        view_subscribers_shrink: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.bg_color = bg_color
        # This parameter is required.
        self.channel_id = channel_id
        self.crop_mode = crop_mode
        self.region_color = region_color
        self.start_without_channel = start_without_channel
        self.start_without_channel_wait_time = start_without_channel_wait_time
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.template_id = template_id
        self.view_content = view_content
        self.view_subscribers_shrink = view_subscribers_shrink

    def validate(self):
        if self.bg_color:
            self.bg_color.validate()
        if self.region_color:
            self.region_color.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.bg_color is not None:
            result['BgColor'] = self.bg_color.to_map()

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode

        if self.region_color is not None:
            result['RegionColor'] = self.region_color.to_map()

        if self.start_without_channel is not None:
            result['StartWithoutChannel'] = self.start_without_channel

        if self.start_without_channel_wait_time is not None:
            result['StartWithoutChannelWaitTime'] = self.start_without_channel_wait_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.view_content is not None:
            result['ViewContent'] = self.view_content

        if self.view_subscribers_shrink is not None:
            result['ViewSubscribers'] = self.view_subscribers_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BgColor') is not None:
            temp_model = main_models.StartViewShrinkRequestBgColor()
            self.bg_color = temp_model.from_map(m.get('BgColor'))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')

        if m.get('RegionColor') is not None:
            temp_model = main_models.StartViewShrinkRequestRegionColor()
            self.region_color = temp_model.from_map(m.get('RegionColor'))

        if m.get('StartWithoutChannel') is not None:
            self.start_without_channel = m.get('StartWithoutChannel')

        if m.get('StartWithoutChannelWaitTime') is not None:
            self.start_without_channel_wait_time = m.get('StartWithoutChannelWaitTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('ViewContent') is not None:
            self.view_content = m.get('ViewContent')

        if m.get('ViewSubscribers') is not None:
            self.view_subscribers_shrink = m.get('ViewSubscribers')

        return self

class StartViewShrinkRequestRegionColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # B。
        self.b = b
        # G。
        self.g = g
        # R。
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartViewShrinkRequestBgColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # B。
        self.b = b
        # G。
        self.g = g
        # R。
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

