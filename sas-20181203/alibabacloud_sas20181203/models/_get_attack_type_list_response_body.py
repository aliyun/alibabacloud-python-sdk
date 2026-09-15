# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAttackTypeListResponseBody(DaraModel):
    def __init__(
        self,
        attack_type_list: List[main_models.GetAttackTypeListResponseBodyAttackTypeList] = None,
        request_id: str = None,
    ):
        # The list of attack types.
        self.attack_type_list = attack_type_list
        # The request ID. Alibaba Cloud generates a unique identifier for each request. You can use the request ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.attack_type_list:
            for v1 in self.attack_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttackTypeList'] = []
        if self.attack_type_list is not None:
            for k1 in self.attack_type_list:
                result['AttackTypeList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_type_list = []
        if m.get('AttackTypeList') is not None:
            for k1 in m.get('AttackTypeList'):
                temp_model = main_models.GetAttackTypeListResponseBodyAttackTypeList()
                self.attack_type_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAttackTypeListResponseBodyAttackTypeList(DaraModel):
    def __init__(
        self,
        label: str = None,
        status_type: str = None,
        value: str = None,
    ):
        # The internationalization (i18n) translation key of the attack type, such as sas.attack.type.type12. The caller must resolve this key by using internationalization resources to obtain a human-readable attack type name.
        self.label = label
        # The attack source. Valid values:
        # 
        # - **cfw**: Cloud Firewall.
        # - **alinet**: Network defense plugin.
        # - **waf**: Web Application Firewall (WAF).
        self.status_type = status_type
        # The type value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.status_type is not None:
            result['Status_Type'] = self.status_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Status_Type') is not None:
            self.status_type = m.get('Status_Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

