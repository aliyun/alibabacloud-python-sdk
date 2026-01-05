# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListHealthCheckTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        health_check_templates: List[main_models.ListHealthCheckTemplatesResponseBodyHealthCheckTemplates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The health check templates.
        self.health_check_templates = health_check_templates
        # The number of entries returned per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.health_check_templates:
            for v1 in self.health_check_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HealthCheckTemplates'] = []
        if self.health_check_templates is not None:
            for k1 in self.health_check_templates:
                result['HealthCheckTemplates'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.health_check_templates = []
        if m.get('HealthCheckTemplates') is not None:
            for k1 in m.get('HealthCheckTemplates'):
                temp_model = main_models.ListHealthCheckTemplatesResponseBodyHealthCheckTemplates()
                self.health_check_templates.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHealthCheckTemplatesResponseBodyHealthCheckTemplates(DaraModel):
    def __init__(
        self,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_template_id: str = None,
        health_check_template_name: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        resource_group_id: str = None,
        tags: List[main_models.ListHealthCheckTemplatesResponseBodyHealthCheckTemplatesTags] = None,
        unhealthy_threshold: int = None,
    ):
        # The HTTP status codes that indicate healthy backend servers.
        self.health_check_codes = health_check_codes
        # The port that is used for health checks.
        # 
        # Valid values: \\*\\* 0 to 65535\\*\\*.
        # 
        # The default value is **0**, which specifies that the port of a backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$SERVER_IP** (default): the private IP address of a backend server. If an IP address is specified, or this parameter is not specified, the ALB instance uses the private IP address of each backend server as the domain name for health checks.
        # *   **domain**: The domain name must be 1 to 80 characters in length, and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # >  This parameter takes effect only if you set `HealthCheckProtocol` to **HTTP** or **HTTPS**.
        self.health_check_host = health_check_host
        # The HTTP version for health checks.
        # 
        # Valid values: **HTTP 1.0** and **HTTP 1.1**.
        # 
        # Default value: **HTTP 1.1**.
        # 
        # >  This parameter takes effect only if you set `HealthCheckProtocol` to **HTTP** or **HTTPS**.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds. Valid values: **1 to 50**. Default value: **2**.
        self.health_check_interval = health_check_interval
        # The HTTP method that is used for health checks. Valid values:
        # 
        # *   **HEAD** (default): By default, HTTP and HTTPS health checks use the HEAD method.
        # *   **GET**: If the length of a response exceeds 8 KB, the response is truncated. However, the health check result is not affected.
        # *   **POST**: gRPC health checks use the POST method by default.
        # 
        # >  This parameter takes effect only if you set **HealthCheckProtocol** to **HTTP**, **HTTPS**, or **gRPC**.
        self.health_check_method = health_check_method
        # The URL path that you want to use for health checks.
        # 
        # The URL must be 1 to 80 characters in length, and can contain letters, digits, the following special characters: - / . % ? # &, and the following extended characters: `_ ; ~ ! ( ) * [ ] @ $ ^ : \\" , +`. The URL must start with a forward slash (/).
        self.health_check_path = health_check_path
        # The protocol that is used for health checks. Valid values:
        # 
        # *   **HTTP** (default): The ALB instance sends HEAD or GET requests, which simulate browser requests, to check whether the backend server is healthy.
        # *   **HTTPS**: HTTPS health checks simulate browser behaviors by sending HEAD or GET requests to probe the availability of backend servers. HTTPS provides higher security because HTTPS supports data encryption.
        # *   **TCP**: TCP health checks send TCP SYN packets to a backend server to check whether the port of the backend server is reachable.
        # *   **gRPC**: gRPC health checks send POST or GET requests to a backend server to check whether the backend server is healthy.
        self.health_check_protocol = health_check_protocol
        # The ID of the health check template.
        self.health_check_template_id = health_check_template_id
        # The name of the health check template.
        # 
        # The name must be 2 to 128 character characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.health_check_template_name = health_check_template_name
        # The timeout period of a health check response. If a backend Elastic Compute Service (ECS) instance does not respond within the specified timeout period, the ECS instance fails to pass the health check.
        # 
        # Valid values: **1 to 300**. Unit: seconds.
        # 
        # Default value: **5**.
        self.health_check_timeout = health_check_timeout
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from **fail** to **success**.
        # 
        # Valid values: **2 to 10**.
        # 
        # Default value: **3**.
        self.healthy_threshold = healthy_threshold
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from **success** to **fail**.
        # 
        # Valid values: **2 to 10**.
        # 
        # Default value: **3**.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host

        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method

        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path

        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol

        if self.health_check_template_id is not None:
            result['HealthCheckTemplateId'] = self.health_check_template_id

        if self.health_check_template_name is not None:
            result['HealthCheckTemplateName'] = self.health_check_template_name

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')

        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')

        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')

        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')

        if m.get('HealthCheckTemplateId') is not None:
            self.health_check_template_id = m.get('HealthCheckTemplateId')

        if m.get('HealthCheckTemplateName') is not None:
            self.health_check_template_name = m.get('HealthCheckTemplateName')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListHealthCheckTemplatesResponseBodyHealthCheckTemplatesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

class ListHealthCheckTemplatesResponseBodyHealthCheckTemplatesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length, and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

