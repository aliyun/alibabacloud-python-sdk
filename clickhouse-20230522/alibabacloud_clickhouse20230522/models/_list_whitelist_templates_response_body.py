# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class ListWhitelistTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListWhitelistTemplatesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListWhitelistTemplatesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListWhitelistTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        curr_page_numbers: int = None,
        has_next: bool = None,
        has_prev: bool = None,
        page_size: int = None,
        templates: List[main_models.ListWhitelistTemplatesResponseBodyDataTemplates] = None,
        total_count: int = None,
        total_page_numbers: int = None,
    ):
        self.curr_page_numbers = curr_page_numbers
        self.has_next = has_next
        self.has_prev = has_prev
        self.page_size = page_size
        self.templates = templates
        self.total_count = total_count
        self.total_page_numbers = total_page_numbers

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.curr_page_numbers is not None:
            result['CurrPageNumbers'] = self.curr_page_numbers

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.has_prev is not None:
            result['HasPrev'] = self.has_prev

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page_numbers is not None:
            result['TotalPageNumbers'] = self.total_page_numbers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrPageNumbers') is not None:
            self.curr_page_numbers = m.get('CurrPageNumbers')

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('HasPrev') is not None:
            self.has_prev = m.get('HasPrev')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.ListWhitelistTemplatesResponseBodyDataTemplates()
                self.templates.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPageNumbers') is not None:
            self.total_page_numbers = m.get('TotalPageNumbers')

        return self

class ListWhitelistTemplatesResponseBodyDataTemplates(DaraModel):
    def __init__(
        self,
        db_instances: List[main_models.ListWhitelistTemplatesResponseBodyDataTemplatesDbInstances] = None,
        security_iplist: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        self.db_instances = db_instances
        self.security_iplist = security_iplist
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        if self.db_instances:
            for v1 in self.db_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DbInstances'] = []
        if self.db_instances is not None:
            for k1 in self.db_instances:
                result['DbInstances'].append(k1.to_map() if k1 else None)

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_instances = []
        if m.get('DbInstances') is not None:
            for k1 in m.get('DbInstances'):
                temp_model = main_models.ListWhitelistTemplatesResponseBodyDataTemplatesDbInstances()
                self.db_instances.append(temp_model.from_map(k1))

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class ListWhitelistTemplatesResponseBodyDataTemplatesDbInstances(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

