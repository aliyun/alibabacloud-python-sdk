# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateRoutineCodeDeploymentResponseBody(DaraModel):
    def __init__(
        self,
        code_versions: List[main_models.CreateRoutineCodeDeploymentResponseBodyCodeVersions] = None,
        deployment_id: str = None,
        request_id: str = None,
        strategy: str = None,
    ):
        # The configuration list of the phased release version number.
        self.code_versions = code_versions
        # The deployment record ID.
        self.deployment_id = deployment_id
        # The request ID.
        self.request_id = request_id
        # The phased release policy. The constant string is "percentage".
        self.strategy = strategy

    def validate(self):
        if self.code_versions:
            for v1 in self.code_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CodeVersions'] = []
        if self.code_versions is not None:
            for k1 in self.code_versions:
                result['CodeVersions'].append(k1.to_map() if k1 else None)

        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_versions = []
        if m.get('CodeVersions') is not None:
            for k1 in m.get('CodeVersions'):
                temp_model = main_models.CreateRoutineCodeDeploymentResponseBodyCodeVersions()
                self.code_versions.append(temp_model.from_map(k1))

        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class CreateRoutineCodeDeploymentResponseBodyCodeVersions(DaraModel):
    def __init__(
        self,
        code_version: str = None,
        percentage: int = None,
    ):
        # The version of the code.
        self.code_version = code_version
        # The phased release ratio.
        self.percentage = percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        return self

