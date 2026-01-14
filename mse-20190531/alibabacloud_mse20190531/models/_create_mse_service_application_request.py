# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMseServiceApplicationRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        extra_info: str = None,
        language: str = None,
        mse_version: str = None,
        region: str = None,
        sentinel_enable: str = None,
        source: str = None,
        switch_enable: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The name of the application.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The additional information.
        self.extra_info = extra_info
        # The programming language of the application.
        self.language = language
        # The edition of the MSE instance that you want to purchase.
        # 
        # *   mse_pro: Professional Edition.
        # *   mse_dev: Developer Edition.
        self.mse_version = mse_version
        # The ID of the region where the instance resides. Examples:
        # 
        # *   cn-hangzhou: China (Hangzhou)
        # *   cn-beijing: China (Beijing)
        # *   cn-shanghai: China (Shanghai)
        # *   cn-zhangjiakou: China (Zhangjiakou)
        # *   cn-shenzhen: China (Shenzhen)
        # 
        # This parameter is required.
        self.region = region
        # Specifies whether to enable the Sentinel-compatible mode.
        self.sentinel_enable = sentinel_enable
        # The service source.
        self.source = source
        # Specifies whether to enable switching.
        self.switch_enable = switch_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.language is not None:
            result['Language'] = self.language

        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version

        if self.region is not None:
            result['Region'] = self.region

        if self.sentinel_enable is not None:
            result['SentinelEnable'] = self.sentinel_enable

        if self.source is not None:
            result['Source'] = self.source

        if self.switch_enable is not None:
            result['SwitchEnable'] = self.switch_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SentinelEnable') is not None:
            self.sentinel_enable = m.get('SentinelEnable')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SwitchEnable') is not None:
            self.switch_enable = m.get('SwitchEnable')

        return self

