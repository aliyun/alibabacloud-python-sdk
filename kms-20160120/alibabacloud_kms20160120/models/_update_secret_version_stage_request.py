# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSecretVersionStageRequest(DaraModel):
    def __init__(
        self,
        move_to_version: str = None,
        remove_from_version: str = None,
        secret_name: str = None,
        version_stage: str = None,
    ):
        # The version number of the secret. This parameter specifies that the version stage set by VersionStage is attached to this version.
        # 
        # > - You must specify at least one of RemoveFromVersion and MoveToVersion.
        # >
        # > - If you set VersionStage to ACSCurrent or ACSPrevious, you must specify this parameter.
        self.move_to_version = move_to_version
        # The version number of the secret. This parameter specifies that the version stage set by VersionStage is removed from this version.
        # 
        # > You must specify at least one of RemoveFromVersion and MoveToVersion.
        self.remove_from_version = remove_from_version
        # The name or Alibaba Cloud Resource Name (ARN) of the secret.
        # 
        # > To access a secret in a different Alibaba Cloud account, you must specify the ARN of the secret. The ARN is in the format of `acs:kms:${region}:${account}:secret/${secret-name}`.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The version stage of the secret.
        # 
        # **Scenario 1: Add a version stage to a specified secret version.**
        # 
        # Specify this parameter and MoveToVersion. Do not specify RemoveFromVersion. This parameter can be set to ACSCurrent, ACSPrevious, or a custom stage.
        # 
        # **Scenario 2: Remove a version stage from a specified secret version.**
        # 
        # Specify this parameter and RemoveFromVersion. Do not specify MoveToVersion. This parameter must be set to a custom stage.
        # 
        # > ACSCurrent and ACSPrevious are system-reserved stages. You cannot directly remove them. You can only remove them from one secret version and attach them to another.
        # 
        # **Scenario 3: Remove a version stage from a specified secret version and attach it to another secret version.**
        # 
        # Specify this parameter, MoveToVersion, and RemoveFromVersion. This parameter can be set to ACSCurrent, ACSPrevious, or a custom stage.
        # 
        # This parameter is required.
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.move_to_version is not None:
            result['MoveToVersion'] = self.move_to_version

        if self.remove_from_version is not None:
            result['RemoveFromVersion'] = self.remove_from_version

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoveToVersion') is not None:
            self.move_to_version = m.get('MoveToVersion')

        if m.get('RemoveFromVersion') is not None:
            self.remove_from_version = m.get('RemoveFromVersion')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')

        return self

