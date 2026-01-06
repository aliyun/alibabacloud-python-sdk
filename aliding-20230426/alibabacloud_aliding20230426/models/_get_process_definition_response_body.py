# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetProcessDefinitionResponseBody(DaraModel):
    def __init__(
        self,
        form_uuid: str = None,
        originator: main_models.GetProcessDefinitionResponseBodyOriginator = None,
        out_result: str = None,
        owners: List[main_models.GetProcessDefinitionResponseBodyOwners] = None,
        process_id: str = None,
        process_instance_id: str = None,
        request_id: str = None,
        status: str = None,
        tasks: List[main_models.GetProcessDefinitionResponseBodyTasks] = None,
        title: str = None,
        variables: Dict[str, Any] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.form_uuid = form_uuid
        self.originator = originator
        self.out_result = out_result
        self.owners = owners
        self.process_id = process_id
        self.process_instance_id = process_instance_id
        self.request_id = request_id
        self.status = status
        self.tasks = tasks
        self.title = title
        self.variables = variables
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.originator:
            self.originator.validate()
        if self.owners:
            for v1 in self.owners:
                 if v1:
                    v1.validate()
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form_uuid is not None:
            result['formUuid'] = self.form_uuid

        if self.originator is not None:
            result['originator'] = self.originator.to_map()

        if self.out_result is not None:
            result['outResult'] = self.out_result

        result['owners'] = []
        if self.owners is not None:
            for k1 in self.owners:
                result['owners'].append(k1.to_map() if k1 else None)

        if self.process_id is not None:
            result['processId'] = self.process_id

        if self.process_instance_id is not None:
            result['processInstanceId'] = self.process_instance_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        result['tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['tasks'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        if self.variables is not None:
            result['variables'] = self.variables

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formUuid') is not None:
            self.form_uuid = m.get('formUuid')

        if m.get('originator') is not None:
            temp_model = main_models.GetProcessDefinitionResponseBodyOriginator()
            self.originator = temp_model.from_map(m.get('originator'))

        if m.get('outResult') is not None:
            self.out_result = m.get('outResult')

        self.owners = []
        if m.get('owners') is not None:
            for k1 in m.get('owners'):
                temp_model = main_models.GetProcessDefinitionResponseBodyOwners()
                self.owners.append(temp_model.from_map(k1))

        if m.get('processId') is not None:
            self.process_id = m.get('processId')

        if m.get('processInstanceId') is not None:
            self.process_instance_id = m.get('processInstanceId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tasks = []
        if m.get('tasks') is not None:
            for k1 in m.get('tasks'):
                temp_model = main_models.GetProcessDefinitionResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('variables') is not None:
            self.variables = m.get('variables')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetProcessDefinitionResponseBodyTasks(DaraModel):
    def __init__(
        self,
        actioner_id: str = None,
        activity: main_models.GetProcessDefinitionResponseBodyTasksActivity = None,
        status: str = None,
        task_id: int = None,
    ):
        self.actioner_id = actioner_id
        self.activity = activity
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.activity:
            self.activity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actioner_id is not None:
            result['ActionerId'] = self.actioner_id

        if self.activity is not None:
            result['Activity'] = self.activity.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionerId') is not None:
            self.actioner_id = m.get('ActionerId')

        if m.get('Activity') is not None:
            temp_model = main_models.GetProcessDefinitionResponseBodyTasksActivity()
            self.activity = temp_model.from_map(m.get('Activity'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetProcessDefinitionResponseBodyTasksActivity(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        activity_instance_status: str = None,
        activity_name: str = None,
        activity_name_in_english: str = None,
        id: int = None,
    ):
        self.activity_id = activity_id
        self.activity_instance_status = activity_instance_status
        self.activity_name = activity_name
        self.activity_name_in_english = activity_name_in_english
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.activity_instance_status is not None:
            result['ActivityInstanceStatus'] = self.activity_instance_status

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.activity_name_in_english is not None:
            result['ActivityNameInEnglish'] = self.activity_name_in_english

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ActivityInstanceStatus') is not None:
            self.activity_instance_status = m.get('ActivityInstanceStatus')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('ActivityNameInEnglish') is not None:
            self.activity_name_in_english = m.get('ActivityNameInEnglish')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class GetProcessDefinitionResponseBodyOwners(DaraModel):
    def __init__(
        self,
        department_description: str = None,
        display_en_name: str = None,
        display_name: str = None,
        master_data_departments: List[main_models.GetProcessDefinitionResponseBodyOwnersMasterDataDepartments] = None,
        order_number: str = None,
        personal_photo: str = None,
        status: str = None,
        tb_wang: str = None,
        user_id: str = None,
        user_info: str = None,
    ):
        self.department_description = department_description
        self.display_en_name = display_en_name
        self.display_name = display_name
        self.master_data_departments = master_data_departments
        self.order_number = order_number
        self.personal_photo = personal_photo
        self.status = status
        self.tb_wang = tb_wang
        self.user_id = user_id
        self.user_info = user_info

    def validate(self):
        if self.master_data_departments:
            for v1 in self.master_data_departments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_description is not None:
            result['DepartmentDescription'] = self.department_description

        if self.display_en_name is not None:
            result['DisplayEnName'] = self.display_en_name

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        result['MasterDataDepartments'] = []
        if self.master_data_departments is not None:
            for k1 in self.master_data_departments:
                result['MasterDataDepartments'].append(k1.to_map() if k1 else None)

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        if self.personal_photo is not None:
            result['PersonalPhoto'] = self.personal_photo

        if self.status is not None:
            result['Status'] = self.status

        if self.tb_wang is not None:
            result['TbWang'] = self.tb_wang

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentDescription') is not None:
            self.department_description = m.get('DepartmentDescription')

        if m.get('DisplayEnName') is not None:
            self.display_en_name = m.get('DisplayEnName')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        self.master_data_departments = []
        if m.get('MasterDataDepartments') is not None:
            for k1 in m.get('MasterDataDepartments'):
                temp_model = main_models.GetProcessDefinitionResponseBodyOwnersMasterDataDepartments()
                self.master_data_departments.append(temp_model.from_map(k1))

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        if m.get('PersonalPhoto') is not None:
            self.personal_photo = m.get('PersonalPhoto')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TbWang') is not None:
            self.tb_wang = m.get('TbWang')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')

        return self

class GetProcessDefinitionResponseBodyOwnersMasterDataDepartments(DaraModel):
    def __init__(
        self,
        dept_name: str = None,
        dept_name_in_english: str = None,
        dept_no: str = None,
        dept_path: str = None,
        human_source_group_order_number: str = None,
        human_source_group_work_no: str = None,
        id: int = None,
        master_work_no: str = None,
    ):
        self.dept_name = dept_name
        self.dept_name_in_english = dept_name_in_english
        self.dept_no = dept_no
        self.dept_path = dept_path
        self.human_source_group_order_number = human_source_group_order_number
        self.human_source_group_work_no = human_source_group_work_no
        self.id = id
        self.master_work_no = master_work_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_name is not None:
            result['DeptName'] = self.dept_name

        if self.dept_name_in_english is not None:
            result['DeptNameInEnglish'] = self.dept_name_in_english

        if self.dept_no is not None:
            result['DeptNo'] = self.dept_no

        if self.dept_path is not None:
            result['DeptPath'] = self.dept_path

        if self.human_source_group_order_number is not None:
            result['HumanSourceGroupOrderNumber'] = self.human_source_group_order_number

        if self.human_source_group_work_no is not None:
            result['HumanSourceGroupWorkNo'] = self.human_source_group_work_no

        if self.id is not None:
            result['Id'] = self.id

        if self.master_work_no is not None:
            result['MasterWorkNo'] = self.master_work_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeptName') is not None:
            self.dept_name = m.get('DeptName')

        if m.get('DeptNameInEnglish') is not None:
            self.dept_name_in_english = m.get('DeptNameInEnglish')

        if m.get('DeptNo') is not None:
            self.dept_no = m.get('DeptNo')

        if m.get('DeptPath') is not None:
            self.dept_path = m.get('DeptPath')

        if m.get('HumanSourceGroupOrderNumber') is not None:
            self.human_source_group_order_number = m.get('HumanSourceGroupOrderNumber')

        if m.get('HumanSourceGroupWorkNo') is not None:
            self.human_source_group_work_no = m.get('HumanSourceGroupWorkNo')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MasterWorkNo') is not None:
            self.master_work_no = m.get('MasterWorkNo')

        return self

class GetProcessDefinitionResponseBodyOriginator(DaraModel):
    def __init__(
        self,
        department_description: str = None,
        display_en_name: str = None,
        display_name: str = None,
        master_data_departments: List[main_models.GetProcessDefinitionResponseBodyOriginatorMasterDataDepartments] = None,
        order_number: str = None,
        personal_photo: str = None,
        status: str = None,
        tb_wang: str = None,
        user_id: str = None,
        user_info: str = None,
    ):
        self.department_description = department_description
        self.display_en_name = display_en_name
        self.display_name = display_name
        self.master_data_departments = master_data_departments
        self.order_number = order_number
        self.personal_photo = personal_photo
        self.status = status
        self.tb_wang = tb_wang
        self.user_id = user_id
        self.user_info = user_info

    def validate(self):
        if self.master_data_departments:
            for v1 in self.master_data_departments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_description is not None:
            result['DepartmentDescription'] = self.department_description

        if self.display_en_name is not None:
            result['DisplayEnName'] = self.display_en_name

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        result['MasterDataDepartments'] = []
        if self.master_data_departments is not None:
            for k1 in self.master_data_departments:
                result['MasterDataDepartments'].append(k1.to_map() if k1 else None)

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        if self.personal_photo is not None:
            result['PersonalPhoto'] = self.personal_photo

        if self.status is not None:
            result['Status'] = self.status

        if self.tb_wang is not None:
            result['TbWang'] = self.tb_wang

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentDescription') is not None:
            self.department_description = m.get('DepartmentDescription')

        if m.get('DisplayEnName') is not None:
            self.display_en_name = m.get('DisplayEnName')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        self.master_data_departments = []
        if m.get('MasterDataDepartments') is not None:
            for k1 in m.get('MasterDataDepartments'):
                temp_model = main_models.GetProcessDefinitionResponseBodyOriginatorMasterDataDepartments()
                self.master_data_departments.append(temp_model.from_map(k1))

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        if m.get('PersonalPhoto') is not None:
            self.personal_photo = m.get('PersonalPhoto')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TbWang') is not None:
            self.tb_wang = m.get('TbWang')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')

        return self

class GetProcessDefinitionResponseBodyOriginatorMasterDataDepartments(DaraModel):
    def __init__(
        self,
        dept_name: str = None,
        dept_name_in_english: str = None,
        dept_no: str = None,
        dept_path: str = None,
        human_source_group_order_number: str = None,
        human_source_group_work_no: str = None,
        id: int = None,
        master_work_no: str = None,
    ):
        self.dept_name = dept_name
        self.dept_name_in_english = dept_name_in_english
        self.dept_no = dept_no
        self.dept_path = dept_path
        self.human_source_group_order_number = human_source_group_order_number
        self.human_source_group_work_no = human_source_group_work_no
        self.id = id
        self.master_work_no = master_work_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_name is not None:
            result['DeptName'] = self.dept_name

        if self.dept_name_in_english is not None:
            result['DeptNameInEnglish'] = self.dept_name_in_english

        if self.dept_no is not None:
            result['DeptNo'] = self.dept_no

        if self.dept_path is not None:
            result['DeptPath'] = self.dept_path

        if self.human_source_group_order_number is not None:
            result['HumanSourceGroupOrderNumber'] = self.human_source_group_order_number

        if self.human_source_group_work_no is not None:
            result['HumanSourceGroupWorkNo'] = self.human_source_group_work_no

        if self.id is not None:
            result['Id'] = self.id

        if self.master_work_no is not None:
            result['MasterWorkNo'] = self.master_work_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeptName') is not None:
            self.dept_name = m.get('DeptName')

        if m.get('DeptNameInEnglish') is not None:
            self.dept_name_in_english = m.get('DeptNameInEnglish')

        if m.get('DeptNo') is not None:
            self.dept_no = m.get('DeptNo')

        if m.get('DeptPath') is not None:
            self.dept_path = m.get('DeptPath')

        if m.get('HumanSourceGroupOrderNumber') is not None:
            self.human_source_group_order_number = m.get('HumanSourceGroupOrderNumber')

        if m.get('HumanSourceGroupWorkNo') is not None:
            self.human_source_group_work_no = m.get('HumanSourceGroupWorkNo')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MasterWorkNo') is not None:
            self.master_work_no = m.get('MasterWorkNo')

        return self

