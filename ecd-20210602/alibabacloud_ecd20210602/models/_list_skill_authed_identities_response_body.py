# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20210602 import models as main_models
from darabonba.model import DaraModel

class ListSkillAuthedIdentitiesResponseBody(DaraModel):
    def __init__(
        self,
        identities: List[main_models.ListSkillAuthedIdentitiesResponseBodyIdentities] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of authorized objects.
        self.identities = identities
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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
        result['Identities'] = []
        if self.identities is not None:
            for k1 in self.identities:
                result['Identities'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.identities = []
        if m.get('Identities') is not None:
            for k1 in m.get('Identities'):
                temp_model = main_models.ListSkillAuthedIdentitiesResponseBodyIdentities()
                self.identities.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSkillAuthedIdentitiesResponseBodyIdentities(DaraModel):
    def __init__(
        self,
        auto_install: bool = None,
        identity_id: str = None,
    ):
        # Indicates whether automatic installation is enabled. Valid values:
        # 
        # - true: Automatic installation is enabled.
        # - false: Automatic installation is disabled.
        self.auto_install = auto_install
        # The ID of the authorized object.
        self.identity_id = identity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')

        return self

