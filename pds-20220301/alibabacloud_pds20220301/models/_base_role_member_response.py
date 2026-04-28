# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseRoleMemberResponse(DaraModel):
    def __init__(
        self,
        assignment_list: List[main_models.BaseAssignmentResponse] = None,
        created_at: str = None,
        creator: str = None,
        domain_id: str = None,
        identity: main_models.Identity = None,
        identity_name: str = None,
        is_admin: bool = None,
        subdomain_id: str = None,
    ):
        self.assignment_list = assignment_list
        self.created_at = created_at
        self.creator = creator
        self.domain_id = domain_id
        self.identity = identity
        self.identity_name = identity_name
        self.is_admin = is_admin
        self.subdomain_id = subdomain_id

    def validate(self):
        if self.assignment_list:
            for v1 in self.assignment_list:
                 if v1:
                    v1.validate()
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['assignment_list'] = []
        if self.assignment_list is not None:
            for k1 in self.assignment_list:
                result['assignment_list'].append(k1.to_map() if k1 else None)

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.identity is not None:
            result['identity'] = self.identity.to_map()

        if self.identity_name is not None:
            result['identity_name'] = self.identity_name

        if self.is_admin is not None:
            result['is_admin'] = self.is_admin

        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assignment_list = []
        if m.get('assignment_list') is not None:
            for k1 in m.get('assignment_list'):
                temp_model = main_models.BaseAssignmentResponse()
                self.assignment_list.append(temp_model.from_map(k1))

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('identity') is not None:
            temp_model = main_models.Identity()
            self.identity = temp_model.from_map(m.get('identity'))

        if m.get('identity_name') is not None:
            self.identity_name = m.get('identity_name')

        if m.get('is_admin') is not None:
            self.is_admin = m.get('is_admin')

        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')

        return self

