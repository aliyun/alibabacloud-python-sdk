# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20210602 import models as main_models
from darabonba.model import DaraModel

class SetIdentitySkillAuthRequest(DaraModel):
    def __init__(
        self,
        auto_install: bool = None,
        identities: List[main_models.SetIdentitySkillAuthRequestIdentities] = None,
        operation_type: str = None,
        skill_channel: str = None,
        skill_ids: List[str] = None,
    ):
        # Specifies whether to automatically install. Valid values:
        # 
        # - true: yes
        # - false: no
        # 
        # This parameter is required.
        self.auto_install = auto_install
        # The list of authorized objects.
        # 
        # This parameter is required.
        self.identities = identities
        # The operation type.
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # The skill channel. Valid values:
        # 
        # - ENTERPRISE: enterprise edition
        # - BUSINESS: business edition
        # 
        # This parameter is required.
        self.skill_channel = skill_channel
        # The list of skill IDs.
        # 
        # This parameter is required.
        self.skill_ids = skill_ids

    def validate(self):
        if self.identities:
            for v1 in self.identities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        result['Identities'] = []
        if self.identities is not None:
            for k1 in self.identities:
                result['Identities'].append(k1.to_map() if k1 else None)

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.skill_channel is not None:
            result['SkillChannel'] = self.skill_channel

        if self.skill_ids is not None:
            result['SkillIds'] = self.skill_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        self.identities = []
        if m.get('Identities') is not None:
            for k1 in m.get('Identities'):
                temp_model = main_models.SetIdentitySkillAuthRequestIdentities()
                self.identities.append(temp_model.from_map(k1))

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('SkillChannel') is not None:
            self.skill_channel = m.get('SkillChannel')

        if m.get('SkillIds') is not None:
            self.skill_ids = m.get('SkillIds')

        return self

class SetIdentitySkillAuthRequestIdentities(DaraModel):
    def __init__(
        self,
        identity_id: str = None,
        region_id: str = None,
    ):
        # The ID of the authorized object.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

