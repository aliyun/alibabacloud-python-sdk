# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudGtmMonitorTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        evaluation_count: int = None,
        extend_info: str = None,
        failure_rate: int = None,
        interval: int = None,
        ip_version: str = None,
        isp_city_nodes_shrink: str = None,
        name: str = None,
        protocol: str = None,
        timeout: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US: English. This is the default value.
        self.accept_language = accept_language
        # The client token that is used to ensure the idempotence of the request. Make sure that the client token is unique for each request. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The number of consecutive failures that must occur before the system considers the application service unhealthy. This setting helps prevent false alarms caused by transient issues such as network jitter. Valid values:
        # 
        # - 1
        # 
        # - 2
        # 
        # - 3
        # 
        # This parameter is required.
        self.evaluation_count = evaluation_count
        # The extended information in a JSON string. The parameters vary based on the protocol.
        # 
        # - http(s):
        # 
        #   **host**: The Host field in the header of the HTTP or HTTPS request. This field identifies the website that you want to access. The default value is the primary domain name. If the destination website uses a specific host, change this value as needed.
        # 
        #   **path**: The URL path for the HTTP or HTTPS health check. The default value is "/".
        # 
        #   **code**: For an HTTP or HTTPS health check, the system determines whether the web server is working correctly based on the return code. If the return code is greater than this threshold, the system considers the application service unhealthy.
        # 
        #   - 400: Bad Request. If an HTTP or HTTPS request contains incorrect parameters, the web server returns a code greater than 400. If you set the threshold to 400, make sure that you specify the exact URL path.
        # 
        #   - 500: Server Error. If an exception occurs on the web server, it returns a code greater than 500. The default threshold is 500.
        # 
        #   **sni**: Specifies whether to enable Server Name Indication (SNI). This parameter applies only to the HTTPS protocol. SNI is a Transport Layer Security (TLS) extension that allows a client to specify the hostname to connect to at the start of the TLS handshake. This allows the server to present the correct certificate for the requested service.
        # 
        #   - true: Enable SNI.
        # 
        #   - false: Disable SNI.
        # 
        #   **followRedirect**: Specifies whether to follow 3xx redirects.
        # 
        #   - true: Follows the redirect if the detection point receives a 3xx status code, such as 301, 302, 303, 307, or 308.
        # 
        #   - false: Does not follow the redirect.
        # 
        # - ping:
        # 
        #   **packetNum**: The number of ICMP packets to send for each ping health check. Valid values: 20, 50, and 100.
        # 
        #   **packetLossRate**: The packet loss rate that triggers an alarm. For each ping health check, the system calculates the packet loss rate based on the sent ICMP packets. Packet loss rate = (Number of lost packets / Total number of sent ICMP packets) × 100%. An alarm is triggered if the packet loss rate reaches this threshold. Valid values: 10, 30, 40, 80, 90, and 100.
        self.extend_info = extend_info
        # The failure rate threshold. An endpoint is considered unhealthy if the percentage of unhealthy detection points exceeds this value. Valid values:
        # 
        # - 20
        # 
        # - 50
        # 
        # - 80
        # 
        # - 100
        # 
        # This parameter is required.
        self.failure_rate = failure_rate
        # The health check interval in seconds. The default value is 60. The minimum interval is 15 seconds, which is available only for Ultimate Edition instances.
        # 
        # This parameter is required.
        self.interval = interval
        # The IP address type for health checks.
        # 
        # - IPv4: The destination address is an IPv4 address.
        # 
        # - IPv6: The destination address is an IPv6 address.
        # 
        # This parameter is required.
        self.ip_version = ip_version
        # A list of detection points. For more information, see [ListCloudGtmMonitorNodes](https://help.aliyun.com/document_detail/2797349.html).
        # 
        # This parameter is required.
        self.isp_city_nodes_shrink = isp_city_nodes_shrink
        # The name of the health check template. Name the template to easily identify the health check protocol.
        # 
        # This parameter is required.
        self.name = name
        # The protocol for health checks on the destination IP address.
        # 
        # - ping
        # 
        # - tcp
        # 
        # - http
        # 
        # - https
        # 
        # This parameter is required.
        self.protocol = protocol
        # The health check timeout in milliseconds. If a packet is not returned within the timeout period, the health check is considered to have timed out. Valid values:
        # 
        # - 2000
        # 
        # - 3000
        # 
        # - 5000
        # 
        # - 10000
        # 
        # This parameter is required.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.failure_rate is not None:
            result['FailureRate'] = self.failure_rate

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.isp_city_nodes_shrink is not None:
            result['IspCityNodes'] = self.isp_city_nodes_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('FailureRate') is not None:
            self.failure_rate = m.get('FailureRate')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IspCityNodes') is not None:
            self.isp_city_nodes_shrink = m.get('IspCityNodes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

