# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPrometheusUserSettingRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
    ):
        self.aliyun_lang = aliyun_lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['aliyunLang'] = self.aliyun_lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunLang') is not None:
            self.aliyun_lang = m.get('aliyunLang')

        return self

