# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGlobalPoliciesRequest(DaraModel):
    def __init__(
        self,
        attach_resource_type: str = None,
        class_name: str = None,
        enable: bool = None,
        environment_id: str = None,
        gateway_id: str = None,
        global_policy_type: str = None,
        ip_access_control_content: str = None,
        ip_access_control_protocol_layer: str = None,
        ip_access_control_resource_name: str = None,
        ip_access_control_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Filters by mounted resource type. This parameter takes effect only for the BlackOrWhite policy type. By default, the Gateway, Domain, and Route types are queried.
        self.attach_resource_type = attach_resource_type
        # The policy class name. You can specify multiple values separated by commas.
        self.class_name = class_name
        # Filters by enabling status.
        self.enable = enable
        # Filters by environment ID.
        self.environment_id = environment_id
        # Filters by gateway ID at the attachment level.
        self.gateway_id = gateway_id
        # The global policy type.
        self.global_policy_type = global_policy_type
        # Filters by IP content by performing a LIKE query on the configuration.
        self.ip_access_control_content = ip_access_control_content
        # Filters by protocol layer. If you specify L4, configurations containing L4 are queried. If you specify L7, configurations that do not contain L4 are queried.
        self.ip_access_control_protocol_layer = ip_access_control_protocol_layer
        # Filters by resource name by performing a LIKE query on the configuration.
        self.ip_access_control_resource_name = ip_access_control_resource_name
        # Filters by IP access control type by performing a LIKE query on the configuration.
        self.ip_access_control_type = ip_access_control_type
        # Filters by exact policy name.
        self.name = name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.class_name is not None:
            result['className'] = self.class_name

        if self.enable is not None:
            result['enable'] = self.enable

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.global_policy_type is not None:
            result['globalPolicyType'] = self.global_policy_type

        if self.ip_access_control_content is not None:
            result['ipAccessControlContent'] = self.ip_access_control_content

        if self.ip_access_control_protocol_layer is not None:
            result['ipAccessControlProtocolLayer'] = self.ip_access_control_protocol_layer

        if self.ip_access_control_resource_name is not None:
            result['ipAccessControlResourceName'] = self.ip_access_control_resource_name

        if self.ip_access_control_type is not None:
            result['ipAccessControlType'] = self.ip_access_control_type

        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('globalPolicyType') is not None:
            self.global_policy_type = m.get('globalPolicyType')

        if m.get('ipAccessControlContent') is not None:
            self.ip_access_control_content = m.get('ipAccessControlContent')

        if m.get('ipAccessControlProtocolLayer') is not None:
            self.ip_access_control_protocol_layer = m.get('ipAccessControlProtocolLayer')

        if m.get('ipAccessControlResourceName') is not None:
            self.ip_access_control_resource_name = m.get('ipAccessControlResourceName')

        if m.get('ipAccessControlType') is not None:
            self.ip_access_control_type = m.get('ipAccessControlType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

