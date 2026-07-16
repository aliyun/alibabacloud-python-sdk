# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeOutgoingDestinationIPResponseBody(DaraModel):
    def __init__(
        self,
        dst_iplist: List[main_models.DescribeOutgoingDestinationIPResponseBodyDstIPList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of destination IP addresses for outgoing connections.
        self.dst_iplist = dst_iplist
        # The request ID.
        self.request_id = request_id
        # The total number of outgoing IPs.
        self.total_count = total_count

    def validate(self):
        if self.dst_iplist:
            for v1 in self.dst_iplist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DstIPList'] = []
        if self.dst_iplist is not None:
            for k1 in self.dst_iplist:
                result['DstIPList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dst_iplist = []
        if m.get('DstIPList') is not None:
            for k1 in m.get('DstIPList'):
                temp_model = main_models.DescribeOutgoingDestinationIPResponseBodyDstIPList()
                self.dst_iplist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOutgoingDestinationIPResponseBodyDstIPList(DaraModel):
    def __init__(
        self,
        acl_coverage: str = None,
        acl_recommend_detail: str = None,
        acl_status: str = None,
        address_group_list: List[main_models.DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList] = None,
        application_port_list: List[main_models.DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList] = None,
        asset_count: int = None,
        category_class_id: str = None,
        category_id: str = None,
        category_name: str = None,
        dst_ip: str = None,
        group_name: str = None,
        has_acl: str = None,
        has_acl_recommend: bool = None,
        in_bytes: int = None,
        is_mark_normal: bool = None,
        location_name: str = None,
        out_bytes: int = None,
        private_asset_count: int = None,
        rule_id: str = None,
        rule_name: str = None,
        security_reason: str = None,
        security_suggest: str = None,
        session_count: int = None,
        tag_list: List[main_models.DescribeOutgoingDestinationIPResponseBodyDstIPListTagList] = None,
        total_bytes: str = None,
    ):
        # Indicates whether an access control policy is applied. Valid values:
        # 
        # - **Uncovered**: No policy is applied.
        # 
        # - **FullCoverage**: A policy is applied.
        self.acl_coverage = acl_coverage
        # Details of the ACL recommendation.
        self.acl_recommend_detail = acl_recommend_detail
        # The health status of the access control policy. Valid values:
        # 
        # - **Normal**: Healthy.
        # 
        # - **Abnormal**: Unhealthy.
        self.acl_status = acl_status
        # A list of address books that contain this destination IP address.
        self.address_group_list = address_group_list
        # The list of application ports.
        # 
        # > This response returns a maximum of 99 application ports. If more than 99 ports exist, only the first 99 are returned.
        self.application_port_list = application_port_list
        # The total number of assets that initiated outgoing connections to this destination IP.
        self.asset_count = asset_count
        # The threat intelligence category of the destination IP address. Valid values:
        # 
        # - **Suspicious**
        # 
        # - **Malicious**
        # 
        # - **Trusted**
        self.category_class_id = category_class_id
        # The ID of the service category. Valid values:
        # 
        # - **Aliyun**: The destination is an Alibaba Cloud product.
        # 
        # - **NotAliyun**: The destination is a non-Alibaba Cloud product.
        self.category_id = category_id
        # The service category of the destination IP address. Valid values:
        # 
        # - **Alibaba Cloud product**
        # 
        # - **non-Alibaba Cloud product**
        self.category_name = category_name
        # The destination IP address of the outgoing connection.
        self.dst_ip = dst_ip
        # The name of the rule group.
        self.group_name = group_name
        # Indicates whether an access control rule exists. Valid values:
        # 
        # - **true**: An access control rule exists.
        # 
        # - **false**: No access control rule exists.
        self.has_acl = has_acl
        # Indicates whether an ACL is recommended. Valid values:
        # 
        # - **true**: An ACL is recommended.
        # 
        # - **false**: No ACL is recommended.
        self.has_acl_recommend = has_acl_recommend
        # The total inbound traffic in bytes.
        self.in_bytes = in_bytes
        # Indicates whether the destination IP address is added to the allowlist. Valid values:
        # 
        # - **true**: The destination IP address is on the allowlist.
        # 
        # - **false**: The destination IP address is not on the allowlist.
        self.is_mark_normal = is_mark_normal
        # The geographical location of the destination IP address.
        self.location_name = location_name
        # The total outbound traffic in bytes.
        self.out_bytes = out_bytes
        # The total number of private assets that initiated outgoing connections to this destination IP.
        self.private_asset_count = private_asset_count
        # The UUID of the ACL rule.
        self.rule_id = rule_id
        # The name of the ACL rule.
        self.rule_name = rule_name
        # The reason for the security recommendation.
        self.security_reason = security_reason
        # The recommended security action for the outgoing connection. Valid values:
        # 
        # - **pass**: Allows the connection.
        # 
        # - **alert**: Rejects the connection.
        # 
        # - **drop**: Drops the connection.
        self.security_suggest = security_suggest
        # The number of requests.
        self.session_count = session_count
        # A list of tags associated with the destination IP.
        self.tag_list = tag_list
        # The total traffic volume in bytes.
        self.total_bytes = total_bytes

    def validate(self):
        if self.address_group_list:
            for v1 in self.address_group_list:
                 if v1:
                    v1.validate()
        if self.application_port_list:
            for v1 in self.application_port_list:
                 if v1:
                    v1.validate()
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_coverage is not None:
            result['AclCoverage'] = self.acl_coverage

        if self.acl_recommend_detail is not None:
            result['AclRecommendDetail'] = self.acl_recommend_detail

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        result['AddressGroupList'] = []
        if self.address_group_list is not None:
            for k1 in self.address_group_list:
                result['AddressGroupList'].append(k1.to_map() if k1 else None)

        result['ApplicationPortList'] = []
        if self.application_port_list is not None:
            for k1 in self.application_port_list:
                result['ApplicationPortList'].append(k1.to_map() if k1 else None)

        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count

        if self.category_class_id is not None:
            result['CategoryClassId'] = self.category_class_id

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.has_acl is not None:
            result['HasAcl'] = self.has_acl

        if self.has_acl_recommend is not None:
            result['HasAclRecommend'] = self.has_acl_recommend

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.is_mark_normal is not None:
            result['IsMarkNormal'] = self.is_mark_normal

        if self.location_name is not None:
            result['LocationName'] = self.location_name

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.private_asset_count is not None:
            result['PrivateAssetCount'] = self.private_asset_count

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.security_reason is not None:
            result['SecurityReason'] = self.security_reason

        if self.security_suggest is not None:
            result['SecuritySuggest'] = self.security_suggest

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclCoverage') is not None:
            self.acl_coverage = m.get('AclCoverage')

        if m.get('AclRecommendDetail') is not None:
            self.acl_recommend_detail = m.get('AclRecommendDetail')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        self.address_group_list = []
        if m.get('AddressGroupList') is not None:
            for k1 in m.get('AddressGroupList'):
                temp_model = main_models.DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList()
                self.address_group_list.append(temp_model.from_map(k1))

        self.application_port_list = []
        if m.get('ApplicationPortList') is not None:
            for k1 in m.get('ApplicationPortList'):
                temp_model = main_models.DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList()
                self.application_port_list.append(temp_model.from_map(k1))

        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')

        if m.get('CategoryClassId') is not None:
            self.category_class_id = m.get('CategoryClassId')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HasAcl') is not None:
            self.has_acl = m.get('HasAcl')

        if m.get('HasAclRecommend') is not None:
            self.has_acl_recommend = m.get('HasAclRecommend')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('IsMarkNormal') is not None:
            self.is_mark_normal = m.get('IsMarkNormal')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('PrivateAssetCount') is not None:
            self.private_asset_count = m.get('PrivateAssetCount')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SecurityReason') is not None:
            self.security_reason = m.get('SecurityReason')

        if m.get('SecuritySuggest') is not None:
            self.security_suggest = m.get('SecuritySuggest')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeOutgoingDestinationIPResponseBodyDstIPListTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        return self

class DescribeOutgoingDestinationIPResponseBodyDstIPListTagList(DaraModel):
    def __init__(
        self,
        class_id: str = None,
        risk_level: int = None,
        tag_describe: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        # The category of the threat intelligence tag. Valid values:
        # 
        # - **Suspicious**
        # 
        # - **Malicious**
        # 
        # - **Trusted**
        self.class_id = class_id
        # The risk level. Valid values:
        # 
        # - **1**: Low
        # 
        # - **2**: Medium
        # 
        # - **3**: High
        self.risk_level = risk_level
        # The description of the threat intelligence tag.
        self.tag_describe = tag_describe
        # The ID of the threat intelligence tag.
        self.tag_id = tag_id
        # The name of the threat intelligence tag.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_id is not None:
            result['ClassId'] = self.class_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.tag_describe is not None:
            result['TagDescribe'] = self.tag_describe

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('TagDescribe') is not None:
            self.tag_describe = m.get('TagDescribe')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        port: int = None,
        unknown_reason: List[str] = None,
    ):
        # The application protocol detected for the connection. Valid values:
        # 
        # - **FTP**
        # 
        # - **HTTP**
        # 
        # - **HTTPS**
        # 
        # - **Memcache**
        # 
        # - **MongoDB**
        # 
        # - **MQTT**
        # 
        # - **MySQL**
        # 
        # - **RDP**
        # 
        # - **Redis**
        # 
        # - **SMTP**
        # 
        # - **SMTPS**
        # 
        # - **SSH**
        # 
        # - **SSL_No_Cert**
        # 
        # - **SSL**
        # 
        # - **VNC**
        # 
        # >
        self.application_name = application_name
        # The application port.
        self.port = port
        # A list of reasons why the application protocol was not identified.
        self.unknown_reason = unknown_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.port is not None:
            result['Port'] = self.port

        if self.unknown_reason is not None:
            result['UnknownReason'] = self.unknown_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('UnknownReason') is not None:
            self.unknown_reason = m.get('UnknownReason')

        return self

class DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList(DaraModel):
    def __init__(
        self,
        address_group_name: str = None,
        address_group_uuid: str = None,
    ):
        # The name of the address book.
        self.address_group_name = address_group_name
        # The UUID of the address book.
        self.address_group_uuid = address_group_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_group_name is not None:
            result['AddressGroupName'] = self.address_group_name

        if self.address_group_uuid is not None:
            result['AddressGroupUUID'] = self.address_group_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressGroupName') is not None:
            self.address_group_name = m.get('AddressGroupName')

        if m.get('AddressGroupUUID') is not None:
            self.address_group_uuid = m.get('AddressGroupUUID')

        return self

