# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOutgoingDestinationIPRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        category_id: str = None,
        current_page: str = None,
        dst_ip: str = None,
        end_time: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        port: str = None,
        private_ip: str = None,
        public_ip: str = None,
        sort: str = None,
        start_time: str = None,
        tag_id_new: str = None,
    ):
        # The application type supported by the access control policy.
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
        # > The supported application types depend on the protocol type specified in the Proto parameter. If Proto is set to TCP, all application types listed above are supported. If both ApplicationName and ApplicationNameList are specified, the value of ApplicationNameList takes precedence.
        self.application_name = application_name
        # The ID of the service category. Valid values:
        # 
        # - **All**: all categories
        # 
        # - **RiskDomain**: risk domains
        # 
        # - **RiskIP**: risk IPs
        # 
        # - **AliYun**: Alibaba Cloud services
        # 
        # - **NotAliYun**: services other than Alibaba Cloud services
        self.category_id = category_id
        # The page number to return.
        # 
        # Default value: 1.
        self.current_page = current_page
        # The destination IP address of the outbound connection.
        self.dst_ip = dst_ip
        # The end of the time range to query. The value is a timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The sort order. Valid values:
        # 
        # - **asc**: ascending order.
        # 
        # - **desc** (default): descending order.
        self.order = order
        # The number of entries to return on each page.
        # 
        # Default value: 6. Maximum value: 10.
        self.page_size = page_size
        # The port number.
        self.port = port
        # The private IP address of the ECS instance that initiates the outbound connection.
        self.private_ip = private_ip
        # The public IP address of the ECS instance that initiates the outbound connection.
        self.public_ip = public_ip
        # The field by which to sort the results. Valid values:
        # 
        # - **SessionCount** (default): request count.
        # 
        # - **TotalBytes**: total traffic.
        self.sort = sort
        # The start of the time range to query. The value is a timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the threat intelligence tag. Valid values:
        # 
        # - **AliYun**: Alibaba Cloud service
        # 
        # - **RiskDomain**: risk domain
        # 
        # - **RiskIP**: risk IP
        # 
        # - **TrustedDomain**: trusted website
        # 
        # - **AliPay**: Alipay
        # 
        # - **DingDing**: DingTalk
        # 
        # - **WeChat**: WeChat
        # 
        # - **QQ**: Tencent QQ
        # 
        # - **SecurityService**: security service
        # 
        # - **Microsoft**: Microsoft
        # 
        # - **Amazon**: Amazon
        # 
        # - **Pan**: cloud drive
        # 
        # - **Map**: map
        # 
        # - **Code**: code hosting
        # 
        # - **SystemService**: system service
        # 
        # - **Taobao**: Taobao
        # 
        # - **Google**: Google
        # 
        # - **ThirdPartyService**: third-party service
        # 
        # - **FirstFlow**: first access
        # 
        # - **Downloader**: malicious downloader
        # 
        # - **Alexa Top1M**: popular website
        # 
        # - **Miner**: mining pool
        # 
        # - **Intelligence**: threat intelligence
        # 
        # - **DDoS**: DDoS trojan
        # 
        # - **Ransomware**: ransomware
        # 
        # - **Spyware**: spyware
        # 
        # - **Rogue**: rogue software
        # 
        # - **Botnet**: botnet
        # 
        # - **Suspicious**: suspicious website
        # 
        # - **C\\&C**: command and control (C\\&C)
        # 
        # - **Gang**: threat actor group
        # 
        # - **CVE**: CVE
        # 
        # - **Backdoor**: backdoor
        # 
        # - **Phishing**: phishing website
        # 
        # - **APT**: APT attack
        # 
        # - **Supply Chain Attack**: supply chain attack
        # 
        # - **Malicious software**: malware
        self.tag_id_new = tag_id_new

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tag_id_new is not None:
            result['TagIdNew'] = self.tag_id_new

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TagIdNew') is not None:
            self.tag_id_new = m.get('TagIdNew')

        return self

