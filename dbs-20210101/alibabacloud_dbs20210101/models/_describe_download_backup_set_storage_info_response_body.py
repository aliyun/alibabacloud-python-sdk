# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dbs20210101 import models as main_models
from darabonba.model import DaraModel

class DescribeDownloadBackupSetStorageInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeDownloadBackupSetStorageInfoResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code returned if the request failed.
        self.code = code
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The error message returned if the request failed.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

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

        if m.get('Data') is not None:
            temp_model = main_models.DescribeDownloadBackupSetStorageInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDownloadBackupSetStorageInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        expiration_time: int = None,
        private_url: str = None,
        public_url: str = None,
    ):
        # The validity period of the URL.
        # 
        # > This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expiration_time = expiration_time
        # The private download URL of the backup set.
        self.private_url = private_url
        # The public download URL of the backup set.
        self.public_url = public_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.private_url is not None:
            result['PrivateUrl'] = self.private_url

        if self.public_url is not None:
            result['PublicUrl'] = self.public_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('PrivateUrl') is not None:
            self.private_url = m.get('PrivateUrl')

        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')

        return self

