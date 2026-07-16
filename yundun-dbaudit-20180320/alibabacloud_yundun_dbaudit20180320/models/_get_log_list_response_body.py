# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class GetLogListResponseBody(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        incomplete: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        results: List[main_models.GetLogListResponseBodyResults] = None,
        total_count: int = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.incomplete = incomplete
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.results = results
        self.total_count = total_count

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.incomplete is not None:
            result['Incomplete'] = self.incomplete

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Incomplete') is not None:
            self.incomplete = m.get('Incomplete')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.GetLogListResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetLogListResponseBodyResults(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        app_client_ip: str = None,
        app_username: str = None,
        capture_time: str = None,
        client_ip: str = None,
        client_ip_alias: str = None,
        client_mac: str = None,
        client_os_user: str = None,
        client_port: int = None,
        client_program: str = None,
        db_id: int = None,
        db_server: str = None,
        db_user: str = None,
        exec_cost_us: int = None,
        fetch_cost_us: int = None,
        inst_name: str = None,
        response_code: str = None,
        response_text: str = None,
        risk_level: int = None,
        rule_id: int = None,
        rule_key_id: int = None,
        rule_name: str = None,
        rule_type: int = None,
        schema: str = None,
        server_mac: str = None,
        session_id: str = None,
        session_login_time: str = None,
        session_logout_time: str = None,
        sql_content: str = None,
        sql_id: str = None,
        sql_type: str = None,
        template_id: str = None,
    ):
        self.affect_rows = affect_rows
        self.app_client_ip = app_client_ip
        self.app_username = app_username
        self.capture_time = capture_time
        self.client_ip = client_ip
        self.client_ip_alias = client_ip_alias
        self.client_mac = client_mac
        self.client_os_user = client_os_user
        self.client_port = client_port
        self.client_program = client_program
        self.db_id = db_id
        self.db_server = db_server
        self.db_user = db_user
        self.exec_cost_us = exec_cost_us
        self.fetch_cost_us = fetch_cost_us
        self.inst_name = inst_name
        self.response_code = response_code
        self.response_text = response_text
        self.risk_level = risk_level
        self.rule_id = rule_id
        self.rule_key_id = rule_key_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.schema = schema
        self.server_mac = server_mac
        self.session_id = session_id
        self.session_login_time = session_login_time
        self.session_logout_time = session_logout_time
        self.sql_content = sql_content
        self.sql_id = sql_id
        self.sql_type = sql_type
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows

        if self.app_client_ip is not None:
            result['AppClientIp'] = self.app_client_ip

        if self.app_username is not None:
            result['AppUsername'] = self.app_username

        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_ip_alias is not None:
            result['ClientIpAlias'] = self.client_ip_alias

        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac

        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user

        if self.client_port is not None:
            result['ClientPort'] = self.client_port

        if self.client_program is not None:
            result['ClientProgram'] = self.client_program

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_server is not None:
            result['DbServer'] = self.db_server

        if self.db_user is not None:
            result['DbUser'] = self.db_user

        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us

        if self.fetch_cost_us is not None:
            result['FetchCostUS'] = self.fetch_cost_us

        if self.inst_name is not None:
            result['InstName'] = self.inst_name

        if self.response_code is not None:
            result['ResponseCode'] = self.response_code

        if self.response_text is not None:
            result['ResponseText'] = self.response_text

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_key_id is not None:
            result['RuleKeyId'] = self.rule_key_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.session_login_time is not None:
            result['SessionLoginTime'] = self.session_login_time

        if self.session_logout_time is not None:
            result['SessionLogoutTime'] = self.session_logout_time

        if self.sql_content is not None:
            result['SqlContent'] = self.sql_content

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')

        if m.get('AppClientIp') is not None:
            self.app_client_ip = m.get('AppClientIp')

        if m.get('AppUsername') is not None:
            self.app_username = m.get('AppUsername')

        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientIpAlias') is not None:
            self.client_ip_alias = m.get('ClientIpAlias')

        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')

        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')

        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')

        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbServer') is not None:
            self.db_server = m.get('DbServer')

        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')

        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')

        if m.get('FetchCostUS') is not None:
            self.fetch_cost_us = m.get('FetchCostUS')

        if m.get('InstName') is not None:
            self.inst_name = m.get('InstName')

        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')

        if m.get('ResponseText') is not None:
            self.response_text = m.get('ResponseText')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleKeyId') is not None:
            self.rule_key_id = m.get('RuleKeyId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SessionLoginTime') is not None:
            self.session_login_time = m.get('SessionLoginTime')

        if m.get('SessionLogoutTime') is not None:
            self.session_logout_time = m.get('SessionLogoutTime')

        if m.get('SqlContent') is not None:
            self.sql_content = m.get('SqlContent')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

