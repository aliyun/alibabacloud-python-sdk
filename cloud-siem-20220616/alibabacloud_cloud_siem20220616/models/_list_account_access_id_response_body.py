# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListAccountAccessIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListAccountAccessIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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

        if self.message is not None:
            result['Message'] = self.message

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
                temp_model = main_models.ListAccountAccessIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAccountAccessIdResponseBodyData(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        access_id_md_5: str = None,
        account_id: str = None,
        account_str: str = None,
        bound: int = None,
        cloud_code: str = None,
        sub_user_id: int = None,
    ):
        # The AccessKey ID of the cloud account that is added to the threat analysis feature.
        self.access_id = access_id
        # The MD5 hash value of the AccessKey ID.
        self.access_id_md_5 = access_id_md_5
        # The ID of the cloud account.
        self.account_id = account_id
        # The information about the cloud account to which the AccessKey ID belongs. The value is in the following format: Alibaba Cloud account ID|Alibaba Cloud account username|AccessKey ID.
        self.account_str = account_str
        # Indicates whether the cloud account to which the AccessKey ID belongs is added to the threat analysis feature. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.bound = bound
        # The code of the cloud service provider.
        self.cloud_code = cloud_code
        # The ID of the Alibaba Cloud account that is used to add the third-party cloud account.
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.access_id_md_5 is not None:
            result['AccessIdMd5'] = self.access_id_md_5

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_str is not None:
            result['AccountStr'] = self.account_str

        if self.bound is not None:
            result['Bound'] = self.bound

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('AccessIdMd5') is not None:
            self.access_id_md_5 = m.get('AccessIdMd5')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountStr') is not None:
            self.account_str = m.get('AccountStr')

        if m.get('Bound') is not None:
            self.bound = m.get('Bound')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

