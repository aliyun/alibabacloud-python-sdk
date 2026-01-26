# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEventBridgeIntegrationsResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.ListEventBridgeIntegrationsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The information about EventBridge integrations that is returned on each page.
        self.page_bean = page_bean
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.ListEventBridgeIntegrationsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEventBridgeIntegrationsResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        event_bridge_integrations: List[main_models.ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The EventBridge integrations.
        self.event_bridge_integrations = event_bridge_integrations
        # The number of the returned page.
        self.page = page
        # The number of entries returned per page.
        self.size = size
        # The total number of EventBridge integrations that are returned.
        self.total = total

    def validate(self):
        if self.event_bridge_integrations:
            for v1 in self.event_bridge_integrations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventBridgeIntegrations'] = []
        if self.event_bridge_integrations is not None:
            for k1 in self.event_bridge_integrations:
                result['EventBridgeIntegrations'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_bridge_integrations = []
        if m.get('EventBridgeIntegrations') is not None:
            for k1 in m.get('EventBridgeIntegrations'):
                temp_model = main_models.ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations()
                self.event_bridge_integrations.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        # The description of the EventBridge integration.
        self.description = description
        # The ID of the EventBridge integration.
        self.id = id
        # The name of the EventBridge integration.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

