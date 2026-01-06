# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class SearchFormDataSecondGenerationResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.SearchFormDataSecondGenerationResponseBodyData] = None,
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
                temp_model = main_models.SearchFormDataSecondGenerationResponseBodyData()
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

class SearchFormDataSecondGenerationResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time_gmt: str = None,
        creator_user_id: str = None,
        form_data: Dict[str, Any] = None,
        form_instance_id: str = None,
        form_uuid: str = None,
        id: int = None,
        instance_value: str = None,
        modified_time_gmt: str = None,
        modifier: str = None,
        modify_user: main_models.SearchFormDataSecondGenerationResponseBodyDataModifyUser = None,
        originator: main_models.SearchFormDataSecondGenerationResponseBodyDataOriginator = None,
        sequence: str = None,
        serial_number: str = None,
        title: str = None,
        version: int = None,
    ):
        self.create_time_gmt = create_time_gmt
        self.creator_user_id = creator_user_id
        self.form_data = form_data
        self.form_instance_id = form_instance_id
        self.form_uuid = form_uuid
        self.id = id
        self.instance_value = instance_value
        self.modified_time_gmt = modified_time_gmt
        self.modifier = modifier
        self.modify_user = modify_user
        self.originator = originator
        self.sequence = sequence
        self.serial_number = serial_number
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
        if self.create_time_gmt is not None:
            result['CreateTimeGMT'] = self.create_time_gmt

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.form_data is not None:
            result['FormData'] = self.form_data

        if self.form_instance_id is not None:
            result['FormInstanceId'] = self.form_instance_id

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_value is not None:
            result['InstanceValue'] = self.instance_value

        if self.modified_time_gmt is not None:
            result['ModifiedTimeGMT'] = self.modified_time_gmt

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user.to_map()

        if self.originator is not None:
            result['Originator'] = self.originator.to_map()

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.title is not None:
            result['Title'] = self.title

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeGMT') is not None:
            self.create_time_gmt = m.get('CreateTimeGMT')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('FormData') is not None:
            self.form_data = m.get('FormData')

        if m.get('FormInstanceId') is not None:
            self.form_instance_id = m.get('FormInstanceId')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceValue') is not None:
            self.instance_value = m.get('InstanceValue')

        if m.get('ModifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('ModifiedTimeGMT')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifyUser') is not None:
            temp_model = main_models.SearchFormDataSecondGenerationResponseBodyDataModifyUser()
            self.modify_user = temp_model.from_map(m.get('ModifyUser'))

        if m.get('Originator') is not None:
            temp_model = main_models.SearchFormDataSecondGenerationResponseBodyDataOriginator()
            self.originator = temp_model.from_map(m.get('Originator'))

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class SearchFormDataSecondGenerationResponseBodyDataOriginator(DaraModel):
    def __init__(
        self,
        name: main_models.SearchFormDataSecondGenerationResponseBodyDataOriginatorName = None,
        user_id: str = None,
    ):
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
        if self.name is not None:
            result['Name'] = self.name.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            temp_model = main_models.SearchFormDataSecondGenerationResponseBodyDataOriginatorName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class SearchFormDataSecondGenerationResponseBodyDataOriginatorName(DaraModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
    ):
        self.name_in_chinese = name_in_chinese
        self.name_in_english = name_in_english

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameInChinese') is not None:
            self.name_in_chinese = m.get('NameInChinese')

        if m.get('NameInEnglish') is not None:
            self.name_in_english = m.get('NameInEnglish')

        return self

class SearchFormDataSecondGenerationResponseBodyDataModifyUser(DaraModel):
    def __init__(
        self,
        name: main_models.SearchFormDataSecondGenerationResponseBodyDataModifyUserName = None,
        user_id: str = None,
    ):
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
        if self.name is not None:
            result['Name'] = self.name.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            temp_model = main_models.SearchFormDataSecondGenerationResponseBodyDataModifyUserName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class SearchFormDataSecondGenerationResponseBodyDataModifyUserName(DaraModel):
    def __init__(
        self,
        name_in_chinese: str = None,
        name_in_english: str = None,
    ):
        self.name_in_chinese = name_in_chinese
        self.name_in_english = name_in_english

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameInChinese') is not None:
            self.name_in_chinese = m.get('NameInChinese')

        if m.get('NameInEnglish') is not None:
            self.name_in_english = m.get('NameInEnglish')

        return self

