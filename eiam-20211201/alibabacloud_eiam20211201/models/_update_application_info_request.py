# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationInfoRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        application_owner: main_models.UpdateApplicationInfoRequestApplicationOwner = None,
        application_visibility: List[str] = None,
        client_token: str = None,
        custom_fields: List[main_models.UpdateApplicationInfoRequestCustomFields] = None,
        instance_id: str = None,
        logo_url: str = None,
    ):
        # IDaaS的应用主键id
        # 
        # This parameter is required.
        self.application_id = application_id
        # 应用的表示名称
        self.application_name = application_name
        self.application_owner = application_owner
        self.application_visibility = application_visibility
        self.client_token = client_token
        self.custom_fields = custom_fields
        # IDaaS EIAM的实例id
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 应用Logo地址
        self.logo_url = logo_url

    def validate(self):
        if self.application_owner:
            self.application_owner.validate()
        if self.custom_fields:
            for v1 in self.custom_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_owner is not None:
            result['ApplicationOwner'] = self.application_owner.to_map()

        if self.application_visibility is not None:
            result['ApplicationVisibility'] = self.application_visibility

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['CustomFields'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationOwner') is not None:
            temp_model = main_models.UpdateApplicationInfoRequestApplicationOwner()
            self.application_owner = temp_model.from_map(m.get('ApplicationOwner'))

        if m.get('ApplicationVisibility') is not None:
            self.application_visibility = m.get('ApplicationVisibility')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k1 in m.get('CustomFields'):
                temp_model = main_models.UpdateApplicationInfoRequestCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        return self

class UpdateApplicationInfoRequestCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
        operation: str = None,
    ):
        self.field_name = field_name
        self.field_value = field_value
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.operation is not None:
            result['Operation'] = self.operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        return self

class UpdateApplicationInfoRequestApplicationOwner(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.group_ids = group_ids
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

