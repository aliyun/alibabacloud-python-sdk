# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListExternalApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        external_applications: main_models.ListExternalApplicationsResponseBodyExternalApplications = None,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
    ):
        self.external_applications = external_applications
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when `IsTruncated` is `true`.
        self.marker = marker
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.external_applications:
            self.external_applications.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_applications is not None:
            result['ExternalApplications'] = self.external_applications.to_map()

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalApplications') is not None:
            temp_model = main_models.ListExternalApplicationsResponseBodyExternalApplications()
            self.external_applications = temp_model.from_map(m.get('ExternalApplications'))

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListExternalApplicationsResponseBodyExternalApplications(DaraModel):
    def __init__(
        self,
        external_application: List[main_models.ListExternalApplicationsResponseBodyExternalApplicationsExternalApplication] = None,
    ):
        self.external_application = external_application

    def validate(self):
        if self.external_application:
            for v1 in self.external_application:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExternalApplication'] = []
        if self.external_application is not None:
            for k1 in self.external_application:
                result['ExternalApplication'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.external_application = []
        if m.get('ExternalApplication') is not None:
            for k1 in m.get('ExternalApplication'):
                temp_model = main_models.ListExternalApplicationsResponseBodyExternalApplicationsExternalApplication()
                self.external_application.append(temp_model.from_map(k1))

        return self

class ListExternalApplicationsResponseBodyExternalApplicationsExternalApplication(DaraModel):
    def __init__(
        self,
        app_principal_name: str = None,
        create_date: str = None,
        delegated_scope: main_models.ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScope = None,
        display_name: str = None,
        foreign_app_id: str = None,
        tenant_id: str = None,
        update_date: str = None,
    ):
        self.app_principal_name = app_principal_name
        self.create_date = create_date
        self.delegated_scope = delegated_scope
        self.display_name = display_name
        self.foreign_app_id = foreign_app_id
        self.tenant_id = tenant_id
        self.update_date = update_date

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_principal_name is not None:
            result['AppPrincipalName'] = self.app_principal_name

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.foreign_app_id is not None:
            result['ForeignAppId'] = self.foreign_app_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPrincipalName') is not None:
            self.app_principal_name = m.get('AppPrincipalName')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DelegatedScope') is not None:
            temp_model = main_models.ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m.get('DelegatedScope'))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ForeignAppId') is not None:
            self.foreign_app_id = m.get('ForeignAppId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScope(DaraModel):
    def __init__(
        self,
        predefined_scopes: main_models.ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScopePredefinedScopes = None,
    ):
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = main_models.ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m.get('PredefinedScopes'))

        return self

class ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScopePredefinedScopes(DaraModel):
    def __init__(
        self,
        predefined_scope: List[main_models.ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for v1 in self.predefined_scope:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k1 in self.predefined_scope:
                result['PredefinedScope'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k1 in m.get('PredefinedScope'):
                temp_model = main_models.ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k1))

        return self

class ListExternalApplicationsResponseBodyExternalApplicationsExternalApplicationDelegatedScopePredefinedScopesPredefinedScope(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

