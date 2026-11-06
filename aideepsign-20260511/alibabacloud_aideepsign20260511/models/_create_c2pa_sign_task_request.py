# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateC2paSignTaskRequest(DaraModel):
    def __init__(
        self,
        custom_assertions: str = None,
        file_url: str = None,
        software_agent: str = None,
        source_type: str = None,
    ):
        # The JSON string of the custom assertion list.
        self.custom_assertions = custom_assertions
        # The absolute HTTP or HTTPS URL of the file to be signed. The URL can be up to 4,096 characters in length.
        # 
        # This parameter is required.
        self.file_url = file_url
        # This parameter is not supported in the current version.
        self.software_agent = software_agent
        # This parameter is not supported in the current version.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_assertions is not None:
            result['CustomAssertions'] = self.custom_assertions

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.software_agent is not None:
            result['SoftwareAgent'] = self.software_agent

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAssertions') is not None:
            self.custom_assertions = m.get('CustomAssertions')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('SoftwareAgent') is not None:
            self.software_agent = m.get('SoftwareAgent')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

