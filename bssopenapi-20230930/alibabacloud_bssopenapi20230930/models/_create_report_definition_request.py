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
        self.begin_billing_cycle = begin_billing_cycle
        self.include_members = include_members
        self.mc_project = mc_project
        self.mc_table_name = mc_table_name
        self.nbid = nbid
        self.not_send_on_no_data = not_send_on_no_data
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_owner_account_id = oss_bucket_owner_account_id
        self.oss_bucket_path = oss_bucket_path
        self.report_source_type = report_source_type
        # This parameter is required.
        self.report_type = report_type
        self.send_with_attach = send_with_attach
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

