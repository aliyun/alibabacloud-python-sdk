# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class CreateAccessKeyResponseBody(DaraModel):
    def __init__(
        self,
        access_key: main_models.CreateAccessKeyResponseBodyAccessKey = None,
        request_id: str = None,
    ):
        # The information about the AccessKey pair.
        self.access_key = access_key
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_key:
            self.access_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            temp_model = main_models.CreateAccessKeyResponseBodyAccessKey()
            self.access_key = temp_model.from_map(m.get('AccessKey'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAccessKeyResponseBodyAccessKey(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        create_date: str = None,
        status: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The AccessKey secret.
        self.access_key_secret = access_key_secret
        # The time when the AccessKey pair was created.
        self.create_date = create_date
        # The status of the AccessKey pair. Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

