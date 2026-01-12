# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LogInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        is_truncated: bool = None,
        pod_id: str = None,
        pod_uid: str = None,
        source: str = None,
        time: str = None,
    ):
        self.content = content
        self.id = id
        self.is_truncated = is_truncated
        self.pod_id = pod_id
        self.pod_uid = pod_uid
        self.source = source
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.pod_id is not None:
            result['PodId'] = self.pod_id

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.source is not None:
            result['Source'] = self.source

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

