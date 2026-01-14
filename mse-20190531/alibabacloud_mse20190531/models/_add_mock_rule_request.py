# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMockRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        consumer_app_ids: str = None,
        dubbo_mock_items: str = None,
        enable: bool = None,
        extra_json: str = None,
        mock_type: int = None,
        name: str = None,
        provider_app_id: str = None,
        provider_app_name: str = None,
        region: str = None,
        sc_mock_items: str = None,
        source: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the custom application.
        # 
        # This parameter is required.
        self.consumer_app_ids = consumer_app_ids
        # The items in the recycle bin.
        # 
        # This parameter is required.
        self.dubbo_mock_items = dubbo_mock_items
        # Specifies whether to enable the alert rule. Valid values:
        # 
        # *   `true`: enables the alert rule.
        # *   `false`: disables the alert rule.
        self.enable = enable
        # The description.
        # 
        # This parameter is required.
        self.extra_json = extra_json
        # The response time (RT) threshold of slow calls. Valid values:
        # 
        # *   \\- 15: 15 ms
        # *   \\- 30: 30 ms
        # *   \\- 60: 60 ms
        # *   \\- 120: 120 ms
        self.mock_type = mock_type
        # The name of the rule.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the service provider application.
        self.provider_app_id = provider_app_id
        # The name of the service provider application.
        self.provider_app_name = provider_app_name
        # The ID of the region.
        # 
        # This parameter is required.
        self.region = region
        # The input parameters. The JSON format is supported.
        # 
        # This parameter is required.
        self.sc_mock_items = sc_mock_items
        # The rule source.
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

        if self.consumer_app_ids is not None:
            result['ConsumerAppIds'] = self.consumer_app_ids

        if self.dubbo_mock_items is not None:
            result['DubboMockItems'] = self.dubbo_mock_items

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json

        if self.mock_type is not None:
            result['MockType'] = self.mock_type

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id

        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name

        if self.region is not None:
            result['Region'] = self.region

        if self.sc_mock_items is not None:
            result['ScMockItems'] = self.sc_mock_items

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ConsumerAppIds') is not None:
            self.consumer_app_ids = m.get('ConsumerAppIds')

        if m.get('DubboMockItems') is not None:
            self.dubbo_mock_items = m.get('DubboMockItems')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')

        if m.get('MockType') is not None:
            self.mock_type = m.get('MockType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')

        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ScMockItems') is not None:
            self.sc_mock_items = m.get('ScMockItems')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

