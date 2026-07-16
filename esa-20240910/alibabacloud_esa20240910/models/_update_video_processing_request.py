# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVideoProcessingRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        flv_seek_end: str = None,
        flv_seek_start: str = None,
        flv_video_seek_mode: str = None,
        mp_4seek_end: str = None,
        mp_4seek_start: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        video_seek_enable: str = None,
    ):
        # The configuration ID. You can call the [ListVideoProcessings](~~ListVideoProcessings~~) operation to obtain the configuration ID.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The custom FLV end parameter.
        self.flv_seek_end = flv_seek_end
        # The custom FLV start parameter.
        self.flv_seek_start = flv_seek_start
        # The FLV seeking mode. Valid values:
        # - by_byte: seek by byte.
        # - by_time: seek by time.
        self.flv_video_seek_mode = flv_video_seek_mode
        # The custom MP4 end parameter.
        self.mp_4seek_end = mp_4seek_end
        # The custom MP4 start parameter.
        self.mp_4seek_start = mp_4seek_start
        # The rule content, which uses a conditional expression to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: set the value to true.
        # - Match specified requests: set the value to a custom expression, such as (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Specifies whether to enable the video seeking feature. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.video_seek_enable = video_seek_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.flv_seek_end is not None:
            result['FlvSeekEnd'] = self.flv_seek_end

        if self.flv_seek_start is not None:
            result['FlvSeekStart'] = self.flv_seek_start

        if self.flv_video_seek_mode is not None:
            result['FlvVideoSeekMode'] = self.flv_video_seek_mode

        if self.mp_4seek_end is not None:
            result['Mp4SeekEnd'] = self.mp_4seek_end

        if self.mp_4seek_start is not None:
            result['Mp4SeekStart'] = self.mp_4seek_start

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.video_seek_enable is not None:
            result['VideoSeekEnable'] = self.video_seek_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('FlvSeekEnd') is not None:
            self.flv_seek_end = m.get('FlvSeekEnd')

        if m.get('FlvSeekStart') is not None:
            self.flv_seek_start = m.get('FlvSeekStart')

        if m.get('FlvVideoSeekMode') is not None:
            self.flv_video_seek_mode = m.get('FlvVideoSeekMode')

        if m.get('Mp4SeekEnd') is not None:
            self.mp_4seek_end = m.get('Mp4SeekEnd')

        if m.get('Mp4SeekStart') is not None:
            self.mp_4seek_start = m.get('Mp4SeekStart')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('VideoSeekEnable') is not None:
            self.video_seek_enable = m.get('VideoSeekEnable')

        return self

