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
        # Specifies whether to enable the dry run mode. Valid values:
        # 
        # - true: Enables the dry run mode.
        # - false: Disables the dry run mode. This is the default value.
        # 
        # The dry run mode is used to test API calls, verify whether you have the required permissions on the resources, and check whether the request parameters are correctly configured. After the dry run mode is enabled, KMS always returns a failure and provides the cause of the failure. The causes include:
        # 
        # - DryRunOperationError: The request would succeed if the DryRun parameter is not configured.
        # - ValidationError: The specified parameters in the request are invalid.
        # - AccessDeniedError: You do not have the permissions to perform the operation on the KMS resource.
        self.dry_run = dry_run
        # Specifies whether to retrieve the extended configuration of the secret. Valid values:
        # 
        # - true: Retrieves the extended configuration.
        # - false: Does not retrieve the extended configuration. This is the default value.
        # 
        # > Generic secrets do not support extended configurations. If you specify this parameter for a generic secret, it is ignored.
        self.fetch_extended_config = fetch_extended_config
        # The remote attestation.
        self.recipient = recipient
        # The name or Alibaba Cloud Resource Name (ARN) of the secret.
        # > To access a secret that belongs to another Alibaba Cloud account, you must specify the ARN of the secret. The ARN of a secret is in the `acs:kms:${region}:${account}:secret/${secret-name}` format.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The version ID.
        # 
        # > ApsaraDB RDS secrets, PolarDB secrets, Redis/Tair secrets, RAM secrets, and ECS secrets do not support the VersionId parameter. If you specify this parameter, it is ignored.
        self.version_id = version_id
        # The version stage. Default value: ACSCurrent.
        # 
        # If you specify this parameter, the secret value of the specified version stage is returned. If you do not specify this parameter, the secret value of the ACSCurrent version stage is returned.
        # > For ApsaraDB RDS secrets, PolarDB secrets, Redis/Tair secrets, RAM secrets, and ECS secrets, you can only retrieve the secret values of the versions marked with ACSPrevious and ACSCurrent.
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

