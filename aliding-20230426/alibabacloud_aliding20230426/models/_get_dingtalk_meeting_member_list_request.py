# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetDingtalkMeetingMemberListRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.GetDingtalkMeetingMemberListRequestTenantContext = None,
        cluster_name: str = None,
        conference_id: str = None,
        current_page: int = None,
        org_id: str = None,
        page_size: int = None,
    ):
        self.tenant_context = tenant_context
        self.cluster_name = cluster_name
        # This parameter is required.
        self.conference_id = conference_id
        self.current_page = current_page
        self.org_id = org_id
        self.page_size = page_size

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.GetDingtalkMeetingMemberListRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

class GetDingtalkMeetingMemberListRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

