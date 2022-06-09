# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateMajorProtectionBlackIpRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        expired_time: int = None,
        instance_id: str = None,
        ip_list: str = None,
        rule_id: int = None,
        template_id: int = None,
    ):
        # 防护对象1domain 	描述信息。
        self.description = description
        self.expired_time = expired_time
        self.instance_id = instance_id
        self.ip_list = ip_list
        self.rule_id = rule_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMajorProtectionBlackIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMajorProtectionBlackIpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMajorProtectionBlackIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceResponseBodyDetails(TeaModel):
    def __init__(
        self,
        acl_rule_max_ip_count: int = None,
        anti_scan: bool = None,
        anti_scan_template_max_count: int = None,
        backend_max_count: int = None,
        base_waf_group: bool = None,
        base_waf_group_rule_in_template_max_count: int = None,
        base_waf_group_rule_template_max_count: int = None,
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
        exclusive_ip: bool = None,
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
        vast_ip_blacklist_in_file_max_count: int = None,
        vast_ip_blacklist_in_operation_max_count: int = None,
        vast_ip_blacklist_max_count: int = None,
        whitelist: bool = None,
        whitelist_logical: str = None,
        whitelist_rule_condition: str = None,
        whitelist_rule_in_template_max_count: int = None,
        whitelist_template_max_count: int = None,
    ):
        self.acl_rule_max_ip_count = acl_rule_max_ip_count
        # 支持扫描防护
        self.anti_scan = anti_scan
        # 扫描防护模板数
        self.anti_scan_template_max_count = anti_scan_template_max_count
        # 最大回源数
        self.backend_max_count = backend_max_count
        # 基础防护
        self.base_waf_group = base_waf_group
        # 基础防护规则
        self.base_waf_group_rule_in_template_max_count = base_waf_group_rule_in_template_max_count
        # 基础防护规则最大数量
        self.base_waf_group_rule_template_max_count = base_waf_group_rule_template_max_count
        # 最大可添加CNAME数
        self.cname_resource_max_count = cname_resource_max_count
        # 支持自定义响应
        self.custom_response = custom_response
        # 自定义响应模板包含规则数
        self.custom_response_rule_in_template_max_count = custom_response_rule_in_template_max_count
        # 自定义响应模板数
        self.custom_response_template_max_count = custom_response_template_max_count
        # 支持自定义规则
        self.custom_rule = custom_rule
        # 包含字符串
        self.custom_rule_action = custom_rule_action
        # 自定义规则匹配条件
        self.custom_rule_condition = custom_rule_condition
        # 自定义规则模板包含规则数
        self.custom_rule_in_template_max_count = custom_rule_in_template_max_count
        # 自定义规则限速对象
        self.custom_rule_ratelimitor = custom_rule_ratelimitor
        # 自定义规则模板数
        self.custom_rule_template_max_count = custom_rule_template_max_count
        # 最大防护组数量
        self.defense_group_max_count = defense_group_max_count
        # 一个防护组内最大包含对象数量
        self.defense_object_in_group_max_count = defense_object_in_group_max_count
        # 一个模板内关联对象的最大数量
        self.defense_object_in_template_max_count = defense_object_in_template_max_count
        # 最大防护对象数量
        self.defense_object_max_count = defense_object_max_count
        # 独享IP
        self.exclusive_ip = exclusive_ip
        # Gslb
        self.gslb = gslb
        # HTTP端口可用范围
        self.http_ports = http_ports
        # HTTPS端口可用范围
        self.https_ports = https_ports
        # 支持IP黑名单
        self.ip_blacklist = ip_blacklist
        # IP黑名单规则包含IP数
        self.ip_blacklist_ip_in_rule_max_count = ip_blacklist_ip_in_rule_max_count
        # IP黑名单模板包含规则数
        self.ip_blacklist_rule_in_template_max_count = ip_blacklist_rule_in_template_max_count
        # /黑名单模板数
        self.ip_blacklist_template_max_count = ip_blacklist_template_max_count
        # Ipv6
        self.ipv_6 = ipv_6
        # 日志服务是否开启
        self.log_service = log_service
        # 是否支持重保
        self.major_protection = major_protection
        # 重保模板的最大数量
        self.major_protection_template_max_count = major_protection_template_max_count
        # 海量IP单次上传文件IP的最大数量
        self.vast_ip_blacklist_in_file_max_count = vast_ip_blacklist_in_file_max_count
        # 海量IP单次页面操作的最大数量
        self.vast_ip_blacklist_in_operation_max_count = vast_ip_blacklist_in_operation_max_count
        # 海量IP的最大数量（单用户）
        self.vast_ip_blacklist_max_count = vast_ip_blacklist_max_count
        # 是否支持白名单
        self.whitelist = whitelist
        # 白名单规则匹配条件
        self.whitelist_logical = whitelist_logical
        # 白名单规则匹配条件
        self.whitelist_rule_condition = whitelist_rule_condition
        # 白名单模板包含规则数
        self.whitelist_rule_in_template_max_count = whitelist_rule_in_template_max_count
        # 白名单模板数
        self.whitelist_template_max_count = whitelist_template_max_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.exclusive_ip is not None:
            result['ExclusiveIp'] = self.exclusive_ip
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
        if m.get('ExclusiveIp') is not None:
            self.exclusive_ip = m.get('ExclusiveIp')
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


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        details: DescribeInstanceResponseBodyDetails = None,
        edition: str = None,
        instance_id: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # 实例详情
        self.details = details
        # 套餐
        self.edition = edition
        # 实例ID
        self.instance_id = instance_id
        # RegionId
        self.region_id = region_id
        self.request_id = request_id

    def validate(self):
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.details is not None:
            result['Details'] = self.details.to_map()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Details') is not None:
            temp_model = DescribeInstanceResponseBodyDetails()
            self.details = temp_model.from_map(m['Details'])
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceCompatibleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceCompatibleResponseBodyDetails(TeaModel):
    def __init__(
        self,
        anti_scan: bool = None,
        anti_scan_template_max_count: int = None,
        backend_max_count: int = None,
        base_waf_group: bool = None,
        base_waf_group_rule_in_template_max_count: int = None,
        base_waf_group_rule_template_max_count: int = None,
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
        exclusive_ip: bool = None,
        gslb: bool = None,
        ip_blacklist: bool = None,
        ip_blacklist_ip_in_rule_max_count: int = None,
        ip_blacklist_rule_in_template_max_count: int = None,
        ip_blacklist_template_max_count: int = None,
        ipv_6: bool = None,
        log_service: bool = None,
        whitelist: bool = None,
        whitelist_logical: str = None,
        whitelist_rule_condition: str = None,
        whitelist_rule_in_template_max_count: int = None,
        whitelist_template_max_count: int = None,
    ):
        # 支持扫描防护
        self.anti_scan = anti_scan
        # 扫描防护模板数
        self.anti_scan_template_max_count = anti_scan_template_max_count
        # 最大回源数
        self.backend_max_count = backend_max_count
        # 基础防护
        self.base_waf_group = base_waf_group
        # 基础防护规则
        self.base_waf_group_rule_in_template_max_count = base_waf_group_rule_in_template_max_count
        # 基础防护规则最大数量
        self.base_waf_group_rule_template_max_count = base_waf_group_rule_template_max_count
        # 最大可添加CNAME数
        self.cname_resource_max_count = cname_resource_max_count
        # 支持自定义响应
        self.custom_response = custom_response
        # 自定义响应模板包含规则数
        self.custom_response_rule_in_template_max_count = custom_response_rule_in_template_max_count
        # 自定义响应模板数
        self.custom_response_template_max_count = custom_response_template_max_count
        # 支持自定义规则
        self.custom_rule = custom_rule
        # 包含字符串
        self.custom_rule_action = custom_rule_action
        # 自定义规则匹配条件
        self.custom_rule_condition = custom_rule_condition
        # 自定义规则模板包含规则数
        self.custom_rule_in_template_max_count = custom_rule_in_template_max_count
        # 自定义规则限速对象
        self.custom_rule_ratelimitor = custom_rule_ratelimitor
        # 自定义规则模板数
        self.custom_rule_template_max_count = custom_rule_template_max_count
        # 最大防护组数量
        self.defense_group_max_count = defense_group_max_count
        # 一个防护组内最大包含对象数量
        self.defense_object_in_group_max_count = defense_object_in_group_max_count
        # 一个模板内关联对象的最大数量
        self.defense_object_in_template_max_count = defense_object_in_template_max_count
        # 最大防护对象数量
        self.defense_object_max_count = defense_object_max_count
        # 独享IP
        self.exclusive_ip = exclusive_ip
        # Gslb
        self.gslb = gslb
        # 支持IP黑名单
        self.ip_blacklist = ip_blacklist
        # IP黑名单规则包含IP数
        self.ip_blacklist_ip_in_rule_max_count = ip_blacklist_ip_in_rule_max_count
        # IP黑名单模板包含规则数
        self.ip_blacklist_rule_in_template_max_count = ip_blacklist_rule_in_template_max_count
        # /黑名单模板数
        self.ip_blacklist_template_max_count = ip_blacklist_template_max_count
        # Ipv6
        self.ipv_6 = ipv_6
        # 日志服务是否开启
        self.log_service = log_service
        # 是否支持白名单
        self.whitelist = whitelist
        # 白名单规则匹配条件
        self.whitelist_logical = whitelist_logical
        # 白名单规则匹配条件
        self.whitelist_rule_condition = whitelist_rule_condition
        # 白名单模板包含规则数
        self.whitelist_rule_in_template_max_count = whitelist_rule_in_template_max_count
        # 白名单模板数
        self.whitelist_template_max_count = whitelist_template_max_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.exclusive_ip is not None:
            result['ExclusiveIp'] = self.exclusive_ip
        if self.gslb is not None:
            result['Gslb'] = self.gslb
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
        if m.get('ExclusiveIp') is not None:
            self.exclusive_ip = m.get('ExclusiveIp')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
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


class DescribeInstanceCompatibleResponseBody(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        details: DescribeInstanceCompatibleResponseBodyDetails = None,
        edition: str = None,
        instance_id: str = None,
        pay_type: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        self.commodity_code = commodity_code
        # 实例详情
        self.details = details
        # 套餐
        self.edition = edition
        # 实例ID
        self.instance_id = instance_id
        # 付费类型
        self.pay_type = pay_type
        # RegionId
        self.region_id = region_id
        self.request_id = request_id

    def validate(self):
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.details is not None:
            result['Details'] = self.details.to_map()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Details') is not None:
            temp_model = DescribeInstanceCompatibleResponseBodyDetails()
            self.details = temp_model.from_map(m['Details'])
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceCompatibleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceCompatibleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceCompatibleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceExtendRequest(TeaModel):
    def __init__(
        self,
        edition: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.edition = edition
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceExtendResponseBodyInstances(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceExtendResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstanceExtendResponseBodyInstances] = None,
        request_id: str = None,
    ):
        self.instances = instances
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstanceExtendResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceExtendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceExtendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceExtendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


