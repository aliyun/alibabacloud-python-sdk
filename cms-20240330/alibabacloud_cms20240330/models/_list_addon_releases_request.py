# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAddonReleasesRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        max_results: str = None,
        next_token: str = None,
        parent_addon_release_id: str = None,
    ):
        # The name of the add-on.
        self.addon_name = addon_name
        self.max_results = max_results
        self.next_token = next_token
        # The parent AddonRelease ID.
        self.parent_addon_release_id = parent_addon_release_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['addonName'] = self.addon_name

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.parent_addon_release_id is not None:
            result['parentAddonReleaseId'] = self.parent_addon_release_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('parentAddonReleaseId') is not None:
            self.parent_addon_release_id = m.get('parentAddonReleaseId')

        return self

