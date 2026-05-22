# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListVideoProcessingsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListVideoProcessingsResponseBodyConfigs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The configurations.
        self.configs = configs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The total number of pages returned.
        self.total_page = total_page

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListVideoProcessingsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListVideoProcessingsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        flv_seek_end: str = None,
        flv_seek_start: str = None,
        flv_video_seek_mode: str = None,
        mp_4seek_end: str = None,
        mp_4seek_start: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
        video_seek_enable: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The type of the configuration. Valid values:
        # 
        # *   global: global configuration.
        # *   rule: rule configuration.
        self.config_type = config_type
        # The custom end parameter for FLV files.
        self.flv_seek_end = flv_seek_end
        # The custom start parameter for FLV files.
        self.flv_seek_start = flv_seek_start
        # FLV seeking. Valid values:
        # 
        # *   by_byte: Seek by byte.
        # *   by_time: Seek by time.
        self.flv_video_seek_mode = flv_video_seek_mode
        # Customize the mp4 end parameter.
        self.mp_4seek_end = mp_4seek_end
        # Customize the mp4 start parameter.
        self.mp_4seek_start = mp_4seek_start
        # The rule content.
        self.rule = rule
        # Indicates whether the rule is enabled. Valid values:
        # 
        # *   on
        # *   off
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The order in which the rule is executed. The smaller the value, the higher the priority.
        self.sequence = sequence
        # The version number of the website configurations.
        self.site_version = site_version
        # Video seeking. Valid values:
        # 
        # *   on
        # *   off
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

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

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

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.video_seek_enable is not None:
            result['VideoSeekEnable'] = self.video_seek_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

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

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('VideoSeekEnable') is not None:
            self.video_seek_enable = m.get('VideoSeekEnable')

        return self

