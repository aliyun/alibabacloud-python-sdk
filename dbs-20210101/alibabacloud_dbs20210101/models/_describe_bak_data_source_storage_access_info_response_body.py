# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dbs20210101 import models as main_models
from darabonba.model import DaraModel

class DescribeBakDataSourceStorageAccessInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeBakDataSourceStorageAccessInfoResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.DescribeBakDataSourceStorageAccessInfoResponseBodyData()
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

class DescribeBakDataSourceStorageAccessInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        oss_access_info: main_models.DescribeBakDataSourceStorageAccessInfoResponseBodyDataOssAccessInfo = None,
        storage_type: str = None,
    ):
        self.oss_access_info = oss_access_info
        self.storage_type = storage_type

    def validate(self):
        if self.oss_access_info:
            self.oss_access_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_access_info is not None:
            result['OssAccessInfo'] = self.oss_access_info.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssAccessInfo') is not None:
            temp_model = main_models.DescribeBakDataSourceStorageAccessInfoResponseBodyDataOssAccessInfo()
            self.oss_access_info = temp_model.from_map(m.get('OssAccessInfo'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeBakDataSourceStorageAccessInfoResponseBodyDataOssAccessInfo(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        expired_time: str = None,
        object_key: str = None,
        oss_endpoint: str = None,
        oss_internal_endpoint: str = None,
        oss_region: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.bucket_name = bucket_name
        self.expired_time = expired_time
        self.object_key = object_key
        self.oss_endpoint = oss_endpoint
        self.oss_internal_endpoint = oss_internal_endpoint
        self.oss_region = oss_region
        self.security_token = security_token

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

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_internal_endpoint is not None:
            result['OssInternalEndpoint'] = self.oss_internal_endpoint

        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssInternalEndpoint') is not None:
            self.oss_internal_endpoint = m.get('OssInternalEndpoint')

        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

