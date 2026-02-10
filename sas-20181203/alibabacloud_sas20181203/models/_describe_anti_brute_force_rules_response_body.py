# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAntiBruteForceRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeAntiBruteForceRulesResponseBodyPageInfo = None,
        request_id: str = None,
        rules: List[main_models.DescribeAntiBruteForceRulesResponseBodyRules] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the defense rules returned.
        self.rules = rules

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeAntiBruteForceRulesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeAntiBruteForceRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeAntiBruteForceRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        default_rule: bool = None,
        enable_smart_rule: bool = None,
        fail_count: int = None,
        forbidden_time: int = None,
        id: int = None,
        machine_count: int = None,
        name: str = None,
        protocol_type: main_models.DescribeAntiBruteForceRulesResponseBodyRulesProtocolType = None,
        span: int = None,
        uuid_list: List[str] = None,
    ):
        # 防暴力破解规则创建时间戳。单位：毫秒。
        self.create_timestamp = create_timestamp
        # Indicates whether the defense rule is the default rule. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  The default rule takes effect on all servers that are not protected by defense rules against brute-force attacks.
        self.default_rule = default_rule
        # This parameter is deprecated.
        self.enable_smart_rule = enable_smart_rule
        # The threshold of logon failures that you specify.
        self.fail_count = fail_count
        # The period of time during which logons from an account are not allowed. Unit: minutes.
        self.forbidden_time = forbidden_time
        # The ID of the defense rule.
        self.id = id
        # The number of servers to which the defense rule is applied.
        self.machine_count = machine_count
        # The name of the defense rule.
        self.name = name
        # The types of protocols that the brute force cracking rule supports to intercept.
        self.protocol_type = protocol_type
        # The period of time during which logon failures from an account are measured. Unit: minutes. If **Span** is set to 10, the defense rule takes effect when the logon failures measured within 10 minutes reaches the specified threshold. The IP address of attackers cannot be used to log on to the server in the specified period of time.
        self.span = span
        # An array consisting of the UUIDs of servers to which the defense rule is applied.
        self.uuid_list = uuid_list

    def validate(self):
        if self.protocol_type:
            self.protocol_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule

        if self.enable_smart_rule is not None:
            result['EnableSmartRule'] = self.enable_smart_rule

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.forbidden_time is not None:
            result['ForbiddenTime'] = self.forbidden_time

        if self.id is not None:
            result['Id'] = self.id

        if self.machine_count is not None:
            result['MachineCount'] = self.machine_count

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type.to_map()

        if self.span is not None:
            result['Span'] = self.span

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')

        if m.get('EnableSmartRule') is not None:
            self.enable_smart_rule = m.get('EnableSmartRule')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('ForbiddenTime') is not None:
            self.forbidden_time = m.get('ForbiddenTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MachineCount') is not None:
            self.machine_count = m.get('MachineCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProtocolType') is not None:
            temp_model = main_models.DescribeAntiBruteForceRulesResponseBodyRulesProtocolType()
            self.protocol_type = temp_model.from_map(m.get('ProtocolType'))

        if m.get('Span') is not None:
            self.span = m.get('Span')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

class DescribeAntiBruteForceRulesResponseBodyRulesProtocolType(DaraModel):
    def __init__(
        self,
        rdp: str = None,
        sql_server: str = None,
        ssh: str = None,
    ):
        # RDP interception method, values: 
        # - **on**: enable 
        # - **off**: disable
        self.rdp = rdp
        # SqlServer interception mode, with values: 
        # - **on**: enable 
        # - **off**: disable
        self.sql_server = sql_server
        # SSH interception method, with values: 
        # - **on**: enabled 
        # - **off**: disabled
        self.ssh = ssh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rdp is not None:
            result['Rdp'] = self.rdp

        if self.sql_server is not None:
            result['SqlServer'] = self.sql_server

        if self.ssh is not None:
            result['Ssh'] = self.ssh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rdp') is not None:
            self.rdp = m.get('Rdp')

        if m.get('SqlServer') is not None:
            self.sql_server = m.get('SqlServer')

        if m.get('Ssh') is not None:
            self.ssh = m.get('Ssh')

        return self

class DescribeAntiBruteForceRulesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

