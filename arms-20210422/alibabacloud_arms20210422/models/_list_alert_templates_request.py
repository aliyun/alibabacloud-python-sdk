# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertTemplatesRequest(DaraModel):
    def __init__(
        self,
        alert_provider: str = None,
        labels: str = None,
        name: str = None,
        region_id: str = None,
        status: bool = None,
        template_provider: str = None,
        type: str = None,
    ):
        self.alert_provider = alert_provider
        self.labels = labels
        self.name = name
        # This parameter is required.
        self.region_id = region_id
        self.status = status
        self.template_provider = template_provider
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_provider is not None:
            result['AlertProvider'] = self.alert_provider

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.template_provider is not None:
            result['TemplateProvider'] = self.template_provider

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertProvider') is not None:
            self.alert_provider = m.get('AlertProvider')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateProvider') is not None:
            self.template_provider = m.get('TemplateProvider')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

