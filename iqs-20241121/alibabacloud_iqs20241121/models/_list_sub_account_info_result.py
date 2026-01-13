# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241121 import models as main_models
from darabonba.model import DaraModel

class ListSubAccountInfoResult(DaraModel):
    def __init__(
        self,
        sub_account_infos: List[main_models.ListSubAccountInfoResultSubAccountInfos] = None,
    ):
        self.sub_account_infos = sub_account_infos

    def validate(self):
        if self.sub_account_infos:
            for v1 in self.sub_account_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['subAccountInfos'] = []
        if self.sub_account_infos is not None:
            for k1 in self.sub_account_infos:
                result['subAccountInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_account_infos = []
        if m.get('subAccountInfos') is not None:
            for k1 in m.get('subAccountInfos'):
                temp_model = main_models.ListSubAccountInfoResultSubAccountInfos()
                self.sub_account_infos.append(temp_model.from_map(k1))

        return self

class ListSubAccountInfoResultSubAccountInfos(DaraModel):
    def __init__(
        self,
        account_name: str = None,
    ):
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['accountName'] = self.account_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')

        return self

