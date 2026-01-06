# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetInstancesByIdListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetInstancesByIdListResponseBodyResult] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.GetInstancesByIdListResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetInstancesByIdListResponseBodyResult(DaraModel):
    def __init__(
        self,
        action_executor: List[main_models.GetInstancesByIdListResponseBodyResultActionExecutor] = None,
        approved_result: str = None,
        data: Dict[str, Any] = None,
        form_uuid: str = None,
        instance_status: str = None,
        originator: main_models.GetInstancesByIdListResponseBodyResultOriginator = None,
        process_code: str = None,
        process_instance_id: str = None,
        title: str = None,
    ):
        self.action_executor = action_executor
        self.approved_result = approved_result
        self.data = data
        self.form_uuid = form_uuid
        self.instance_status = instance_status
        self.originator = originator
        self.process_code = process_code
        self.process_instance_id = process_instance_id
        self.title = title

    def validate(self):
        if self.action_executor:
            for v1 in self.action_executor:
                 if v1:
                    v1.validate()
        if self.originator:
            self.originator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActionExecutor'] = []
        if self.action_executor is not None:
            for k1 in self.action_executor:
                result['ActionExecutor'].append(k1.to_map() if k1 else None)

        if self.approved_result is not None:
            result['ApprovedResult'] = self.approved_result

        if self.data is not None:
            result['Data'] = self.data

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.originator is not None:
            result['Originator'] = self.originator.to_map()

        if self.process_code is not None:
            result['ProcessCode'] = self.process_code

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_executor = []
        if m.get('ActionExecutor') is not None:
            for k1 in m.get('ActionExecutor'):
                temp_model = main_models.GetInstancesByIdListResponseBodyResultActionExecutor()
                self.action_executor.append(temp_model.from_map(k1))

        if m.get('ApprovedResult') is not None:
            self.approved_result = m.get('ApprovedResult')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('Originator') is not None:
            temp_model = main_models.GetInstancesByIdListResponseBodyResultOriginator()
            self.originator = temp_model.from_map(m.get('Originator'))

        if m.get('ProcessCode') is not None:
            self.process_code = m.get('ProcessCode')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetInstancesByIdListResponseBodyResultOriginator(DaraModel):
    def __init__(
        self,
        department_name: str = None,
        email: str = None,
        name: main_models.GetInstancesByIdListResponseBodyResultOriginatorName = None,
        user_id: str = None,
    ):
        self.department_name = department_name
        self.email = email
        self.name = name
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name

        if self.email is not None:
            result['Email'] = self.email

        if self.name is not None:
            result['Name'] = self.name.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            temp_model = main_models.GetInstancesByIdListResponseBodyResultOriginatorName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetInstancesByIdListResponseBodyResultOriginatorName(DaraModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        self.name_in_chinese = name_in_chinese
        self.name_in_english = name_in_english
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_in_chinese is not None:
            result['NameInChinese'] = self.name_in_chinese

        if self.name_in_english is not None:
            result['NameInEnglish'] = self.name_in_english

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameInChinese') is not None:
            self.name_in_chinese = m.get('NameInChinese')

        if m.get('NameInEnglish') is not None:
            self.name_in_english = m.get('NameInEnglish')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetInstancesByIdListResponseBodyResultActionExecutor(DaraModel):
    def __init__(
        self,
        department_name: str = None,
        email: str = None,
        name: main_models.GetInstancesByIdListResponseBodyResultActionExecutorName = None,
        user_id: str = None,
    ):
        self.department_name = department_name
        self.email = email
        self.name = name
        self.user_id = user_id

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name

        if self.email is not None:
            result['Email'] = self.email

        if self.name is not None:
            result['Name'] = self.name.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            temp_model = main_models.GetInstancesByIdListResponseBodyResultActionExecutorName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetInstancesByIdListResponseBodyResultActionExecutorName(DaraModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
        type: str = None,
    ):
        self.name_in_chinese = name_in_chinese
        self.name_in_english = name_in_english
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_in_chinese is not None:
            result['NameInChinese'] = self.name_in_chinese

        if self.name_in_english is not None:
            result['NameInEnglish'] = self.name_in_english

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameInChinese') is not None:
            self.name_in_chinese = m.get('NameInChinese')

        if m.get('NameInEnglish') is not None:
            self.name_in_english = m.get('NameInEnglish')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

