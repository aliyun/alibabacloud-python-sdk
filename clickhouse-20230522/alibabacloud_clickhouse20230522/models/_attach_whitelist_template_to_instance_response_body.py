# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class AttachWhitelistTemplateToInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.AttachWhitelistTemplateToInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Request ID.
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
            temp_model = main_models.AttachWhitelistTemplateToInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AttachWhitelistTemplateToInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        attach_fail_list: List[main_models.AttachWhitelistTemplateToInstanceResponseBodyDataAttachFailList] = None,
        attach_successed_list: List[main_models.AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedList] = None,
        status: str = None,
    ):
        # Instances that failed to be attached.
        self.attach_fail_list = attach_fail_list
        # Instances to which the template was successfully attached.
        self.attach_successed_list = attach_successed_list
        # The status of the operation. A value of `ok` indicates success.
        self.status = status

    def validate(self):
        if self.attach_fail_list:
            for v1 in self.attach_fail_list:
                 if v1:
                    v1.validate()
        if self.attach_successed_list:
            for v1 in self.attach_successed_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachFailList'] = []
        if self.attach_fail_list is not None:
            for k1 in self.attach_fail_list:
                result['AttachFailList'].append(k1.to_map() if k1 else None)

        result['AttachSuccessedList'] = []
        if self.attach_successed_list is not None:
            for k1 in self.attach_successed_list:
                result['AttachSuccessedList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attach_fail_list = []
        if m.get('AttachFailList') is not None:
            for k1 in m.get('AttachFailList'):
                temp_model = main_models.AttachWhitelistTemplateToInstanceResponseBodyDataAttachFailList()
                self.attach_fail_list.append(temp_model.from_map(k1))

        self.attach_successed_list = []
        if m.get('AttachSuccessedList') is not None:
            for k1 in m.get('AttachSuccessedList'):
                temp_model = main_models.AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedList()
                self.attach_successed_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedList(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        templates: List[main_models.AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedListTemplates] = None,
    ):
        # The name of the instance.
        self.dbinstance_id = dbinstance_id
        # The list of whitelist templates.
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedListTemplates()
                self.templates.append(temp_model.from_map(k1))

        return self

class AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedListTemplates(DaraModel):
    def __init__(
        self,
        db_instances: List[main_models.AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedListTemplatesDbInstances] = None,
        security_iplist: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # The list of attached instances.
        self.db_instances = db_instances
        # The IP address whitelist.
        self.security_iplist = security_iplist
        # The ID of the whitelist template.
        self.template_id = template_id
        # The name of the whitelist template.
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
                temp_model = main_models.AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedListTemplatesDbInstances()
                self.db_instances.append(temp_model.from_map(k1))

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class AttachWhitelistTemplateToInstanceResponseBodyDataAttachSuccessedListTemplatesDbInstances(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        # The ID of the instance.
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



class AttachWhitelistTemplateToInstanceResponseBodyDataAttachFailList(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        reason: str = None,
    ):
        # The name of the instance.
        self.dbinstance_id = dbinstance_id
        # The reason for the attachment failure.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

