# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        language: str = None,
        namespace: str = None,
        region: str = None,
        sentinel_enable: str = None,
        source: str = None,
        switch_enable: str = None,
        tags: List[main_models.CreateApplicationRequestTags] = None,
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
        # The programming language of the application.
        self.language = language
        # MSE命名空间名字。
        self.namespace = namespace
        # The region to which the application belongs.
        # 
        # This parameter is required.
        self.region = region
        # Specifies whether to start the switch.
        self.sentinel_enable = sentinel_enable
        # The service where the application is deployed. A value of ACK indicates Container Service for Kubernetes.
        self.source = source
        # The name of the Microservices Engine (MSE) namespace.
        self.switch_enable = switch_enable
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.language is not None:
            result['Language'] = self.language

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        if self.sentinel_enable is not None:
            result['SentinelEnable'] = self.sentinel_enable

        if self.source is not None:
            result['Source'] = self.source

        if self.switch_enable is not None:
            result['SwitchEnable'] = self.switch_enable

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SentinelEnable') is not None:
            self.sentinel_enable = m.get('SentinelEnable')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SwitchEnable') is not None:
            self.switch_enable = m.get('SwitchEnable')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateApplicationRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateApplicationRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

