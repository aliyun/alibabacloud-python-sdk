# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class QueryAlertRulesFilter(DaraModel):
    def __init__(
        self,
        datasource_type: str = None,
        display_name: main_models.DisplayNameFilter = None,
        enabled: main_models.EnabledFilter = None,
        labels: main_models.LabelsFilter = None,
        observe_resource_global_scope: bool = None,
        observe_resource_instance_id: str = None,
        observe_resource_type: str = None,
        severity_levels: str = None,
        status: main_models.StatusFilter = None,
        uuid: main_models.UuidFilter = None,
    ):
        self.datasource_type = datasource_type
        # Filters alert rules by display name.
        self.display_name = display_name
        # Filters alert rules by enabled status.
        self.enabled = enabled
        # Filters alert rules by label.
        self.labels = labels
        self.observe_resource_global_scope = observe_resource_global_scope
        self.observe_resource_instance_id = observe_resource_instance_id
        self.observe_resource_type = observe_resource_type
        self.severity_levels = severity_levels
        # Filters alert rules by status.
        self.status = status
        # Filters alert rules by UUID.
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
        if self.datasource_type is not None:
            result['datasourceType'] = self.datasource_type

        if self.display_name is not None:
            result['displayName'] = self.display_name.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled.to_map()

        if self.labels is not None:
            result['labels'] = self.labels.to_map()

        if self.observe_resource_global_scope is not None:
            result['observeResourceGlobalScope'] = self.observe_resource_global_scope

        if self.observe_resource_instance_id is not None:
            result['observeResourceInstanceId'] = self.observe_resource_instance_id

        if self.observe_resource_type is not None:
            result['observeResourceType'] = self.observe_resource_type

        if self.severity_levels is not None:
            result['severityLevels'] = self.severity_levels

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.uuid is not None:
            result['uuid'] = self.uuid.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasourceType') is not None:
            self.datasource_type = m.get('datasourceType')

        if m.get('displayName') is not None:
            temp_model = main_models.DisplayNameFilter()
            self.display_name = temp_model.from_map(m.get('displayName'))

        if m.get('enabled') is not None:
            temp_model = main_models.EnabledFilter()
            self.enabled = temp_model.from_map(m.get('enabled'))

        if m.get('labels') is not None:
            temp_model = main_models.LabelsFilter()
            self.labels = temp_model.from_map(m.get('labels'))

        if m.get('observeResourceGlobalScope') is not None:
            self.observe_resource_global_scope = m.get('observeResourceGlobalScope')

        if m.get('observeResourceInstanceId') is not None:
            self.observe_resource_instance_id = m.get('observeResourceInstanceId')

        if m.get('observeResourceType') is not None:
            self.observe_resource_type = m.get('observeResourceType')

        if m.get('severityLevels') is not None:
            self.severity_levels = m.get('severityLevels')

        if m.get('status') is not None:
            temp_model = main_models.StatusFilter()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('uuid') is not None:
            temp_model = main_models.UuidFilter()
            self.uuid = temp_model.from_map(m.get('uuid'))

        return self

