# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyAntiBruteForceRuleRequest(DaraModel):
    def __init__(
        self,
        default_rule: bool = None,
        fail_count: int = None,
        forbidden_time: int = None,
        id: int = None,
        name: str = None,
        protocol_type: main_models.ModifyAntiBruteForceRuleRequestProtocolType = None,
        resource_owner_id: int = None,
        source_ip: str = None,
        span: int = None,
        uuid_list: List[str] = None,
    ):
        # Specifies whether to set the defense rule as the default rule. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.default_rule = default_rule
        # The threshold of logon failures that you specify. Valid values:
        # 
        # *   **2**
        # *   **3**
        # *   **4**
        # *   **5**
        # *   **10**
        # *   **50**
        # *   **80**
        # *   **100**
        self.fail_count = fail_count
        # The period of time during which logons from an account are not allowed. Unit: minutes. Valid values:
        # 
        # *   **5**
        # *   **15**
        # *   **30**
        # *   **60**
        # *   **120**
        # *   **360**
        # *   **720**
        # *   **1440**
        # *   **10080**
        # *   **52560000**: permanent
        self.forbidden_time = forbidden_time
        # The ID of the defense rule.
        # 
        # This parameter is required.
        self.id = id
        # The name of the defense rule.
        self.name = name
        # The protocol types supported by the anti-brute force rule for interception.
        self.protocol_type = protocol_type
        self.resource_owner_id = resource_owner_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The period of time during which logon failures from an account are measured. Unit: minutes. Valid values:
        # 
        # *   **1**
        # *   **2**
        # *   **5**
        # *   **10**
        # *   **15**
        self.span = span
        # An array consisting of the UUIDs of the servers to which the defense rule is applied.
        self.uuid_list = uuid_list

    def validate(self):
        if self.protocol_type:
            self.protocol_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.forbidden_time is not None:
            result['ForbiddenTime'] = self.forbidden_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type.to_map()

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.span is not None:
            result['Span'] = self.span

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('ForbiddenTime') is not None:
            self.forbidden_time = m.get('ForbiddenTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProtocolType') is not None:
            temp_model = main_models.ModifyAntiBruteForceRuleRequestProtocolType()
            self.protocol_type = temp_model.from_map(m.get('ProtocolType'))

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Span') is not None:
            self.span = m.get('Span')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

class ModifyAntiBruteForceRuleRequestProtocolType(DaraModel):
    def __init__(
        self,
        rdp: str = None,
        sql_server: str = None,
        ssh: str = None,
    ):
        # Whether to modify the RDP interception method, which is enabled by default. Values:
        #   - **on**: Enable
        #   - **off**: Disable
        self.rdp = rdp
        # Whether to modify the SQL Server interception method, which is disabled by default. Values:
        #   - **on**: Enable
        #   - **off**: Disable
        self.sql_server = sql_server
        # Whether to modify the SSH interception method, which is enabled by default. Values:
        #   - **on**: Enable
        #   - **off**: Disable
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

