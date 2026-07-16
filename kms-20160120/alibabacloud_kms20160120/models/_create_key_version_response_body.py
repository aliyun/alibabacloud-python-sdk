# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class CreateKeyVersionResponseBody(DaraModel):
    def __init__(
        self,
        key_version: main_models.CreateKeyVersionResponseBodyKeyVersion = None,
        request_id: str = None,
    ):
        # The metadata of the version.
        self.key_version = key_version
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.key_version:
            self.key_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_version is not None:
            result['KeyVersion'] = self.key_version.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyVersion') is not None:
            temp_model = main_models.CreateKeyVersionResponseBodyKeyVersion()
            self.key_version = temp_model.from_map(m.get('KeyVersion'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateKeyVersionResponseBodyKeyVersion(DaraModel):
    def __init__(
        self,
        creation_date: str = None,
        key_id: str = None,
        key_version_id: str = None,
    ):
        # The date and time when the version was created. The time is displayed in UTC.
        self.creation_date = creation_date
        # The ID of the CMK. The ID must be globally unique.
        self.key_id = key_id
        # The ID of the version.
        self.key_version_id = key_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        return self

