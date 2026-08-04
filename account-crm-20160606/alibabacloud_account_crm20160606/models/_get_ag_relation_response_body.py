# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class GetAgRelationResponseBody(DaraModel):
    def __init__(
        self,
        ag_relation_dto: main_models.GetAgRelationResponseBodyAgRelationDto = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.ag_relation_dto = ag_relation_dto
        self.code = code
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetAgRelationResponseBodyAgRelationDto()
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

class GetAgRelationResponseBodyAgRelationDto(DaraModel):
    def __init__(
        self,
        mpk: str = None,
        pk: str = None,
        type: str = None,
    ):
        self.mpk = mpk
        self.pk = pk
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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

