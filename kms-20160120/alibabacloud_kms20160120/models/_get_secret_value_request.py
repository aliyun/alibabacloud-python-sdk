# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSecretValueRequest(DaraModel):
    def __init__(
        self,
        dry_run: str = None,
        fetch_extended_config: bool = None,
        secret_name: str = None,
        version_id: str = None,
        version_stage: str = None,
    ):
        # Indicates whether to enable DryRun mode.
        # 
        # - true: Enabled  
        # - false (Default Value): Disabled  
        # 
        # DryRun mode is used for Testing API Calls to authenticate whether you have the required permissions on the specified resource and whether the Request Parameters are correctly configured. When DryRun mode is enabled, KMS always returns a failed response along with the failure reason. Possible failure reasons include:
        # 
        # - DryRunOperationError: The request would succeed if the DryRun parameter were not specified.  
        # - ValidationError: One or more parameters in the request are invalid.  
        # - AccessDeniedError: You do not have permission to execute this operation on the KMS resource.
        self.dry_run = dry_run
        # Indicates whether to retrieve the extended configuration of the credential. Valid values:
        # 
        # - true: Retrieve  
        # - false (Default Value): Do not retrieve  
        # 
        # > Generic secrets do not support extended configuration. If you specify this parameter, it will be ignored.
        self.fetch_extended_config = fetch_extended_config
        # The name or ARN of the credential.  
        # > When accessing a credential under another Alibaba Cloud account, you must specify the credential ARN. The ARN format is `acs:kms:${region}:${account}:secret/${secret-name}`.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # Version number.
        # 
        # > The VersionId parameter is not supported for RDS credentials, PolarDB credentials, Redis/Tair credentials, RAM credentials, and ECS credentials. If you specify this parameter, it will be ignored.
        self.version_id = version_id
        # The version stage. Default value: ACSCurrent.  
        # 
        # If you specify this parameter, the credential value of the specified version stage is returned. If you do not specify this parameter, the credential value of the ACSCurrent version stage is returned.  
        # > For RDS credentials, PolarDB credentials, Redis/Tair credentials, RAM credentials, and ECS credentials, you can retrieve only the credential values corresponding to the ACSPrevious or ACSCurrent version stages.
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

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')

        return self

