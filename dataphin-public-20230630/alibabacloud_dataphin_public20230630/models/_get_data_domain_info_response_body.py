# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDataDomainInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_domain_info: main_models.GetDataDomainInfoResponseBodyDataDomainInfo = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data_domain_info = data_domain_info
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data_domain_info:
            self.data_domain_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data_domain_info is not None:
            result['DataDomainInfo'] = self.data_domain_info.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('DataDomainInfo') is not None:
            temp_model = main_models.GetDataDomainInfoResponseBodyDataDomainInfo()
            self.data_domain_info = temp_model.from_map(m.get('DataDomainInfo'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataDomainInfoResponseBodyDataDomainInfo(DaraModel):
    def __init__(
        self,
        abbreviation: str = None,
        biz_unit_id: int = None,
        description: str = None,
        display_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        last_modifier: str = None,
        last_modifier_name: str = None,
        name: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
        parent_id: int = None,
    ):
        self.abbreviation = abbreviation
        self.biz_unit_id = biz_unit_id
        self.description = description
        self.display_name = display_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.last_modifier = last_modifier
        self.last_modifier_name = last_modifier_name
        self.name = name
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abbreviation is not None:
            result['Abbreviation'] = self.abbreviation

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abbreviation') is not None:
            self.abbreviation = m.get('Abbreviation')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

