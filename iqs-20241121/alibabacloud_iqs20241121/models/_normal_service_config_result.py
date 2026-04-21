# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241121 import models as main_models
from darabonba.model import DaraModel

class NormalServiceConfigResult(DaraModel):
    def __init__(
        self,
        available_time: str = None,
        gmt_create: str = None,
        status: str = None,
        user_apicount_infos: List[main_models.UserAPICountInfo] = None,
    ):
        self.available_time = available_time
        self.gmt_create = gmt_create
        self.status = status
        self.user_apicount_infos = user_apicount_infos

    def validate(self):
        if self.user_apicount_infos:
            for v1 in self.user_apicount_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_time is not None:
            result['availableTime'] = self.available_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.status is not None:
            result['status'] = self.status

        result['userAPICountInfos'] = []
        if self.user_apicount_infos is not None:
            for k1 in self.user_apicount_infos:
                result['userAPICountInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableTime') is not None:
            self.available_time = m.get('availableTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.user_apicount_infos = []
        if m.get('userAPICountInfos') is not None:
            for k1 in m.get('userAPICountInfos'):
                temp_model = main_models.UserAPICountInfo()
                self.user_apicount_infos.append(temp_model.from_map(k1))

        return self

