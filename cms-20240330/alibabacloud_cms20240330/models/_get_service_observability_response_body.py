# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetServiceObservabilityResponseBody(DaraModel):
    def __init__(
        self,
        entry_point_info: main_models.GetServiceObservabilityResponseBodyEntryPointInfo = None,
        fee_type: str = None,
        quotas: Dict[str, str] = None,
        region_id: str = None,
        request_id: str = None,
        settings: Dict[str, str] = None,
        status: str = None,
        type: str = None,
        workspace: str = None,
    ):
        # Endpoint and Authentication Information
        self.entry_point_info = entry_point_info
        # Billing Type
        self.fee_type = fee_type
        # Quota Configuration
        self.quotas = quotas
        # Region
        self.region_id = region_id
        # Request ID
        self.request_id = request_id
        # System Configuration
        self.settings = settings
        # Resource Initialization Status
        self.status = status
        # Application Observability Type
        self.type = type
        # Workspace Name
        self.workspace = workspace

    def validate(self):
        if self.entry_point_info:
            self.entry_point_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry_point_info is not None:
            result['entryPointInfo'] = self.entry_point_info.to_map()

        if self.fee_type is not None:
            result['feeType'] = self.fee_type

        if self.quotas is not None:
            result['quotas'] = self.quotas

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.settings is not None:
            result['settings'] = self.settings

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entryPointInfo') is not None:
            temp_model = main_models.GetServiceObservabilityResponseBodyEntryPointInfo()
            self.entry_point_info = temp_model.from_map(m.get('entryPointInfo'))

        if m.get('feeType') is not None:
            self.fee_type = m.get('feeType')

        if m.get('quotas') is not None:
            self.quotas = m.get('quotas')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('settings') is not None:
            self.settings = m.get('settings')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetServiceObservabilityResponseBodyEntryPointInfo(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        private_domain: str = None,
        project: str = None,
        public_domain: str = None,
    ):
        # Authentication Token for Data Reporting
        self.auth_token = auth_token
        # Private Network Access Address
        self.private_domain = private_domain
        # SLS Project
        self.project = project
        # Public Network Access Address
        self.public_domain = public_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.private_domain is not None:
            result['privateDomain'] = self.private_domain

        if self.project is not None:
            result['project'] = self.project

        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('privateDomain') is not None:
            self.private_domain = m.get('privateDomain')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')

        return self

