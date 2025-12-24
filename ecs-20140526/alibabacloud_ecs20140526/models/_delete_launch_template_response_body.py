# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DeleteLaunchTemplateResponseBody(DaraModel):
    def __init__(
        self,
        launch_template_id: str = None,
        launch_template_version_numbers: main_models.DeleteLaunchTemplateResponseBodyLaunchTemplateVersionNumbers = None,
        request_id: str = None,
    ):
        # The ID of the launch template. For more information, see [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html).
        # 
        # You must specify `LaunchTemplateId` or `LaunchTemplateName` to specify a launch template.
        self.launch_template_id = launch_template_id
        # The versions of the deleted launch template.
        self.launch_template_version_numbers = launch_template_version_numbers
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.launch_template_version_numbers:
            self.launch_template_version_numbers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_version_numbers is not None:
            result['LaunchTemplateVersionNumbers'] = self.launch_template_version_numbers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateVersionNumbers') is not None:
            temp_model = main_models.DeleteLaunchTemplateResponseBodyLaunchTemplateVersionNumbers()
            self.launch_template_version_numbers = temp_model.from_map(m.get('LaunchTemplateVersionNumbers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteLaunchTemplateResponseBodyLaunchTemplateVersionNumbers(DaraModel):
    def __init__(
        self,
        version_numbers: List[int] = None,
    ):
        self.version_numbers = version_numbers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version_numbers is not None:
            result['versionNumbers'] = self.version_numbers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionNumbers') is not None:
            self.version_numbers = m.get('versionNumbers')

        return self

