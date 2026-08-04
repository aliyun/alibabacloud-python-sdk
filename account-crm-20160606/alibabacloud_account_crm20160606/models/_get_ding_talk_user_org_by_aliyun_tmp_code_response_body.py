# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class GetDingTalkUserOrgByAliyunTmpCodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDingTalkUserOrgByAliyunTmpCodeResponseBodyData = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

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

        if m.get('Data') is not None:
            temp_model = main_models.GetDingTalkUserOrgByAliyunTmpCodeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDingTalkUserOrgByAliyunTmpCodeResponseBodyData(DaraModel):
    def __init__(
        self,
        associated_union_id: str = None,
        nick: str = None,
        org_dto_list: List[main_models.GetDingTalkUserOrgByAliyunTmpCodeResponseBodyDataOrgDtoList] = None,
    ):
        self.associated_union_id = associated_union_id
        self.nick = nick
        self.org_dto_list = org_dto_list

    def validate(self):
        if self.org_dto_list:
            for v1 in self.org_dto_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_union_id is not None:
            result['AssociatedUnionId'] = self.associated_union_id

        if self.nick is not None:
            result['Nick'] = self.nick

        result['OrgDtoList'] = []
        if self.org_dto_list is not None:
            for k1 in self.org_dto_list:
                result['OrgDtoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedUnionId') is not None:
            self.associated_union_id = m.get('AssociatedUnionId')

        if m.get('Nick') is not None:
            self.nick = m.get('Nick')

        self.org_dto_list = []
        if m.get('OrgDtoList') is not None:
            for k1 in m.get('OrgDtoList'):
                temp_model = main_models.GetDingTalkUserOrgByAliyunTmpCodeResponseBodyDataOrgDtoList()
                self.org_dto_list.append(temp_model.from_map(k1))

        return self

class GetDingTalkUserOrgByAliyunTmpCodeResponseBodyDataOrgDtoList(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.corp_id = corp_id
        self.org_id = org_id
        self.org_name = org_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.org_name is not None:
            result['OrgName'] = self.org_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        return self

