# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudGtmMonitorTemplateResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        evaluation_count: int = None,
        extend_info: str = None,
        failure_rate: int = None,
        interval: int = None,
        ip_version: str = None,
        isp_city_nodes: main_models.DescribeCloudGtmMonitorTemplateResponseBodyIspCityNodes = None,
        name: str = None,
        protocol: str = None,
        remark: str = None,
        request_id: str = None,
        template_id: str = None,
        timeout: int = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the health check template was created.
        self.create_time = create_time
        # The UNIX timestamp that indicates when the health check template was created.
        self.create_timestamp = create_timestamp
        # The number of consecutive times that a health check must fail before the application service is declared abnormal. This prevents false alarms caused by transient issues such as network jitter. Valid values:
        # 
        # - 1
        # 
        # - 2
        # 
        # - 3
        self.evaluation_count = evaluation_count
        # The extended information in a JSON string. The parameters vary based on the protocol.
        # 
        # - For HTTP and HTTPS:
        # 
        #   **host**: The Host field in the HTTP or HTTPS request header. This field identifies the website that you want to access. The default value is the primary domain name. If the target website has specific host requirements, modify this parameter.
        # 
        #   **path**: The URL path for HTTP or HTTPS health checks. The default value is /.
        # 
        #   **code**: The system determines whether the web server is working as expected based on the return code. If the return code is greater than the specified threshold, the application service is considered abnormal.
        # 
        #   - 400: Bad Request. If an HTTP or HTTPS request contains incorrect parameters, the web server returns a code greater than 400. If you set the threshold to 400, specify the exact URL path.
        # 
        #   - 500: Server Error. If an exception occurs on the web server, it returns a code greater than 500. The default threshold is 500.
        # 
        #   **sni**: Specifies whether to enable Server Name Indication (SNI). This parameter is used only for the HTTPS protocol. SNI is a Transport Layer Security (TLS) extension that allows a client to specify the hostname it wants to connect to at the start of the TLS handshake. This allows the server to present the correct certificate for that hostname.
        # 
        #   - true: Enable SNI.
        # 
        #   - false: Disable SNI.
        # 
        #   **followRedirect**: Specifies whether to follow 3xx redirections.
        # 
        #   - true: If the status code returned by the detection point is 3xx (301, 302, 303, 307, or 308), the system follows the redirection.
        # 
        #   - false: The system does not follow the redirection.
        # 
        # - For ping:
        # 
        #   **packetNum**: The number of ICMP packets to send for each ping health check. Valid values: 20, 50, and 100.
        # 
        #   **packetLossRate**: The packet loss rate threshold. For each ping health check, the system calculates the packet loss rate. If the packet loss rate reaches the threshold, an alert is triggered. Packet loss rate = (Number of lost packets / Total number of sent ICMP packets) × 100%. Valid values for the packet loss rate are 10, 30, 40, 80, 90, and 100.
        self.extend_info = extend_info
        # The percentage of failed detection points. If the percentage of failed detection points exceeds this value, the endpoint is declared abnormal. Valid values:
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
        # The IP address type of the detection points:
        # 
        # - IPv4: The target address is an IPv4 address.
        # 
        # - IPv6: The target address is an IPv6 address.
        self.ip_version = ip_version
        self.isp_city_nodes = isp_city_nodes
        # The name of the health check template. To easily identify the template, specify a name that indicates the health check protocol.
        self.name = name
        # The protocol used to probe the target IP address:
        # 
        # - ping
        # 
        # - tcp
        # 
        # - http
        # 
        # - https
        self.protocol = protocol
        # The remarks on the health check template.
        self.remark = remark
        # The unique request ID.
        self.request_id = request_id
        # The unique ID of the health check template.
        self.template_id = template_id
        # The health check timeout period in milliseconds. If a packet is not returned within the specified timeout period, the health check fails. Valid values:
        # 
        # - 2000
        # 
        # - 3000
        # 
        # - 5000
        # 
        # - 10000
        self.timeout = timeout
        # The time when the health check template was last modified.
        self.update_time = update_time
        # The UNIX timestamp that indicates when the health check template was last modified.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.isp_city_nodes:
            self.isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

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

        if self.isp_city_nodes is not None:
            result['IspCityNodes'] = self.isp_city_nodes.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

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
            temp_model = main_models.DescribeCloudGtmMonitorTemplateResponseBodyIspCityNodes()
            self.isp_city_nodes = temp_model.from_map(m.get('IspCityNodes'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeCloudGtmMonitorTemplateResponseBodyIspCityNodes(DaraModel):
    def __init__(
        self,
        isp_city_node: List[main_models.DescribeCloudGtmMonitorTemplateResponseBodyIspCityNodesIspCityNode] = None,
    ):
        self.isp_city_node = isp_city_node

    def validate(self):
        if self.isp_city_node:
            for v1 in self.isp_city_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k1 in self.isp_city_node:
                result['IspCityNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k1 in m.get('IspCityNode'):
                temp_model = main_models.DescribeCloudGtmMonitorTemplateResponseBodyIspCityNodesIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmMonitorTemplateResponseBodyIspCityNodesIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        country_code: str = None,
        country_name: str = None,
        group_name: str = None,
        group_type: str = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.country_code = country_code
        self.country_name = country_name
        self.group_name = group_name
        self.group_type = group_type
        self.isp_code = isp_code
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.isp_code is not None:
            result['IspCode'] = self.isp_code

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        return self

