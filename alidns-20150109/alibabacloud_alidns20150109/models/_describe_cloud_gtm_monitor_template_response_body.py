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
        # Health check template creation time.
        self.create_time = create_time
        # Health check template creation time (timestamp).
        self.create_timestamp = create_timestamp
        # Retries count. The system will only judge the application service as abnormal after consecutive monitoring failures to prevent inaccurate monitoring results due to momentary network fluctuations or other reasons. Available retry counts are:
        # - 1
        # - 2
        # - 3
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
        #     *   400: indicates an invalid request. If an HTTP or HTTPS request contains invalid request parameters, a web server returns a status code that is greater than 400. You must specify an exact URL for path if you set code to 400.
        #     *   500: indicates a server error. If some exceptions occur on a web server, the web server returns a status code that is greater than 500. This value is used by default.
        # 
        #     **sni**: indicates whether Server Name Indication (SNI) is enabled. This parameter is used only when the health check protocol is HTTPS. SNI is an extension to the Transport Layer Security (TLS) protocol, which allows a client to specify the host to be connected when the client sends a TLS handshake request. TLS handshakes occur before any data of HTTP requests is sent. Therefore, SNI enables servers to identify the services that clients are attempting to access before certificates are sent. This allows the servers to present correct certificates to the clients. Valid values:
        # 
        #     *   true: SNI is enabled.
        #     *   false: SNI is disabled.
        # 
        #     **followRedirect**: indicates whether 3XX redirects are followed. Valid values:
        # 
        #     *   true: 3XX redirects are followed. You are redirected to the destination address if a 3XX status code such as 301, 302, 303, 307, or 308 is returned.
        #     *   false: 3XX redirects are not followed.
        # 
        # *   ping:
        # 
        #     **packetNum**: the total number of Internet Control Message Protocol (ICMP) packets that are sent to the address for each ping-based health check. Valid values: 20, 50, and 100.
        # 
        #     **packetLossRate**: the ICMP packet loss rate for each ping-based health check. The packet loss rate in a health check can be calculated by using the following formula: Packet loss rate in a health check = (Number of lost packets/Total number of sent ICMP packets) × 100%. If the packet loss rate reaches the threshold, an alert is triggered. Valid values: 10, 30, 40, 80, 90, and 100.
        self.extend_info = extend_info
        # Percentage of selected node probe failures (%), that is, the percentage of abnormal detection points among the total detection points. When the failure ratio exceeds the set threshold, the service address is judged as abnormal. The available failure ratio thresholds are:
        # - 20
        # - 50
        # - 80
        # - 100
        self.failure_rate = failure_rate
        # The time interval (in seconds) between each check, with a default interval of 1 minute. The minimum supported health check interval is 15 seconds, available for flagship edition instances.
        self.interval = interval
        # Detect the type of the node IP address:
        # - IPv4: Applicable when the target address type is IPv4;
        # - IPv6: Applicable when the target address type is IPv6.
        self.ip_version = ip_version
        # Probe node list, detailed information can be obtained by calling ListCloudGtmMonitorNodes.
        self.isp_city_nodes = isp_city_nodes
        # The name of the health check probe template, which is recommended to be distinguishable for configuration personnel to differentiate and remember, ideally indicating the health check protocol.
        self.name = name
        # Protocol types to initiate probes to the target IP address:
        # - ping
        # - tcp
        # - http
        # - https
        self.protocol = protocol
        # Remarks for the health check template.
        self.remark = remark
        # Unique request identification code.
        self.request_id = request_id
        # The ID of the health check template. This ID uniquely identifies the health check template.
        self.template_id = template_id
        # Probe timeout (in milliseconds), data packets not returned within the timeout period are deemed as health check timeouts:
        # - 2000
        # - 3000
        # - 5000
        # - 10000
        self.timeout = timeout
        # Health check template configuration modification time.
        self.update_time = update_time
        # Health check template configuration modification time (timestamp).
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
        # City code
        self.city_code = city_code
        # City name
        self.city_name = city_name
        # Country Code
        self.country_code = country_code
        # Country Name
        self.country_name = country_name
        # Probe node group type name
        self.group_name = group_name
        # Probe node group types:
        # - BGP: BGP nodes
        # - OVERSEAS: International nodes
        # - ISP: Carrier nodes
        self.group_type = group_type
        # Operator Code
        self.isp_code = isp_code
        # Operator Name
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

