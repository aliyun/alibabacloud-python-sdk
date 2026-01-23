# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetInviteStatusRequest(DaraModel):
    def __init__(
        self,
        invite_status_list: List[main_models.GetInviteStatusRequestInviteStatusList] = None,
    ):
        # inviteId list</br>
        # `Sub-levels <= 5`
        # 
        # This parameter is required.
        self.invite_status_list = invite_status_list

    def validate(self):
        if self.invite_status_list:
            for v1 in self.invite_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InviteStatusList'] = []
        if self.invite_status_list is not None:
            for k1 in self.invite_status_list:
                result['InviteStatusList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invite_status_list = []
        if m.get('InviteStatusList') is not None:
            for k1 in m.get('InviteStatusList'):
                temp_model = main_models.GetInviteStatusRequestInviteStatusList()
                self.invite_status_list.append(temp_model.from_map(k1))

        return self

class GetInviteStatusRequestInviteStatusList(DaraModel):
    def __init__(
        self,
        invite_id: int = None,
    ):
        # Invitation ID, From interface InviteSubAccount
        self.invite_id = invite_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')

        return self

