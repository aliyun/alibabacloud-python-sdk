# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class QueryReceiverByParamResponseBody(DaraModel):
    def __init__(
        self,
        next_start: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: main_models.QueryReceiverByParamResponseBodyData = None,
    ):
        # Used for pagination. If there are more results, set this returned value to the NextStart in the next request.
        self.next_start = next_start
        # Number of items displayed per page.
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Detailed information of the recipient list
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_start is not None:
            result['NextStart'] = self.next_start

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.QueryReceiverByParamResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class QueryReceiverByParamResponseBodyData(DaraModel):
    def __init__(
        self,
        receiver: List[main_models.QueryReceiverByParamResponseBodyDataReceiver] = None,
    ):
        self.receiver = receiver

    def validate(self):
        if self.receiver:
            for v1 in self.receiver:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['receiver'] = []
        if self.receiver is not None:
            for k1 in self.receiver:
                result['receiver'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.receiver = []
        if m.get('receiver') is not None:
            for k1 in m.get('receiver'):
                temp_model = main_models.QueryReceiverByParamResponseBodyDataReceiver()
                self.receiver.append(temp_model.from_map(k1))

        return self

class QueryReceiverByParamResponseBodyDataReceiver(DaraModel):
    def __init__(
        self,
        count: str = None,
        create_time: str = None,
        desc: str = None,
        receiver_id: str = None,
        receivers_alias: str = None,
        receivers_name: str = None,
        receivers_status: str = None,
        utc_create_time: int = None,
    ):
        # Total number of recipient addresses
        self.count = count
        # Creation time
        self.create_time = create_time
        # Description
        self.desc = desc
        # Recipient list ID
        self.receiver_id = receiver_id
        # Recipient list alias
        self.receivers_alias = receivers_alias
        # Recipient list name
        self.receivers_name = receivers_name
        # List status. Values:
        # 
        # - 0: Uploading
        # - 1: Upload completed
        self.receivers_status = receivers_status
        # UTC formatted creation time
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

        if self.receivers_alias is not None:
            result['ReceiversAlias'] = self.receivers_alias

        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name

        if self.receivers_status is not None:
            result['ReceiversStatus'] = self.receivers_status

        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        if m.get('ReceiversAlias') is not None:
            self.receivers_alias = m.get('ReceiversAlias')

        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')

        if m.get('ReceiversStatus') is not None:
            self.receivers_status = m.get('ReceiversStatus')

        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')

        return self

