# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PutRecordStorageLifeCycleRequest(DaraModel):
    def __init__(
        self,
        stream_ids: List[str] = None,
        tag: str = None,
        unix_timestamp: int = None,
    ):
        # This parameter is required.
        self.stream_ids = stream_ids
        # This parameter is required.
        self.tag = tag
        # This parameter is required.
        self.unix_timestamp = unix_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stream_ids is not None:
            result['StreamIds'] = self.stream_ids

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.unix_timestamp is not None:
            result['UnixTimestamp'] = self.unix_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamIds') is not None:
            self.stream_ids = m.get('StreamIds')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('UnixTimestamp') is not None:
            self.unix_timestamp = m.get('UnixTimestamp')

        return self

