# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class SecurityContext(DaraModel):
    def __init__(
        self,
        capabilities: main_models.SecurityContextCapabilities = None,
        privileged: bool = None,
        run_as_group: int = None,
        run_as_user: int = None,
        seccomp_profile: main_models.SeccompProfile = None,
    ):
        self.capabilities = capabilities
        self.privileged = privileged
        self.run_as_group = run_as_group
        self.run_as_user = run_as_user
        self.seccomp_profile = seccomp_profile

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()
        if self.seccomp_profile:
            self.seccomp_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities.to_map()

        if self.privileged is not None:
            result['Privileged'] = self.privileged

        if self.run_as_group is not None:
            result['RunAsGroup'] = self.run_as_group

        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user

        if self.seccomp_profile is not None:
            result['SeccompProfile'] = self.seccomp_profile.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capabilities') is not None:
            temp_model = main_models.SecurityContextCapabilities()
            self.capabilities = temp_model.from_map(m.get('Capabilities'))

        if m.get('Privileged') is not None:
            self.privileged = m.get('Privileged')

        if m.get('RunAsGroup') is not None:
            self.run_as_group = m.get('RunAsGroup')

        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')

        if m.get('SeccompProfile') is not None:
            temp_model = main_models.SeccompProfile()
            self.seccomp_profile = temp_model.from_map(m.get('SeccompProfile'))

        return self

