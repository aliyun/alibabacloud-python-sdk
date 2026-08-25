# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetUserIdRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        external_id: main_models.GetUserIdRequestExternalId = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The identifier information about the user that is synchronized from an external identity provider (IdP).
        self.external_id = external_id

    def validate(self):
        if self.external_id:
            self.external_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.external_id is not None:
            result['ExternalId'] = self.external_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('ExternalId') is not None:
            temp_model = main_models.GetUserIdRequestExternalId()
            self.external_id = temp_model.from_map(m.get('ExternalId'))

        return self

class GetUserIdRequestExternalId(DaraModel):
    def __init__(
        self,
        id: str = None,
        issuer: str = None,
    ):
        # The identifier of the user that is synchronized from an external IdP.
        self.id = id
        # The method for external identity synchronization. Only System for Cross-domain Identity Management (SCIM) synchronization is supported.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        return self

