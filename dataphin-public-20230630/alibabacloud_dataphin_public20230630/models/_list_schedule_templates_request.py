# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListScheduleTemplatesRequest(DaraModel):
    def __init__(
        self,
        list_schedule_templates_command: main_models.ListScheduleTemplatesRequestListScheduleTemplatesCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # This parameter is required.
        self.list_schedule_templates_command = list_schedule_templates_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id

    def validate(self):
        if self.list_schedule_templates_command:
            self.list_schedule_templates_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_schedule_templates_command is not None:
            result['ListScheduleTemplatesCommand'] = self.list_schedule_templates_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListScheduleTemplatesCommand') is not None:
            temp_model = main_models.ListScheduleTemplatesRequestListScheduleTemplatesCommand()
            self.list_schedule_templates_command = temp_model.from_map(m.get('ListScheduleTemplatesCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListScheduleTemplatesRequestListScheduleTemplatesCommand(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        schedule_template_type: str = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.schedule_template_type = schedule_template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.schedule_template_type is not None:
            result['ScheduleTemplateType'] = self.schedule_template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScheduleTemplateType') is not None:
            self.schedule_template_type = m.get('ScheduleTemplateType')

        return self

