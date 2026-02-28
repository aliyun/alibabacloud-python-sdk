# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class GetErAttachmentResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.GetErAttachmentResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response data.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is displayed.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.GetErAttachmentResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetErAttachmentResponseBodyContent(DaraModel):
    def __init__(
        self,
        across: bool = None,
        auto_receive_all_route: bool = None,
        create_time: str = None,
        er_attachment_id: str = None,
        er_attachment_name: str = None,
        er_id: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        message: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Whether cross-account. Valid values:
        # 
        # *   **true**: The network instance is a cross-account resource.
        # *   **false**: The current network instance is a resource of the current account.
        self.across = across
        # Indicates whether to automatically receive all routes from all instances under the Lingjun HUB. Valid values:
        # 
        # *   **true**: received automatically.
        # *   **false**: Not received.
        self.auto_receive_all_route = auto_receive_all_route
        # The time when the activation code was created.
        self.create_time = create_time
        # The ID of the Lingjun HUB network instance.
        self.er_attachment_id = er_attachment_id
        # The name of the Lingjun HUB network instance.
        self.er_attachment_name = er_attachment_name
        # The ID of the Lingjun HUB instance.
        self.er_id = er_id
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The ID of the network instance. Valid values: **VPD** and **VCC**.
        # 
        # For more information, see [What is Lingjun?](https://help.aliyun.com/document_detail/444430.html)
        # 
        # You can query **Lingjun CIDR blocks** and **Lingjun connections** by [ListVpds](https://help.aliyun.com/document_detail/2331077.html) and [ListVccs](https://help.aliyun.com/document_detail/2399526.html?) respectively.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The database type. Valid values:
        # 
        # *   **VPD**: indicates the Lingjun CIDR block.
        # *   **VCC**: indicates a Lingjun connection.
        self.instance_type = instance_type
        # The returned message.
        self.message = message
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # The status of the cache reserve instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.across is not None:
            result['Across'] = self.across

        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id

        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.message is not None:
            result['Message'] = self.message

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Across') is not None:
            self.across = m.get('Across')

        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')

        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

