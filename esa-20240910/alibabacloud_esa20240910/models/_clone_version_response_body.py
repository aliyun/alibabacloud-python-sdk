# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneVersionResponseBody(DaraModel):
    def __init__(
        self,
        clone_version: int = None,
        origin_version: int = None,
        request_id: str = None,
    ):
        # The version number of the cloned version.
        self.clone_version = clone_version
        # The version number that was cloned.
        self.origin_version = origin_version
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clone_version is not None:
            result['CloneVersion'] = self.clone_version

        if self.origin_version is not None:
            result['OriginVersion'] = self.origin_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloneVersion') is not None:
            self.clone_version = m.get('CloneVersion')

        if m.get('OriginVersion') is not None:
            self.origin_version = m.get('OriginVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

