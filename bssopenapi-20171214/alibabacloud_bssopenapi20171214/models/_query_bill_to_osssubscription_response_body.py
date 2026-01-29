# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryBillToOSSSubscriptionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryBillToOSSSubscriptionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.QueryBillToOSSSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryBillToOSSSubscriptionResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        items: main_models.QueryBillToOSSSubscriptionResponseBodyDataItems = None,
    ):
        # The ID of the account used to perform the query.
        self.account_id = account_id
        # The name of the account used to perform the query.
        self.account_name = account_name
        # The details of the subscribed bill.
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountID'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.items is not None:
            result['Items'] = self.items.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Items') is not None:
            temp_model = main_models.QueryBillToOSSSubscriptionResponseBodyDataItems()
            self.items = temp_model.from_map(m.get('Items'))

        return self

class QueryBillToOSSSubscriptionResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.QueryBillToOSSSubscriptionResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.QueryBillToOSSSubscriptionResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class QueryBillToOSSSubscriptionResponseBodyDataItemsItem(DaraModel):
    def __init__(
        self,
        bucket_owner_id: int = None,
        bucket_path: str = None,
        row_limit_per_file: int = None,
        subscribe_bucket: str = None,
        subscribe_language: str = None,
        subscribe_time: str = None,
        subscribe_type: str = None,
    ):
        # The owner ID of the Object Storage Service (OSS) bucket.
        self.bucket_owner_id = bucket_owner_id
        # The path in the OSS bucket.
        self.bucket_path = bucket_path
        # The maximum number of data rows in a single file. If the number of data rows in a bill exceeds the upper limit, the bill is split into multiple files. Then, multiple files are merged and compressed into a package.
        self.row_limit_per_file = row_limit_per_file
        # The ID of the OSS bucket that stores the subscribed bill.
        self.subscribe_bucket = subscribe_bucket
        # The code of the language.
        # 
        # Valid values:
        # 
        # *   en: English
        # *   zh: Chinese
        self.subscribe_language = subscribe_language
        # The time when the subscribed bill was stored in the OSS bucket. The time is displayed in the YYYY-MM-DD hh:mm:ss format.
        self.subscribe_time = subscribe_time
        # The type of the subscribed bill. Valid values:
        # 
        # *   BillingItemDetailForBillingPeriod: the bill of a billable item.
        # *   InstanceDetailForBillingPeriod: the bill of an instance.
        self.subscribe_type = subscribe_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id

        if self.bucket_path is not None:
            result['BucketPath'] = self.bucket_path

        if self.row_limit_per_file is not None:
            result['RowLimitPerFile'] = self.row_limit_per_file

        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket

        if self.subscribe_language is not None:
            result['SubscribeLanguage'] = self.subscribe_language

        if self.subscribe_time is not None:
            result['SubscribeTime'] = self.subscribe_time

        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')

        if m.get('BucketPath') is not None:
            self.bucket_path = m.get('BucketPath')

        if m.get('RowLimitPerFile') is not None:
            self.row_limit_per_file = m.get('RowLimitPerFile')

        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')

        if m.get('SubscribeLanguage') is not None:
            self.subscribe_language = m.get('SubscribeLanguage')

        if m.get('SubscribeTime') is not None:
            self.subscribe_time = m.get('SubscribeTime')

        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')

        return self

