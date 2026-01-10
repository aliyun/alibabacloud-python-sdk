# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class BrowserConfiguration(DaraModel):
    def __init__(
        self,
        browser_type: str = None,
        enable_extension: List[str] = None,
        headless: bool = None,
        user_agent: str = None,
        view_port: main_models.ViewPortConfiguration = None,
    ):
        self.browser_type = browser_type
        # 要启用的浏览器扩展列表
        self.enable_extension = enable_extension
        # 是否以无头模式运行浏览器
        self.headless = headless
        # 浏览器用户代理字符串
        self.user_agent = user_agent
        self.view_port = view_port

    def validate(self):
        if self.view_port:
            self.view_port.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_type is not None:
            result['browserType'] = self.browser_type

        if self.enable_extension is not None:
            result['enableExtension'] = self.enable_extension

        if self.headless is not None:
            result['headless'] = self.headless

        if self.user_agent is not None:
            result['userAgent'] = self.user_agent

        if self.view_port is not None:
            result['viewPort'] = self.view_port.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserType') is not None:
            self.browser_type = m.get('browserType')

        if m.get('enableExtension') is not None:
            self.enable_extension = m.get('enableExtension')

        if m.get('headless') is not None:
            self.headless = m.get('headless')

        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')

        if m.get('viewPort') is not None:
            temp_model = main_models.ViewPortConfiguration()
            self.view_port = temp_model.from_map(m.get('viewPort'))

        return self

