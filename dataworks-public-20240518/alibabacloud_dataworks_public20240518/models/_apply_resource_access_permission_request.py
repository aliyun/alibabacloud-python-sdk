# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ApplyResourceAccessPermissionRequest(DaraModel):
    def __init__(
        self,
        apply_contents: List[main_models.ApplyResourceAccessPermissionRequestApplyContents] = None,
        client_token: str = None,
        reason: str = None,
    ):
        # This parameter is required.
        self.apply_contents = apply_contents
        self.client_token = client_token
        # This parameter is required.
        self.reason = reason

    def validate(self):
        if self.apply_contents:
            for v1 in self.apply_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplyContents'] = []
        if self.apply_contents is not None:
            for k1 in self.apply_contents:
                result['ApplyContents'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_contents = []
        if m.get('ApplyContents') is not None:
            for k1 in m.get('ApplyContents'):
                temp_model = main_models.ApplyResourceAccessPermissionRequestApplyContents()
                self.apply_contents.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

class ApplyResourceAccessPermissionRequestApplyContents(DaraModel):
    def __init__(
        self,
        access_types: List[str] = None,
        auth_method: str = None,
        expiration_time: int = None,
        grantee: main_models.ApplyResourceAccessPermissionRequestApplyContentsGrantee = None,
        resource: main_models.ApplyResourceAccessPermissionRequestApplyContentsResource = None,
    ):
        # This parameter is required.
        self.access_types = access_types
        self.auth_method = auth_method
        self.expiration_time = expiration_time
        # This parameter is required.
        self.grantee = grantee
        self.resource = resource

    def validate(self):
        if self.grantee:
            self.grantee.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_types is not None:
            result['AccessTypes'] = self.access_types

        if self.auth_method is not None:
            result['AuthMethod'] = self.auth_method

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.grantee is not None:
            result['Grantee'] = self.grantee.to_map()

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTypes') is not None:
            self.access_types = m.get('AccessTypes')

        if m.get('AuthMethod') is not None:
            self.auth_method = m.get('AuthMethod')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('Grantee') is not None:
            temp_model = main_models.ApplyResourceAccessPermissionRequestApplyContentsGrantee()
            self.grantee = temp_model.from_map(m.get('Grantee'))

        if m.get('Resource') is not None:
            temp_model = main_models.ApplyResourceAccessPermissionRequestApplyContentsResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        return self

class ApplyResourceAccessPermissionRequestApplyContentsResource(DaraModel):
    def __init__(
        self,
        def_schema: str = None,
        def_version: str = None,
        meta_data: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.def_schema = def_schema
        self.def_version = def_version
        self.meta_data = meta_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.def_version is not None:
            result['DefVersion'] = self.def_version

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('DefVersion') is not None:
            self.def_version = m.get('DefVersion')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        return self

class ApplyResourceAccessPermissionRequestApplyContentsGrantee(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # This parameter is required.
        self.principal_id = principal_id
        # This parameter is required.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

