# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAlertRecordAnalysisResultShrinkRequest(DaraModel):
    def __init__(
        self,
        alarm_unique_info: str = None,
        aliyun_lang: str = None,
        unique_info: str = None,
        unique_tag_list_shrink: str = None,
        uuid: str = None,
    ):
        self.alarm_unique_info = alarm_unique_info
        self.aliyun_lang = aliyun_lang
        self.unique_info = unique_info
        self.unique_tag_list_shrink = unique_tag_list_shrink
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info

        if self.unique_tag_list_shrink is not None:
            result['UniqueTagList'] = self.unique_tag_list_shrink

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')

        if m.get('UniqueTagList') is not None:
            self.unique_tag_list_shrink = m.get('UniqueTagList')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

