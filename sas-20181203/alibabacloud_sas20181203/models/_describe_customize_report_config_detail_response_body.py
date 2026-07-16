# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomizeReportConfigDetailResponseBody(DaraModel):
    def __init__(
        self,
        chart_ids: str = None,
        group_type: str = None,
        is_default: int = None,
        member_account_sync_flag: bool = None,
        pinned_time: int = None,
        recipients: str = None,
        report_days: int = None,
        report_end_date: str = None,
        report_id: int = None,
        report_lang: str = None,
        report_send_type: str = None,
        report_start_date: str = None,
        report_status: str = None,
        report_type: str = None,
        request_id: str = None,
        send_end_time: str = None,
        send_period_days: int = None,
        send_period_type: str = None,
        send_start_time: str = None,
        send_time: str = None,
        target_groups: str = None,
        target_uids: str = None,
        title: str = None,
    ):
        # The report chart configuration IDs, separated by commas.
        self.chart_ids = chart_ids
        # The group type. Valid values:
        # - **ALIYUN_RG**: ALIYUN_RG.
        # - **SAS_GROUP**: SAS_GROUP.
        self.group_type = group_type
        # Indicates whether the report is a default report. Valid values:
        # - **0**: Not a default report.
        # - **1**: A default report.
        self.is_default = is_default
        # Specifies whether newly added accounts are included by default. Valid values:
        # 
        # - **true**: Included.
        # - **false**: Not included.
        # > Only version 2.0.0 supports this parameter.
        self.member_account_sync_flag = member_account_sync_flag
        # The pinned time.
        self.pinned_time = pinned_time
        # The recipient email addresses, separated by commas.
        self.recipients = recipients
        # The number of recent days covered by the report statistics.
        self.report_days = report_days
        # The end date for report delivery.
        self.report_end_date = report_end_date
        # The report ID.
        self.report_id = report_id
        # The language type. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.report_lang = report_lang
        # The report delivery time range. Valid values:
        # - **1**: 0:00 to 6:00.
        # - **2**: 6:00 to 12:00.
        # - **3**: 12:00 to 18:00.
        # - **4**: 18:00 to 24:00.
        self.report_send_type = report_send_type
        # The start date for report delivery.
        self.report_start_date = report_start_date
        # The report status. Valid values:
        #  - **0**: Disabled.
        #  - **1**: Enabled.
        self.report_status = report_status
        # The report type. Valid values:
        # 
        # - **0**: Daily report.
        # - **1**: Weekly report.
        # - **2**: Monthly report.
        # - **3**: Custom period.
        self.report_type = report_type
        # The request ID.
        self.request_id = request_id
        # The delivery end time, in the format of HH:mm:ss.
        self.send_end_time = send_end_time
        # The specific execution dates within the delivery period.
        self.send_period_days = send_period_days
        # The delivery period type. Valid values:
        # - **DAY**: day.
        # - **WEEK**: week.
        # - **MONTH**: month.
        self.send_period_type = send_period_type
        # The delivery start time, in the format of HH:mm:ss.
        self.send_start_time = send_start_time
        # The delivery time, in the format of HH:mm:ss.
        self.send_time = send_time
        # The targets within the group.
        self.target_groups = target_groups
        # The list of target UIDs, separated by commas.
        self.target_uids = target_uids
        # The title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chart_ids is not None:
            result['ChartIds'] = self.chart_ids

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.send_end_time is not None:
            result['SendEndTime'] = self.send_end_time

        if self.send_period_days is not None:
            result['SendPeriodDays'] = self.send_period_days

        if self.send_period_type is not None:
            result['SendPeriodType'] = self.send_period_type

        if self.send_start_time is not None:
            result['SendStartTime'] = self.send_start_time

        if self.send_time is not None:
            result['SendTime'] = self.send_time

        if self.target_groups is not None:
            result['TargetGroups'] = self.target_groups

        if self.target_uids is not None:
            result['TargetUids'] = self.target_uids

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChartIds') is not None:
            self.chart_ids = m.get('ChartIds')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SendEndTime') is not None:
            self.send_end_time = m.get('SendEndTime')

        if m.get('SendPeriodDays') is not None:
            self.send_period_days = m.get('SendPeriodDays')

        if m.get('SendPeriodType') is not None:
            self.send_period_type = m.get('SendPeriodType')

        if m.get('SendStartTime') is not None:
            self.send_start_time = m.get('SendStartTime')

        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')

        if m.get('TargetGroups') is not None:
            self.target_groups = m.get('TargetGroups')

        if m.get('TargetUids') is not None:
            self.target_uids = m.get('TargetUids')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

