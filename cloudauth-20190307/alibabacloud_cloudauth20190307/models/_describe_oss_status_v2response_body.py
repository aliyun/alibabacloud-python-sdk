# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeOssStatusV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeOssStatusV2ResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Return code
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object
        # Whether the response was successful.
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeOssStatusV2ResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeOssStatusV2ResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        region: str = None,
        user_status: str = None,
    ):
        # Bucket name.
        self.bucket_name = bucket_name
        # Region.
        self.region = region
        # User activation status, **SUCCESS** indicates activated.
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.region is not None:
            result['Region'] = self.region

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

