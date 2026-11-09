# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class BatchQuerySessionByClientIdsResponseBody(DaraModel):
    def __init__(
        self,
        online_status_list: List[main_models.BatchQuerySessionByClientIdsResponseBodyOnlineStatusList] = None,
        request_id: str = None,
    ):
        # The list of client statuses.
        self.online_status_list = online_status_list
        # The request ID. It is unique for each request.
        self.request_id = request_id

    def validate(self):
        if self.online_status_list:
            for v1 in self.online_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OnlineStatusList'] = []
        if self.online_status_list is not None:
            for k1 in self.online_status_list:
                result['OnlineStatusList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.online_status_list = []
        if m.get('OnlineStatusList') is not None:
            for k1 in m.get('OnlineStatusList'):
                temp_model = main_models.BatchQuerySessionByClientIdsResponseBodyOnlineStatusList()
                self.online_status_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class BatchQuerySessionByClientIdsResponseBodyOnlineStatusList(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        online_status: bool = None,
    ):
        # The client ID of the client. For more information about client IDs, see [Glossary](https://help.aliyun.com/document_detail/42420.html).
        self.client_id = client_id
        # Indicates whether the device is online. Valid values:
        # 
        # - **true**: Online.
        # - **false**: Offline.
        self.online_status = online_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        return self

