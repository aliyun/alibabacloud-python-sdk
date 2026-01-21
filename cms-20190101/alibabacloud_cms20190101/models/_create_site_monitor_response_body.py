# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateSiteMonitorResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_result_list: main_models.CreateSiteMonitorResponseBodyCreateResultList = None,
        data: main_models.CreateSiteMonitorResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The returned result.
        # 
        # If a site monitoring task is created, the result is returned. If a site monitoring task fails to be created, no result is returned.
        self.create_result_list = create_result_list
        # The result of the site monitoring task.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.create_result_list:
            self.create_result_list.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_result_list is not None:
            result['CreateResultList'] = self.create_result_list.to_map()

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateResultList') is not None:
            temp_model = main_models.CreateSiteMonitorResponseBodyCreateResultList()
            self.create_result_list = temp_model.from_map(m.get('CreateResultList'))

        if m.get('Data') is not None:
            temp_model = main_models.CreateSiteMonitorResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateSiteMonitorResponseBodyData(DaraModel):
    def __init__(
        self,
        attach_alert_result: main_models.CreateSiteMonitorResponseBodyDataAttachAlertResult = None,
    ):
        # The result that is returned after you associate the existing alert rule with the site monitoring task.
        self.attach_alert_result = attach_alert_result

    def validate(self):
        if self.attach_alert_result:
            self.attach_alert_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_alert_result is not None:
            result['AttachAlertResult'] = self.attach_alert_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachAlertResult') is not None:
            temp_model = main_models.CreateSiteMonitorResponseBodyDataAttachAlertResult()
            self.attach_alert_result = temp_model.from_map(m.get('AttachAlertResult'))

        return self

class CreateSiteMonitorResponseBodyDataAttachAlertResult(DaraModel):
    def __init__(
        self,
        contact: List[main_models.CreateSiteMonitorResponseBodyDataAttachAlertResultContact] = None,
    ):
        self.contact = contact

    def validate(self):
        if self.contact:
            for v1 in self.contact:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contact'] = []
        if self.contact is not None:
            for k1 in self.contact:
                result['Contact'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact = []
        if m.get('Contact') is not None:
            for k1 in m.get('Contact'):
                temp_model = main_models.CreateSiteMonitorResponseBodyDataAttachAlertResultContact()
                self.contact.append(temp_model.from_map(k1))

        return self

class CreateSiteMonitorResponseBodyDataAttachAlertResultContact(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        rule_id: str = None,
        success: str = None,
    ):
        # The status code that is returned after you associate the existing alert rule with the site monitoring task.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The message that is returned after you associate the existing alert rule with the site monitoring task.
        self.message = message
        # The ID of the request that was sent to associate the existing alert rule with the site monitoring task.
        self.request_id = request_id
        # The ID of the alert rule.
        self.rule_id = rule_id
        # Indicates whether the existing alert rule was associated with the site monitoring task. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateSiteMonitorResponseBodyCreateResultList(DaraModel):
    def __init__(
        self,
        create_result_list: List[main_models.CreateSiteMonitorResponseBodyCreateResultListCreateResultList] = None,
    ):
        self.create_result_list = create_result_list

    def validate(self):
        if self.create_result_list:
            for v1 in self.create_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CreateResultList'] = []
        if self.create_result_list is not None:
            for k1 in self.create_result_list:
                result['CreateResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_result_list = []
        if m.get('CreateResultList') is not None:
            for k1 in m.get('CreateResultList'):
                temp_model = main_models.CreateSiteMonitorResponseBodyCreateResultListCreateResultList()
                self.create_result_list.append(temp_model.from_map(k1))

        return self

class CreateSiteMonitorResponseBodyCreateResultListCreateResultList(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        task_name: str = None,
    ):
        # The ID of the site monitoring task.
        self.task_id = task_id
        # The name of the site monitoring task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

