# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GrafanaWorkspaceAccount(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_notes: str = None,
        aliyun_uid: str = None,
        aliyun_user_name: str = None,
        gmt_create: float = None,
        orgs: List[main_models.GrafanaWorkspaceUserOrg] = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.account_notes = account_notes
        self.aliyun_uid = aliyun_uid
        self.aliyun_user_name = aliyun_user_name
        self.gmt_create = gmt_create
        self.orgs = orgs
        self.type = type

    def validate(self):
        if self.orgs:
            for v1 in self.orgs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.account_notes is not None:
            result['accountNotes'] = self.account_notes

        if self.aliyun_uid is not None:
            result['aliyunUid'] = self.aliyun_uid

        if self.aliyun_user_name is not None:
            result['aliyunUserName'] = self.aliyun_user_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        result['orgs'] = []
        if self.orgs is not None:
            for k1 in self.orgs:
                result['orgs'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('accountNotes') is not None:
            self.account_notes = m.get('accountNotes')

        if m.get('aliyunUid') is not None:
            self.aliyun_uid = m.get('aliyunUid')

        if m.get('aliyunUserName') is not None:
            self.aliyun_user_name = m.get('aliyunUserName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        self.orgs = []
        if m.get('orgs') is not None:
            for k1 in m.get('orgs'):
                temp_model = main_models.GrafanaWorkspaceUserOrg()
                self.orgs.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

