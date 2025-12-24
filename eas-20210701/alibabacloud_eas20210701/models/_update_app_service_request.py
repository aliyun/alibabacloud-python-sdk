# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateAppServiceRequest(DaraModel):
    def __init__(
        self,
        quota_id: str = None,
        workspace_id: str = None,
        app_type: str = None,
        app_version: str = None,
        config: Dict[str, Any] = None,
        replicas: int = None,
        service_spec: str = None,
    ):
        # The quota ID.
        self.quota_id = quota_id
        # The workspace ID.
        self.workspace_id = workspace_id
        # The application type.
        # 
        # Valid values:
        # 
        # *   LLM: the large language model (LLM) application
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.app_type = app_type
        # The application version.
        self.app_version = app_version
        # The additional configurations that are required for service deployment.
        self.config = config
        # The number of instances. This value must be greater than 0.
        self.replicas = replicas
        # The service specifications. Valid values:
        # 
        # *   llama_7b_fp16
        # *   llama_7b_int8
        # *   llama_13b_fp16
        # *   llama_7b_int8
        # *   chatglm_6b_fp16
        # *   chatglm_6b_int8
        # *   chatglm2_6b_fp16
        # *   baichuan_7b_int8
        # *   baichuan_13b_fp16
        # *   baichuan_7b_fp16
        self.service_spec = service_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')

        return self

