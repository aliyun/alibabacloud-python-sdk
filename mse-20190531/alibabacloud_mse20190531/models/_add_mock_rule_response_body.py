# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class AddMockRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.AddMockRuleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The details of the data.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AddMockRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddMockRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        consumer_app_id: str = None,
        consumer_app_name: str = None,
        enable: bool = None,
        extra_json: str = None,
        id: int = None,
        mock_type: int = None,
        name: str = None,
        namespace_id: str = None,
        provider_app_id: str = None,
        provider_app_name: str = None,
        region: str = None,
        sc_mock_item_json: str = None,
        source: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The ID of the consumer application.
        self.consumer_app_id = consumer_app_id
        # The name of the consumer application.
        self.consumer_app_name = consumer_app_name
        # Indicates whether the mock rule is enabled.
        # 
        # *   `true`: enabled
        # *   `false`: disabled
        self.enable = enable
        # The description.
        self.extra_json = extra_json
        # The ID of the rule.
        self.id = id
        # The mock type. Valid values:
        # 
        # *   \\- `[unk]0[unk]`: desktop client
        # *   \\- `[unk]1[unk]`: mobile client
        self.mock_type = mock_type
        # The name.
        self.name = name
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The ID of the service provider application.
        self.provider_app_id = provider_app_id
        # The name of the service provider application.
        self.provider_app_name = provider_app_name
        # The region ID.
        self.region = region
        # The HTTP mock rule.
        self.sc_mock_item_json = sc_mock_item_json
        # The service source.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.consumer_app_id is not None:
            result['ConsumerAppId'] = self.consumer_app_id

        if self.consumer_app_name is not None:
            result['ConsumerAppName'] = self.consumer_app_name

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json

        if self.id is not None:
            result['Id'] = self.id

        if self.mock_type is not None:
            result['MockType'] = self.mock_type

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id

        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name

        if self.region is not None:
            result['Region'] = self.region

        if self.sc_mock_item_json is not None:
            result['ScMockItemJson'] = self.sc_mock_item_json

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ConsumerAppId') is not None:
            self.consumer_app_id = m.get('ConsumerAppId')

        if m.get('ConsumerAppName') is not None:
            self.consumer_app_name = m.get('ConsumerAppName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MockType') is not None:
            self.mock_type = m.get('MockType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')

        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ScMockItemJson') is not None:
            self.sc_mock_item_json = m.get('ScMockItemJson')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

