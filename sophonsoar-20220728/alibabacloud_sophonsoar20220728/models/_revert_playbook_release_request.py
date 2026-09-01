# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevertPlaybookReleaseRequest(DaraModel):
    def __init__(
        self,
        is_publish: bool = None,
        play_release_id: int = None,
        playbook_uuid: str = None,
    ):
        # Specifies whether to publish the playbook after the rollback.
        # 
        # - **true** (default): Publishes the playbook after the rollback.
        # 
        # - **false**: Rolls back the playbook without publishing it.
        self.is_publish = is_publish
        # The ID of the published playbook version.
        # 
        # > Call the [DescribePlaybookReleases](~~DescribePlaybookReleases~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.play_release_id = play_release_id
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
        if self.is_publish is not None:
            result['IsPublish'] = self.is_publish

        if self.play_release_id is not None:
            result['PlayReleaseId'] = self.play_release_id

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPublish') is not None:
            self.is_publish = m.get('IsPublish')

        if m.get('PlayReleaseId') is not None:
            self.play_release_id = m.get('PlayReleaseId')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        return self

