# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SimpleTemplate(DaraModel):
    def __init__(
        self,
        abandon_reasons: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        shared_mode: str = None,
        status: str = None,
        tags: List[str] = None,
        template_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        # Reasons for template deprecation
        self.abandon_reasons = abandon_reasons
        # Template description
        self.description = description
        # Creation Time
        self.gmt_create_time = gmt_create_time
        # Update Time
        self.gmt_modified_time = gmt_modified_time
        # Is shared
        self.shared_mode = shared_mode
        # Status
        self.status = status
        # List of tags
        self.tags = tags
        # Template ID
        self.template_id = template_id
        # Template Name
        self.template_name = template_name
        # Tenant ID of the template
        self.tenant_id = tenant_id
        # Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abandon_reasons is not None:
            result['AbandonReasons'] = self.abandon_reasons

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonReasons') is not None:
            self.abandon_reasons = m.get('AbandonReasons')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

