# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeEventLogResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeEventLogResponseBodyDataList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of ISPs.
        self.data_list = data_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeEventLogResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEventLogResponseBodyDataList(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        attack_app: str = None,
        attack_type: int = None,
        direction: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        hit_content: str = None,
        hit_type: str = None,
        ip_protocol: str = None,
        member_uid: int = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_result: int = None,
        rule_source: int = None,
        sni: str = None,
        src_ip: str = None,
        src_port: int = None,
        ssl_cipher: str = None,
        ssl_error_index: str = None,
        ssl_error_msg: str = None,
        ssl_handshake_res: str = None,
        ssl_protocol: str = None,
        start_time: int = None,
        url: str = None,
        vul_level: int = None,
    ):
        # The application type supported by the access control policy. We recommend that you use ApplicationNameList. Valid values:
        # - **FTP**
        # - **HTTP**
        # - **HTTPS**
        # - **Memcache**
        # - **MongoDB**
        # - **MQTT**
        # - **MySQL**
        # - **RDP**
        # - **Redis**
        # - **SMTP**
        # - **SMTPS**
        # - **SSH**
        # - **SSL**
        # - **VNC**
        # - **ANY** (all application types)
        self.application_name = application_name
        # The name of the attacked application.
        self.attack_app = attack_app
        # The attack type of the intrusion prevention event. Valid values:
        # - **1**: Abnormal connection.
        # - **2**: Command execution.
        # - **3**: Brute-force attack.
        # - **4**: Scanning.
        # - **5**: Other.
        # - **6**: Information leakage.
        # - **7**: DoS attack.
        # - **8**: Overflow attack.
        # - **9**: Web attack.
        # - **10**: Trojan backdoor.
        # - **11**: Viruses and worms.
        # - **12**: Mining behavior.
        # - **13**: Reverse shell.
        self.attack_type = attack_type
        # The traffic direction of the intrusion prevention event. Valid values:
        # - **in**: Inbound.
        # - **out**: Outbound.
        self.direction = direction
        # The destination IP address that is queried. This indicates that the intrusion prevention event involves this destination IP address.
        self.dst_ip = dst_ip
        # The destination port.
        self.dst_port = dst_port
        # The hit content.
        self.hit_content = hit_content
        # The hit type.
        self.hit_type = hit_type
        # The protocol type.
        self.ip_protocol = ip_protocol
        # The UID of the Cloud Firewall member account.
        self.member_uid = member_uid
        # The ID of the protection rule for the intrusion prevention event.
        self.rule_id = rule_id
        # The rule name.
        self.rule_name = rule_name
        # The defense status. Valid values:
        # - **1**: Alert.
        # - **2**: Block.
        self.rule_result = rule_result
        # The source of the detection rule for the intrusion prevention event. Valid values:
        # - **1**: Basic protection.
        # - **2**: Virtual patches.
        # - **4**: Threat intelligence.
        self.rule_source = rule_source
        # The SNI used when the TLS connection is established.
        self.sni = sni
        # The source IP address that is queried. This indicates that the intrusion prevention event involves this source IP address.
        self.src_ip = src_ip
        # The source port.
        self.src_port = src_port
        # The cipher suite used for TLS handshake negotiation, such as TLS_AES_128_GCM_SHA256.
        self.ssl_cipher = ssl_cipher
        # The phase in which the TLS handshake fails, such as Certificate.
        self.ssl_error_index = ssl_error_index
        # The reason why the TLS handshake fails, such as BAD_PACKET_LENGTH.
        self.ssl_error_msg = ssl_error_msg
        # The TLS handshake result. For example, success indicates that the handshake is successful.
        self.ssl_handshake_res = ssl_handshake_res
        # The TLS version, such as TLSv1.3.
        self.ssl_protocol = ssl_protocol
        # The start time of the data. The value is a timestamp in seconds.
        self.start_time = start_time
        # The document path.
        self.url = url
        # The severity level of the intrusion prevention event. Valid values:
        # - **1**: Low.
        # - **2**: Medium.
        # - **3**: High.
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.hit_content is not None:
            result['HitContent'] = self.hit_content

        if self.hit_type is not None:
            result['HitType'] = self.hit_type

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source

        if self.sni is not None:
            result['Sni'] = self.sni

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_port is not None:
            result['SrcPort'] = self.src_port

        if self.ssl_cipher is not None:
            result['SslCipher'] = self.ssl_cipher

        if self.ssl_error_index is not None:
            result['SslErrorIndex'] = self.ssl_error_index

        if self.ssl_error_msg is not None:
            result['SslErrorMsg'] = self.ssl_error_msg

        if self.ssl_handshake_res is not None:
            result['SslHandshakeRes'] = self.ssl_handshake_res

        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.url is not None:
            result['Url'] = self.url

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('HitContent') is not None:
            self.hit_content = m.get('HitContent')

        if m.get('HitType') is not None:
            self.hit_type = m.get('HitType')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')

        if m.get('Sni') is not None:
            self.sni = m.get('Sni')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')

        if m.get('SslCipher') is not None:
            self.ssl_cipher = m.get('SslCipher')

        if m.get('SslErrorIndex') is not None:
            self.ssl_error_index = m.get('SslErrorIndex')

        if m.get('SslErrorMsg') is not None:
            self.ssl_error_msg = m.get('SslErrorMsg')

        if m.get('SslHandshakeRes') is not None:
            self.ssl_handshake_res = m.get('SslHandshakeRes')

        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        return self

