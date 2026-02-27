# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListTrustedServiceStatusResponseBody(DaraModel):
    def __init__(
        self,
        enabled_service_principals: main_models.ListTrustedServiceStatusResponseBodyEnabledServicePrincipals = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.enabled_service_principals = enabled_service_principals
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.enabled_service_principals:
            self.enabled_service_principals.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled_service_principals is not None:
            result['EnabledServicePrincipals'] = self.enabled_service_principals.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnabledServicePrincipals') is not None:
            temp_model = main_models.ListTrustedServiceStatusResponseBodyEnabledServicePrincipals()
            self.enabled_service_principals = temp_model.from_map(m.get('EnabledServicePrincipals'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTrustedServiceStatusResponseBodyEnabledServicePrincipals(DaraModel):
    def __init__(
        self,
        enabled_service_principal: List[main_models.ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal] = None,
    ):
        self.enabled_service_principal = enabled_service_principal

    def validate(self):
        if self.enabled_service_principal:
            for v1 in self.enabled_service_principal:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnabledServicePrincipal'] = []
        if self.enabled_service_principal is not None:
            for k1 in self.enabled_service_principal:
                result['EnabledServicePrincipal'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.enabled_service_principal = []
        if m.get('EnabledServicePrincipal') is not None:
            for k1 in m.get('EnabledServicePrincipal'):
                temp_model = main_models.ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal()
                self.enabled_service_principal.append(temp_model.from_map(k1))

        return self

class ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal(DaraModel):
    def __init__(
        self,
        enable_time: str = None,
        service_principal: str = None,
    ):
        self.enable_time = enable_time
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time

        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')

        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')

        return self

