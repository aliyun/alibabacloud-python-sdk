# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAnnouncementShrinkRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        display_page: str = None,
        display_type: str = None,
        effective_end: str = None,
        effective_start: str = None,
        priority: str = None,
        publish_now: bool = None,
        target_role_codes_shrink: str = None,
        target_role_mode: str = None,
        target_tenant_ids_shrink: str = None,
        target_tenant_mode: str = None,
        tenant_id: str = None,
        title: str = None,
    ):
        # The content of the notice.
        # 
        # This parameter is required.
        self.content = content
        # The display page. Valid values: ALL, FRONTEND, and BACKEND.
        self.display_page = display_page
        # The display type and group label.
        self.display_type = display_type
        # The effective end time.
        self.effective_end = effective_end
        # The effective start time in ISO 8601 format with time zone. If this parameter is not specified, the notice takes effect immediately.
        self.effective_start = effective_start
        # The priority. Valid values:
        # 
        # This parameter is required.
        self.priority = priority
        # Specifies whether to publish the notice immediately after creation.
        self.publish_now = publish_now
        # The list of system role codes. This parameter is used when targetRoleMode is set to SPECIFIED.
        self.target_role_codes_shrink = target_role_codes_shrink
        # The target role scope. Valid values: ALL and SPECIFIED.
        self.target_role_mode = target_role_mode
        # The list of target tenant IDs. This parameter is used when targetTenantMode is set to SPECIFIED.
        self.target_tenant_ids_shrink = target_tenant_ids_shrink
        # The target tenant scope. Valid values: ALL and SPECIFIED.
        self.target_tenant_mode = target_tenant_mode
        # The ID of the tenant for which the notice takes effect.
        self.tenant_id = tenant_id
        # The title of the notice.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.display_page is not None:
            result['displayPage'] = self.display_page

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.effective_end is not None:
            result['effectiveEnd'] = self.effective_end

        if self.effective_start is not None:
            result['effectiveStart'] = self.effective_start

        if self.priority is not None:
            result['priority'] = self.priority

        if self.publish_now is not None:
            result['publishNow'] = self.publish_now

        if self.target_role_codes_shrink is not None:
            result['targetRoleCodes'] = self.target_role_codes_shrink

        if self.target_role_mode is not None:
            result['targetRoleMode'] = self.target_role_mode

        if self.target_tenant_ids_shrink is not None:
            result['targetTenantIds'] = self.target_tenant_ids_shrink

        if self.target_tenant_mode is not None:
            result['targetTenantMode'] = self.target_tenant_mode

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('displayPage') is not None:
            self.display_page = m.get('displayPage')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('effectiveEnd') is not None:
            self.effective_end = m.get('effectiveEnd')

        if m.get('effectiveStart') is not None:
            self.effective_start = m.get('effectiveStart')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('publishNow') is not None:
            self.publish_now = m.get('publishNow')

        if m.get('targetRoleCodes') is not None:
            self.target_role_codes_shrink = m.get('targetRoleCodes')

        if m.get('targetRoleMode') is not None:
            self.target_role_mode = m.get('targetRoleMode')

        if m.get('targetTenantIds') is not None:
            self.target_tenant_ids_shrink = m.get('targetTenantIds')

        if m.get('targetTenantMode') is not None:
            self.target_tenant_mode = m.get('targetTenantMode')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

