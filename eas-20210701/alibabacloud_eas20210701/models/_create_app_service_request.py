# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateAppServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        quota_id: str = None,
        workspace_id: str = None,
        app_type: str = None,
        app_version: str = None,
        config: Dict[str, Any] = None,
        replicas: int = None,
        service_name: str = None,
        service_spec: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. Valid values:
        # - true: performs a dry run and does not create the instance. The system checks whether the required parameters are specified, the request format is valid, the service limits are met, and the ECS inventory is sufficient. If the request fails the check, an error is returned. If the request passes the check, the DryRunOperation error code is returned.
        # - false (default): performs a normal request and creates the instance if the request passes the check.
        self.dry_run = dry_run
        # The quota ID.
        self.quota_id = quota_id
        # The workspace ID.
        self.workspace_id = workspace_id
        # The type of the application service.
        # 
        # This parameter is required.
        self.app_type = app_type
        # The application version.
        self.app_version = app_version
        # The additional configuration information required for deployment.
        self.config = config
        # The number of instances.
        # 
        # This parameter is required.
        self.replicas = replicas
        # The name of the service.
        # 
        # This parameter is required.
        self.service_name = service_name
        # The service specifications. Valid values:
        # - llama_7b_fp16
        # - llama_7b_int8
        # - llama_13b_fp16
        # - llama_7b_int8
        # - chatglm_6b_fp16
        # - chatglm_6b_int8
        # - chatglm2_6b_fp16
        # - baichuan_7b_int8
        # - baichuan_13b_fp16
        # - baichuan_7b_fp16
        # 
        # This parameter is required.
        self.service_spec = service_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.config is not None:
            result['Config'] = self.config

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')

        return self

