# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class SearchCloudGtmMonitorTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        templates: main_models.SearchCloudGtmMonitorTemplatesResponseBodyTemplates = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        # The health check templates.
        self.templates = templates
        self.total_items = total_items
        self.total_pages = total_pages

    def validate(self):
        if self.templates:
            self.templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.templates is not None:
            result['Templates'] = self.templates.to_map()

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Templates') is not None:
            temp_model = main_models.SearchCloudGtmMonitorTemplatesResponseBodyTemplates()
            self.templates = temp_model.from_map(m.get('Templates'))

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class SearchCloudGtmMonitorTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        template: List[main_models.SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for v1 in self.template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Template'] = []
        if self.template is not None:
            for k1 in self.template:
                result['Template'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('Template') is not None:
            for k1 in m.get('Template'):
                temp_model = main_models.SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplate()
                self.template.append(temp_model.from_map(k1))

        return self

class SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplate(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        evaluation_count: int = None,
        extend_info: str = None,
        failure_rate: int = None,
        interval: int = None,
        ip_version: str = None,
        isp_city_nodes: main_models.SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplateIspCityNodes = None,
        name: str = None,
        protocol: str = None,
        remark: str = None,
        template_id: str = None,
        timeout: int = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.evaluation_count = evaluation_count
        # The extended information. The value of this parameter is a JSON string. The required parameters vary based on the health check protocol. Valid values:
        # 
        # *   **http(s)**:
        # 
        #     **host**: indicates the Host field of an HTTP or HTTPS request header during an HTTP or HTTPS health check. The parameter value indicates the HTTP website that you want to visit. By default, the value is the primary domain name. You can change the value based on your business requirements.
        # 
        #     **path**: the URL for HTTP or HTTPS health checks. Default value: /.
        # 
        #     **code**: indicates the alert threshold. During an HTTP or HTTPS health check, the system checks whether a web server functions as expected based on the status code that is returned from the web server. If the returned status code is greater than the specified threshold, the corresponding application service address is deemed abnormal. Valid values:
        # 
        #     *   400: indicates an invalid request. If an HTTP or HTTPS request contains invalid request parameters, a web server returns a status code that is greater than 400. If Verification Content is set to "The error code is greater than 400", you must specify an exact URL for the path parameter.
        #     *   500: indicates a server error. If some exceptions occur on a web server, the web server returns a status code that is greater than 500. The error code that is greater than 500 is used as the alert threshold by default.
        # 
        #     **sni**: indicates whether Server Name Indication (SNI) is enabled for HTTPS. SNI is an extension to the Transport Layer Security (TLS) protocol, which allows a client to specify the host to be connected when the client sends a TLS handshake request. TLS handshakes occur before any data of HTTP requests is sent. Therefore, SNI enables servers to identify the services that clients are attempting to access before certificates are sent. This allows the servers to present correct certificates to the clients. Valid values:
        # 
        #     *   true: SNI is enabled.
        #     *   false: SNI is disabled.
        # 
        #     **followRedirect**: indicates whether 3XX redirection is followed. Valid values:
        # 
        #     *   true: You are redirected to the destination address if a status code 3XX, such as 301, 302, 303, 307, or 308, is returned.
        #     *   false: You are not redirected to the destination address.
        # 
        # *   **ping**:
        # 
        #     **packetNum**: The total number of Internet Control Message Protocol (ICMP) packets that are sent to the address for each ping-based health check. Valid values: 20, 50, and 100.
        # 
        #     **packetLossRate**: The packet loss rate for each ping-based health check. The packet loss rate in a check can be calculated by using the following formula: Packet loss rate = (Number of lost packets/Total number of sent ICMP packets) × 100%. If the packet loss rate reaches the threshold, an alert is triggered. Valid values: 10, 30, 40, 80, 90, and 100.
        self.extend_info = extend_info
        self.failure_rate = failure_rate
        self.interval = interval
        # The IP address type of health check nodes. Valid values:
        # 
        # *   IPv4: applicable when the destination address of health checks is an IPv4 address
        # *   IPv6: applicable when the destination address of health checks is an IPv6 address
        self.ip_version = ip_version
        # The health check nodes.
        self.isp_city_nodes = isp_city_nodes
        self.name = name
        self.protocol = protocol
        self.remark = remark
        self.template_id = template_id
        self.timeout = timeout
        self.update_time = update_time
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
            temp_model = main_models.SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplateIspCityNodes()
            self.isp_city_nodes = temp_model.from_map(m.get('IspCityNodes'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplateIspCityNodes(DaraModel):
    def __init__(
        self,
        isp_city_node: List[main_models.SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplateIspCityNodesIspCityNode] = None,
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
                temp_model = main_models.SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplateIspCityNodesIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        return self

class SearchCloudGtmMonitorTemplatesResponseBodyTemplatesTemplateIspCityNodesIspCityNode(DaraModel):
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
        # The group type of health check nodes. Valid values:
        # 
        # *   BGP: BGP node
        # *   OVERSEAS: node outside the Chinese mainland
        # *   ISP: Internet service provider (ISP) node
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

