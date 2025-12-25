# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DeleteWhitelistTemplateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DeleteWhitelistTemplateResponseBodyData = None,
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
            temp_model = main_models.DeleteWhitelistTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteWhitelistTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        templates: List[main_models.DeleteWhitelistTemplateResponseBodyDataTemplates] = None,
    ):
        self.templates = templates

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
        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.DeleteWhitelistTemplateResponseBodyDataTemplates()
                self.templates.append(temp_model.from_map(k1))

        return self

class DeleteWhitelistTemplateResponseBodyDataTemplates(DaraModel):
    def __init__(
        self,
        db_instances: List[main_models.DeleteWhitelistTemplateResponseBodyDataTemplatesDbInstances] = None,
        security_iplist: str = None,
        template_id: str = None,
    ):
        self.db_instances = db_instances
        self.security_iplist = security_iplist
        self.template_id = template_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_instances = []
        if m.get('DbInstances') is not None:
            for k1 in m.get('DbInstances'):
                temp_model = main_models.DeleteWhitelistTemplateResponseBodyDataTemplatesDbInstances()
                self.db_instances.append(temp_model.from_map(k1))

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class DeleteWhitelistTemplateResponseBodyDataTemplatesDbInstances(DaraModel):
    def __init__(
        self,
        db_instance_name: str = None,
    ):
        self.db_instance_name = db_instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        return self

