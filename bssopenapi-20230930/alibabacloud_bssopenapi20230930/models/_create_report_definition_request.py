# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReportDefinitionRequest(DaraModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        include_members: str = None,
        mc_project: str = None,
        mc_table_name: str = None,
        nbid: str = None,
        not_send_on_no_data: str = None,
        oss_bucket_name: str = None,
        oss_bucket_owner_account_id: int = None,
        oss_bucket_path: str = None,
        report_source_type: str = None,
        report_type: str = None,
        send_with_attach: str = None,
        split_file_on_user_id: str = None,
    ):
        # The start billing cycle for push. After the subscription succeeds, the system automatically pushes data from the start billing cycle to the current time. This parameter is invalid for monthly bill PDF subscriptions, and historical data will not be re-pushed. You can push data within the last year.
        self.begin_billing_cycle = begin_billing_cycle
        # The email subscription configuration that specifies whether to include multi-account members of the organization in bills.
        self.include_members = include_members
        # The name of the MaxCompute project.
        self.mc_project = mc_project
        # The name of the MaxCompute subscription table.
        self.mc_table_name = mc_table_name
        # The first-level site ID. If this parameter is left empty, the site ID of the current user is used by default.
        self.nbid = nbid
        # The email subscription configuration that specifies whether to skip sending emails when no bills are available.
        self.not_send_on_no_data = not_send_on_no_data
        # The name of the OSS bucket for file storage.
        self.oss_bucket_name = oss_bucket_name
        # The UID of the OSS bucket owner that stores the files. If this is a Bid/Reseller subscription and you need to push data to a sub-account\\"s OSS, specify this parameter. The account must be a sub-account of the calling account, and the AliyunConsumeDump2OSSRole permission must be granted to this account. Regular users do not need to specify this parameter. The default value is the calling account.
        self.oss_bucket_owner_account_id = oss_bucket_owner_account_id
        # The storage path of the OSS bucket.
        self.oss_bucket_path = oss_bucket_path
        # The subscription source. Valid values: OSS, MC, and MSC_EMAIL.
        self.report_source_type = report_source_type
        # The subscription type. Valid values:
        # - consumeDetailBillV2: consumption details. This value is supported only by OSS/MC subscriptions.
        # - splitDetailBillV2: split details. This value is supported only by OSS/MC subscriptions.
        # - costDetailBillV2: cost details. This value is supported only by OSS/MC subscriptions.
        # - monthBillOverview: monthly bill overview. This value is supported only by OSS/MSC_EMAIL subscriptions.
        # - focus: FOCUS bill. This value is supported only by OSS/MC subscriptions.
        # 
        # This parameter is required.
        self.report_type = report_type
        # The email subscription configuration that specifies whether to send emails with bill attachments.
        self.send_with_attach = send_with_attach
        # The email subscription configuration that specifies whether to split attachments by user ID.
        self.split_file_on_user_id = split_file_on_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle

        if self.include_members is not None:
            result['IncludeMembers'] = self.include_members

        if self.mc_project is not None:
            result['McProject'] = self.mc_project

        if self.mc_table_name is not None:
            result['McTableName'] = self.mc_table_name

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.not_send_on_no_data is not None:
            result['NotSendOnNoData'] = self.not_send_on_no_data

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_bucket_owner_account_id is not None:
            result['OssBucketOwnerAccountId'] = self.oss_bucket_owner_account_id

        if self.oss_bucket_path is not None:
            result['OssBucketPath'] = self.oss_bucket_path

        if self.report_source_type is not None:
            result['ReportSourceType'] = self.report_source_type

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.send_with_attach is not None:
            result['SendWithAttach'] = self.send_with_attach

        if self.split_file_on_user_id is not None:
            result['SplitFileOnUserId'] = self.split_file_on_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')

        if m.get('IncludeMembers') is not None:
            self.include_members = m.get('IncludeMembers')

        if m.get('McProject') is not None:
            self.mc_project = m.get('McProject')

        if m.get('McTableName') is not None:
            self.mc_table_name = m.get('McTableName')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('NotSendOnNoData') is not None:
            self.not_send_on_no_data = m.get('NotSendOnNoData')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssBucketOwnerAccountId') is not None:
            self.oss_bucket_owner_account_id = m.get('OssBucketOwnerAccountId')

        if m.get('OssBucketPath') is not None:
            self.oss_bucket_path = m.get('OssBucketPath')

        if m.get('ReportSourceType') is not None:
            self.report_source_type = m.get('ReportSourceType')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('SendWithAttach') is not None:
            self.send_with_attach = m.get('SendWithAttach')

        if m.get('SplitFileOnUserId') is not None:
            self.split_file_on_user_id = m.get('SplitFileOnUserId')

        return self

