# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeOrgsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        orgs: List[main_models.DescribeOrgsResponseBodyOrgs] = None,
        request_id: str = None,
    ):
        # The token that determines the start point of the query. The return value is the value of the NextToken response parameter that was returned last time the DescribeOrgs operation was called.
        self.next_token = next_token
        # The organizations.
        self.orgs = orgs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.orgs:
            for v1 in self.orgs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Orgs'] = []
        if self.orgs is not None:
            for k1 in self.orgs:
                result['Orgs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.orgs = []
        if m.get('Orgs') is not None:
            for k1 in m.get('Orgs'):
                temp_model = main_models.DescribeOrgsResponseBodyOrgs()
                self.orgs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOrgsResponseBodyOrgs(DaraModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        org_name_path: str = None,
        parent_org_id: str = None,
    ):
        # The organization ID.
        self.org_id = org_id
        # The name of the organizational unit.
        self.org_name = org_name
        self.org_name_path = org_name_path
        # The parent organization ID.
        self.parent_org_id = parent_org_id

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

        if self.org_name_path is not None:
            result['OrgNamePath'] = self.org_name_path

        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        if m.get('OrgNamePath') is not None:
            self.org_name_path = m.get('OrgNamePath')

        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')

        return self

