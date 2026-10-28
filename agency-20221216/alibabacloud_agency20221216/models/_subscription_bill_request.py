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
        # The billing month from which to start pushing bills. Format: yyyy-MM.
        # 
        # After a successful subscription, the system automatically pushes data from the start billing cycle to the current time. Data for up to the last six months (including the current month) can be pushed. If the specified month exceeds this range, the subscription is invalid.
        # 
        # This parameter is required.
        self.begin_billing_cycle = begin_billing_cycle
        # The bill file format. Valid values:
        # - csv
        # - parquet
        # 
        # If you subscribe to multiple file types, use separate buckets to avoid file overwriting.
        # 
        # This parameter is required.
        self.bill_format = bill_format
        # The UID of the account that owns the OSS bucket for storing files.
        # 
        # If a partner subscribes and needs to push files to the OSS bucket of a subordinate partner account, this account must be a subordinate partner account of the partner account. Grant the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission to the subordinate partner account. 
        # 
        # If a partner subscribes and pushes files to the partner account\\"s own OSS bucket, grant the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission to the partner account.
        # 
        # This parameter is required.
        self.bucket_owner_id = bucket_owner_id
        # The name of the OSS bucket for storing bill files.
        # 
        # This parameter is required.
        self.subscribe_bucket = subscribe_bucket
        # The row count threshold for a single bill file. If the number of rows exceeds this threshold, the file is automatically split into multiple files. The naming convention for split files is `uid_billType_billCycle_SquenceNo_fileNo`.
        # 
        # All information in the file names is identical except for fileNo. These files belong to the same billing cycle and the same file type but are split into multiple files.
        self.subscribe_segment_size = subscribe_segment_size
        # The subscription type. Valid values: 
        # - PartnerBillingItemDetailForBillingPeriod: billing item detail.
        # - PartnerBillingItemDetailMonthly: billing item monthly bill.
        # - PartnerInstanceDetailForBillingPeriod: instance bill detail.
        # - PartnerInstanceDetailMonthly: instance monthly bill.
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

