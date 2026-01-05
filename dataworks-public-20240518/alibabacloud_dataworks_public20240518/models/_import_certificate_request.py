# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportCertificateRequest(DaraModel):
    def __init__(
        self,
        certificate_file: str = None,
        description: str = None,
        name: str = None,
        project_id: int = None,
    ):
        # The certificate file to upload. Upload method: Upload the file by creating an InputStream.
        # 
        # This parameter is required.
        self.certificate_file = certificate_file
        # The description of the task.
        self.description = description
        # The certificate file name. In a project workspace, certificate file names must be unique.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the workspace to which the certificate file belongs.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_file is not None:
            result['CertificateFile'] = self.certificate_file

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateFile') is not None:
            self.certificate_file = m.get('CertificateFile')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

