# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveCustomizeReportConfigRequest(DaraModel):
    def __init__(
        self,
        group_type: str = None,
        member_account_sync_flag: bool = None,
        pinned_time: int = None,
        recipients: str = None,
        report_days: int = None,
        report_end_date: str = None,
        report_id: int = None,
        report_lang: str = None,
        report_send_type: int = None,
        report_start_date: str = None,
        report_status: int = None,
        report_type: int = None,
        report_version: str = None,
        resource_directory_account_id: int = None,
        send_end_time: str = None,
        send_period_days: int = None,
        send_period_type: str = None,
        send_start_time: str = None,
        target_groups: str = None,
        target_uids: str = None,
        title: str = None,
    ):
        # The group type. Valid values:
        # - **ALIYUN_RG**: Alibaba Cloud resource group.
        # - **SAS_GROUP**: Security Center group.
        # > This parameter is supported only in version 2.0.0.
        self.group_type = group_type
        # Specifies whether newly added accounts are included by default. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        # > This parameter is supported only in version 2.0.0.
        self.member_account_sync_flag = member_account_sync_flag
        # The pinned time. Unit: milliseconds.
        # 
        # > This parameter is supported only in version 2.0.0.
        self.pinned_time = pinned_time
        # The email addresses of contacts. Separate multiple email addresses with commas (,).
        # 
        # This parameter is required.
        self.recipients = recipients
        # The number of recent days for report statistics.
        # > This parameter is supported only in version 2.0.0.
        self.report_days = report_days
        # The end date for report statistics. Format: yyyy-MM-dd.
        # > This parameter is required when ReportType is set to 3.
        self.report_end_date = report_end_date
        # The report ID.
        # >Call [DescribeCustomizeReportList](~~DescribeCustomizeReportList~~) to obtain this parameter.
        self.report_id = report_id
        # The language of the report. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.report_lang = report_lang
        # The report sending type. Valid values:
        # - **1**: 0:00 to 6:00.
        # - **2**: 6:00 to 12:00.
        # - **3**: 12:00 to 18:00.
        # - **4**: 18:00 to 24:00.
        self.report_send_type = report_send_type
        # The start date for report statistics. Format: yyyy-MM-dd.
        # > This parameter is required when ReportType is set to 3.
        self.report_start_date = report_start_date
        # The report status. Valid values:
        #  - **0**: disabled.
        #  - **1**: enabled.
        # 
        # This parameter is required.
        self.report_status = report_status
        # The report type. Valid values:
        # 
        # - **0**: daily report.
        # - **1**: weekly report.
        # - **2**: monthly report.
        # - **3**: custom period.
        # - **4**: latest period.
        # 
        # This parameter is required.
        self.report_type = report_type
        # The security report version. Valid values:
        # - **1.0.0**
        # - **2.0.0**
        self.report_version = report_version
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # >Invoke [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The send end time. Format: HH:mm:ss.
        # > This parameter is required when ReportType is set to 0, 1, 2, or 4.
        self.send_end_time = send_end_time
        # The specific execution dates within the send period.
        # > This parameter is supported only in version 2.0.0.
        self.send_period_days = send_period_days
        # The send period type. Valid values:
        # - **DAY**: day.
        # - **WEEK**: week.
        # - **MONTH**: month.
        # > This parameter is supported only in version 2.0.0.
        self.send_period_type = send_period_type
        # The send start time. Format: HH:mm:ss.
        # > This parameter is required when ReportType is set to 0, 1, 2, or 4.
        self.send_start_time = send_start_time
        # The targets within the group.
        # > This parameter is supported only in version 2.0.0.
        self.target_groups = target_groups
        # The list of target users. Separate multiple values with commas (,).
        # > This parameter is supported only in version 2.0.0.
        self.target_uids = target_uids
        # The report name.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.member_account_sync_flag is not None:
            result['MemberAccountSyncFlag'] = self.member_account_sync_flag

        if self.pinned_time is not None:
            result['PinnedTime'] = self.pinned_time

        if self.recipients is not None:
            result['Recipients'] = self.recipients

        if self.report_days is not None:
            result['ReportDays'] = self.report_days

        if self.report_end_date is not None:
            result['ReportEndDate'] = self.report_end_date

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_lang is not None:
            result['ReportLang'] = self.report_lang

        if self.report_send_type is not None:
            result['ReportSendType'] = self.report_send_type

        if self.report_start_date is not None:
            result['ReportStartDate'] = self.report_start_date

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.report_version is not None:
            result['ReportVersion'] = self.report_version

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.send_end_time is not None:
            result['SendEndTime'] = self.send_end_time

        if self.send_period_days is not None:
            result['SendPeriodDays'] = self.send_period_days

        if self.send_period_type is not None:
            result['SendPeriodType'] = self.send_period_type

        if self.send_start_time is not None:
            result['SendStartTime'] = self.send_start_time

        if self.target_groups is not None:
            result['TargetGroups'] = self.target_groups

        if self.target_uids is not None:
            result['TargetUids'] = self.target_uids

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('MemberAccountSyncFlag') is not None:
            self.member_account_sync_flag = m.get('MemberAccountSyncFlag')

        if m.get('PinnedTime') is not None:
            self.pinned_time = m.get('PinnedTime')

        if m.get('Recipients') is not None:
            self.recipients = m.get('Recipients')

        if m.get('ReportDays') is not None:
            self.report_days = m.get('ReportDays')

        if m.get('ReportEndDate') is not None:
            self.report_end_date = m.get('ReportEndDate')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportLang') is not None:
            self.report_lang = m.get('ReportLang')

        if m.get('ReportSendType') is not None:
            self.report_send_type = m.get('ReportSendType')

        if m.get('ReportStartDate') is not None:
            self.report_start_date = m.get('ReportStartDate')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('ReportVersion') is not None:
            self.report_version = m.get('ReportVersion')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SendEndTime') is not None:
            self.send_end_time = m.get('SendEndTime')

        if m.get('SendPeriodDays') is not None:
            self.send_period_days = m.get('SendPeriodDays')

        if m.get('SendPeriodType') is not None:
            self.send_period_type = m.get('SendPeriodType')

        if m.get('SendStartTime') is not None:
            self.send_start_time = m.get('SendStartTime')

        if m.get('TargetGroups') is not None:
            self.target_groups = m.get('TargetGroups')

        if m.get('TargetUids') is not None:
            self.target_uids = m.get('TargetUids')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

