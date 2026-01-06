# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class SearchFormDatasResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.SearchFormDatasResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.current_page = current_page
        self.data = data
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
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

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
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.SearchFormDatasResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class SearchFormDatasResponseBodyData(DaraModel):
    def __init__(
        self,
        created_time_gmt: str = None,
        creator_user_id: str = None,
        data_id: int = None,
        form_data: Dict[str, Any] = None,
        form_instance_id: str = None,
        form_uuid: str = None,
        instance_value: str = None,
        model_uuid: str = None,
        modified_time_gmt: str = None,
        modifier_user_id: str = None,
        modify_user: main_models.SearchFormDatasResponseBodyDataModifyUser = None,
        originator: main_models.SearchFormDatasResponseBodyDataOriginator = None,
        sequence: str = None,
        serial_no: str = None,
        title: str = None,
        version: int = None,
    ):
        self.created_time_gmt = created_time_gmt
        self.creator_user_id = creator_user_id
        self.data_id = data_id
        self.form_data = form_data
        self.form_instance_id = form_instance_id
        self.form_uuid = form_uuid
        self.instance_value = instance_value
        self.model_uuid = model_uuid
        self.modified_time_gmt = modified_time_gmt
        self.modifier_user_id = modifier_user_id
        self.modify_user = modify_user
        self.originator = originator
        self.sequence = sequence
        self.serial_no = serial_no
        self.title = title
        self.version = version

    def validate(self):
        if self.modify_user:
            self.modify_user.validate()
        if self.originator:
            self.originator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time_gmt is not None:
            result['CreatedTimeGMT'] = self.created_time_gmt

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.form_data is not None:
            result['FormData'] = self.form_data

        if self.form_instance_id is not None:
            result['FormInstanceId'] = self.form_instance_id

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.instance_value is not None:
            result['InstanceValue'] = self.instance_value

        if self.model_uuid is not None:
            result['ModelUuid'] = self.model_uuid

        if self.modified_time_gmt is not None:
            result['ModifiedTimeGMT'] = self.modified_time_gmt

        if self.modifier_user_id is not None:
            result['ModifierUserId'] = self.modifier_user_id

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user.to_map()

        if self.originator is not None:
            result['Originator'] = self.originator.to_map()

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no

        if self.title is not None:
            result['Title'] = self.title

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimeGMT') is not None:
            self.created_time_gmt = m.get('CreatedTimeGMT')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('FormData') is not None:
            self.form_data = m.get('FormData')

        if m.get('FormInstanceId') is not None:
            self.form_instance_id = m.get('FormInstanceId')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('InstanceValue') is not None:
            self.instance_value = m.get('InstanceValue')

        if m.get('ModelUuid') is not None:
            self.model_uuid = m.get('ModelUuid')

        if m.get('ModifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('ModifiedTimeGMT')

        if m.get('ModifierUserId') is not None:
            self.modifier_user_id = m.get('ModifierUserId')

        if m.get('ModifyUser') is not None:
            temp_model = main_models.SearchFormDatasResponseBodyDataModifyUser()
            self.modify_user = temp_model.from_map(m.get('ModifyUser'))

        if m.get('Originator') is not None:
            temp_model = main_models.SearchFormDatasResponseBodyDataOriginator()
            self.originator = temp_model.from_map(m.get('Originator'))

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class SearchFormDatasResponseBodyDataOriginator(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: main_models.SearchFormDatasResponseBodyDataOriginatorUserName = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.user_name:
            self.user_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            temp_model = main_models.SearchFormDatasResponseBodyDataOriginatorUserName()
            self.user_name = temp_model.from_map(m.get('UserName'))

        return self

class SearchFormDatasResponseBodyDataOriginatorUserName(DaraModel):
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

class SearchFormDatasResponseBodyDataModifyUser(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: main_models.SearchFormDatasResponseBodyDataModifyUserUserName = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.user_name:
            self.user_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            temp_model = main_models.SearchFormDatasResponseBodyDataModifyUserUserName()
            self.user_name = temp_model.from_map(m.get('UserName'))

        return self

class SearchFormDatasResponseBodyDataModifyUserUserName(DaraModel):
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

