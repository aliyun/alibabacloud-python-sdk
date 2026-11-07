# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppMessageQueueRouteRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        namespace: str = None,
        region: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh: Chinese
        # - en: English
        self.accept_language = accept_language
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The MSE namespace name.
        self.namespace = namespace
        # The region where the cluster is deployed, including but not limited to:
        # - `cn-hangzhou`: Hangzhou
        # - `cn-beijing`: Beijing
        # - `cn-shanghai`: Shanghai
        # - `cn-zhangjiakou`: Zhangjiakou
        # - `cn-shenzhen`: Shenzhen
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

