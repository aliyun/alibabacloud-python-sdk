# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLakebaseS3AccountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_acc_ak: str = None,
        user_acc_policy: str = None,
        user_acc_sk: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The Access Key of the S3 account.
        self.user_acc_ak = user_acc_ak
        # The policy document of the S3 account.
        self.user_acc_policy = user_acc_policy
        # The Secret Key of the S3 account (masked).
        self.user_acc_sk = user_acc_sk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_acc_ak is not None:
            result['UserAccAk'] = self.user_acc_ak

        if self.user_acc_policy is not None:
            result['UserAccPolicy'] = self.user_acc_policy

        if self.user_acc_sk is not None:
            result['UserAccSk'] = self.user_acc_sk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserAccAk') is not None:
            self.user_acc_ak = m.get('UserAccAk')

        if m.get('UserAccPolicy') is not None:
            self.user_acc_policy = m.get('UserAccPolicy')

        if m.get('UserAccSk') is not None:
            self.user_acc_sk = m.get('UserAccSk')

        return self

