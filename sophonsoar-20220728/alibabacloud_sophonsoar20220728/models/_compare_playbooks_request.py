# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ComparePlaybooksRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        new_playbook_release_id: int = None,
        old_playbook_release_id: int = None,
        playbook_uuid: str = None,
    ):
        # The language of the request and response.
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The UUID of the second published version for comparison.
        # 
        # > To obtain the UUID of a historical version, call the [DescribePlaybookReleases](~~DescribePlaybookReleases~~) operation. The system automatically generates a UUID for a new version.
        # 
        # This parameter is required.
        self.new_playbook_release_id = new_playbook_release_id
        # The UUID of the first published version for comparison.
        # 
        # > To obtain the UUID of a historical version, call the [DescribePlaybookReleases](~~DescribePlaybookReleases~~) operation. The system automatically generates a UUID for a new version.
        # 
        # This parameter is required.
        self.old_playbook_release_id = old_playbook_release_id
        # The UUID of the playbook.
        # 
        # > Call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.new_playbook_release_id is not None:
            result['NewPlaybookReleaseId'] = self.new_playbook_release_id

        if self.old_playbook_release_id is not None:
            result['OldPlaybookReleaseId'] = self.old_playbook_release_id

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NewPlaybookReleaseId') is not None:
            self.new_playbook_release_id = m.get('NewPlaybookReleaseId')

        if m.get('OldPlaybookReleaseId') is not None:
            self.old_playbook_release_id = m.get('OldPlaybookReleaseId')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        return self

