# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetInstancesResponseBodyData] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.data = data
        self.page_number = page_number
        self.request_id = request_id
        self.total_count = total_count
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        action_executor: List[main_models.GetInstancesResponseBodyDataActionExecutor] = None,
        approved_result: str = None,
        create_time_gmt: str = None,
        data: Dict[str, Any] = None,
        form_uuid: str = None,
        instance_status: str = None,
        modified_time_gmt: str = None,
        originator: main_models.GetInstancesResponseBodyDataOriginator = None,
        process_code: str = None,
        process_instance_id: str = None,
        title: str = None,
        version: int = None,
    ):
        self.action_executor = action_executor
        self.approved_result = approved_result
        self.create_time_gmt = create_time_gmt
        self.data = data
        self.form_uuid = form_uuid
        self.instance_status = instance_status
        self.modified_time_gmt = modified_time_gmt
        self.originator = originator
        self.process_code = process_code
        self.process_instance_id = process_instance_id
        self.title = title
        self.version = version

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

        if self.create_time_gmt is not None:
            result['CreateTimeGMT'] = self.create_time_gmt

        if self.data is not None:
            result['Data'] = self.data

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.modified_time_gmt is not None:
            result['ModifiedTimeGMT'] = self.modified_time_gmt

        if self.originator is not None:
            result['Originator'] = self.originator.to_map()

        if self.process_code is not None:
            result['ProcessCode'] = self.process_code

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.title is not None:
            result['Title'] = self.title

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_executor = []
        if m.get('ActionExecutor') is not None:
            for k1 in m.get('ActionExecutor'):
                temp_model = main_models.GetInstancesResponseBodyDataActionExecutor()
                self.action_executor.append(temp_model.from_map(k1))

        if m.get('ApprovedResult') is not None:
            self.approved_result = m.get('ApprovedResult')

        if m.get('CreateTimeGMT') is not None:
            self.create_time_gmt = m.get('CreateTimeGMT')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('ModifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('ModifiedTimeGMT')

        if m.get('Originator') is not None:
            temp_model = main_models.GetInstancesResponseBodyDataOriginator()
            self.originator = temp_model.from_map(m.get('Originator'))

        if m.get('ProcessCode') is not None:
            self.process_code = m.get('ProcessCode')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetInstancesResponseBodyDataOriginator(DaraModel):
    def __init__(
        self,
        dept_name: str = None,
        email: str = None,
        name: main_models.GetInstancesResponseBodyDataOriginatorName = None,
        user_id: str = None,
    ):
        self.dept_name = dept_name
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
        if self.dept_name is not None:
            result['DeptName'] = self.dept_name

        if self.email is not None:
            result['Email'] = self.email

        if self.name is not None:
            result['Name'] = self.name.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeptName') is not None:
            self.dept_name = m.get('DeptName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            temp_model = main_models.GetInstancesResponseBodyDataOriginatorName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetInstancesResponseBodyDataOriginatorName(DaraModel):
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

class GetInstancesResponseBodyDataActionExecutor(DaraModel):
    def __init__(
        self,
        dept_name: str = None,
        email: str = None,
        name: main_models.GetInstancesResponseBodyDataActionExecutorName = None,
        user_id: str = None,
    ):
        self.dept_name = dept_name
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
        if self.dept_name is not None:
            result['DeptName'] = self.dept_name

        if self.email is not None:
            result['Email'] = self.email

        if self.name is not None:
            result['Name'] = self.name.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeptName') is not None:
            self.dept_name = m.get('DeptName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            temp_model = main_models.GetInstancesResponseBodyDataActionExecutorName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetInstancesResponseBodyDataActionExecutorName(DaraModel):
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

