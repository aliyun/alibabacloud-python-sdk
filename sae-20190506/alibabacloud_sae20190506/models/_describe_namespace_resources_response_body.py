# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeNamespaceResourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeNamespaceResourcesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: indicates that the request was successful.
        # *   **3xx**: indicates that the request was redirected.
        # *   **4xx**: indicates that the request failed.
        # *   **5xx**: indicates that a server error occurred.
        self.code = code
        # The returned data.
        self.data = data
        # The error code.
        # 
        # *   The **ErrorCode** parameter is not returned when the request succeeds.
        # *   The **ErrorCode** parameter is returned when the request fails. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # The returned message.
        # 
        # *   **success** is returned when the request succeeds.
        # *   An error code is returned when the request fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the information about resources in the namespace was queried successfully. Valid values:
        # 
        # *   **true**: indicates that the query was successful.
        # *   **false**: indicates that the query failed.
        self.success = success
        # The ID of the trace. It can be used to query the details of a request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeNamespaceResourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeNamespaceResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        apm_java_agent_version: str = None,
        app_count: int = None,
        belong_region: str = None,
        description: str = None,
        jump_server_app_id: str = None,
        jump_server_ip: str = None,
        last_change_order_id: str = None,
        last_change_order_running: bool = None,
        last_change_order_status: str = None,
        name_space_short_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        notification_expired: bool = None,
        security_group_id: str = None,
        sls_configs: str = None,
        tenant_id: str = None,
        user_id: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.apm_java_agent_version = apm_java_agent_version
        # The number of applications.
        self.app_count = app_count
        # The region to which the namespace belongs.
        self.belong_region = belong_region
        # The description of the namespace.
        self.description = description
        # The ID of the jump server application.
        self.jump_server_app_id = jump_server_app_id
        # The IP address of the jump server.
        self.jump_server_ip = jump_server_ip
        # The ID of the change order.
        self.last_change_order_id = last_change_order_id
        # Indicates whether a change order is being executed in the namespace. Valid values:
        # 
        # *   **true**: indicates that a change order is being executed in the namespace.
        # *   **false**: indicates that no change orders are being executed in the namespace.
        self.last_change_order_running = last_change_order_running
        # The status of the latest change order. Valid values:
        # 
        # *   **READY**: The change order is ready.
        # *   **RUNNING**: The change order is being executed.
        # *   **SUCCESS**: The change order was executed.
        # *   **FAIL**: The change order could not be executed.
        # *   **ABORT**: The change order was terminated.
        # *   **WAIT_BATCH_CONFIRM**: The change order is pending execution. You must manually confirm the release batch.
        # *   **AUTO_BATCH_WAIT**: The change order is pending execution. SAE will automatically confirm the release batch.
        # *   **SYSTEM_FAIL**: A system exception occurred.
        # *   **WAIT_APPROVAL**: The change order is pending approval.
        # *   **APPROVED**: The change order is approved and is pending execution.
        self.last_change_order_status = last_change_order_status
        self.name_space_short_id = name_space_short_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # Indicates whether the notification of a change order is expired. Valid values:
        # 
        # *   **true**: indicates that the notification is expired.
        # *   **false**: indicates that the notification is not expired.
        self.notification_expired = notification_expired
        # The ID of the security group.
        self.security_group_id = security_group_id
        self.sls_configs = sls_configs
        # The ID of the tenant in the SAE namespace.
        self.tenant_id = tenant_id
        # The ID of the user.
        self.user_id = user_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The name of the vSwitch.
        self.v_switch_name = v_switch_name
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apm_java_agent_version is not None:
            result['ApmJavaAgentVersion'] = self.apm_java_agent_version

        if self.app_count is not None:
            result['AppCount'] = self.app_count

        if self.belong_region is not None:
            result['BelongRegion'] = self.belong_region

        if self.description is not None:
            result['Description'] = self.description

        if self.jump_server_app_id is not None:
            result['JumpServerAppId'] = self.jump_server_app_id

        if self.jump_server_ip is not None:
            result['JumpServerIp'] = self.jump_server_ip

        if self.last_change_order_id is not None:
            result['LastChangeOrderId'] = self.last_change_order_id

        if self.last_change_order_running is not None:
            result['LastChangeOrderRunning'] = self.last_change_order_running

        if self.last_change_order_status is not None:
            result['LastChangeOrderStatus'] = self.last_change_order_status

        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.notification_expired is not None:
            result['NotificationExpired'] = self.notification_expired

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApmJavaAgentVersion') is not None:
            self.apm_java_agent_version = m.get('ApmJavaAgentVersion')

        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')

        if m.get('BelongRegion') is not None:
            self.belong_region = m.get('BelongRegion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('JumpServerAppId') is not None:
            self.jump_server_app_id = m.get('JumpServerAppId')

        if m.get('JumpServerIp') is not None:
            self.jump_server_ip = m.get('JumpServerIp')

        if m.get('LastChangeOrderId') is not None:
            self.last_change_order_id = m.get('LastChangeOrderId')

        if m.get('LastChangeOrderRunning') is not None:
            self.last_change_order_running = m.get('LastChangeOrderRunning')

        if m.get('LastChangeOrderStatus') is not None:
            self.last_change_order_status = m.get('LastChangeOrderStatus')

        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NotificationExpired') is not None:
            self.notification_expired = m.get('NotificationExpired')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

