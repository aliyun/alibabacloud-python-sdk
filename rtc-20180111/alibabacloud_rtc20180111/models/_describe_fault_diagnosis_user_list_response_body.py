# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeFaultDiagnosisUserListResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
        user_list: List[main_models.DescribeFaultDiagnosisUserListResponseBodyUserList] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_cnt = total_cnt
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for v1 in self.user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.DescribeFaultDiagnosisUserListResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class DescribeFaultDiagnosisUserListResponseBodyUserList(DaraModel):
    def __init__(
        self,
        channel_created_ts: int = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        fault_list: List[main_models.DescribeFaultDiagnosisUserListResponseBodyUserListFaultList] = None,
        user_id: str = None,
    ):
        self.channel_created_ts = channel_created_ts
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.fault_list = fault_list
        self.user_id = user_id

    def validate(self):
        if self.fault_list:
            for v1 in self.fault_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_created_ts is not None:
            result['ChannelCreatedTs'] = self.channel_created_ts

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts

        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts

        result['FaultList'] = []
        if self.fault_list is not None:
            for k1 in self.fault_list:
                result['FaultList'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCreatedTs') is not None:
            self.channel_created_ts = m.get('ChannelCreatedTs')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')

        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')

        self.fault_list = []
        if m.get('FaultList') is not None:
            for k1 in m.get('FaultList'):
                temp_model = main_models.DescribeFaultDiagnosisUserListResponseBodyUserListFaultList()
                self.fault_list.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeFaultDiagnosisUserListResponseBodyUserListFaultList(DaraModel):
    def __init__(
        self,
        fault_type: str = None,
    ):
        self.fault_type = fault_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')

        return self

