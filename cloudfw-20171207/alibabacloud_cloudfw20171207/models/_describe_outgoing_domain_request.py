# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOutgoingDomainRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        current_page: str = None,
        data_type: str = None,
        domain: str = None,
        end_time: str = None,
        is_aitraffic: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        public_ip: str = None,
        sort: str = None,
        start_time: str = None,
        tag_id_new: str = None,
    ):
        # The product category. Default value: empty. Valid values:
        # 
        # - **All**: All categories.
        # - **RiskDomain**: Risky domain names.
        # - **RiskIP**: Risky IP addresses.
        # - **AliYun**: Alibaba Cloud services.
        # - **NotAliYun**: Non-Alibaba Cloud services.
        self.category_id = category_id
        # Settings for the page number to return for a paging query. Default value: 1.
        self.current_page = current_page
        # The source of the traffic statistics. Default value: internet. Valid values:
        # 
        # - **internet**: Internet firewall.
        # - **nat**: NAT firewall.
        self.data_type = data_type
        # The domain name for outbound connections.
        self.domain = domain
        # Specifies the end time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Specifies whether to collect statistics only on traffic that accesses AI services. Default value: false. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.is_aitraffic = is_aitraffic
        # The language of the request message. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # Specifies the sort order. Valid values:
        # 
        # - **asc**: Ascending order.
        # - **desc** (default): Descending order.
        self.order = order
        # Settings for the number of entries to return on each page for a paging query. Default value: 6. Maximum value: 100. If the specified value exceeds 100, the value 100 is used.
        self.page_size = page_size
        # The public IP address of the ECS instance that initiates the outbound connection.
        self.public_ip = public_ip
        # Specifies the field by which to sort the query results. Valid values:
        # 
        # - **SessionCount** (default): Number of requests.
        # - **TotalBytes**: Total traffic volume.
        self.sort = sort
        # Specifies the start time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the intelligence label. Valid values:
        # 
        # - **AliYun**: Alibaba Cloud services.
        # - **RiskDomain**: Risky domain names.
        # - **RiskIP**: Risky IP addresses.
        # - **TrustedDomain**: Trusted websites.
        # - **AliPay**: Alipay.
        # - **DingDing**: DingTalk.
        # - **WeChat**: WeChat.
        # - **QQ**: Tencent QQ.
        # - **SecurityService**: Security services.
        # - **Microsoft**: Microsoft.
        # - **Amazon**: Amazon.
        # - **Pan**: Cloud storage.
        # - **Map**: Maps.
        # - **Code**: Code hosting.
        # - **SystemService**: System services.
        # - **Taobao**: Taobao.
        # - **Google**: Google.
        # - **ThirdPartyService**: Third-party platform services.
        # - **FirstFlow**: First visit.
        # - **Downloader**: Malicious downloads.
        # - **Alexa Top1M**: Popular websites.
        # - **Miner**: Miner pools.
        # - **Intelligence**: Threat intelligence.
        # - **DDoS**: DDoS trojans.
        # - **Ransomware**: Ransomware.
        # - **Spyware**: Spyware.
        # - **Rogue**: Rogue software.
        # - **Botnet**: Botnets.
        # - **Suspicious**: Suspicious websites.
        # - **C&C**: Remote control.
        # - **Gang**: Gangs.
        # - **CVE**: CVE vulnerabilities.
        # - **Backdoor**: Backdoor trojans.
        # - **Phishing**: Phishing websites.
        # - **APT**: APT attacks.
        # - **Supply Chain Attack**: Supply chain attacks.
        # - **Malicious software**: Malware.
        self.tag_id_new = tag_id_new

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_aitraffic is not None:
            result['IsAITraffic'] = self.is_aitraffic

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsAITraffic') is not None:
            self.is_aitraffic = m.get('IsAITraffic')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TagIdNew') is not None:
            self.tag_id_new = m.get('TagIdNew')

        return self

