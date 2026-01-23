# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubscriptionBillRequest(DaraModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        bill_format: str = None,
        bucket_owner_id: int = None,
        subscribe_bucket: str = None,
        subscribe_segment_size: int = None,
        subscribe_type: str = None,
    ):
        # The start month from which the bills are pushed. Specify the value in the yyyy-MM format.
        # 
        # After the subscription is generated, the system automatically pushes the bill data that is generated from the month that you specified to the current point in time. Data of up to six months can be pushed. The current month is included. If you subscribe to the bills for more than six months, the subscription is invalid.
        # 
        # This parameter is required.
        self.begin_billing_cycle = begin_billing_cycle
        # The file format of the bill. Valid values: csv and parquet.
        # 
        # If you subscribe to the bills of multiple file formats, we recommend that you store the bills in different OSS buckets to prevent file overwriting.
        # 
        # This parameter is required.
        self.bill_format = bill_format
        # The ID of the user to which the OSS bucket belongs.
        # 
        # If you are an eco-partner of Alibaba Cloud and you need to push the bills to the OSS bucket of a subordinate partner account, you must set this parameter to the ID of the subordinate partner account and grant the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission to the subordinate partner account.
        # 
        # If you are an eco-partner of Alibaba Cloud and you need to push the bills to the OSS bucket of your own account, your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        # 
        # This parameter is required.
        self.bucket_owner_id = bucket_owner_id
        # The name of the Object Storage Service (OSS) bucket in which you want to store the bills.
        # 
        # This parameter is required.
        self.subscribe_bucket = subscribe_bucket
        # The maximum rows in a single bill file. If the number of bill rows exceed the upper limit, the bill is automatically split into multiple files. The name of each split file is in the `uid_billType_billCycle_SquenceNo_fileNo` format.
        # 
        # Files whose names are the same except for the fileNo field are of the same type and belong to the same billing cycle.
        self.subscribe_segment_size = subscribe_segment_size
        # The type of the bill to which you want to subscribe. Valid values: PartnerBillingItemDetailForBillingPeriod, PartnerBillingItemDetailMonthly, PartnerInstanceDetailForBillingPeriod, and PartnerInstanceDetailMonthly.
        # 
        # This parameter is required.
        self.subscribe_type = subscribe_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle

        if self.bill_format is not None:
            result['BillFormat'] = self.bill_format

        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id

        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket

        if self.subscribe_segment_size is not None:
            result['SubscribeSegmentSize'] = self.subscribe_segment_size

        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')

        if m.get('BillFormat') is not None:
            self.bill_format = m.get('BillFormat')

        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')

        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')

        if m.get('SubscribeSegmentSize') is not None:
            self.subscribe_segment_size = m.get('SubscribeSegmentSize')

        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')

        return self

