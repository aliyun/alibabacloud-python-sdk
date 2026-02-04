# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListDelegatedServicesForAccountResponseBody(DaraModel):
    def __init__(
        self,
        delegated_services: main_models.ListDelegatedServicesForAccountResponseBodyDelegatedServices = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about the trusted services.
        # 
        # > If the value of this parameter is empty, the member is not specified as a delegated administrator account.
        self.delegated_services = delegated_services
        self.max_results = max_results
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.delegated_services:
            self.delegated_services.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delegated_services is not None:
            result['DelegatedServices'] = self.delegated_services.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelegatedServices') is not None:
            temp_model = main_models.ListDelegatedServicesForAccountResponseBodyDelegatedServices()
            self.delegated_services = temp_model.from_map(m.get('DelegatedServices'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDelegatedServicesForAccountResponseBodyDelegatedServices(DaraModel):
    def __init__(
        self,
        delegated_service: List[main_models.ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService] = None,
    ):
        self.delegated_service = delegated_service

    def validate(self):
        if self.delegated_service:
            for v1 in self.delegated_service:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DelegatedService'] = []
        if self.delegated_service is not None:
            for k1 in self.delegated_service:
                result['DelegatedService'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delegated_service = []
        if m.get('DelegatedService') is not None:
            for k1 in m.get('DelegatedService'):
                temp_model = main_models.ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService()
                self.delegated_service.append(temp_model.from_map(k1))

        return self

class ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService(DaraModel):
    def __init__(
        self,
        delegation_enabled_time: str = None,
        service_principal: str = None,
        status: str = None,
    ):
        # The time when the member was specified as a delegated administrator account.
        self.delegation_enabled_time = delegation_enabled_time
        # The identifier of the trusted service.
        self.service_principal = service_principal
        # The status of the trusted service. Valid values:
        # 
        # *   ENABLED: enabled
        # *   DISABLED: disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delegation_enabled_time is not None:
            result['DelegationEnabledTime'] = self.delegation_enabled_time

        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelegationEnabledTime') is not None:
            self.delegation_enabled_time = m.get('DelegationEnabledTime')

        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

