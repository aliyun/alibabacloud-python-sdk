# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class CreateAgAccountResponseBody(DaraModel):
    def __init__(
        self,
        ag_relation_dto: main_models.CreateAgAccountResponseBodyAgRelationDto = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The relationship between the account that is used to call the CreateAgAccount operation and the account that is created.
        self.ag_relation_dto = ag_relation_dto
        # The status code returned.
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.ag_relation_dto:
            self.ag_relation_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ag_relation_dto is not None:
            result['AgRelationDto'] = self.ag_relation_dto.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgRelationDto') is not None:
            temp_model = main_models.CreateAgAccountResponseBodyAgRelationDto()
            self.ag_relation_dto = temp_model.from_map(m.get('AgRelationDto'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateAgAccountResponseBodyAgRelationDto(DaraModel):
    def __init__(
        self,
        mpk: str = None,
        pk: str = None,
        ram_admin_role_name: str = None,
        type: str = None,
    ):
        # The ID of the account that is used to call the CreateAgAccount operation.
        self.mpk = mpk
        # The ID of the account that is created.
        self.pk = pk
        # The role of the account that is created.
        self.ram_admin_role_name = ram_admin_role_name
        # The type of the relationship.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.ram_admin_role_name is not None:
            result['RamAdminRoleName'] = self.ram_admin_role_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('RamAdminRoleName') is not None:
            self.ram_admin_role_name = m.get('RamAdminRoleName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

