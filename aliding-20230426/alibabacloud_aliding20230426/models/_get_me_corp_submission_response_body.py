# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetMeCorpSubmissionResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetMeCorpSubmissionResponseBodyData] = None,
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
                temp_model = main_models.GetMeCorpSubmissionResponseBodyData()
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

class GetMeCorpSubmissionResponseBodyData(DaraModel):
    def __init__(
        self,
        actioner: List[main_models.GetMeCorpSubmissionResponseBodyDataActioner] = None,
        actioner_id: List[str] = None,
        actioner_name: List[str] = None,
        app_type: str = None,
        create_time_gmt: str = None,
        current_activity_instances: List[main_models.GetMeCorpSubmissionResponseBodyDataCurrentActivityInstances] = None,
        data_map: Dict[str, Any] = None,
        data_type: str = None,
        finish_time_gmt: str = None,
        form_instance_id: str = None,
        form_uuid: str = None,
        instance_value: str = None,
        modified_time_gmt: str = None,
        originator_avatar: str = None,
        originator_display_name: str = None,
        originator_id: str = None,
        process_approved_result: str = None,
        process_approved_result_text: str = None,
        process_code: str = None,
        process_id: int = None,
        process_instance_id: str = None,
        process_instance_status: str = None,
        process_instance_status_text: str = None,
        process_name: str = None,
        title: str = None,
        version: int = None,
    ):
        self.actioner = actioner
        self.actioner_id = actioner_id
        self.actioner_name = actioner_name
        self.app_type = app_type
        self.create_time_gmt = create_time_gmt
        self.current_activity_instances = current_activity_instances
        self.data_map = data_map
        self.data_type = data_type
        self.finish_time_gmt = finish_time_gmt
        self.form_instance_id = form_instance_id
        self.form_uuid = form_uuid
        self.instance_value = instance_value
        self.modified_time_gmt = modified_time_gmt
        self.originator_avatar = originator_avatar
        self.originator_display_name = originator_display_name
        self.originator_id = originator_id
        self.process_approved_result = process_approved_result
        self.process_approved_result_text = process_approved_result_text
        self.process_code = process_code
        self.process_id = process_id
        self.process_instance_id = process_instance_id
        self.process_instance_status = process_instance_status
        self.process_instance_status_text = process_instance_status_text
        self.process_name = process_name
        self.title = title
        self.version = version

    def validate(self):
        if self.actioner:
            for v1 in self.actioner:
                 if v1:
                    v1.validate()
        if self.current_activity_instances:
            for v1 in self.current_activity_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actioner'] = []
        if self.actioner is not None:
            for k1 in self.actioner:
                result['Actioner'].append(k1.to_map() if k1 else None)

        if self.actioner_id is not None:
            result['ActionerId'] = self.actioner_id

        if self.actioner_name is not None:
            result['ActionerName'] = self.actioner_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.create_time_gmt is not None:
            result['CreateTimeGMT'] = self.create_time_gmt

        result['CurrentActivityInstances'] = []
        if self.current_activity_instances is not None:
            for k1 in self.current_activity_instances:
                result['CurrentActivityInstances'].append(k1.to_map() if k1 else None)

        if self.data_map is not None:
            result['DataMap'] = self.data_map

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.finish_time_gmt is not None:
            result['FinishTimeGMT'] = self.finish_time_gmt

        if self.form_instance_id is not None:
            result['FormInstanceId'] = self.form_instance_id

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.instance_value is not None:
            result['InstanceValue'] = self.instance_value

        if self.modified_time_gmt is not None:
            result['ModifiedTimeGMT'] = self.modified_time_gmt

        if self.originator_avatar is not None:
            result['OriginatorAvatar'] = self.originator_avatar

        if self.originator_display_name is not None:
            result['OriginatorDisplayName'] = self.originator_display_name

        if self.originator_id is not None:
            result['OriginatorId'] = self.originator_id

        if self.process_approved_result is not None:
            result['ProcessApprovedResult'] = self.process_approved_result

        if self.process_approved_result_text is not None:
            result['ProcessApprovedResultText'] = self.process_approved_result_text

        if self.process_code is not None:
            result['ProcessCode'] = self.process_code

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.process_instance_status is not None:
            result['ProcessInstanceStatus'] = self.process_instance_status

        if self.process_instance_status_text is not None:
            result['ProcessInstanceStatusText'] = self.process_instance_status_text

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.title is not None:
            result['Title'] = self.title

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actioner = []
        if m.get('Actioner') is not None:
            for k1 in m.get('Actioner'):
                temp_model = main_models.GetMeCorpSubmissionResponseBodyDataActioner()
                self.actioner.append(temp_model.from_map(k1))

        if m.get('ActionerId') is not None:
            self.actioner_id = m.get('ActionerId')

        if m.get('ActionerName') is not None:
            self.actioner_name = m.get('ActionerName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CreateTimeGMT') is not None:
            self.create_time_gmt = m.get('CreateTimeGMT')

        self.current_activity_instances = []
        if m.get('CurrentActivityInstances') is not None:
            for k1 in m.get('CurrentActivityInstances'):
                temp_model = main_models.GetMeCorpSubmissionResponseBodyDataCurrentActivityInstances()
                self.current_activity_instances.append(temp_model.from_map(k1))

        if m.get('DataMap') is not None:
            self.data_map = m.get('DataMap')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('FinishTimeGMT') is not None:
            self.finish_time_gmt = m.get('FinishTimeGMT')

        if m.get('FormInstanceId') is not None:
            self.form_instance_id = m.get('FormInstanceId')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('InstanceValue') is not None:
            self.instance_value = m.get('InstanceValue')

        if m.get('ModifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('ModifiedTimeGMT')

        if m.get('OriginatorAvatar') is not None:
            self.originator_avatar = m.get('OriginatorAvatar')

        if m.get('OriginatorDisplayName') is not None:
            self.originator_display_name = m.get('OriginatorDisplayName')

        if m.get('OriginatorId') is not None:
            self.originator_id = m.get('OriginatorId')

        if m.get('ProcessApprovedResult') is not None:
            self.process_approved_result = m.get('ProcessApprovedResult')

        if m.get('ProcessApprovedResultText') is not None:
            self.process_approved_result_text = m.get('ProcessApprovedResultText')

        if m.get('ProcessCode') is not None:
            self.process_code = m.get('ProcessCode')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('ProcessInstanceStatus') is not None:
            self.process_instance_status = m.get('ProcessInstanceStatus')

        if m.get('ProcessInstanceStatusText') is not None:
            self.process_instance_status_text = m.get('ProcessInstanceStatusText')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetMeCorpSubmissionResponseBodyDataCurrentActivityInstances(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        activity_instance_status: str = None,
        activity_name: str = None,
        activity_name_en: str = None,
        id: int = None,
    ):
        self.activity_id = activity_id
        self.activity_instance_status = activity_instance_status
        self.activity_name = activity_name
        self.activity_name_en = activity_name_en
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

        if self.activity_name_en is not None:
            result['ActivityNameEn'] = self.activity_name_en

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

        if m.get('ActivityNameEn') is not None:
            self.activity_name_en = m.get('ActivityNameEn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class GetMeCorpSubmissionResponseBodyDataActioner(DaraModel):
    def __init__(
        self,
        bu_name: str = None,
        email: str = None,
        employee_type: str = None,
        employee_type_information: str = None,
        human_resource_group_work_number: str = None,
        is_system_admin: bool = None,
        level: str = None,
        name: str = None,
        nick_name: str = None,
        order_number: str = None,
        personal_photo: str = None,
        personal_photo_url: str = None,
        pinyin_name_all: str = None,
        pinyin_nick_name: str = None,
        state: str = None,
        super_user_id: str = None,
        tb_wang: str = None,
        user_id: str = None,
    ):
        self.bu_name = bu_name
        self.email = email
        self.employee_type = employee_type
        self.employee_type_information = employee_type_information
        self.human_resource_group_work_number = human_resource_group_work_number
        self.is_system_admin = is_system_admin
        self.level = level
        self.name = name
        self.nick_name = nick_name
        self.order_number = order_number
        self.personal_photo = personal_photo
        self.personal_photo_url = personal_photo_url
        self.pinyin_name_all = pinyin_name_all
        self.pinyin_nick_name = pinyin_nick_name
        self.state = state
        self.super_user_id = super_user_id
        self.tb_wang = tb_wang
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bu_name is not None:
            result['BuName'] = self.bu_name

        if self.email is not None:
            result['Email'] = self.email

        if self.employee_type is not None:
            result['EmployeeType'] = self.employee_type

        if self.employee_type_information is not None:
            result['EmployeeTypeInformation'] = self.employee_type_information

        if self.human_resource_group_work_number is not None:
            result['HumanResourceGroupWorkNumber'] = self.human_resource_group_work_number

        if self.is_system_admin is not None:
            result['IsSystemAdmin'] = self.is_system_admin

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        if self.personal_photo is not None:
            result['PersonalPhoto'] = self.personal_photo

        if self.personal_photo_url is not None:
            result['PersonalPhotoUrl'] = self.personal_photo_url

        if self.pinyin_name_all is not None:
            result['PinyinNameAll'] = self.pinyin_name_all

        if self.pinyin_nick_name is not None:
            result['PinyinNickName'] = self.pinyin_nick_name

        if self.state is not None:
            result['State'] = self.state

        if self.super_user_id is not None:
            result['SuperUserId'] = self.super_user_id

        if self.tb_wang is not None:
            result['TbWang'] = self.tb_wang

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuName') is not None:
            self.bu_name = m.get('BuName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmployeeType') is not None:
            self.employee_type = m.get('EmployeeType')

        if m.get('EmployeeTypeInformation') is not None:
            self.employee_type_information = m.get('EmployeeTypeInformation')

        if m.get('HumanResourceGroupWorkNumber') is not None:
            self.human_resource_group_work_number = m.get('HumanResourceGroupWorkNumber')

        if m.get('IsSystemAdmin') is not None:
            self.is_system_admin = m.get('IsSystemAdmin')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        if m.get('PersonalPhoto') is not None:
            self.personal_photo = m.get('PersonalPhoto')

        if m.get('PersonalPhotoUrl') is not None:
            self.personal_photo_url = m.get('PersonalPhotoUrl')

        if m.get('PinyinNameAll') is not None:
            self.pinyin_name_all = m.get('PinyinNameAll')

        if m.get('PinyinNickName') is not None:
            self.pinyin_nick_name = m.get('PinyinNickName')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SuperUserId') is not None:
            self.super_user_id = m.get('SuperUserId')

        if m.get('TbWang') is not None:
            self.tb_wang = m.get('TbWang')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

