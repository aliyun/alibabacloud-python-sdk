# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeNamespaceListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeNamespaceListResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The list of namespaces.
        self.data = data
        # The error code. Valid values:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The returned message. Valid values:
        # 
        # *   success: If the call is successful, **success** is returned.
        # *   An error code: If the call fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the list of namespaces was queried. Valid values:
        # 
        # *   **true**: The list was queried.
        # *   **false**: The list failed to be queried.
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeNamespaceListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class DescribeNamespaceListResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_install: str = None,
        current: bool = None,
        custom: bool = None,
        hybrid_cloud_enable: bool = None,
        name_space_short_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The command that was run to install the agent.
        self.agent_install = agent_install
        # This parameter is no longer valid.
        self.current = current
        # Indicates whether custom namespaces are returned. Valid values:
        # 
        # *   **true**: Custom namespaces are returned.
        # *   **false**: Custom namespaces are not returned.
        self.custom = custom
        # Indicates whether hybrid cloud namespaces are excluded. Valid values:
        # 
        # *   **true**: Hybrid cloud namespaces are excluded.
        # *   **false**: Hybrid cloud namespaces are included.
        self.hybrid_cloud_enable = hybrid_cloud_enable
        # The short ID of the namespace.
        self.name_space_short_id = name_space_short_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The region to which the namespace belongs.
        self.region_id = region_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_install is not None:
            result['AgentInstall'] = self.agent_install

        if self.current is not None:
            result['Current'] = self.current

        if self.custom is not None:
            result['Custom'] = self.custom

        if self.hybrid_cloud_enable is not None:
            result['HybridCloudEnable'] = self.hybrid_cloud_enable

        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstall') is not None:
            self.agent_install = m.get('AgentInstall')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('Custom') is not None:
            self.custom = m.get('Custom')

        if m.get('HybridCloudEnable') is not None:
            self.hybrid_cloud_enable = m.get('HybridCloudEnable')

        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

