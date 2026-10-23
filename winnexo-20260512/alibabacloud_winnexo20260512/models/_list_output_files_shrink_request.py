# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOutputFilesShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        collaboration_group_id: str = None,
        item_type: str = None,
        keyword: str = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        session_id: str = None,
        shared_only: bool = None,
        tags_shrink: str = None,
        tenant_id: str = None,
    ):
        # The business ID used for exact filtering. The length is 1 to 128 characters. This value is derived from the businessId of the file registration or associated workflow instance.
        self.biz_id = biz_id
        # The ID of the collaboration workspace. The length is 1 to 64 characters. This parameter is optional. If not specified, the personal outputs of the current user are queried. If specified, the real-time permissions of the workspace members and source resources are verified.
        self.collaboration_group_id = collaboration_group_id
        # The output item type. Valid values: ppt, html, document, picture, slides, video, audio, email, and others.
        self.item_type = item_type
        # The keyword used to match the output title or detail name.
        self.keyword = keyword
        # The name of the digital employee (operating object). Filters outputs by name.
        self.operating_object_name = operating_object_name
        # The page number. Pages start from 1. Default value: 1.
        self.page = page
        # The number of items per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The session ID used for exact filtering. The length is 1 to 128 characters. This parameter applies to regular sessions, skill sessions, and the executionId of task executions.
        self.session_id = session_id
        # Specifies whether to display only shared outputs and output details.
        self.shared_only = shared_only
        # The tags used for exact filtering. All specified tags must be matched simultaneously. You can specify up to 20 tags. Each tag must be a non-empty string of 1 to 128 characters. Tags are derived from file registrations or the variables.tags of associated instances.
        self.tags_shrink = tags_shrink
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used. The identity and tenant permissions are determined by the gateway and backend authentication.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.shared_only is not None:
            result['sharedOnly'] = self.shared_only

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sharedOnly') is not None:
            self.shared_only = m.get('sharedOnly')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

