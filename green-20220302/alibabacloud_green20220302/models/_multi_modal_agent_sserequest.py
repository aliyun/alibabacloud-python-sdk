# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MultiModalAgentSSERequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        service_parameters: str = None,
        stream: str = None,
    ):
        # The unique identifier of the whiteboard application. To obtain the whiteboard application ID, see [CreateApp](https://help.aliyun.com/document_detail/204234.html).
        self.app_id = app_id
        # The parameter set required by the moderation service, in JSON string format. The input parameter for text content is content (String), the custom data ID is DataId (String), and the cache type is CacheType (String, valid value: ephemeral).
        self.service_parameters = service_parameters
        # Specifies whether to use streaming output.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppID'] = self.app_id

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

