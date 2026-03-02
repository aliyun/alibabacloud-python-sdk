# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetApplicationProvisionInfoResponseBody(DaraModel):
    def __init__(
        self,
        application_provision_info: main_models.GetApplicationProvisionInfoResponseBodyApplicationProvisionInfo = None,
        request_id: str = None,
    ):
        self.application_provision_info = application_provision_info
        self.request_id = request_id

    def validate(self):
        if self.application_provision_info:
            self.application_provision_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_provision_info is not None:
            result['ApplicationProvisionInfo'] = self.application_provision_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationProvisionInfo') is not None:
            temp_model = main_models.GetApplicationProvisionInfoResponseBodyApplicationProvisionInfo()
            self.application_provision_info = temp_model.from_map(m.get('ApplicationProvisionInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationProvisionInfoResponseBodyApplicationProvisionInfo(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        app_id: str = None,
        app_name: str = None,
        create_date: str = None,
        delegated_scope: main_models.GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScope = None,
        display_name: str = None,
        update_date: str = None,
    ):
        self.account_id = account_id
        self.app_id = app_id
        self.app_name = app_name
        self.create_date = create_date
        self.delegated_scope = delegated_scope
        self.display_name = display_name
        self.update_date = update_date

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DelegatedScope') is not None:
            temp_model = main_models.GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScope()
            self.delegated_scope = temp_model.from_map(m.get('DelegatedScope'))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScope(DaraModel):
    def __init__(
        self,
        predefined_scopes: main_models.GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScopePredefinedScopes = None,
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
            temp_model = main_models.GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m.get('PredefinedScopes'))

        return self

class GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScopePredefinedScopes(DaraModel):
    def __init__(
        self,
        predefined_scope: List[main_models.GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScopePredefinedScopesPredefinedScope] = None,
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
                temp_model = main_models.GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k1))

        return self

class GetApplicationProvisionInfoResponseBodyApplicationProvisionInfoDelegatedScopePredefinedScopesPredefinedScope(DaraModel):
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

