# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_pai20240521 import models as main_models
from darabonba.model import DaraModel

class QuickStartModel(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        deployment_count: int = None,
        domain: str = None,
        extra_info: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[main_models.Label] = None,
        latest_version: main_models.ModelVersion = None,
        model_description: str = None,
        model_doc: str = None,
        model_id: str = None,
        model_name: str = None,
        order_number: int = None,
        origin: str = None,
        owner_id: str = None,
        provider: str = None,
        quick_start_model_description: Dict[str, Any] = None,
        quick_start_model_name: Dict[str, Any] = None,
        related_model_id: str = None,
        task: str = None,
        training_count: int = None,
        user_id: str = None,
        view_count: int = None,
        view_count_7days: int = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.deployment_count = deployment_count
        self.domain = domain
        self.extra_info = extra_info
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.labels = labels
        self.latest_version = latest_version
        self.model_description = model_description
        self.model_doc = model_doc
        self.model_id = model_id
        self.model_name = model_name
        self.order_number = order_number
        self.origin = origin
        self.owner_id = owner_id
        self.provider = provider
        self.quick_start_model_description = quick_start_model_description
        self.quick_start_model_name = quick_start_model_name
        self.related_model_id = related_model_id
        self.task = task
        self.training_count = training_count
        self.user_id = user_id
        self.view_count = view_count
        self.view_count_7days = view_count_7days
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.latest_version:
            self.latest_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.deployment_count is not None:
            result['DeploymentCount'] = self.deployment_count

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()

        if self.model_description is not None:
            result['ModelDescription'] = self.model_description

        if self.model_doc is not None:
            result['ModelDoc'] = self.model_doc

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.quick_start_model_description is not None:
            result['QuickStartModelDescription'] = self.quick_start_model_description

        if self.quick_start_model_name is not None:
            result['QuickStartModelName'] = self.quick_start_model_name

        if self.related_model_id is not None:
            result['RelatedModelId'] = self.related_model_id

        if self.task is not None:
            result['Task'] = self.task

        if self.training_count is not None:
            result['TrainingCount'] = self.training_count

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.view_count is not None:
            result['ViewCount'] = self.view_count

        if self.view_count_7days is not None:
            result['ViewCount7Days'] = self.view_count_7days

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('DeploymentCount') is not None:
            self.deployment_count = m.get('DeploymentCount')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatestVersion') is not None:
            temp_model = main_models.ModelVersion()
            self.latest_version = temp_model.from_map(m.get('LatestVersion'))

        if m.get('ModelDescription') is not None:
            self.model_description = m.get('ModelDescription')

        if m.get('ModelDoc') is not None:
            self.model_doc = m.get('ModelDoc')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('QuickStartModelDescription') is not None:
            self.quick_start_model_description = m.get('QuickStartModelDescription')

        if m.get('QuickStartModelName') is not None:
            self.quick_start_model_name = m.get('QuickStartModelName')

        if m.get('RelatedModelId') is not None:
            self.related_model_id = m.get('RelatedModelId')

        if m.get('Task') is not None:
            self.task = m.get('Task')

        if m.get('TrainingCount') is not None:
            self.training_count = m.get('TrainingCount')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')

        if m.get('ViewCount7Days') is not None:
            self.view_count_7days = m.get('ViewCount7Days')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

