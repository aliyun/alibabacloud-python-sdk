# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeTraceDiagnoseReportResponseBody(DaraModel):
    def __init__(
        self,
        client_addr: str = None,
        client_info: main_models.DescribeTraceDiagnoseReportResponseBodyClientInfo = None,
        client_ip: str = None,
        create_time: str = None,
        diagnose_id: str = None,
        diagnose_report_link: str = None,
        diagnose_url: str = None,
        domain: str = None,
        expire_time: int = None,
        remain_diagnose_times: int = None,
        report: main_models.DescribeTraceDiagnoseReportResponseBodyReport = None,
        request_id: str = None,
        state: str = None,
        status: int = None,
        task_id: str = None,
        time_consuming: int = None,
        trace_display_link: str = None,
        trace_id: str = None,
    ):
        # IP address of the local DNS server.
        self.client_addr = client_addr
        # Client information.
        self.client_info = client_info
        # Client IP.
        self.client_ip = client_ip
        # Creation time. Format: yyyy-MM-dd HH:mm:ss. Time zone: +08:00.
        self.create_time = create_time
        # Diagnostic ID.
        self.diagnose_id = diagnose_id
        # Diagnostic report link.
        self.diagnose_report_link = diagnose_report_link
        # Diagnostic link.
        self.diagnose_url = diagnose_url
        # The diagnosed domain name.
        self.domain = domain
        # Expiration time. Timestamp in seconds.
        self.expire_time = expire_time
        # Remaining available diagnostic attempts.
        self.remain_diagnose_times = remain_diagnose_times
        # Diagnostic report details.
        self.report = report
        # ID of the request
        self.request_id = request_id
        # Report generation status.
        # 
        # 0: Successful.
        # 1: Failed.
        # 2: Timed out.
        # 3: Running.
        # 4: Waiting.
        self.state = state
        # Status of the diagnostic link.
        # 
        # 1: Active.
        # 0: Expired.
        self.status = status
        # Task ID.
        self.task_id = task_id
        # Time consumed for report generation, in seconds.
        self.time_consuming = time_consuming
        # Trace display link.
        self.trace_display_link = trace_display_link
        # Diagnostic trace ID.
        self.trace_id = trace_id

    def validate(self):
        if self.client_info:
            self.client_info.validate()
        if self.report:
            self.report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr

        if self.client_info is not None:
            result['ClientInfo'] = self.client_info.to_map()

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        if self.diagnose_report_link is not None:
            result['DiagnoseReportLink'] = self.diagnose_report_link

        if self.diagnose_url is not None:
            result['DiagnoseUrl'] = self.diagnose_url

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.remain_diagnose_times is not None:
            result['RemainDiagnoseTimes'] = self.remain_diagnose_times

        if self.report is not None:
            result['Report'] = self.report.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.time_consuming is not None:
            result['TimeConsuming'] = self.time_consuming

        if self.trace_display_link is not None:
            result['TraceDisplayLink'] = self.trace_display_link

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')

        if m.get('ClientInfo') is not None:
            temp_model = main_models.DescribeTraceDiagnoseReportResponseBodyClientInfo()
            self.client_info = temp_model.from_map(m.get('ClientInfo'))

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        if m.get('DiagnoseReportLink') is not None:
            self.diagnose_report_link = m.get('DiagnoseReportLink')

        if m.get('DiagnoseUrl') is not None:
            self.diagnose_url = m.get('DiagnoseUrl')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RemainDiagnoseTimes') is not None:
            self.remain_diagnose_times = m.get('RemainDiagnoseTimes')

        if m.get('Report') is not None:
            temp_model = main_models.DescribeTraceDiagnoseReportResponseBodyReport()
            self.report = temp_model.from_map(m.get('Report'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TimeConsuming') is not None:
            self.time_consuming = m.get('TimeConsuming')

        if m.get('TraceDisplayLink') is not None:
            self.trace_display_link = m.get('TraceDisplayLink')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeTraceDiagnoseReportResponseBodyReport(DaraModel):
    def __init__(
        self,
        client_info: str = None,
        diagnose_result: str = None,
        response_header: str = None,
        static_html: str = None,
    ):
        # Client information.
        self.client_info = client_info
        # Diagnostic result.
        self.diagnose_result = diagnose_result
        # Client request response header.
        self.response_header = response_header
        # Static snapshot page.
        self.static_html = static_html

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info

        if self.diagnose_result is not None:
            result['DiagnoseResult'] = self.diagnose_result

        if self.response_header is not None:
            result['ResponseHeader'] = self.response_header

        if self.static_html is not None:
            result['StaticHtml'] = self.static_html

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')

        if m.get('DiagnoseResult') is not None:
            self.diagnose_result = m.get('DiagnoseResult')

        if m.get('ResponseHeader') is not None:
            self.response_header = m.get('ResponseHeader')

        if m.get('StaticHtml') is not None:
            self.static_html = m.get('StaticHtml')

        return self

class DescribeTraceDiagnoseReportResponseBodyClientInfo(DaraModel):
    def __init__(
        self,
        browser_info: str = None,
        os: str = None,
        ua_string: str = None,
    ):
        # Browser.
        self.browser_info = browser_info
        # Operating system name.
        self.os = os
        # Version.
        self.ua_string = ua_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_info is not None:
            result['BrowserInfo'] = self.browser_info

        if self.os is not None:
            result['Os'] = self.os

        if self.ua_string is not None:
            result['UaString'] = self.ua_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserInfo') is not None:
            self.browser_info = m.get('BrowserInfo')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('UaString') is not None:
            self.ua_string = m.get('UaString')

        return self

