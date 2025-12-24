# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DeleteLaunchTemplateVersionResponseBody(DaraModel):
    def __init__(
        self,
        launch_template_versions: main_models.DeleteLaunchTemplateVersionResponseBodyLaunchTemplateVersions = None,
        request_id: str = None,
    ):
        # The deleted launch template versions.
        self.launch_template_versions = launch_template_versions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.launch_template_versions:
            self.launch_template_versions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.launch_template_versions is not None:
            result['LaunchTemplateVersions'] = self.launch_template_versions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaunchTemplateVersions') is not None:
            temp_model = main_models.DeleteLaunchTemplateVersionResponseBodyLaunchTemplateVersions()
            self.launch_template_versions = temp_model.from_map(m.get('LaunchTemplateVersions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteLaunchTemplateVersionResponseBodyLaunchTemplateVersions(DaraModel):
    def __init__(
        self,
        launch_template_version: List[main_models.DeleteLaunchTemplateVersionResponseBodyLaunchTemplateVersionsLaunchTemplateVersion] = None,
    ):
        self.launch_template_version = launch_template_version

    def validate(self):
        if self.launch_template_version:
            for v1 in self.launch_template_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LaunchTemplateVersion'] = []
        if self.launch_template_version is not None:
            for k1 in self.launch_template_version:
                result['LaunchTemplateVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.launch_template_version = []
        if m.get('LaunchTemplateVersion') is not None:
            for k1 in m.get('LaunchTemplateVersion'):
                temp_model = main_models.DeleteLaunchTemplateVersionResponseBodyLaunchTemplateVersionsLaunchTemplateVersion()
                self.launch_template_version.append(temp_model.from_map(k1))

        return self

class DeleteLaunchTemplateVersionResponseBodyLaunchTemplateVersionsLaunchTemplateVersion(DaraModel):
    def __init__(
        self,
        launch_template_id: str = None,
        launch_template_version_number: int = None,
    ):
        # The ID of the launch template.
        self.launch_template_id = launch_template_id
        # The version number of the launch template.
        self.launch_template_version_number = launch_template_version_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_version_number is not None:
            result['LaunchTemplateVersionNumber'] = self.launch_template_version_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateVersionNumber') is not None:
            self.launch_template_version_number = m.get('LaunchTemplateVersionNumber')

        return self

