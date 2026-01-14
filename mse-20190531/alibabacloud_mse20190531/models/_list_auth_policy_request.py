# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthPolicyRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        name: str = None,
        namespace: str = None,
        page_number: str = None,
        page_size: str = None,
        protocol: str = None,
        region: str = None,
        source: str = None,
    ):
        # The language of the response. Valid values: zh-CN and en-US. Default value: zh-CN. The value zh-CN indicates Chinese and the value en-US indicates English.
        self.accept_language = accept_language
        # The application ID.
        self.app_id = app_id
        # The name of the authentication rule.
        self.name = name
        # The name of the Microservices Engine (MSE) namespace.
        self.namespace = namespace
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The protocol type. Valid values:
        # 
        # *   **SPRING_CLOUD**
        # *   **DUBBO**
        # *   **istio**
        self.protocol = protocol
        # The region ID.
        # 
        # This parameter is required.
        self.region = region
        # The service source.
        # 
        # This parameter is required.
        self.source = source

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

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region is not None:
            result['Region'] = self.region

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

