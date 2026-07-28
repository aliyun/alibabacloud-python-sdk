# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class DescribeProfileResponseBody(DaraModel):
    def __init__(
        self,
        profile: str = None,
        profile_summary: Any = None,
        request_id: str = None,
    ):
        # The profile text. This parameter is not yet supported.
        self.profile = profile
        # The profile summary.
        self.profile_summary = profile_summary
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.profile is not None:
            result['Profile'] = self.profile

        if self.profile_summary is not None:
            result['ProfileSummary'] = self.profile_summary

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('ProfileSummary') is not None:
            self.profile_summary = m.get('ProfileSummary')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

