# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnDiagnoseReportResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeCdnDiagnoseReportResponseBodyContent = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.DescribeCdnDiagnoseReportResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnDiagnoseReportResponseBodyContent(DaraModel):
    def __init__(
        self,
        aliuid: str = None,
        client_addr: str = None,
        client_info: main_models.DescribeCdnDiagnoseReportResponseBodyContentClientInfo = None,
        client_ip: str = None,
        create_time: str = None,
        diagnose_id: str = None,
        diagnose_report_link: str = None,
        diagnose_url: str = None,
        domain: str = None,
        expire_time: int = None,
        remain_diagnose_times: int = None,
        report: main_models.DescribeCdnDiagnoseReportResponseBodyContentReport = None,
        state: str = None,
        status: int = None,
        task_id: str = None,
        time_consuming: int = None,
        trace_display_link: str = None,
        trace_id: str = None,
    ):
        self.aliuid = aliuid
        self.client_addr = client_addr
        self.client_info = client_info
        self.client_ip = client_ip
        self.create_time = create_time
        self.diagnose_id = diagnose_id
        self.diagnose_report_link = diagnose_report_link
        self.diagnose_url = diagnose_url
        self.domain = domain
        self.expire_time = expire_time
        self.remain_diagnose_times = remain_diagnose_times
        self.report = report
        self.state = state
        self.status = status
        self.task_id = task_id
        self.time_consuming = time_consuming
        self.trace_display_link = trace_display_link
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
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

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
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')

        if m.get('ClientInfo') is not None:
            temp_model = main_models.DescribeCdnDiagnoseReportResponseBodyContentClientInfo()
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
            temp_model = main_models.DescribeCdnDiagnoseReportResponseBodyContentReport()
            self.report = temp_model.from_map(m.get('Report'))

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

class DescribeCdnDiagnoseReportResponseBodyContentReport(DaraModel):
    def __init__(
        self,
        client_info: str = None,
        diagnose_result: str = None,
        l_1node: str = None,
        l_1tengine: main_models.DescribeCdnDiagnoseReportResponseBodyContentReportL1Tengine = None,
        source_info: List[str] = None,
    ):
        self.client_info = client_info
        self.diagnose_result = diagnose_result
        self.l_1node = l_1node
        self.l_1tengine = l_1tengine
        self.source_info = source_info

    def validate(self):
        if self.l_1tengine:
            self.l_1tengine.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_info is not None:
            result['ClientInfo'] = self.client_info

        if self.diagnose_result is not None:
            result['DiagnoseResult'] = self.diagnose_result

        if self.l_1node is not None:
            result['L1Node'] = self.l_1node

        if self.l_1tengine is not None:
            result['L1Tengine'] = self.l_1tengine.to_map()

        if self.source_info is not None:
            result['SourceInfo'] = self.source_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')

        if m.get('DiagnoseResult') is not None:
            self.diagnose_result = m.get('DiagnoseResult')

        if m.get('L1Node') is not None:
            self.l_1node = m.get('L1Node')

        if m.get('L1Tengine') is not None:
            temp_model = main_models.DescribeCdnDiagnoseReportResponseBodyContentReportL1Tengine()
            self.l_1tengine = temp_model.from_map(m.get('L1Tengine'))

        if m.get('SourceInfo') is not None:
            self.source_info = m.get('SourceInfo')

        return self

class DescribeCdnDiagnoseReportResponseBodyContentReportL1Tengine(DaraModel):
    def __init__(
        self,
        addr: str = None,
        code: str = None,
        error_log: str = None,
        fbt: str = None,
        intro: str = None,
        req_header: str = None,
        req_time: str = None,
        resp_header: str = None,
        resp_size: int = None,
        rt: str = None,
        station: str = None,
    ):
        self.addr = addr
        self.code = code
        self.error_log = error_log
        self.fbt = fbt
        self.intro = intro
        self.req_header = req_header
        self.req_time = req_time
        self.resp_header = resp_header
        self.resp_size = resp_size
        self.rt = rt
        self.station = station

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr

        if self.code is not None:
            result['Code'] = self.code

        if self.error_log is not None:
            result['ErrorLog'] = self.error_log

        if self.fbt is not None:
            result['Fbt'] = self.fbt

        if self.intro is not None:
            result['Intro'] = self.intro

        if self.req_header is not None:
            result['ReqHeader'] = self.req_header

        if self.req_time is not None:
            result['ReqTime'] = self.req_time

        if self.resp_header is not None:
            result['RespHeader'] = self.resp_header

        if self.resp_size is not None:
            result['RespSize'] = self.resp_size

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.station is not None:
            result['Station'] = self.station

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorLog') is not None:
            self.error_log = m.get('ErrorLog')

        if m.get('Fbt') is not None:
            self.fbt = m.get('Fbt')

        if m.get('Intro') is not None:
            self.intro = m.get('Intro')

        if m.get('ReqHeader') is not None:
            self.req_header = m.get('ReqHeader')

        if m.get('ReqTime') is not None:
            self.req_time = m.get('ReqTime')

        if m.get('RespHeader') is not None:
            self.resp_header = m.get('RespHeader')

        if m.get('RespSize') is not None:
            self.resp_size = m.get('RespSize')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('Station') is not None:
            self.station = m.get('Station')

        return self

class DescribeCdnDiagnoseReportResponseBodyContentClientInfo(DaraModel):
    def __init__(
        self,
        browser_info: str = None,
        os: str = None,
        uastring: str = None,
    ):
        self.browser_info = browser_info
        self.os = os
        self.uastring = uastring

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

        if self.uastring is not None:
            result['UAString'] = self.uastring

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserInfo') is not None:
            self.browser_info = m.get('BrowserInfo')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('UAString') is not None:
            self.uastring = m.get('UAString')

        return self

