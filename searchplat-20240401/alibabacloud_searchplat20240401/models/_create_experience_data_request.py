# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExperienceDataRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        data_size: int = None,
        data_type: str = None,
        data_value: str = None,
        name: str = None,
        service_type: str = None,
        dry_run: bool = None,
    ):
        # The data content type. Valid values:
        # - pdf
        # - text
        # - html
        # - doc.
        self.content_type = content_type
        # The data size.
        self.data_size = data_size
        # The data type. Valid values:
        # - file: file
        # - url: URL.
        self.data_type = data_type
        # The data content.
        # - If dataType is set to file, this field specifies the OSS address of the file.
        # - If dataType is set to url, this field specifies the HTTP URL of the data.
        self.data_value = data_value
        # The data name. This parameter is required when dataType is set to file.
        self.name = name
        # The service type.
        self.service_type = service_type
        # Specifies whether to perform a dry run request.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.data_size is not None:
            result['dataSize'] = self.data_size

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.data_value is not None:
            result['dataValue'] = self.data_value

        if self.name is not None:
            result['name'] = self.name

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('dataSize') is not None:
            self.data_size = m.get('dataSize')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('dataValue') is not None:
            self.data_value = m.get('dataValue')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

