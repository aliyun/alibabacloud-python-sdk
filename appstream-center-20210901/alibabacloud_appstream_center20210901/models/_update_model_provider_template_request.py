# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class UpdateModelProviderTemplateRequest(DaraModel):
    def __init__(
        self,
        config: main_models.UpdateModelProviderTemplateRequestConfig = None,
        description: str = None,
        enable_wuying_proxy: bool = None,
        name: str = None,
        provider_template_id: str = None,
    ):
        self.config = config
        self.description = description
        self.enable_wuying_proxy = enable_wuying_proxy
        self.name = name
        # This parameter is required.
        self.provider_template_id = provider_template_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_wuying_proxy is not None:
            result['EnableWuyingProxy'] = self.enable_wuying_proxy

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.UpdateModelProviderTemplateRequestConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableWuyingProxy') is not None:
            self.enable_wuying_proxy = m.get('EnableWuyingProxy')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        return self

class UpdateModelProviderTemplateRequestConfig(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        api_type: str = None,
        base_url: str = None,
    ):
        self.api_key = api_key
        self.api_type = api_type
        self.base_url = base_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        return self

