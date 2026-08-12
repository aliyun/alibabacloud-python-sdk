# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class BatchExportHttpApisRequest(DaraModel):
    def __init__(
        self,
        api_ids: List[str] = None,
        api_type: str = None,
        extension_config: main_models.BatchExportHttpApisRequestExtensionConfig = None,
        format: str = None,
        gateway_id: str = None,
    ):
        # This parameter is required.
        self.api_ids = api_ids
        # This parameter is required.
        self.api_type = api_type
        self.extension_config = extension_config
        self.format = format
        self.gateway_id = gateway_id

    def validate(self):
        if self.extension_config:
            self.extension_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids

        if self.api_type is not None:
            result['apiType'] = self.api_type

        if self.extension_config is not None:
            result['extensionConfig'] = self.extension_config.to_map()

        if self.format is not None:
            result['format'] = self.format

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')

        if m.get('apiType') is not None:
            self.api_type = m.get('apiType')

        if m.get('extensionConfig') is not None:
            temp_model = main_models.BatchExportHttpApisRequestExtensionConfig()
            self.extension_config = temp_model.from_map(m.get('extensionConfig'))

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        return self

class BatchExportHttpApisRequestExtensionConfig(DaraModel):
    def __init__(
        self,
        with_auth_config: bool = None,
        with_auth_consumer: bool = None,
        with_plugin: bool = None,
        with_policy: bool = None,
        with_service: bool = None,
    ):
        self.with_auth_config = with_auth_config
        self.with_auth_consumer = with_auth_consumer
        self.with_plugin = with_plugin
        self.with_policy = with_policy
        self.with_service = with_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.with_auth_config is not None:
            result['withAuthConfig'] = self.with_auth_config

        if self.with_auth_consumer is not None:
            result['withAuthConsumer'] = self.with_auth_consumer

        if self.with_plugin is not None:
            result['withPlugin'] = self.with_plugin

        if self.with_policy is not None:
            result['withPolicy'] = self.with_policy

        if self.with_service is not None:
            result['withService'] = self.with_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withAuthConfig') is not None:
            self.with_auth_config = m.get('withAuthConfig')

        if m.get('withAuthConsumer') is not None:
            self.with_auth_consumer = m.get('withAuthConsumer')

        if m.get('withPlugin') is not None:
            self.with_plugin = m.get('withPlugin')

        if m.get('withPolicy') is not None:
            self.with_policy = m.get('withPolicy')

        if m.get('withService') is not None:
            self.with_service = m.get('withService')

        return self

