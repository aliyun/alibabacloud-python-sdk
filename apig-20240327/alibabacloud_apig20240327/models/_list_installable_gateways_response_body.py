# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListInstallableGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListInstallableGatewaysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListInstallableGatewaysResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListInstallableGatewaysResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListInstallableGatewaysResponseBodyDataItems] = None,
        page_number: str = None,
        page_size: str = None,
        total_size: str = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListInstallableGatewaysResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListInstallableGatewaysResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        engine_version: str = None,
        gateway_id: str = None,
        gateway_phase: str = None,
        installable: bool = None,
        installable_false_reason_type: str = None,
        installed_plugin_version: str = None,
        name: str = None,
    ):
        self.engine_version = engine_version
        self.gateway_id = gateway_id
        self.gateway_phase = gateway_phase
        self.installable = installable
        self.installable_false_reason_type = installable_false_reason_type
        self.installed_plugin_version = installed_plugin_version
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_phase is not None:
            result['gatewayPhase'] = self.gateway_phase

        if self.installable is not None:
            result['installable'] = self.installable

        if self.installable_false_reason_type is not None:
            result['installableFalseReasonType'] = self.installable_false_reason_type

        if self.installed_plugin_version is not None:
            result['installedPluginVersion'] = self.installed_plugin_version

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayPhase') is not None:
            self.gateway_phase = m.get('gatewayPhase')

        if m.get('installable') is not None:
            self.installable = m.get('installable')

        if m.get('installableFalseReasonType') is not None:
            self.installable_false_reason_type = m.get('installableFalseReasonType')

        if m.get('installedPluginVersion') is not None:
            self.installed_plugin_version = m.get('installedPluginVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

