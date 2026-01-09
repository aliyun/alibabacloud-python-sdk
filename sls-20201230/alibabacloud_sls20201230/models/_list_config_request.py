# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConfigRequest(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        logstore_name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The name of the Logtail configuration, which is used for fuzzy match.
        self.config_name = config_name
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The line from which the query starts. Default value: 0.
        # 
        # This parameter is required.
        self.offset = offset
        # The number of entries per page. Maximum value: 500.
        # 
        # This parameter is required.
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

        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

