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
        # The details of the WAF instance.
        self.details = details
        # The edition of the WAF instance.
        self.edition = edition
        # The expiration time of the WAF instance.
        self.end_time = end_time
        # Indicates whether the WAF instance has overdue payments. Valid values:
        # 
        # *   **0**: The WAF instance does not have overdue payments.
        # *   **1**: The WAF instance has overdue payments.
        self.in_debt = in_debt
        # The ID of the WAF instance.
        self.instance_id = instance_id
        # The billing method of the WAF instance. Valid values:
        # 
        # *   **POSTPAY:** The WAF instance uses the pay-as-you-go billing method.
        # *   **PREPAY:** The WAF instance uses the subscription billing method.
        self.pay_type = pay_type
        self.process_status = process_status
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The purchase time of the WAF instance. The time is in the UNIX timestamp format. The time is displayed in UTC. Unit: milliseconds.
        self.start_time = start_time
        # The status of the WAF instance. Valid values:
        # 
        # *   **1:** The WAF instance is in a normal state.
        # *   **2:** The WAF instance has expired.
        # *   **3:** The WAF instance has been released.
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
        # The maximum number of IP addresses that can be added to the match content of a match condition. For more information, see [Match conditions](https://help.aliyun.com/document_detail/374354.html).
        self.acl_rule_max_ip_count = acl_rule_max_ip_count
        # Indicates whether the scan protection module is supported. Valid values:
        # 
        # *   **true:** The scan protection module is supported.
        # *   **false:** The scan protection module is not supported.
        self.anti_scan = anti_scan
        # The maximum number of scan protection rule templates that can be configured.
        self.anti_scan_template_max_count = anti_scan_template_max_count
        # The maximum number of back-to-origin IP addresses that can be configured.
        self.backend_max_count = backend_max_count
        # Indicates whether the basic protection rule module is supported. Valid values:
        # 
        # *   **true:** The basic protection rule module is supported.
        # *   **false:** The basic protection rule module is not supported.
        self.base_waf_group = base_waf_group
        # The maximum number of protection rules that can be included in a basic protection rule template.
        self.base_waf_group_rule_in_template_max_count = base_waf_group_rule_in_template_max_count
        # The maximum number of basic protection rule templates that can be configured.
        self.base_waf_group_rule_template_max_count = base_waf_group_rule_template_max_count
        # Indicates whether the bot management module is supported. Valid values:
        # 
        # *   **true:** The bot management module is supported.
        # *   **false:** The bot management module is not supported.
        self.bot = bot
        # Indicates whether bot management for app protection is supported. Valid values:
        # 
        # *   **true:** Bot management for app protection is supported.
        # *   **false:** Bot management for app protection is not supported.
        self.bot_app = bot_app
        # The maximum number of bot management rule templates that can be configured.
        self.bot_template_max_count = bot_template_max_count
        # Indicates whether bot management for website protection is supported. Valid values:
        # 
        # *   **true:** Bot management for website protection is supported.
        # *   **false:** Bot management for website protection is not supported.
        self.bot_web = bot_web
        # The maximum number of CNAMEs that can be added.
        self.cname_resource_max_count = cname_resource_max_count
        # Indicates whether the custom response module is supported. Valid values:
        # 
        # *   **true:** The custom response module is supported.
        # *   **false:** The custom response module is not supported.
        self.custom_response = custom_response
        # The maximum number of rules that can be included in a custom response rule template.
        self.custom_response_rule_in_template_max_count = custom_response_rule_in_template_max_count
        # The maximum number of custom response rule templates that can be configured.
        self.custom_response_template_max_count = custom_response_template_max_count
        # Indicates whether the custom rule module is supported. Valid values:
        # 
        # *   **true:** The custom rule module is supported.
        # *   **false:** The custom rule module is not supported.
        self.custom_rule = custom_rule
        # The action that can be included in a custom rule.
        self.custom_rule_action = custom_rule_action
        # The match conditions that can be used in a custom rule. For more information, see **Match condition parameters** in the "**Parameters of custom rules (custom_acl)**" section in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.custom_rule_condition = custom_rule_condition
        # The maximum number of rules that can be included in a custom rule template.
        self.custom_rule_in_template_max_count = custom_rule_in_template_max_count
        # The statistical object for rate limiting in a custom rule.
        self.custom_rule_ratelimitor = custom_rule_ratelimitor
        # The maximum number of custom rule templates that can be configured.
        self.custom_rule_template_max_count = custom_rule_template_max_count
        # The maximum number of protected object groups that can be configured.
        self.defense_group_max_count = defense_group_max_count
        # The maximum number of protected objects that can be included in a protected object group.
        self.defense_object_in_group_max_count = defense_object_in_group_max_count
        # The maximum number of protected objects to which a protection rule template can be applied.
        self.defense_object_in_template_max_count = defense_object_in_template_max_count
        # The maximum number of protected objects that can be configured.
        self.defense_object_max_count = defense_object_max_count
        # Indicates whether the data leakage prevention module is supported. Valid values:
        # 
        # *   **true:** The data leakage prevention module is supported.
        # *   **false:** The data leakage prevention module is not supported.
        self.dlp = dlp
        # The maximum number of rules that can be included in a data leakage prevention rule template.
        self.dlp_rule_in_template_max_count = dlp_rule_in_template_max_count
        # The maximum number of data leakage prevention rule templates that can be configured.
        self.dlp_template_max_count = dlp_template_max_count
        self.elastic_qps = elastic_qps
        # Indicates whether exclusive IP addresses are supported. Valid values:
        # 
        # *   **true:** Exclusive IP addresses are supported.
        # *   **false:** Exclusive IP addresses are not supported.
        self.exclusive_ip = exclusive_ip
        self.extend_qps = extend_qps
        self.free_qps = free_qps
        # Indicates whether global server load balancing (GSLB) is supported. Valid values:
        # 
        # *   **true:** GSLB is supported.
        # *   **false:** GSLB is not supported.
        self.gslb = gslb
        # The HTTP port range that is supported. For more information, see [View supported ports](https://help.aliyun.com/document_detail/385578.html).
        self.http_ports = http_ports
        # The HTTPS port range that is supported. For more information, see [View supported ports](https://help.aliyun.com/document_detail/385578.html).
        self.https_ports = https_ports
        # Indicates whether the IP address blacklist module is supported. Valid values:
        # 
        # *   **true:** The IP address blacklist module is supported.
        # *   **false:** The IP address blacklist module is not supported.
        self.ip_blacklist = ip_blacklist
        # The maximum number of IP addresses that can be added to an IP address blacklist rule.
        self.ip_blacklist_ip_in_rule_max_count = ip_blacklist_ip_in_rule_max_count
        # The maximum number of rules that can be included in an IP address blacklist rule template.
        self.ip_blacklist_rule_in_template_max_count = ip_blacklist_rule_in_template_max_count
        # The maximum number of IP address blacklist rule templates that can be configured.
        self.ip_blacklist_template_max_count = ip_blacklist_template_max_count
        # Indicates whether IPv6 is supported. Valid values:
        # 
        # *   **true:** IPv6 is supported.
        # *   **false:** IPv6 is not supported.
        self.ipv_6 = ipv_6
        # Indicates whether the log collection feature is supported. Valid values:
        # 
        # *   **true:** The log collection feature is supported.
        # *   **false:** The log collection feature is not supported.
        self.log_service = log_service
        # Indicates whether major event protection is supported. Valid values:
        # 
        # *   **true:** Major event protection is supported.
        # *   **false:** Major event protection is not supported.
        self.major_protection = major_protection
        # The maximum number of major event protection rule templates that can be configured.
        self.major_protection_template_max_count = major_protection_template_max_count
        self.qps_billing_cap = qps_billing_cap
        # Indicates whether the website tamper-proofing module is supported. Valid values:
        # 
        # *   **true:** The website tamper-proofing module is supported.
        # *   **false:** The website tamper-proofing module is not supported.
        self.tamperproof = tamperproof
        # The maximum number of rules that can be included in a website tamper-proofing rule template.
        self.tamperproof_rule_in_template_max_count = tamperproof_rule_in_template_max_count
        # The maximum number of website tamper-proofing rule templates that can be configured.
        self.tamperproof_template_max_count = tamperproof_template_max_count
        # The maximum number of IP addresses or CIDR blocks that can be added to an IP address blacklist in a batch.
        self.vast_ip_blacklist_in_file_max_count = vast_ip_blacklist_in_file_max_count
        # The maximum number of IP addresses or CIDR blocks that can be added to an IP address blacklist on a page.
        self.vast_ip_blacklist_in_operation_max_count = vast_ip_blacklist_in_operation_max_count
        # The maximum number of IP addresses or CIDR blocks that can be added to an IP address blacklist per Alibaba Cloud account.
        self.vast_ip_blacklist_max_count = vast_ip_blacklist_max_count
        # Indicates whether the whitelist module is supported. Valid values:
        # 
        # *   **true:** The whitelist module is supported.
        # *   **false:** The whitelist module is not supported.
        self.whitelist = whitelist
        # The logical operators that can be used in a whitelist rule. For more information, see **Match condition parameters** in the "**Parameters of whitelist rules (whitelist)**" section in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.whitelist_logical = whitelist_logical
        # The match fields that can be used in a whitelist rule. For more information, see **Match condition parameters** in the "**Parameters of whitelist rules (whitelist)**" section in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.whitelist_rule_condition = whitelist_rule_condition
        # The maximum number of rules that can be included in a whitelist rule template.
        self.whitelist_rule_in_template_max_count = whitelist_rule_in_template_max_count
        # The maximum number of whitelist rule templates that can be configured.
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

