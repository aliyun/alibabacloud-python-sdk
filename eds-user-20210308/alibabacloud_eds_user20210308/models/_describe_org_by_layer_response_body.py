# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeOrgByLayerResponseBody(DaraModel):
    def __init__(
        self,
        orgs: List[main_models.DescribeOrgByLayerResponseBodyOrgs] = None,
        request_id: str = None,
    ):
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
        result['Orgs'] = []
        if self.orgs is not None:
            for k1 in self.orgs:
                result['Orgs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.orgs = []
        if m.get('Orgs') is not None:
            for k1 in m.get('Orgs'):
                temp_model = main_models.DescribeOrgByLayerResponseBodyOrgs()
                self.orgs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOrgByLayerResponseBodyOrgs(DaraModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        parent_org_id: str = None,
    ):
        # The ID of the organization.
        self.org_id = org_id
        # The name of the organization.
        self.org_name = org_name
        # The ID of the parent organization.
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

        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')

        return self

