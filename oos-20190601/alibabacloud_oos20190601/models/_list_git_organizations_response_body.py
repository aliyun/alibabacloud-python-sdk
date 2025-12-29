# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListGitOrganizationsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        git_orgs: List[main_models.ListGitOrganizationsResponseBodyGitOrgs] = None,
        request_id: str = None,
    ):
        self.count = count
        self.git_orgs = git_orgs
        self.request_id = request_id

    def validate(self):
        if self.git_orgs:
            for v1 in self.git_orgs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['GitOrgs'] = []
        if self.git_orgs is not None:
            for k1 in self.git_orgs:
                result['GitOrgs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.git_orgs = []
        if m.get('GitOrgs') is not None:
            for k1 in m.get('GitOrgs'):
                temp_model = main_models.ListGitOrganizationsResponseBodyGitOrgs()
                self.git_orgs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGitOrganizationsResponseBodyGitOrgs(DaraModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
    ):
        self.org_id = org_id
        self.org_name = org_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.org_name is not None:
            result['OrgName'] = self.org_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        return self

