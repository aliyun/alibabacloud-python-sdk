# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[main_models.DescribeDefenseResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of protected objects.
        self.resources = resources
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.DescribeDefenseResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDefenseResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        acw_cookie_status: int = None,
        acw_secure_status: int = None,
        acw_v3secure_status: int = None,
        custom_headers: List[str] = None,
        description: str = None,
        detail: Dict[str, Any] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_id: str = None,
        owner_user_id: str = None,
        pattern: str = None,
        product: str = None,
        resource: str = None,
        resource_group: str = None,
        resource_manager_resource_group_id: str = None,
        resource_origin: str = None,
        response_headers: List[main_models.DescribeDefenseResourcesResponseBodyResourcesResponseHeaders] = None,
        xff_status: int = None,
    ):
        # Indicates whether the tracking cookie feature is enabled.
        # 
        # - **0**: disabled.
        # 
        # - **1**: enabled.
        self.acw_cookie_status = acw_cookie_status
        # Indicates whether the secure attribute of the tracking cookie is enabled.
        # 
        # - **0**: disabled.
        # 
        # - **1**: enabled.
        self.acw_secure_status = acw_secure_status
        # Indicates whether the secure attribute of the slider CAPTCHA cookie is enabled.
        # 
        # - **0**: disabled.
        # 
        # - **1**: enabled.
        self.acw_v3secure_status = acw_v3secure_status
        # The custom XFF header that is used to obtain the real IP address of a client. If \\`XffStatus\\` is set to 1 and this parameter is left empty, the first IP address in the XFF header is used as the client IP address.
        self.custom_headers = custom_headers
        # The description of the protected object.
        self.description = description
        # The details of the protected object. The key-value pairs vary by product type.
        self.detail = detail
        # The time when the protected object was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The time when the protected object was modified. This value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The ID of the WAF instance.
        self.instance_id = instance_id
        # The account to which the asset of the protected object belongs. This parameter is returned in a multi-account management scenario.
        self.owner_user_id = owner_user_id
        # The protection mode of the protected object.
        self.pattern = pattern
        # The type of cloud service to which the protected object belongs.
        self.product = product
        # The name of the protected object.
        self.resource = resource
        # The name of the protected object group to which the protected object is added.
        self.resource_group = resource_group
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The source of the protected object.
        self.resource_origin = resource_origin
        # The custom response headers configured for the protected object.
        self.response_headers = response_headers
        # Indicates whether the X-Forwarded-For (XFF) proxy is enabled for the protected object.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.product is not None:
            result['Product'] = self.product

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_origin is not None:
            result['ResourceOrigin'] = self.resource_origin

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceOrigin') is not None:
            self.resource_origin = m.get('ResourceOrigin')

        self.response_headers = []
        if m.get('ResponseHeaders') is not None:
            for k1 in m.get('ResponseHeaders'):
                temp_model = main_models.DescribeDefenseResourcesResponseBodyResourcesResponseHeaders()
                self.response_headers.append(temp_model.from_map(k1))

        if m.get('XffStatus') is not None:
            self.xff_status = m.get('XffStatus')

        return self

class DescribeDefenseResourcesResponseBodyResourcesResponseHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the custom response header.
        self.key = key
        # The value of the custom response header.
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

