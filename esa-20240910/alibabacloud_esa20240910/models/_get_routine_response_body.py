# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetRoutineResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_related_record: str = None,
        description: str = None,
        envs: List[main_models.GetRoutineResponseBodyEnvs] = None,
        has_assets: bool = None,
        request_id: str = None,
    ):
        # The time when the routine was created.
        self.create_time = create_time
        # The default record name to access.
        self.default_related_record = default_related_record
        # The description of the routine.
        self.description = description
        # The information about the environments.
        self.envs = envs
        self.has_assets = has_assets
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.envs:
            for v1 in self.envs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_related_record is not None:
            result['DefaultRelatedRecord'] = self.default_related_record

        if self.description is not None:
            result['Description'] = self.description

        result['Envs'] = []
        if self.envs is not None:
            for k1 in self.envs:
                result['Envs'].append(k1.to_map() if k1 else None)

        if self.has_assets is not None:
            result['HasAssets'] = self.has_assets

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultRelatedRecord') is not None:
            self.default_related_record = m.get('DefaultRelatedRecord')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.envs = []
        if m.get('Envs') is not None:
            for k1 in m.get('Envs'):
                temp_model = main_models.GetRoutineResponseBodyEnvs()
                self.envs.append(temp_model.from_map(k1))

        if m.get('HasAssets') is not None:
            self.has_assets = m.get('HasAssets')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRoutineResponseBodyEnvs(DaraModel):
    def __init__(
        self,
        code_deploy: main_models.GetRoutineResponseBodyEnvsCodeDeploy = None,
        env: str = None,
    ):
        self.code_deploy = code_deploy
        # The environment type.
        self.env = env

    def validate(self):
        if self.code_deploy:
            self.code_deploy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_deploy is not None:
            result['CodeDeploy'] = self.code_deploy.to_map()

        if self.env is not None:
            result['Env'] = self.env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDeploy') is not None:
            temp_model = main_models.GetRoutineResponseBodyEnvsCodeDeploy()
            self.code_deploy = temp_model.from_map(m.get('CodeDeploy'))

        if m.get('Env') is not None:
            self.env = m.get('Env')

        return self

class GetRoutineResponseBodyEnvsCodeDeploy(DaraModel):
    def __init__(
        self,
        code_versions: List[main_models.GetRoutineResponseBodyEnvsCodeDeployCodeVersions] = None,
        creation_time: str = None,
        deploy_id: str = None,
        strategy: str = None,
    ):
        self.code_versions = code_versions
        self.creation_time = creation_time
        self.deploy_id = deploy_id
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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_versions = []
        if m.get('CodeVersions') is not None:
            for k1 in m.get('CodeVersions'):
                temp_model = main_models.GetRoutineResponseBodyEnvsCodeDeployCodeVersions()
                self.code_versions.append(temp_model.from_map(k1))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class GetRoutineResponseBodyEnvsCodeDeployCodeVersions(DaraModel):
    def __init__(
        self,
        code_version: str = None,
        create_time: str = None,
        description: str = None,
        percentage: int = None,
    ):
        self.code_version = code_version
        self.create_time = create_time
        self.description = description
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        return self

