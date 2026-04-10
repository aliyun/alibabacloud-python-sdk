# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class QueryAlertRulesFilter(DaraModel):
    def __init__(
        self,
        display_name: main_models.DisplayNameFilter = None,
        enabled: main_models.EnabledFilter = None,
        labels: main_models.LabelsFilter = None,
        status: main_models.StatusFilter = None,
        uuid: main_models.UuidFilter = None,
    ):
        self.display_name = display_name
        self.enabled = enabled
        self.labels = labels
        self.status = status
        self.uuid = uuid

    def validate(self):
        if self.display_name:
            self.display_name.validate()
        if self.enabled:
            self.enabled.validate()
        if self.labels:
            self.labels.validate()
        if self.status:
            self.status.validate()
        if self.uuid:
            self.uuid.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled.to_map()

        if self.labels is not None:
            result['labels'] = self.labels.to_map()

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.uuid is not None:
            result['uuid'] = self.uuid.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            temp_model = main_models.DisplayNameFilter()
            self.display_name = temp_model.from_map(m.get('displayName'))

        if m.get('enabled') is not None:
            temp_model = main_models.EnabledFilter()
            self.enabled = temp_model.from_map(m.get('enabled'))

        if m.get('labels') is not None:
            temp_model = main_models.LabelsFilter()
            self.labels = temp_model.from_map(m.get('labels'))

        if m.get('status') is not None:
            temp_model = main_models.StatusFilter()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('uuid') is not None:
            temp_model = main_models.UuidFilter()
            self.uuid = temp_model.from_map(m.get('uuid'))

        return self

