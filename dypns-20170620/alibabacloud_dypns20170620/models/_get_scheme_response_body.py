# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class GetSchemeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSchemeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSchemeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSchemeResponseBodyData(DaraModel):
    def __init__(
        self,
        audit_desc: str = None,
        audit_time: int = None,
        business_type_list: List[int] = None,
        company_id: int = None,
        cycle_list: List[str] = None,
        description: str = None,
        industry_id: str = None,
        scenes_list: List[main_models.GetSchemeResponseBodyDataScenesList] = None,
        scheme_id: int = None,
        scheme_name: str = None,
        scheme_type: int = None,
        statement: str = None,
        status: int = None,
        template_id: int = None,
    ):
        self.audit_desc = audit_desc
        self.audit_time = audit_time
        self.business_type_list = business_type_list
        self.company_id = company_id
        self.cycle_list = cycle_list
        self.description = description
        self.industry_id = industry_id
        self.scenes_list = scenes_list
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.scheme_type = scheme_type
        self.statement = statement
        self.status = status
        self.template_id = template_id

    def validate(self):
        if self.scenes_list:
            for v1 in self.scenes_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_desc is not None:
            result['AuditDesc'] = self.audit_desc

        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time

        if self.business_type_list is not None:
            result['BusinessTypeList'] = self.business_type_list

        if self.company_id is not None:
            result['CompanyId'] = self.company_id

        if self.cycle_list is not None:
            result['CycleList'] = self.cycle_list

        if self.description is not None:
            result['Description'] = self.description

        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id

        result['ScenesList'] = []
        if self.scenes_list is not None:
            for k1 in self.scenes_list:
                result['ScenesList'].append(k1.to_map() if k1 else None)

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name

        if self.scheme_type is not None:
            result['SchemeType'] = self.scheme_type

        if self.statement is not None:
            result['Statement'] = self.statement

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditDesc') is not None:
            self.audit_desc = m.get('AuditDesc')

        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')

        if m.get('BusinessTypeList') is not None:
            self.business_type_list = m.get('BusinessTypeList')

        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')

        if m.get('CycleList') is not None:
            self.cycle_list = m.get('CycleList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')

        self.scenes_list = []
        if m.get('ScenesList') is not None:
            for k1 in m.get('ScenesList'):
                temp_model = main_models.GetSchemeResponseBodyDataScenesList()
                self.scenes_list.append(temp_model.from_map(k1))

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')

        if m.get('SchemeType') is not None:
            self.scheme_type = m.get('SchemeType')

        if m.get('Statement') is not None:
            self.statement = m.get('Statement')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetSchemeResponseBodyDataScenesList(DaraModel):
    def __init__(
        self,
        scenes_id: int = None,
        scenes_name: str = None,
    ):
        self.scenes_id = scenes_id
        self.scenes_name = scenes_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scenes_id is not None:
            result['ScenesId'] = self.scenes_id

        if self.scenes_name is not None:
            result['ScenesName'] = self.scenes_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScenesId') is not None:
            self.scenes_id = m.get('ScenesId')

        if m.get('ScenesName') is not None:
            self.scenes_name = m.get('ScenesName')

        return self

