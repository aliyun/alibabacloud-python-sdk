# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20210602 import models as main_models
from darabonba.model import DaraModel

class SetIdentitySkillSecurityRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        identity_ids: List[main_models.SetIdentitySkillSecurityRequestIdentityIds] = None,
        skill_channel: str = None,
    ):
        # Specifies whether to enable the skill installation permission. Valid values:
        # 
        # - true: enabled.
        # - false: disabled.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The list of resource information.
        # 
        # This parameter is required.
        self.identity_ids = identity_ids
        # The skill channel. Valid values:
        # 
        # - ENTERPRISE: enterprise edition.
        # - BUSINESS: business edition.
        # 
        # This parameter is required.
        self.skill_channel = skill_channel

    def validate(self):
        if self.identity_ids:
            for v1 in self.identity_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['IdentityIds'] = []
        if self.identity_ids is not None:
            for k1 in self.identity_ids:
                result['IdentityIds'].append(k1.to_map() if k1 else None)

        if self.skill_channel is not None:
            result['SkillChannel'] = self.skill_channel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.identity_ids = []
        if m.get('IdentityIds') is not None:
            for k1 in m.get('IdentityIds'):
                temp_model = main_models.SetIdentitySkillSecurityRequestIdentityIds()
                self.identity_ids.append(temp_model.from_map(k1))

        if m.get('SkillChannel') is not None:
            self.skill_channel = m.get('SkillChannel')

        return self

class SetIdentitySkillSecurityRequestIdentityIds(DaraModel):
    def __init__(
        self,
        identity_id: str = None,
        region_id: str = None,
    ):
        # The resource information ID.
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

