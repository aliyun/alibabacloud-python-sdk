# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class PostCustomizeRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.PostCustomizeRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.PostCustomizeRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PostCustomizeRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        alert_type_mds: str = None,
        aliuid: int = None,
        att_ck: str = None,
        data_type: int = None,
        event_transfer_ext: str = None,
        event_transfer_switch: int = None,
        event_transfer_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        log_source: str = None,
        log_source_mds: str = None,
        log_type: str = None,
        log_type_mds: str = None,
        query_cycle: str = None,
        rule_condition: str = None,
        rule_desc: str = None,
        rule_group: str = None,
        rule_name: str = None,
        rule_threshold: str = None,
        rule_type: str = None,
        status: int = None,
        threat_level: str = None,
    ):
        # The risk type.
        self.alert_type = alert_type
        # The internal code of the risk type.
        self.alert_type_mds = alert_type_mds
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.aliuid = aliuid
        # 告警附加字段attck
        self.att_ck = att_ck
        # 自动化响应规则条件字段数据类型。
        self.data_type = data_type
        # The extended information about event generation. If eventTransferType is set to allToSingle, the value of this parameter indicates the length and unit of the alert aggregation window. The HTML escape characters are reversed.
        self.event_transfer_ext = event_transfer_ext
        # Indicates whether the system generates an event for the alert. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.event_transfer_switch = event_transfer_switch
        # The event generation method. Valid values:
        # 
        # *   default: The default method is used.
        # *   singleToSingle: The system generates an event for each alert.
        # *   allToSingle: The system generates an event for alerts within a period of time.
        self.event_transfer_type = event_transfer_type
        # The time when the custom rule was created.
        self.gmt_create = gmt_create
        # The time when the custom rule was last updated.
        self.gmt_modified = gmt_modified
        # The ID of the custom rule.
        self.id = id
        # The log source of the rule.
        self.log_source = log_source
        # The internal code of the log source.
        self.log_source_mds = log_source_mds
        # The log type of the rule.
        self.log_type = log_type
        # The internal code of the log type.
        self.log_type_mds = log_type_mds
        # The window length of the rule. The HTML escape characters are reversed.
        self.query_cycle = query_cycle
        # The query condition of the rule. The value is in the JSON format. The HTML escape characters are reversed.
        self.rule_condition = rule_condition
        # The description of the rule.
        self.rule_desc = rule_desc
        # The log aggregation field of the rule. The value is a JSON string. The HTML escape characters are reversed.
        self.rule_group = rule_group
        # The name of the rule.
        self.rule_name = rule_name
        # The threshold configuration of the rule. The value is in the JSON format. The HTML escape characters are reversed.
        self.rule_threshold = rule_threshold
        # The type of the rule. Valid values:
        # 
        # *   predefine
        # *   customize
        self.rule_type = rule_type
        # The rule status. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   10: The simulation data is tested.
        # *   15: The business data is being tested.
        # *   20: The business data test ends.
        # *   100: The rule takes effect.
        self.status = status
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.att_ck is not None:
            result['AttCk'] = self.att_ck

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext

        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch

        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.log_source is not None:
            result['LogSource'] = self.log_source

        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds

        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle

        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition

        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc

        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.status is not None:
            result['Status'] = self.status

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')

        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')

        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')

        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')

        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')

        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        return self

