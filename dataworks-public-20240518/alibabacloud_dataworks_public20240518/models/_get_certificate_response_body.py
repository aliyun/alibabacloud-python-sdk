# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetCertificateResponseBody(DaraModel):
    def __init__(
        self,
        certificate: main_models.GetCertificateResponseBodyCertificate = None,
        request_id: str = None,
    ):
        # The details of the certificate file.
        self.certificate = certificate
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.certificate:
            self.certificate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = main_models.GetCertificateResponseBodyCertificate()
            self.certificate = temp_model.from_map(m.get('Certificate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCertificateResponseBodyCertificate(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        file_size_in_bytes: int = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
    ):
        # The time when the certificate file was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The ID of the user who created the certificate file.
        self.create_user = create_user
        # The description.
        self.description = description
        # The size of the certificate file, in bytes.
        self.file_size_in_bytes = file_size_in_bytes
        # The ID of the certificate file.
        self.id = id
        # The name of the certificate file.
        self.name = name
        # The ID of the workspace to which the certificate file belongs.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.description is not None:
            result['Description'] = self.description

        if self.file_size_in_bytes is not None:
            result['FileSizeInBytes'] = self.file_size_in_bytes

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSizeInBytes') is not None:
            self.file_size_in_bytes = m.get('FileSizeInBytes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

