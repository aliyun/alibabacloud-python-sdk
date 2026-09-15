# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class InnerCreateSandboxInput(DaraModel):
    def __init__(
        self,
        allow_internet_access: bool = None,
        auto_pause: bool = None,
        auto_resume: bool = None,
        env_vars: Dict[str, str] = None,
        metadata: Dict[str, str] = None,
        network: main_models.E2BNetwork = None,
        runtime: main_models.InnerSandboxRuntimeConfig = None,
        secure: bool = None,
        team_id: str = None,
        template_id: str = None,
        timeout: int = None,
        volume_mounts: main_models.InnerCreateSandboxVolumeMounts = None,
    ):
        self.allow_internet_access = allow_internet_access
        self.auto_pause = auto_pause
        self.auto_resume = auto_resume
        self.env_vars = env_vars
        self.metadata = metadata
        self.network = network
        self.runtime = runtime
        self.secure = secure
        self.team_id = team_id
        self.template_id = template_id
        self.timeout = timeout
        self.volume_mounts = volume_mounts

    def validate(self):
        if self.network:
            self.network.validate()
        if self.runtime:
            self.runtime.validate()
        if self.volume_mounts:
            self.volume_mounts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_internet_access is not None:
            result['allowInternetAccess'] = self.allow_internet_access

        if self.auto_pause is not None:
            result['autoPause'] = self.auto_pause

        if self.auto_resume is not None:
            result['autoResume'] = self.auto_resume

        if self.env_vars is not None:
            result['envVars'] = self.env_vars

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.network is not None:
            result['network'] = self.network.to_map()

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        if self.secure is not None:
            result['secure'] = self.secure

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.volume_mounts is not None:
            result['volumeMounts'] = self.volume_mounts.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowInternetAccess') is not None:
            self.allow_internet_access = m.get('allowInternetAccess')

        if m.get('autoPause') is not None:
            self.auto_pause = m.get('autoPause')

        if m.get('autoResume') is not None:
            self.auto_resume = m.get('autoResume')

        if m.get('envVars') is not None:
            self.env_vars = m.get('envVars')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('network') is not None:
            temp_model = main_models.E2BNetwork()
            self.network = temp_model.from_map(m.get('network'))

        if m.get('runtime') is not None:
            temp_model = main_models.InnerSandboxRuntimeConfig()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('secure') is not None:
            self.secure = m.get('secure')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('volumeMounts') is not None:
            temp_model = main_models.InnerCreateSandboxVolumeMounts()
            self.volume_mounts = temp_model.from_map(m.get('volumeMounts'))

        return self

