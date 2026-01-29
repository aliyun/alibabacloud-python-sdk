# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubscribeBillToOSSRequest(DaraModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        bucket_owner_id: int = None,
        bucket_path: str = None,
        mult_account_rel_subscribe: str = None,
        row_limit_per_file: int = None,
        subscribe_bucket: str = None,
        subscribe_type: str = None,
        using_ssl: str = None,
    ):
        # The initial billing cycle from which bills start to be pushed. After you subscribe to the bills, the system automatically pushes the data that is generated from the initial billing cycle to the current time. If the SubscribeType parameter is set to MonthBill, this parameter is invalid. Historical data is not pushed again. The data generated within the last year can be pushed.
        self.begin_billing_cycle = begin_billing_cycle
        # The owner ID of the OSS bucket that stores the bills. This parameter is required if you are a bidder or reseller and want to push data to an OSS bucket of a member account. In this case, you must specify this account as the account used to call this operation and grant the AliyunConsumeDump2OSSRole permission to this account. If you are a regular user, you do not need to set this parameter. By default, your account is used to call this operation.
        self.bucket_owner_id = bucket_owner_id
        # The path of the OSS bucket.
        self.bucket_path = bucket_path
        # The type of the account whose bills are to be pushed if multi-tier accounts are involved. Valid values:
        # 
        # *   MA: the master account and a non-managed member account in Finance Cloud
        # *   ACP1: a member account of a virtual network operator (VNO)
        # 
        # Default value: MA.
        self.mult_account_rel_subscribe = mult_account_rel_subscribe
        # The upper limit of the number of lines in a single file. When the bill file exceeds the upper limit, it will be split into multiple files and merged into a compressed package.
        self.row_limit_per_file = row_limit_per_file
        # The OSS bucket that stores the bills to which you want to subscribe.
        # 
        # This parameter is required.
        self.subscribe_bucket = subscribe_bucket
        # The type of the bill to which you want to subscribe. Valid values:
        # 
        # *   BillingItemDetailForBillingPeriod: detailed bills of billable items
        # *   InstanceDetailForBillingPeriod: detailed bills of instances
        # *   BillingItemDetailMonthly: billable item-based bills summarized by billing cycle
        # *   InstanceDetailMonthly: instance-based bills summarized by billing cycle
        # *   SplitItemDetailDaily: split bills summarized by day
        # *   MonthBill: monthly bills in the PDF format. You can subscribe to the monthly PDF bills only of the master account.
        self.subscribe_type = subscribe_type
        # Whether to protect network communications through the SSL (Secure Sockets Layer) encryption protocol. When this parameter is set to true, it means that SSL encryption is enabled to ensure the security and integrity of data transmission.
        self.using_ssl = using_ssl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle

        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id

        if self.bucket_path is not None:
            result['BucketPath'] = self.bucket_path

        if self.mult_account_rel_subscribe is not None:
            result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe

        if self.row_limit_per_file is not None:
            result['RowLimitPerFile'] = self.row_limit_per_file

        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket

        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type

        if self.using_ssl is not None:
            result['UsingSsl'] = self.using_ssl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')

        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')

        if m.get('BucketPath') is not None:
            self.bucket_path = m.get('BucketPath')

        if m.get('MultAccountRelSubscribe') is not None:
            self.mult_account_rel_subscribe = m.get('MultAccountRelSubscribe')

        if m.get('RowLimitPerFile') is not None:
            self.row_limit_per_file = m.get('RowLimitPerFile')

        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')

        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')

        if m.get('UsingSsl') is not None:
            self.using_ssl = m.get('UsingSsl')

        return self

