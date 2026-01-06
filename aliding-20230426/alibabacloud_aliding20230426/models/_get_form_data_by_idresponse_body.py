# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetFormDataByIDResponseBody(DaraModel):
    def __init__(
        self,
        form_data: Dict[str, Any] = None,
        form_inst_id: str = None,
        modified_time_gmt: str = None,
        originator: main_models.GetFormDataByIDResponseBodyOriginator = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.form_data = form_data
        self.form_inst_id = form_inst_id
        self.modified_time_gmt = modified_time_gmt
        self.originator = originator
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.originator:
            self.originator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form_data is not None:
            result['formData'] = self.form_data

        if self.form_inst_id is not None:
            result['formInstId'] = self.form_inst_id

        if self.modified_time_gmt is not None:
            result['modifiedTimeGMT'] = self.modified_time_gmt

        if self.originator is not None:
            result['originator'] = self.originator.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formData') is not None:
            self.form_data = m.get('formData')

        if m.get('formInstId') is not None:
            self.form_inst_id = m.get('formInstId')

        if m.get('modifiedTimeGMT') is not None:
            self.modified_time_gmt = m.get('modifiedTimeGMT')

        if m.get('originator') is not None:
            temp_model = main_models.GetFormDataByIDResponseBodyOriginator()
            self.originator = temp_model.from_map(m.get('originator'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetFormDataByIDResponseBodyOriginator(DaraModel):
    def __init__(
        self,
        department_name: str = None,
        email: str = None,
        name: main_models.GetFormDataByIDResponseBodyOriginatorName = None,
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
            temp_model = main_models.GetFormDataByIDResponseBodyOriginatorName()
            self.name = temp_model.from_map(m.get('Name'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetFormDataByIDResponseBodyOriginatorName(DaraModel):
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

