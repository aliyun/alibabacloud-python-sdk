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
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # The client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # This parameter is required.
        self.evaluation_count = evaluation_count
        # The extended information. The value of this parameter is a JSON string. The required parameters vary based on the health check protocol.
        # 
        # *   HTTP or HTTPS:
        # 
        #     **host**: the Host field of an HTTP or HTTPS request header during an HTTP or HTTPS health check. The parameter value indicates the HTTP website that you want to visit. By default, the value is the primary domain name. You can change the value based on your business requirements.
        # 
        #     **path**: the URL for HTTP or HTTPS health checks. Default value: /.
        # 
        #     **code**: the alert threshold. During an HTTP or HTTPS health check, the system checks whether a web server functions as expected based on the status code that is returned from the web server. If the returned status code is greater than the specified threshold, the corresponding application service address is deemed abnormal. Valid values:
        # 
        #     *   400: specifies an invalid request. If an HTTP or HTTPS request contains invalid request parameters, a web server returns a status code that is greater than 400. You must set path to an exact URL if you set code to 400.
        #     *   500: specifies a server error. If some exceptions occur on a web server, the web server returns a status code that is greater than 500. This value is used by default.
        # 
        #     **sni**: specifies whether to enable Server Name Indication (SNI). This parameter is used only when the health check protocol is HTTPS. SNI is an extension to the Transport Layer Security (TLS) protocol, which allows a client to specify the host to be connected when the client sends a TLS handshake request. TLS handshakes occur before any data of HTTP requests is sent. Therefore, SNI enables servers to identify the services that clients are attempting to access before certificates are sent. This allows the servers to present correct certificates to the clients. Valid values:
        # 
        #     *   true: enables SNI.
        #     *   false: disables SNI.
        # 
        #     **followRedirect**: specifies whether to follow 3XX redirects. Valid values:
        # 
        #     *   true: follows 3XX redirects. You are redirected to the destination address if a 3XX status code such as 301, 302, 303, 307, or 308 is returned.
        #     *   false: does not follow 3XX redirects.
        # 
        # *   ping:
        # 
        #     **packetNum**: the total number of Internet Control Message Protocol (ICMP) packets that are sent to the address for each ping-based health check. Valid values: 20, 50, and 100.
        # 
        #     **packetLossRate**: the ICMP packet loss rate for each ping-based health check. The packet loss rate in a health check can be calculated by using the following formula: Packet loss rate in a health check = (Number of lost packets/Total number of sent ICMP packets) × 100%. If the packet loss rate reaches the threshold, an alert is triggered. Valid values: 10, 30, 40, 80, 90, and 100.
        self.extend_info = extend_info
        # This parameter is required.
        self.failure_rate = failure_rate
        # This parameter is required.
        self.interval = interval
        # The IP address type of health check nodes. Valid values:
        # 
        # *   IPv4: You can set IpVersion to IPv4 to perform health checks on IPv4 addresses.
        # *   IPv6: You can set IpVersion to IPv6 to perform health checks on IPv6 addresses.
        # 
        # This parameter is required.
        self.ip_version = ip_version
        # The health check nodes. You can call the [ListCloudGtmMonitorNodes](~~ListCloudGtmMonitorNodes~~) operation to obtain the health check nodes.
        # 
        # This parameter is required.
        self.isp_city_nodes_shrink = isp_city_nodes_shrink
        # The name of the health check template. We recommend that you use a name that distinguishes the type of health check protocol used.
        # 
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.protocol = protocol
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

