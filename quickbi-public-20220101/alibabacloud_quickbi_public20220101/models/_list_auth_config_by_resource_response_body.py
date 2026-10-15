# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListAuthConfigByResourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListAuthConfigByResourceResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The collection of authorization details.
        self.result = result
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListAuthConfigByResourceResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAuthConfigByResourceResponseBodyResult(DaraModel):
    def __init__(
        self,
        authorities: List[str] = None,
        authorized_id: str = None,
        authorized_name: str = None,
        expire_date: str = None,
        gmt_create: str = None,
        resource_id: str = None,
        resource_type: str = None,
        scope: int = None,
    ):
        # The array of permissions granted.
        self.authorities = authorities
        # The ID of the authorized user.
        self.authorized_id = authorized_id
        # The name of the authorized user.
        self.authorized_name = authorized_name
        # The expiration time. This value is a UNIX timestamp in milliseconds.
        self.expire_date = expire_date
        # The time when the permission record was created, in the yyyy-MM-dd mm:hh:ss format.
        self.gmt_create = gmt_create
        # The resource ID.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - dashboard: dashboard
        # - screen: data screen
        # - report: electron
        # - ANALYSIS: ad hoc analysis
        # - dashboardOfflineQuery: self-service data retrieval
        # - dataForm: data form
        # - cube: dataset
        # - datasource: data source
        self.resource_type = resource_type
        # The authorization scope. Valid values:
        # 
        # - 0: user
        # - 1: user group
        # - 2: organization
        # - 3: workspace
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorities is not None:
            result['Authorities'] = self.authorities

        if self.authorized_id is not None:
            result['AuthorizedId'] = self.authorized_id

        if self.authorized_name is not None:
            result['AuthorizedName'] = self.authorized_name

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorities') is not None:
            self.authorities = m.get('Authorities')

        if m.get('AuthorizedId') is not None:
            self.authorized_id = m.get('AuthorizedId')

        if m.get('AuthorizedName') is not None:
            self.authorized_name = m.get('AuthorizedName')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

