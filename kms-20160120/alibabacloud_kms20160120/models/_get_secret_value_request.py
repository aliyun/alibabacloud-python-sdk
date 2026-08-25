# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSecretValueRequest(DaraModel):
    def __init__(
        self,
        dry_run: str = None,
        fetch_extended_config: bool = None,
        recipient: str = None,
        secret_name: str = None,
        version_id: str = None,
        version_stage: str = None,
    ):
        # Specifies whether to enable DryRun mode. Valid values:
        # 
        # - true: enables DryRun mode.
        # - false (default): disables DryRun mode.
        # 
        # DryRun mode is used to test API calls and verify whether you have the required permissions on the corresponding resources and whether the request parameters are correctly configured. When DryRun mode is enabled, KMS always returns a failure and provides the failure reason. Failure reasons include:
        # 
        # - DryRunOperationError: The request would succeed without the DryRun parameter.
        # - ValidationError: The parameters specified in the request are invalid.
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # Specifies whether to retrieve the extended configuration of the secret. Valid values:
        # 
        # - true: retrieves the extended configuration.
        # - false (default): does not retrieve the extended configuration.
        # 
        # > Generic secrets do not support extended configurations. This parameter is ignored if specified.
        self.fetch_extended_config = fetch_extended_config
        self.recipient = recipient
        # The secret name or secret Alibaba Cloud Resource Name (ARN).
        # >To access a secret in another Alibaba Cloud account, you must specify the secret ARN. The format of the secret ARN is `acs:kms:${region}:${account}:secret/${secret-name}`.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The version number.
        # 
        # > ApsaraDB RDS secrets, PolarDB secrets, Redis/Tair secrets, RAM secrets, and ECS secrets do not support specifying VersionId. This parameter is ignored if specified.
        self.version_id = version_id
        # The version stage. Default value: ACSCurrent.
        # 
        # If you specify this parameter, the secret value of the specified version stage is returned. If you do not specify this parameter, the secret value of the ACSCurrent version stage is returned.
        # > For ApsaraDB RDS secrets, PolarDB secrets, Redis/Tair secrets, RAM secrets, and ECS secrets, you can retrieve only the secret values of the ACSPrevious and ACSCurrent versions.
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.fetch_extended_config is not None:
            result['FetchExtendedConfig'] = self.fetch_extended_config

        if self.recipient is not None:
            result['Recipient'] = self.recipient

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FetchExtendedConfig') is not None:
            self.fetch_extended_config = m.get('FetchExtendedConfig')

        if m.get('Recipient') is not None:
            self.recipient = m.get('Recipient')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')

        return self

