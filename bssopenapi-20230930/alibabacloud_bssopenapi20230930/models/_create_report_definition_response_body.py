# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class CreateReportDefinitionResponseBody(DaraModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        metadata: Any = None,
        oss_bucket_name: str = None,
        oss_bucket_owner_account_id: int = None,
        oss_bucket_path: str = None,
        report_source_name: str = None,
        report_source_type: str = None,
        report_task_id: int = None,
        report_type: str = None,
        request_id: str = None,
        subscribe_create_time: str = None,
    ):
        # The start billing cycle for push. After the subscription succeeds, the system automatically pushes data from the start billing cycle to the current time. This parameter is invalid for monthly bill PDF subscriptions, and historical data will not be re-pushed. You can push data within the last year.
        self.begin_billing_cycle = begin_billing_cycle
        # The metadata of the response.
        self.metadata = metadata
        # The name of the OSS bucket for file storage.
        self.oss_bucket_name = oss_bucket_name
        # The UID of the OSS bucket owner that stores the files. If this is a Bid/Reseller subscription and you need to push data to a sub-account\\"s OSS, specify this parameter. The account must be a sub-account of the calling account, and the AliyunConsumeDump2OSSRole permission must be granted to this account. Regular users do not need to specify this parameter. The default value is the calling account.
        self.oss_bucket_owner_account_id = oss_bucket_owner_account_id
        # The storage path of the OSS bucket.
        self.oss_bucket_path = oss_bucket_path
        # The name of the subscription source.
        self.report_source_name = report_source_name
        # The subscription source. Valid values: OSS and MC.
        self.report_source_type = report_source_type
        # The ID of the billing subscription task.
        self.report_task_id = report_task_id
        # The subscription type. Valid values:
        # - consumeDetailBillV2: consumption details. This value is supported only by OSS/MC subscriptions.
        # - splitDetailBillV2: split details. This value is supported only by OSS/MC subscriptions.
        # - costDetailBillV2: cost details. This value is supported only by OSS/MC subscriptions.
        # - monthBillOverview: monthly bill overview. This value is supported only by OSS/MSC_EMAIL subscriptions.
        # - focus: FOCUS bill. This value is supported only by OSS/MC subscriptions.
        self.report_type = report_type
        # The request ID.
        self.request_id = request_id
        # The time when the subscription was created.
        self.subscribe_create_time = subscribe_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_bucket_owner_account_id is not None:
            result['OssBucketOwnerAccountId'] = self.oss_bucket_owner_account_id

        if self.oss_bucket_path is not None:
            result['OssBucketPath'] = self.oss_bucket_path

        if self.report_source_name is not None:
            result['ReportSourceName'] = self.report_source_name

        if self.report_source_type is not None:
            result['ReportSourceType'] = self.report_source_type

        if self.report_task_id is not None:
            result['ReportTaskId'] = self.report_task_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.subscribe_create_time is not None:
            result['SubscribeCreateTime'] = self.subscribe_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssBucketOwnerAccountId') is not None:
            self.oss_bucket_owner_account_id = m.get('OssBucketOwnerAccountId')

        if m.get('OssBucketPath') is not None:
            self.oss_bucket_path = m.get('OssBucketPath')

        if m.get('ReportSourceName') is not None:
            self.report_source_name = m.get('ReportSourceName')

        if m.get('ReportSourceType') is not None:
            self.report_source_type = m.get('ReportSourceType')

        if m.get('ReportTaskId') is not None:
            self.report_task_id = m.get('ReportTaskId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubscribeCreateTime') is not None:
            self.subscribe_create_time = m.get('SubscribeCreateTime')

        return self

