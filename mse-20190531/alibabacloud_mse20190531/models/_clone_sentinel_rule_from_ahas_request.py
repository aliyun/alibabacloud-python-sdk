# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneSentinelRuleFromAhasRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        ahas_namespace: str = None,
        app_name: str = None,
        is_ahaspublic_region: bool = None,
        mse_app_name: str = None,
        namespace: str = None,
    ):
        # The language in which you want to display the results. Valid values: zh and en. zh indicates Chinese, which is the default value. en indicates English.
        self.accept_language = accept_language
        # The namespace (environment) of Application High Availability Service (AHAS).
        # 
        # This parameter is required.
        self.ahas_namespace = ahas_namespace
        # The application name.
        self.app_name = app_name
        # Specifies whether AHAS is deployed in the Internet region.
        self.is_ahaspublic_region = is_ahaspublic_region
        # The name of the MSE application after migration. If this parameter is not specified, the name of the Application High Availability Service (AHAS) application is used by default.
        self.mse_app_name = mse_app_name
        # The namespace.
        # 
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.ahas_namespace is not None:
            result['AhasNamespace'] = self.ahas_namespace

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.is_ahaspublic_region is not None:
            result['IsAHASPublicRegion'] = self.is_ahaspublic_region

        if self.mse_app_name is not None:
            result['MseAppName'] = self.mse_app_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AhasNamespace') is not None:
            self.ahas_namespace = m.get('AhasNamespace')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('IsAHASPublicRegion') is not None:
            self.is_ahaspublic_region = m.get('IsAHASPublicRegion')

        if m.get('MseAppName') is not None:
            self.mse_app_name = m.get('MseAppName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

