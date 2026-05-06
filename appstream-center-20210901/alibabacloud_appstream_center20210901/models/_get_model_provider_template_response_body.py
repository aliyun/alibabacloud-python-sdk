# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetModelProviderTemplateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetModelProviderTemplateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetModelProviderTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetModelProviderTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        config: str = None,
        description: str = None,
        enable_wuying_proxy: bool = None,
        name: str = None,
        provider_name: str = None,
        provider_template_id: str = None,
    ):
        self.config = config
        self.description = description
        self.enable_wuying_proxy = enable_wuying_proxy
        self.name = name
        self.provider_name = provider_name
        self.provider_template_id = provider_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_wuying_proxy is not None:
            result['EnableWuyingProxy'] = self.enable_wuying_proxy

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableWuyingProxy') is not None:
            self.enable_wuying_proxy = m.get('EnableWuyingProxy')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        return self

