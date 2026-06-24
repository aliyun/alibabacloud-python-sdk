# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListOpenSourcePermissionsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListOpenSourcePermissionsResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code. A value of 200 indicates success.
        self.code = code
        # The returned data.
        self.data = data
        # The maximum number of results to return.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # The token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListOpenSourcePermissionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListOpenSourcePermissionsResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_user_id: int = None,
        cinstance_id: str = None,
        configure: str = None,
        name: str = None,
        read: str = None,
        vhost: str = None,
        write: str = None,
    ):
        # The Alibaba Cloud UID.
        self.aliyun_user_id = aliyun_user_id
        # The instance ID.
        self.cinstance_id = cinstance_id
        # The regular expression for configure permissions.
        self.configure = configure
        # The username.
        self.name = name
        # The regular expression for read permissions.
        self.read = read
        # The vhost name.
        self.vhost = vhost
        # The regular expression for write permissions.
        self.write = write

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_user_id is not None:
            result['AliyunUserId'] = self.aliyun_user_id

        if self.cinstance_id is not None:
            result['CInstanceId'] = self.cinstance_id

        if self.configure is not None:
            result['Configure'] = self.configure

        if self.name is not None:
            result['Name'] = self.name

        if self.read is not None:
            result['Read'] = self.read

        if self.vhost is not None:
            result['Vhost'] = self.vhost

        if self.write is not None:
            result['Write'] = self.write

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUserId') is not None:
            self.aliyun_user_id = m.get('AliyunUserId')

        if m.get('CInstanceId') is not None:
            self.cinstance_id = m.get('CInstanceId')

        if m.get('Configure') is not None:
            self.configure = m.get('Configure')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Read') is not None:
            self.read = m.get('Read')

        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')

        if m.get('Write') is not None:
            self.write = m.get('Write')

        return self

