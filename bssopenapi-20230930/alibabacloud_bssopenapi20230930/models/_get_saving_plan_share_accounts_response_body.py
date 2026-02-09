# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class GetSavingPlanShareAccountsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetSavingPlanShareAccountsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetSavingPlanShareAccountsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSavingPlanShareAccountsResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        ali_uid: int = None,
        share_time_list: List[main_models.GetSavingPlanShareAccountsResponseBodyDataShareTimeList] = None,
    ):
        self.account_id = account_id
        self.ali_uid = ali_uid
        self.share_time_list = share_time_list

    def validate(self):
        if self.share_time_list:
            for v1 in self.share_time_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        result['ShareTimeList'] = []
        if self.share_time_list is not None:
            for k1 in self.share_time_list:
                result['ShareTimeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        self.share_time_list = []
        if m.get('ShareTimeList') is not None:
            for k1 in m.get('ShareTimeList'):
                temp_model = main_models.GetSavingPlanShareAccountsResponseBodyDataShareTimeList()
                self.share_time_list.append(temp_model.from_map(k1))

        return self

class GetSavingPlanShareAccountsResponseBodyDataShareTimeList(DaraModel):
    def __init__(
        self,
        share_end_time: str = None,
        share_start_time: str = None,
    ):
        self.share_end_time = share_end_time
        self.share_start_time = share_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.share_end_time is not None:
            result['ShareEndTime'] = self.share_end_time

        if self.share_start_time is not None:
            result['ShareStartTime'] = self.share_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShareEndTime') is not None:
            self.share_end_time = m.get('ShareEndTime')

        if m.get('ShareStartTime') is not None:
            self.share_start_time = m.get('ShareStartTime')

        return self

