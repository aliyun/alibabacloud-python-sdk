# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: main_models.ListApplicationsResponseBodyApplications = None,
        request_id: str = None,
    ):
        self.applications = applications
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Applications') is not None:
            temp_model = main_models.ListApplicationsResponseBodyApplications()
            self.applications = temp_model.from_map(m.get('Applications'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application: List[main_models.ListApplicationsResponseBodyApplicationsApplication] = None,
    ):
        self.application = application

    def validate(self):
        if self.application:
            for v1 in self.application:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Application'] = []
        if self.application is not None:
            for k1 in self.application:
                result['Application'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k1 in m.get('Application'):
                temp_model = main_models.ListApplicationsResponseBodyApplicationsApplication()
                self.application.append(temp_model.from_map(k1))

        return self

class ListApplicationsResponseBodyApplicationsApplication(DaraModel):
    def __init__(
        self,
        access_token_validity: int = None,
        account_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        create_date: str = None,
        delegated_scope: main_models.ListApplicationsResponseBodyApplicationsApplicationDelegatedScope = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        protocol_version: str = None,
        redirect_uris: main_models.ListApplicationsResponseBodyApplicationsApplicationRedirectUris = None,
        refresh_token_validity: int = None,
        secret_required: bool = None,
        update_date: str = None,
    ):
        self.access_token_validity = access_token_validity
        self.account_id = account_id
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.create_date = create_date
        self.delegated_scope = delegated_scope
        self.display_name = display_name
        self.is_multi_tenant = is_multi_tenant
        self.protocol_version = protocol_version
        self.redirect_uris = redirect_uris
        self.refresh_token_validity = refresh_token_validity
        self.secret_required = secret_required
        self.update_date = update_date

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant

        if self.protocol_version is not None:
            result['ProtocolVersion'] = self.protocol_version

        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()

        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity

        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DelegatedScope') is not None:
            temp_model = main_models.ListApplicationsResponseBodyApplicationsApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m.get('DelegatedScope'))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')

        if m.get('ProtocolVersion') is not None:
            self.protocol_version = m.get('ProtocolVersion')

        if m.get('RedirectUris') is not None:
            temp_model = main_models.ListApplicationsResponseBodyApplicationsApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m.get('RedirectUris'))

        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')

        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class ListApplicationsResponseBodyApplicationsApplicationRedirectUris(DaraModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')

        return self

class ListApplicationsResponseBodyApplicationsApplicationDelegatedScope(DaraModel):
    def __init__(
        self,
        predefined_scopes: main_models.ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes = None,
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
            temp_model = main_models.ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m.get('PredefinedScopes'))

        return self

class ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes(DaraModel):
    def __init__(
        self,
        predefined_scope: List[main_models.ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
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
                temp_model = main_models.ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k1))

        return self

class ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        required: bool = None,
    ):
        self.description = description
        self.name = name
        self.required = required

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

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

