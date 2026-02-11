# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostCustomizeRuleRequest(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        alert_type_mds: str = None,
        att_ck: str = None,
        event_transfer_ext: str = None,
        event_transfer_switch: int = None,
        event_transfer_type: str = None,
        id: int = None,
        log_source: str = None,
        log_source_mds: str = None,
        log_type: str = None,
        log_type_mds: str = None,
        query_cycle: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        rule_condition: str = None,
        rule_desc: str = None,
        rule_group: str = None,
        rule_name: str = None,
        rule_threshold: str = None,
        threat_level: str = None,
    ):
        # The risk type.
        self.alert_type = alert_type
        # The internal code of the risk type.
        self.alert_type_mds = alert_type_mds
        # att&ck.
        self.att_ck = att_ck
        # The extended information about event generation. If eventTransferType is set to allToSingle, the value of this parameter indicates the length and unit of the alert aggregation window.
        self.event_transfer_ext = event_transfer_ext
        # Specifies whether to convert an alert to an event. Valid values:
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
        # The ID of the rule.
        self.id = id
        # The log source of the rule.
        self.log_source = log_source
        # The internal code of the log source.
        self.log_source_mds = log_source_mds
        # The log type of the rule.
        self.log_type = log_type
        # The internal code of the log type.
        self.log_type_mds = log_type_mds
        # The window length of the rule.
        self.query_cycle = query_cycle
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
        self.role_type = role_type
        # The query condition of the rule. The value is in the JSON format.
        self.rule_condition = rule_condition
        # The description of the rule.
        self.rule_desc = rule_desc
        # The log aggregation field of the rule. The value is a JSON string.
        self.rule_group = rule_group
        # The name of the rule.
        self.rule_name = rule_name
        # The threshold configuration of the rule. The value is in the JSON format.
        self.rule_threshold = rule_threshold
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

        if self.att_ck is not None:
            result['AttCk'] = self.att_ck

        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext

        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch

        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

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

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')

        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')

        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')

        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')

        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

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

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        return self

