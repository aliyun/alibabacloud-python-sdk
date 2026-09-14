# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBVersionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        version_suggestion: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The recommended upgrade version in the format of "major version,minor version" (separated by a comma). The first value is the target version for major engine version upgrade, and the second value is the target version for minor engine version update.
        self.version_suggestion = version_suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.version_suggestion is not None:
            result['VersionSuggestion'] = self.version_suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VersionSuggestion') is not None:
            self.version_suggestion = m.get('VersionSuggestion')

        return self

