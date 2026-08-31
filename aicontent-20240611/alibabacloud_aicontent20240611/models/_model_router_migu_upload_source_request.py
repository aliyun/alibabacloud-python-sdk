# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterMiguUploadSourceRequest(DaraModel):
    def __init__(
        self,
        file_type: str = None,
        service_name: str = None,
    ):
        # The source file type. Valid values: VIDEO, IMAGE, AUDIO, and TEXT.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The business service name, such as kling, vidu, or wonder.
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        return self

