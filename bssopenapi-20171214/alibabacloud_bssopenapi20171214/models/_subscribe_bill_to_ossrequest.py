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
        # The start billing cycle for pushing. After a successful subscription, the system automatically pushes data from the start billing cycle to the current time. This parameter is invalid for monthly bill PDF subscriptions, and historical data is not re-pushed. Data within the last year can be pushed.
        self.begin_billing_cycle = begin_billing_cycle
        # The UID of the OSS owner that stores the files. Specify this parameter if you are a Bid/Reseller subscriber and need to push files to a sub-account\\"s OSS. The specified account must be a sub-account of the calling account, and the AliyunConsumeDump2OSSRole permission must be granted to this account. Regular users do not need to specify this parameter. The default value is the calling account.
        self.bucket_owner_id = bucket_owner_id
        # The specified directory under the bucket to which the subscription is delivered.
        self.bucket_path = bucket_path
        # For multi-level accounts, specifies the type of bills to push. Valid values:
        # - MA: Pushes bills for the primary account and non-trusteeship linked accounts in the financial cloud.
        # - ACP1: Pushes bills for Partner Platform V2.0 sub-accounts.
        # 
        # Default value: MA.
        self.mult_account_rel_subscribe = mult_account_rel_subscribe
        # The maximum number of rows per file. If a bill file exceeds this limit, it is split into multiple files and compressed into a single archive.
        self.row_limit_per_file = row_limit_per_file
        # The name of the OSS bucket that stores the subscribed bill files.
        # 
        # This parameter is required.
        self.subscribe_bucket = subscribe_bucket
        # The type of the subscribed bill. Valid values:
        # - BillingItemDetailForBillingPeriod: billing item details.
        # - InstanceDetailForBillingPeriod: instance bill details.
        # - BillingItemDetailMonthly: billing item summary by billing cycle.
        # - InstanceDetailMonthly: instance bill summary by billing cycle.
        # - SplitItemDetailDaily: split bill daily summary.
        # - MonthBill: monthly bill PDF. Only MA subscription is supported.
        self.subscribe_type = subscribe_type
        # Specifies whether to use the Secure Sockets Layer (SSL) encryption protocol to protect network communication. Valid values:
        # 
        # - true: Enables SSL encryption to ensure the security and integrity of data transmission.
        # 
        # - false (default): Does not enable SSL encryption.
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

