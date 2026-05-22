# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCacheTagResponseBody(DaraModel):
    def __init__(
        self,
        case_insensitive: str = None,
        request_id: str = None,
        site_version: int = None,
        tag_name: str = None,
    ):
        # Whether to ignore case. Possible values:
        # - on: Enabled, ignores case.
        # - off: Disabled, does not ignore case.
        self.case_insensitive = case_insensitive
        # Request ID.
        self.request_id = request_id
        # Version number of the site.
        self.site_version = site_version
        # Custom CacheTag name.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_insensitive is not None:
            result['CaseInsensitive'] = self.case_insensitive

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseInsensitive') is not None:
            self.case_insensitive = m.get('CaseInsensitive')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

