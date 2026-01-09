# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogtailPipelineConfigRequest(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        config_type: str = None,
        logstore_name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The name of the Logtail pipeline configuration.
        self.config_name = config_name
        self.config_type = config_type
        # The name of the Logstore.
        self.logstore_name = logstore_name
        # The line from which the query starts.
        self.offset = offset
        # The number of Logtail pipeline configurations per page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['configName'] = self.config_name

        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')

        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

