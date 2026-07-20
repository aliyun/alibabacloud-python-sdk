# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetResourceControlEventRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        event_id: str = None,
        event_id_list: List[str] = None,
    ):
        self.aliyun_lang = aliyun_lang
        # This parameter is required.
        self.event_id = event_id
        self.event_id_list = event_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_id_list is not None:
            result['EventIdList'] = self.event_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventIdList') is not None:
            self.event_id_list = m.get('EventIdList')

        return self

