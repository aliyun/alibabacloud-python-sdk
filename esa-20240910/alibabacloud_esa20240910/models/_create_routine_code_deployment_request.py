# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateRoutineCodeDeploymentRequest(DaraModel):
    def __init__(
        self,
        code_versions: List[main_models.CreateRoutineCodeDeploymentRequestCodeVersions] = None,
        env: str = None,
        name: str = None,
        strategy: str = None,
    ):
        # The configuration list of phased release version numbers. A maximum of two versions are supported, and the sum of the total proportions is equal to 100.
        # 
        # This parameter is required.
        self.code_versions = code_versions
        # The name of the environment. Only supports test environment `staging` or production environment `production`.
        # 
        # This parameter is required.
        self.env = env
        # The function name.
        # 
        # This parameter is required.
        self.name = name
        # The deployment policy. Valid value: percentage.
        # 
        # This parameter is required.
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

        if self.env is not None:
            result['Env'] = self.env

        if self.name is not None:
            result['Name'] = self.name

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_versions = []
        if m.get('CodeVersions') is not None:
            for k1 in m.get('CodeVersions'):
                temp_model = main_models.CreateRoutineCodeDeploymentRequestCodeVersions()
                self.code_versions.append(temp_model.from_map(k1))

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class CreateRoutineCodeDeploymentRequestCodeVersions(DaraModel):
    def __init__(
        self,
        code_version: str = None,
        percentage: int = None,
    ):
        # The version of the code.
        # 
        # This parameter is required.
        self.code_version = code_version
        # The phased release ratio of the code version. Valid values: 1 to 100.
        # 
        # This parameter is required.
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

