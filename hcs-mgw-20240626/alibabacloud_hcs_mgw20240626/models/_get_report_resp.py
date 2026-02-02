# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetReportResp(DaraModel):
    def __init__(
        self,
        copied_count: int = None,
        error_message: str = None,
        failed_count: int = None,
        failed_list_prefix: str = None,
        job_create_time: str = None,
        job_end_time: str = None,
        job_execute_time: str = None,
        report_create_time: str = None,
        report_end_time: str = None,
        skipped_count: int = None,
        skipped_list_prefix: str = None,
        status: str = None,
        total_count: int = None,
        total_list_prefix: str = None,
    ):
        self.copied_count = copied_count
        self.error_message = error_message
        self.failed_count = failed_count
        self.failed_list_prefix = failed_list_prefix
        self.job_create_time = job_create_time
        self.job_end_time = job_end_time
        self.job_execute_time = job_execute_time
        self.report_create_time = report_create_time
        self.report_end_time = report_end_time
        self.skipped_count = skipped_count
        self.skipped_list_prefix = skipped_list_prefix
        self.status = status
        self.total_count = total_count
        self.total_list_prefix = total_list_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copied_count is not None:
            result['CopiedCount'] = self.copied_count

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.failed_list_prefix is not None:
            result['FailedListPrefix'] = self.failed_list_prefix

        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time

        if self.job_end_time is not None:
            result['JobEndTime'] = self.job_end_time

        if self.job_execute_time is not None:
            result['JobExecuteTime'] = self.job_execute_time

        if self.report_create_time is not None:
            result['ReportCreateTime'] = self.report_create_time

        if self.report_end_time is not None:
            result['ReportEndTime'] = self.report_end_time

        if self.skipped_count is not None:
            result['SkippedCount'] = self.skipped_count

        if self.skipped_list_prefix is not None:
            result['SkippedListPrefix'] = self.skipped_list_prefix

        if self.status is not None:
            result['Status'] = self.status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_list_prefix is not None:
            result['TotalListPrefix'] = self.total_list_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopiedCount') is not None:
            self.copied_count = m.get('CopiedCount')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('FailedListPrefix') is not None:
            self.failed_list_prefix = m.get('FailedListPrefix')

        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')

        if m.get('JobEndTime') is not None:
            self.job_end_time = m.get('JobEndTime')

        if m.get('JobExecuteTime') is not None:
            self.job_execute_time = m.get('JobExecuteTime')

        if m.get('ReportCreateTime') is not None:
            self.report_create_time = m.get('ReportCreateTime')

        if m.get('ReportEndTime') is not None:
            self.report_end_time = m.get('ReportEndTime')

        if m.get('SkippedCount') is not None:
            self.skipped_count = m.get('SkippedCount')

        if m.get('SkippedListPrefix') is not None:
            self.skipped_list_prefix = m.get('SkippedListPrefix')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalListPrefix') is not None:
            self.total_list_prefix = m.get('TotalListPrefix')

        return self

