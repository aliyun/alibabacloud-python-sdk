# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AgentAccessConfig(DaraModel):
    def __init__(
        self,
        ai_request_log_enabled: bool = None,
        authorization: main_models.AgentAccessConfigAuthorization = None,
        base_path: str = None,
        domain_ids: List[str] = None,
        remove_base_path_on_forward: bool = None,
    ):
        # Specifies whether to enable AI request logging. Default value if omitted: true.
        self.ai_request_log_enabled = ai_request_log_enabled
        # The consumer authorization configuration for Agent access. If omitted, consumer authorization is not enabled.
        self.authorization = authorization
        # The base path of the Agent access entry. The path must start with a forward slash (/).
        # 
        # This parameter is required.
        self.base_path = base_path
        # The list of domain name IDs bound to the Agent access entry. At least one domain name must be specified.
        # 
        # This parameter is required.
        self.domain_ids = domain_ids
        # Specifies whether to remove the base path when forwarding requests to the backend. Default value if omitted: false.
        self.remove_base_path_on_forward = remove_base_path_on_forward

    def validate(self):
        if self.authorization:
            self.authorization.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_request_log_enabled is not None:
            result['aiRequestLogEnabled'] = self.ai_request_log_enabled

        if self.authorization is not None:
            result['authorization'] = self.authorization.to_map()

        if self.base_path is not None:
            result['basePath'] = self.base_path

        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids

        if self.remove_base_path_on_forward is not None:
            result['removeBasePathOnForward'] = self.remove_base_path_on_forward

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiRequestLogEnabled') is not None:
            self.ai_request_log_enabled = m.get('aiRequestLogEnabled')

        if m.get('authorization') is not None:
            temp_model = main_models.AgentAccessConfigAuthorization()
            self.authorization = temp_model.from_map(m.get('authorization'))

        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')

        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')

        if m.get('removeBasePathOnForward') is not None:
            self.remove_base_path_on_forward = m.get('removeBasePathOnForward')

        return self



class AgentAccessConfigAuthorization(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        enabled: bool = None,
        principals: List[main_models.AgentAuthorizationPrincipal] = None,
    ):
        # The authentication type of the Agent access entry. Specify this parameter only when enabled is set to true.
        self.auth_type = auth_type
        # Specifies whether to enable consumer authorization. If set to true, authType must be specified and at least one principal must be provided. If set to false, no principals can be specified.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The list of consumers or consumer groups that are granted Agent access permissions. At least one principal must be specified when enabled is set to true.
        self.principals = principals

    def validate(self):
        if self.principals:
            for v1 in self.principals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['principals'] = []
        if self.principals is not None:
            for k1 in self.principals:
                result['principals'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.principals = []
        if m.get('principals') is not None:
            for k1 in m.get('principals'):
                temp_model = main_models.AgentAuthorizationPrincipal()
                self.principals.append(temp_model.from_map(k1))

        return self

