# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateNacUserCertStatusRequest(DaraModel):
    def __init__(
        self,
        id_list: List[main_models.UpdateNacUserCertStatusRequestIdList] = None,
        status: str = None,
    ):
        self.id_list = id_list
        self.status = status

    def validate(self):
        if self.id_list:
            for v1 in self.id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IdList'] = []
        if self.id_list is not None:
            for k1 in self.id_list:
                result['IdList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.id_list = []
        if m.get('IdList') is not None:
            for k1 in m.get('IdList'):
                temp_model = main_models.UpdateNacUserCertStatusRequestIdList()
                self.id_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class UpdateNacUserCertStatusRequestIdList(DaraModel):
    def __init__(
        self,
        dev_tag: str = None,
        user_id: str = None,
    ):
        self.dev_tag = dev_tag
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

