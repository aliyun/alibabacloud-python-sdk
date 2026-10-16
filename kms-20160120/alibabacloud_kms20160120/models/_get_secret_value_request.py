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
        # - true: Enables DryRun mode.
        # - false (default): Disables DryRun mode.
        # 
        # DryRun mode is used to test API calls, verify whether you have the required permissions on the specified resources, and check whether the request parameters are configured correctly. When DryRun mode is enabled, KMS always returns a failure with the reason for the failure. Possible failure reasons include:
        # 
        # - DryRunOperationError: The request would succeed if the DryRun parameter were not configured.
        # - ValidationError: A parameter specified in the request is invalid.
        # - AccessDeniedError: You do not have permission to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # Specifies whether to retrieve the extended configuration of the secret. Valid values:
        # 
        # - true: Retrieves the extended configuration.
        # - false (default): Does not retrieve the extended configuration.
        # 
        # > Generic secrets do not support extended configuration. If you set this parameter, it is ignored.
        self.fetch_extended_config = fetch_extended_config
        self.recipient = recipient
        # The secret name or secret Alibaba Cloud Resource Name (ARN).
        # >When accessing a secret in another Alibaba Cloud account, you must enter the secret ARN. The format of the secret ARN is `acs:kms:${region}:${account}:secret/${secret-name}`.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The version number.
        # 
        # > Specifying VersionId is not supported for ApsaraDB RDS secrets, PolarDB secrets, Redis/Tair secrets, dynamic RAM secrets, or dynamic ECS secrets. If you set this parameter, it is ignored.
        self.version_id = version_id
        # The version status. Default value: ACSCurrent.
        # 
        # If you specify this parameter, the secret value of the specified version status is returned. If you do not specify this parameter, the secret value of the ACSCurrent version status is returned.
        # > For ApsaraDB RDS secrets, PolarDB secrets, Redis/Tair secrets, dynamic RAM secrets, and dynamic ECS secrets, only the secret values corresponding to ACSPrevious and ACSCurrent can be retrieved.
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

