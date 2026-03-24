# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        details: main_models.DescribeInstanceResponseBodyDetails = None,
        edition: str = None,
        end_time: int = None,
        in_debt: str = None,
        instance_id: str = None,
        pay_type: str = None,
        process_status: str = None,
        region_id: str = None,
        request_id: str = None,
        start_time: int = None,
        status: int = None,
    ):
        # The details of the instance.
        self.details = details
        # The edition of the WAF instance.
        self.edition = edition
        # The expiration time of the instance. This value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # Indicates whether the instance has an overdue payment:
        # 
        # - **0**: No.
        # 
        # - **1**: Yes.
        self.in_debt = in_debt
        # The ID of the WAF instance.
        self.instance_id = instance_id
        # The billing method of the instance. Valid values:
        # 
        # - **POSTPAY**: The instance is a pay-as-you-go instance.
        # 
        # - **PREPAY**: The instance is a subscription instance.
        self.pay_type = pay_type
        # The processing status of the instance. Valid values:
        # 
        # - **commodity_converting**: The instance is being upgraded or downgraded.
        # 
        # - **commodity_convert_check_failed**: The check for the instance upgrade or downgrade fails.
        # 
        # - **commodity_convert_process_failed**: The instance upgrade or downgrade fails.
        # 
        # - **order_create_failed**: The order fails to be created.
        # 
        # - **order_pending_payment**: The order is pending payment.
        self.process_status = process_status
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The time when the instance was purchased. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The current status of the instance. Valid values:
        # 
        # - **1**: Normal.
        # 
        # - **2**: The instance has expired.
        # 
        # - **3**: The instance is released.
        self.status = status

    def validate(self):
        if self.details:
            self.details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.details is not None:
            result['Details'] = self.details.to_map()

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.in_debt is not None:
            result['InDebt'] = self.in_debt

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Details') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyDetails()
            self.details = temp_model.from_map(m.get('Details'))

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeInstanceResponseBodyDetails(DaraModel):
    def __init__(
        self,
        acl_rule_max_ip_count: int = None,
        anti_scan: bool = None,
        anti_scan_template_max_count: int = None,
        backend_max_count: int = None,
        base_waf_group: bool = None,
        base_waf_group_rule_in_template_max_count: int = None,
        base_waf_group_rule_template_max_count: int = None,
        bot: bool = None,
        bot_app: str = None,
        bot_template_max_count: int = None,
        bot_web: str = None,
        cname_resource_max_count: int = None,
        custom_response: bool = None,
        custom_response_rule_in_template_max_count: int = None,
        custom_response_template_max_count: int = None,
        custom_rule: bool = None,
        custom_rule_action: str = None,
        custom_rule_condition: str = None,
        custom_rule_in_template_max_count: int = None,
        custom_rule_ratelimitor: str = None,
        custom_rule_template_max_count: int = None,
        defense_group_max_count: int = None,
        defense_object_in_group_max_count: int = None,
        defense_object_in_template_max_count: int = None,
        defense_object_max_count: int = None,
        dlp: bool = None,
        dlp_rule_in_template_max_count: int = None,
        dlp_template_max_count: int = None,
        elastic_qps: int = None,
        exclusive_ip: bool = None,
        extend_qps: int = None,
        free_qps: int = None,
        gslb: bool = None,
        http_ports: str = None,
        https_ports: str = None,
        ip_blacklist: bool = None,
        ip_blacklist_ip_in_rule_max_count: int = None,
        ip_blacklist_rule_in_template_max_count: int = None,
        ip_blacklist_template_max_count: int = None,
        ipv_6: bool = None,
        log_service: bool = None,
        major_protection: bool = None,
        major_protection_template_max_count: int = None,
        qps_billing_cap: int = None,
        tamperproof: bool = None,
        tamperproof_rule_in_template_max_count: int = None,
        tamperproof_template_max_count: int = None,
        vast_ip_blacklist_in_file_max_count: int = None,
        vast_ip_blacklist_in_operation_max_count: int = None,
        vast_ip_blacklist_max_count: int = None,
        whitelist: bool = None,
        whitelist_logical: str = None,
        whitelist_rule_condition: str = None,
        whitelist_rule_in_template_max_count: int = None,
        whitelist_template_max_count: int = None,
    ):
        # The maximum number of IP addresses that can be added to the match content. For more information about match content, see [Match conditions](https://help.aliyun.com/document_detail/374354.html).
        self.acl_rule_max_ip_count = acl_rule_max_ip_count
        # Indicates whether scan protection is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.anti_scan = anti_scan
        # The maximum number of scan protection templates that can be configured.
        self.anti_scan_template_max_count = anti_scan_template_max_count
        # The maximum number of back-to-origin IP addresses that can be configured.
        self.backend_max_count = backend_max_count
        # Indicates whether basic protection rules are supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.base_waf_group = base_waf_group
        # The maximum number of protection rules that can be included in a single basic protection rule template.
        self.base_waf_group_rule_in_template_max_count = base_waf_group_rule_in_template_max_count
        # The maximum number of basic protection rule templates that can be configured.
        self.base_waf_group_rule_template_max_count = base_waf_group_rule_template_max_count
        # Indicates whether bot management is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.bot = bot
        # Indicates whether scenario-specific bot protection for apps is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.bot_app = bot_app
        # The maximum number of bot management protection templates that can be configured.
        self.bot_template_max_count = bot_template_max_count
        # Indicates whether scenario-specific bot protection for websites is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.bot_web = bot_web
        # The maximum number of CNAMEs that can be added.
        self.cname_resource_max_count = cname_resource_max_count
        # Indicates whether custom responses are supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.custom_response = custom_response
        # The maximum number of protection rules that can be included in a single custom response template.
        self.custom_response_rule_in_template_max_count = custom_response_rule_in_template_max_count
        # The maximum number of custom response templates that can be configured.
        self.custom_response_template_max_count = custom_response_template_max_count
        # Indicates whether custom rules are supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.custom_rule = custom_rule
        # The action string for the custom rule.
        self.custom_rule_action = custom_rule_action
        # The match condition for the custom rule. For more information, see the description of the **conditions** parameter for **custom_acl** rules in CreateDefenseRule.
        self.custom_rule_condition = custom_rule_condition
        # The maximum number of protection rules that can be included in a single custom rule template.
        self.custom_rule_in_template_max_count = custom_rule_in_template_max_count
        # The rate limiting object for the custom rule.
        self.custom_rule_ratelimitor = custom_rule_ratelimitor
        # The maximum number of custom rule templates that can be configured.
        self.custom_rule_template_max_count = custom_rule_template_max_count
        # The maximum number of protection groups that can be configured.
        self.defense_group_max_count = defense_group_max_count
        # The maximum number of protected objects that can be included in a protection group.
        self.defense_object_in_group_max_count = defense_object_in_group_max_count
        # The maximum number of protected objects that can be associated with a template.
        self.defense_object_in_template_max_count = defense_object_in_template_max_count
        # The maximum number of protected objects that can be configured.
        self.defense_object_max_count = defense_object_max_count
        # Indicates whether data leak prevention is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.dlp = dlp
        # The maximum number of protection rules that can be included in a single data leak prevention template.
        self.dlp_rule_in_template_max_count = dlp_rule_in_template_max_count
        # The maximum number of data leak prevention templates that can be configured.
        self.dlp_template_max_count = dlp_template_max_count
        # The pay-as-you-go QPS of the subscription instance. For more information, see [WAF 3.0 subscription plans](https://help.aliyun.com/document_detail/441231.html).
        # 
        # > This parameter has no meaning for pay-as-you-go instances.
        self.elastic_qps = elastic_qps
        # Indicates whether exclusive IP addresses are supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.exclusive_ip = exclusive_ip
        # The extra QPS of the subscription instance. For more information, see [WAF 3.0 subscription plans](https://help.aliyun.com/document_detail/441231.html).
        # 
        # > This parameter has no meaning for pay-as-you-go instances.
        self.extend_qps = extend_qps
        # The free queries per second (QPS) of the subscription instance. For more information, see [WAF 3.0 subscription plans](https://help.aliyun.com/document_detail/441231.html).
        # 
        # > This parameter has no meaning for pay-as-you-go instances.
        self.free_qps = free_qps
        # Indicates whether Global Server Load Balancing (GSLB) is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.gslb = gslb
        # The available HTTP ports. For more information, see [Port numbers supported by WAF]().
        self.http_ports = http_ports
        # The available HTTPS ports. For more information, see [Port numbers supported by WAF]().
        self.https_ports = https_ports
        # Indicates whether the IP address blacklist is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.ip_blacklist = ip_blacklist
        # The maximum number of IP addresses that can be added to a blacklist rule.
        self.ip_blacklist_ip_in_rule_max_count = ip_blacklist_ip_in_rule_max_count
        # The maximum number of protection rules that can be included in a single blacklist template.
        self.ip_blacklist_rule_in_template_max_count = ip_blacklist_rule_in_template_max_count
        # The maximum number of blacklist templates that can be configured.
        self.ip_blacklist_template_max_count = ip_blacklist_template_max_count
        # Indicates whether IPv6 is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.ipv_6 = ipv_6
        # Indicates whether Simple Log Service is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.log_service = log_service
        # Indicates whether critical event protection is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.major_protection = major_protection
        # The maximum number of critical event protection templates that can be configured.
        self.major_protection_template_max_count = major_protection_template_max_count
        # The traffic billing protection threshold for the pay-as-you-go instance. For more information, see [Traffic billing protection](https://help.aliyun.com/document_detail/2249021.html) for pay-as-you-go instances.
        # 
        # > This parameter has no meaning for subscription instances.
        self.qps_billing_cap = qps_billing_cap
        # Indicates whether webpage tamper protection is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.tamperproof = tamperproof
        # The maximum number of protection rules that can be included in a single webpage tamper protection template.
        self.tamperproof_rule_in_template_max_count = tamperproof_rule_in_template_max_count
        # The maximum number of webpage tamper protection templates that can be configured.
        self.tamperproof_template_max_count = tamperproof_template_max_count
        # The maximum number of IP addresses that can be imported to the IP address blacklist in a single batch.
        self.vast_ip_blacklist_in_file_max_count = vast_ip_blacklist_in_file_max_count
        # The maximum number of IP addresses that can be added to the IP address blacklist from the console in a single operation.
        self.vast_ip_blacklist_in_operation_max_count = vast_ip_blacklist_in_operation_max_count
        # The maximum number of IP addresses that can be added to the IP address blacklist for a single user.
        self.vast_ip_blacklist_max_count = vast_ip_blacklist_max_count
        # Indicates whether the IP address whitelist is supported. Valid values:
        # 
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.whitelist = whitelist
        # The logical operator for the whitelist rule. For more information, see the description of the **conditions** parameter for **whitelist** rules in CreateDefenseRule.
        self.whitelist_logical = whitelist_logical
        # The match field for the whitelist rule. For more information, see the description of the **conditions** parameter for **whitelist** rules in CreateDefenseRule.
        self.whitelist_rule_condition = whitelist_rule_condition
        # The maximum number of protection rules that can be included in a single whitelist template.
        self.whitelist_rule_in_template_max_count = whitelist_rule_in_template_max_count
        # The maximum number of whitelist templates that can be configured.
        self.whitelist_template_max_count = whitelist_template_max_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_rule_max_ip_count is not None:
            result['AclRuleMaxIpCount'] = self.acl_rule_max_ip_count

        if self.anti_scan is not None:
            result['AntiScan'] = self.anti_scan

        if self.anti_scan_template_max_count is not None:
            result['AntiScanTemplateMaxCount'] = self.anti_scan_template_max_count

        if self.backend_max_count is not None:
            result['BackendMaxCount'] = self.backend_max_count

        if self.base_waf_group is not None:
            result['BaseWafGroup'] = self.base_waf_group

        if self.base_waf_group_rule_in_template_max_count is not None:
            result['BaseWafGroupRuleInTemplateMaxCount'] = self.base_waf_group_rule_in_template_max_count

        if self.base_waf_group_rule_template_max_count is not None:
            result['BaseWafGroupRuleTemplateMaxCount'] = self.base_waf_group_rule_template_max_count

        if self.bot is not None:
            result['Bot'] = self.bot

        if self.bot_app is not None:
            result['BotApp'] = self.bot_app

        if self.bot_template_max_count is not None:
            result['BotTemplateMaxCount'] = self.bot_template_max_count

        if self.bot_web is not None:
            result['BotWeb'] = self.bot_web

        if self.cname_resource_max_count is not None:
            result['CnameResourceMaxCount'] = self.cname_resource_max_count

        if self.custom_response is not None:
            result['CustomResponse'] = self.custom_response

        if self.custom_response_rule_in_template_max_count is not None:
            result['CustomResponseRuleInTemplateMaxCount'] = self.custom_response_rule_in_template_max_count

        if self.custom_response_template_max_count is not None:
            result['CustomResponseTemplateMaxCount'] = self.custom_response_template_max_count

        if self.custom_rule is not None:
            result['CustomRule'] = self.custom_rule

        if self.custom_rule_action is not None:
            result['CustomRuleAction'] = self.custom_rule_action

        if self.custom_rule_condition is not None:
            result['CustomRuleCondition'] = self.custom_rule_condition

        if self.custom_rule_in_template_max_count is not None:
            result['CustomRuleInTemplateMaxCount'] = self.custom_rule_in_template_max_count

        if self.custom_rule_ratelimitor is not None:
            result['CustomRuleRatelimitor'] = self.custom_rule_ratelimitor

        if self.custom_rule_template_max_count is not None:
            result['CustomRuleTemplateMaxCount'] = self.custom_rule_template_max_count

        if self.defense_group_max_count is not None:
            result['DefenseGroupMaxCount'] = self.defense_group_max_count

        if self.defense_object_in_group_max_count is not None:
            result['DefenseObjectInGroupMaxCount'] = self.defense_object_in_group_max_count

        if self.defense_object_in_template_max_count is not None:
            result['DefenseObjectInTemplateMaxCount'] = self.defense_object_in_template_max_count

        if self.defense_object_max_count is not None:
            result['DefenseObjectMaxCount'] = self.defense_object_max_count

        if self.dlp is not None:
            result['Dlp'] = self.dlp

        if self.dlp_rule_in_template_max_count is not None:
            result['DlpRuleInTemplateMaxCount'] = self.dlp_rule_in_template_max_count

        if self.dlp_template_max_count is not None:
            result['DlpTemplateMaxCount'] = self.dlp_template_max_count

        if self.elastic_qps is not None:
            result['ElasticQps'] = self.elastic_qps

        if self.exclusive_ip is not None:
            result['ExclusiveIp'] = self.exclusive_ip

        if self.extend_qps is not None:
            result['ExtendQps'] = self.extend_qps

        if self.free_qps is not None:
            result['FreeQps'] = self.free_qps

        if self.gslb is not None:
            result['Gslb'] = self.gslb

        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        if self.ip_blacklist is not None:
            result['IpBlacklist'] = self.ip_blacklist

        if self.ip_blacklist_ip_in_rule_max_count is not None:
            result['IpBlacklistIpInRuleMaxCount'] = self.ip_blacklist_ip_in_rule_max_count

        if self.ip_blacklist_rule_in_template_max_count is not None:
            result['IpBlacklistRuleInTemplateMaxCount'] = self.ip_blacklist_rule_in_template_max_count

        if self.ip_blacklist_template_max_count is not None:
            result['IpBlacklistTemplateMaxCount'] = self.ip_blacklist_template_max_count

        if self.ipv_6 is not None:
            result['Ipv6'] = self.ipv_6

        if self.log_service is not None:
            result['LogService'] = self.log_service

        if self.major_protection is not None:
            result['MajorProtection'] = self.major_protection

        if self.major_protection_template_max_count is not None:
            result['MajorProtectionTemplateMaxCount'] = self.major_protection_template_max_count

        if self.qps_billing_cap is not None:
            result['QpsBillingCap'] = self.qps_billing_cap

        if self.tamperproof is not None:
            result['Tamperproof'] = self.tamperproof

        if self.tamperproof_rule_in_template_max_count is not None:
            result['TamperproofRuleInTemplateMaxCount'] = self.tamperproof_rule_in_template_max_count

        if self.tamperproof_template_max_count is not None:
            result['TamperproofTemplateMaxCount'] = self.tamperproof_template_max_count

        if self.vast_ip_blacklist_in_file_max_count is not None:
            result['VastIpBlacklistInFileMaxCount'] = self.vast_ip_blacklist_in_file_max_count

        if self.vast_ip_blacklist_in_operation_max_count is not None:
            result['VastIpBlacklistInOperationMaxCount'] = self.vast_ip_blacklist_in_operation_max_count

        if self.vast_ip_blacklist_max_count is not None:
            result['VastIpBlacklistMaxCount'] = self.vast_ip_blacklist_max_count

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        if self.whitelist_logical is not None:
            result['WhitelistLogical'] = self.whitelist_logical

        if self.whitelist_rule_condition is not None:
            result['WhitelistRuleCondition'] = self.whitelist_rule_condition

        if self.whitelist_rule_in_template_max_count is not None:
            result['WhitelistRuleInTemplateMaxCount'] = self.whitelist_rule_in_template_max_count

        if self.whitelist_template_max_count is not None:
            result['WhitelistTemplateMaxCount'] = self.whitelist_template_max_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclRuleMaxIpCount') is not None:
            self.acl_rule_max_ip_count = m.get('AclRuleMaxIpCount')

        if m.get('AntiScan') is not None:
            self.anti_scan = m.get('AntiScan')

        if m.get('AntiScanTemplateMaxCount') is not None:
            self.anti_scan_template_max_count = m.get('AntiScanTemplateMaxCount')

        if m.get('BackendMaxCount') is not None:
            self.backend_max_count = m.get('BackendMaxCount')

        if m.get('BaseWafGroup') is not None:
            self.base_waf_group = m.get('BaseWafGroup')

        if m.get('BaseWafGroupRuleInTemplateMaxCount') is not None:
            self.base_waf_group_rule_in_template_max_count = m.get('BaseWafGroupRuleInTemplateMaxCount')

        if m.get('BaseWafGroupRuleTemplateMaxCount') is not None:
            self.base_waf_group_rule_template_max_count = m.get('BaseWafGroupRuleTemplateMaxCount')

        if m.get('Bot') is not None:
            self.bot = m.get('Bot')

        if m.get('BotApp') is not None:
            self.bot_app = m.get('BotApp')

        if m.get('BotTemplateMaxCount') is not None:
            self.bot_template_max_count = m.get('BotTemplateMaxCount')

        if m.get('BotWeb') is not None:
            self.bot_web = m.get('BotWeb')

        if m.get('CnameResourceMaxCount') is not None:
            self.cname_resource_max_count = m.get('CnameResourceMaxCount')

        if m.get('CustomResponse') is not None:
            self.custom_response = m.get('CustomResponse')

        if m.get('CustomResponseRuleInTemplateMaxCount') is not None:
            self.custom_response_rule_in_template_max_count = m.get('CustomResponseRuleInTemplateMaxCount')

        if m.get('CustomResponseTemplateMaxCount') is not None:
            self.custom_response_template_max_count = m.get('CustomResponseTemplateMaxCount')

        if m.get('CustomRule') is not None:
            self.custom_rule = m.get('CustomRule')

        if m.get('CustomRuleAction') is not None:
            self.custom_rule_action = m.get('CustomRuleAction')

        if m.get('CustomRuleCondition') is not None:
            self.custom_rule_condition = m.get('CustomRuleCondition')

        if m.get('CustomRuleInTemplateMaxCount') is not None:
            self.custom_rule_in_template_max_count = m.get('CustomRuleInTemplateMaxCount')

        if m.get('CustomRuleRatelimitor') is not None:
            self.custom_rule_ratelimitor = m.get('CustomRuleRatelimitor')

        if m.get('CustomRuleTemplateMaxCount') is not None:
            self.custom_rule_template_max_count = m.get('CustomRuleTemplateMaxCount')

        if m.get('DefenseGroupMaxCount') is not None:
            self.defense_group_max_count = m.get('DefenseGroupMaxCount')

        if m.get('DefenseObjectInGroupMaxCount') is not None:
            self.defense_object_in_group_max_count = m.get('DefenseObjectInGroupMaxCount')

        if m.get('DefenseObjectInTemplateMaxCount') is not None:
            self.defense_object_in_template_max_count = m.get('DefenseObjectInTemplateMaxCount')

        if m.get('DefenseObjectMaxCount') is not None:
            self.defense_object_max_count = m.get('DefenseObjectMaxCount')

        if m.get('Dlp') is not None:
            self.dlp = m.get('Dlp')

        if m.get('DlpRuleInTemplateMaxCount') is not None:
            self.dlp_rule_in_template_max_count = m.get('DlpRuleInTemplateMaxCount')

        if m.get('DlpTemplateMaxCount') is not None:
            self.dlp_template_max_count = m.get('DlpTemplateMaxCount')

        if m.get('ElasticQps') is not None:
            self.elastic_qps = m.get('ElasticQps')

        if m.get('ExclusiveIp') is not None:
            self.exclusive_ip = m.get('ExclusiveIp')

        if m.get('ExtendQps') is not None:
            self.extend_qps = m.get('ExtendQps')

        if m.get('FreeQps') is not None:
            self.free_qps = m.get('FreeQps')

        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        if m.get('IpBlacklist') is not None:
            self.ip_blacklist = m.get('IpBlacklist')

        if m.get('IpBlacklistIpInRuleMaxCount') is not None:
            self.ip_blacklist_ip_in_rule_max_count = m.get('IpBlacklistIpInRuleMaxCount')

        if m.get('IpBlacklistRuleInTemplateMaxCount') is not None:
            self.ip_blacklist_rule_in_template_max_count = m.get('IpBlacklistRuleInTemplateMaxCount')

        if m.get('IpBlacklistTemplateMaxCount') is not None:
            self.ip_blacklist_template_max_count = m.get('IpBlacklistTemplateMaxCount')

        if m.get('Ipv6') is not None:
            self.ipv_6 = m.get('Ipv6')

        if m.get('LogService') is not None:
            self.log_service = m.get('LogService')

        if m.get('MajorProtection') is not None:
            self.major_protection = m.get('MajorProtection')

        if m.get('MajorProtectionTemplateMaxCount') is not None:
            self.major_protection_template_max_count = m.get('MajorProtectionTemplateMaxCount')

        if m.get('QpsBillingCap') is not None:
            self.qps_billing_cap = m.get('QpsBillingCap')

        if m.get('Tamperproof') is not None:
            self.tamperproof = m.get('Tamperproof')

        if m.get('TamperproofRuleInTemplateMaxCount') is not None:
            self.tamperproof_rule_in_template_max_count = m.get('TamperproofRuleInTemplateMaxCount')

        if m.get('TamperproofTemplateMaxCount') is not None:
            self.tamperproof_template_max_count = m.get('TamperproofTemplateMaxCount')

        if m.get('VastIpBlacklistInFileMaxCount') is not None:
            self.vast_ip_blacklist_in_file_max_count = m.get('VastIpBlacklistInFileMaxCount')

        if m.get('VastIpBlacklistInOperationMaxCount') is not None:
            self.vast_ip_blacklist_in_operation_max_count = m.get('VastIpBlacklistInOperationMaxCount')

        if m.get('VastIpBlacklistMaxCount') is not None:
            self.vast_ip_blacklist_max_count = m.get('VastIpBlacklistMaxCount')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        if m.get('WhitelistLogical') is not None:
            self.whitelist_logical = m.get('WhitelistLogical')

        if m.get('WhitelistRuleCondition') is not None:
            self.whitelist_rule_condition = m.get('WhitelistRuleCondition')

        if m.get('WhitelistRuleInTemplateMaxCount') is not None:
            self.whitelist_rule_in_template_max_count = m.get('WhitelistRuleInTemplateMaxCount')

        if m.get('WhitelistTemplateMaxCount') is not None:
            self.whitelist_template_max_count = m.get('WhitelistTemplateMaxCount')

        return self

