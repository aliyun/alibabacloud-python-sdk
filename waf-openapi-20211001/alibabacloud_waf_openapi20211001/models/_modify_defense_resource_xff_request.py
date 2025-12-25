# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class ModifyDefenseResourceXffRequest(DaraModel):
    def __init__(
        self,
        acw_cookie_status: int = None,
        acw_secure_status: int = None,
        acw_v3secure_status: int = None,
        custom_headers: List[str] = None,
        instance_id: str = None,
        region_id: str = None,
        resource: str = None,
        resource_manager_resource_group_id: str = None,
        response_headers: List[main_models.ModifyDefenseResourceXffRequestResponseHeaders] = None,
        xff_status: int = None,
    ):
        # The status of the tracking cookie.
        # 
        # *   **0**: disabled
        # *   **1**: enabled. This is the default value.
        self.acw_cookie_status = acw_cookie_status
        # The status of the secure attribute of the tracking cookie.
        # 
        # *   **0**: disabled. This is the default value.
        # *   **1**: enabled.
        self.acw_secure_status = acw_secure_status
        # The status of the secure attribute of the slider CAPTCHA cookie.
        # 
        # *   **0**: disabled. This is the default value.
        # *   **1**: enabled.
        self.acw_v3secure_status = acw_v3secure_status
        # The custom header fields.
        # 
        # >  The first IP address in the specified custom header field is used as the originating IP address of the client to prevent X-Forwarded-For forgery. If you specify multiple header fields, WAF reads the values of the header fields in sequence until the originating IP address is obtained. If the originating IP address cannot be obtained, the first IP address in the X-Forwarded-For header is used as the originating IP address of the client.
        self.custom_headers = custom_headers
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The name of the protected object.
        # 
        # This parameter is required.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The response header.
        self.response_headers = response_headers
        # Specifies whether a Layer 7 proxy is deployed in front of WAF. Layer 7 proxies include Anti-DDoS Proxy and Alibaba Cloud CDN. Valid values:
        # 
        # *   **0**: No Layer 7 proxies are deployed. This is the default value.
        # *   **1**: A Layer 7 proxy is deployed.
        # 
        # This parameter is required.
        self.xff_status = xff_status

    def validate(self):
        if self.response_headers:
            for v1 in self.response_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acw_cookie_status is not None:
            result['AcwCookieStatus'] = self.acw_cookie_status

        if self.acw_secure_status is not None:
            result['AcwSecureStatus'] = self.acw_secure_status

        if self.acw_v3secure_status is not None:
            result['AcwV3SecureStatus'] = self.acw_v3secure_status

        if self.custom_headers is not None:
            result['CustomHeaders'] = self.custom_headers

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        result['ResponseHeaders'] = []
        if self.response_headers is not None:
            for k1 in self.response_headers:
                result['ResponseHeaders'].append(k1.to_map() if k1 else None)

        if self.xff_status is not None:
            result['XffStatus'] = self.xff_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcwCookieStatus') is not None:
            self.acw_cookie_status = m.get('AcwCookieStatus')

        if m.get('AcwSecureStatus') is not None:
            self.acw_secure_status = m.get('AcwSecureStatus')

        if m.get('AcwV3SecureStatus') is not None:
            self.acw_v3secure_status = m.get('AcwV3SecureStatus')

        if m.get('CustomHeaders') is not None:
            self.custom_headers = m.get('CustomHeaders')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        self.response_headers = []
        if m.get('ResponseHeaders') is not None:
            for k1 in m.get('ResponseHeaders'):
                temp_model = main_models.ModifyDefenseResourceXffRequestResponseHeaders()
                self.response_headers.append(temp_model.from_map(k1))

        if m.get('XffStatus') is not None:
            self.xff_status = m.get('XffStatus')

        return self

class ModifyDefenseResourceXffRequestResponseHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Specifies the key for a custom response header.
        self.key = key
        # Specifies the value for a custom response header.
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

