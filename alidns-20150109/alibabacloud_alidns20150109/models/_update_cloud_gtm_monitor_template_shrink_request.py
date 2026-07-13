# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmMonitorTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        evaluation_count: int = None,
        extend_info: str = None,
        failure_rate: int = None,
        interval: int = None,
        isp_city_nodes_shrink: str = None,
        name: str = None,
        template_id: str = None,
        timeout: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US (default): English
        self.accept_language = accept_language
        # A client-generated token that is used to ensure the idempotence of the request. Make sure that the token is unique for each request. The token can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The number of consecutive health check failures that must occur before an application service is considered abnormal. This helps prevent false alarms caused by transient issues such as network jitter. Valid values:
        # 
        # - 1
        # 
        # - 2
        # 
        # - 3
        self.evaluation_count = evaluation_count
        # The extended information in a JSON string. The parameters vary based on the health check protocol.
        # 
        # - HTTP and HTTPS:
        # 
        #   host: When you perform an HTTP or HTTPS health check, this parameter specifies the Host field in the HTTP request header. It identifies the target website. The default value is the primary domain name. If the target website has specific requirements for the Host field, modify this parameter as needed.
        # 
        #   path: The path for the HTTP or HTTPS health check. The default value is /.
        # 
        #   code: When you perform an HTTP or HTTPS health check, the system uses the return code from the web server to determine its status. If the return code exceeds the specified threshold, the application service is considered abnormal.
        # 
        #   - 400: Bad Request. If an HTTP or HTTPS request contains invalid parameters, the web server returns a code greater than 400. If you set the threshold to 400, make sure that you specify the exact URL path.
        # 
        #   - 500: Server Error. If the web server encounters an error, it returns a code greater than 500. The default threshold is 500.
        # 
        #   sni: Specifies whether to enable Server Name Indication (SNI). This parameter is used only for HTTPS health checks. SNI is an extension to the Transport Layer Security (TLS) protocol. It allows a client to specify the hostname it is trying to connect to at the start of the TLS handshake. Because the TLS handshake occurs before any HTTP data is sent, SNI allows the server to know which service the client is trying to access before sending the certificate. This enables the server to present the correct certificate to the client.
        # 
        #   - true: Enable SNI.
        # 
        #   - false: Disable SNI.
        # 
        #   followRedirect: Specifies whether to follow 3xx redirections.
        # 
        #   - true: Follow the redirection if the detection point receives a 3xx status code (301, 302, 303, 307, or 308).
        # 
        #   - false: Do not follow the redirection.
        # 
        # - Ping:
        # 
        #   packetNum: The number of ICMP packets to send for each ping health check. Valid values: 20, 50, and 100.
        # 
        #   packetLossRate: The packet loss rate that triggers an alarm. For each ping health check, the system calculates the packet loss rate. Packet loss rate = (Number of lost packets / Total number of sent ICMP packets) × 100%. An alarm is triggered if the packet loss rate reaches this threshold. Valid values: 10, 30, 40, 80, 90, and 100.
        self.extend_info = extend_info
        # The percentage of failed detection points. An endpoint is considered abnormal if the percentage of detection points that fail the health check exceeds this threshold. Valid values:
        # 
        # - 20
        # 
        # - 50
        # 
        # - 80
        # 
        # - 100
        self.failure_rate = failure_rate
        # The interval between health checks in seconds. The default value is 60. The minimum interval is 15 seconds. This feature is available only for Ultimate Edition instances.
        self.interval = interval
        # The list of detection points. Call [ListCloudGtmMonitorNodes](https://help.aliyun.com/document_detail/2797327.html) to obtain the information.
        self.isp_city_nodes_shrink = isp_city_nodes_shrink
        # The name of the health check template. For easy identification, name the template based on its health check protocol.
        self.name = name
        # The unique ID of the health check template that you want to modify.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The timeout period for a health check in milliseconds. If a packet is not returned within the specified timeout period, the health check fails. Valid values:
        # 
        # - 2000
        # 
        # - 3000
        # 
        # - 5000
        # 
        # - 10000
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

        if self.isp_city_nodes_shrink is not None:
            result['IspCityNodes'] = self.isp_city_nodes_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

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

        if m.get('IspCityNodes') is not None:
            self.isp_city_nodes_shrink = m.get('IspCityNodes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

