# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScanSbomExportRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        format: str = None,
    ):
        # The file name (including the extension) for the downloaded file. The file name is signed into the Content-Disposition header of the URL. If you leave this parameter empty, the backend generates a file name in the format of project name-sbom-<format>.<extension>. If the file name contains control characters or path separators (/ or \\), or if the length exceeds 255 characters, a 400 InvalidFileName error is returned.
        self.file_name = file_name
        # Valid values:
        # * cyclonedx-json
        # * spdx-json
        # 
        # This parameter is required.
        self.format = format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.format is not None:
            result['format'] = self.format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('format') is not None:
            self.format = m.get('format')

        return self

