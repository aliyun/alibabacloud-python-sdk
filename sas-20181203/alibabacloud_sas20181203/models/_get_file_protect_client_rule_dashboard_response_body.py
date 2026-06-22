# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetFileProtectClientRuleDashboardResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileProtectClientRuleDashboardResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned when the API call is successful.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFileProtectClientRuleDashboardResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileProtectClientRuleDashboardResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_total: str = None,
        bind_count: int = None,
        protected_directories_count: int = None,
        protected_instances_count: int = None,
    ):
        # The total number of web tamper-proofing licenses.
        self.auth_total = auth_total
        # The number of bound tamper-proofing licenses.
        self.bind_count = bind_count
        # The total number of web tamper-proofing rules.
        self.protected_directories_count = protected_directories_count
        # The total number of online web tamper-proofing clients.
        self.protected_instances_count = protected_instances_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_total is not None:
            result['AuthTotal'] = self.auth_total

        if self.bind_count is not None:
            result['BindCount'] = self.bind_count

        if self.protected_directories_count is not None:
            result['ProtectedDirectoriesCount'] = self.protected_directories_count

        if self.protected_instances_count is not None:
            result['ProtectedInstancesCount'] = self.protected_instances_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTotal') is not None:
            self.auth_total = m.get('AuthTotal')

        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')

        if m.get('ProtectedDirectoriesCount') is not None:
            self.protected_directories_count = m.get('ProtectedDirectoriesCount')

        if m.get('ProtectedInstancesCount') is not None:
            self.protected_instances_count = m.get('ProtectedInstancesCount')

        return self

